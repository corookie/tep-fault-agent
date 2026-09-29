"""将约定格式的 TEP Markdown 手册切成可追溯片段；仅使用 Python 标准库。

这是本项目的结构切分器，不是任意 PDF/Markdown 的通用解析器。
运行：python3 chunk_knowledge.py
输出：knowledge_build/{chunks.jsonl,preview.md,manifest.json}
"""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
import tempfile

BASE = Path(__file__).resolve().parent
VERSION = "1.0.0"
ROLE_LABELS = {"section_context": "本节限定", "units_and_sources": "单位与来源",
               "fault_boundary": "故障解释边界", "source_correction": "来源差异处理",
               "body": "补充上下文"}
KIND_LABELS = {"scope": "适用范围", "chemistry": "组分与反应", "process_overview": "工艺总览",
               "stream": "物料流", "utility": "冷却水回路", "equipment": "设备",
               "variable_conventions": "变量约定", "variable": "变量", "sampling": "采样与延迟",
               "dataset_scope": "数据范围", "editorial_guidance": "数据处理说明",
               "fault_conventions": "故障解释约定", "fault": "故障",
               "limitations": "知识边界", "source_correction": "来源差异"}
# 业务关系显式登记：修改表述后依然按稳定 ID 关联，不用关键词猜错。
CONFLICT_TARGETS = {
    "C01": ["VAR-X22", "EQUIP-CONDENSER"],
    "C02": ["VAR-X52", "EQUIP-CONDENSER"],
    "C03": ["FAULT-IDV10"],
    "C04": ["SCOPE-001", *[f"FAULT-IDV{i:02}" for i in range(16, 22)]],
    "C05": ["FAULT-IDV03"],
    "C06": ["CHEM-001"],
    "C07": ["SCOPE-001", "VARS-001"],
    "C08": ["PROC-001", "STREAM-07", "UTILITY-13"],
    "C09": ["DATA-TIMING"],
    "C10": ["FAULTS-001"],
}


@dataclass
class Piece:
    """一段原文或由表头+数据行转换的文字，保留其精确行号区间。"""
    text: str
    start: int
    end: int
    role: str = "body"


@dataclass
class Section:
    level: int
    title: str
    start: int
    direct_end: int
    end: int
    path: list[str]


@dataclass
class Unit:
    key: str
    title: str
    kind: str
    section: Section
    body: Piece
    context: list[Piece]
    atomic: bool = False


class Handbook:
    def __init__(self, path: Path):
        self.path = path.resolve()
        self.raw = path.read_text(encoding="utf-8")
        self.lines = self.raw.splitlines()
        if not self.lines or self.lines[0] != "---":
            raise ValueError("手册缺少元数据头")
        fence = self.lines.index("---", 1)
        self.meta = dict(line.split(": ", 1) for line in self.lines[1:fence])
        for key in ("document_id", "version", "scope", "status"):
            if not self.meta.get(key):
                raise ValueError(f"元数据缺少 {key}")
        # 不把 fenced code 内的 # 当标题。
        headings, in_code = [], False
        for i, line in enumerate(self.lines):
            if line.startswith("```"):
                in_code = not in_code
            if not in_code and (m := re.match(r"^(#{1,6}) (.+)$", line)):
                headings.append((i, len(m[1]), m[2]))
        self.sections = []
        stack = []
        for j, (i, level, title) in enumerate(headings):
            while stack and stack[-1][0] >= level:
                stack.pop()
            stack.append((level, title))
            end = next((k for k, lv, _ in headings[j + 1:] if lv <= level), len(self.lines))
            direct_end = headings[j + 1][0] if j + 1 < len(headings) else len(self.lines)
            self.sections.append(Section(level, title, i, direct_end, end, [s[1] for s in stack]))

    def section(self, prefix: str) -> Section:
        found = [s for s in self.sections if s.title.startswith(prefix)]
        if len(found) != 1:
            raise ValueError(f"章节 {prefix!r} 不唯一或不存在")
        return found[0]

    def piece(self, start: int, end: int, role="body") -> Piece:
        # 输入为 Python 的半开区间；输出行号是读者看到的 1 起始闭区间。
        while start < end and not self.lines[start].strip():
            start += 1
        while end > start and not self.lines[end - 1].strip():
            end -= 1
        return Piece("\n".join(self.lines[start:end]), start + 1, end, role)

    def body(self, section: Section, full=False) -> Piece:
        return self.piece(section.start + 1, section.end if full else section.direct_end)

    def rows(self, section: Section) -> tuple[list[tuple[list[str], Piece]], list[Piece]]:
        """提取表格行，并把表格外的限定、来源和单位保存为继承上下文。"""
        rows, outside, headers = [], [], None
        for i in range(section.start + 1, section.direct_end):
            line = self.lines[i]
            if line.startswith("|"):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if headers is None:
                    headers = cells
                elif all(re.fullmatch(r":?-+:?", c) for c in cells):
                    continue
                else:
                    if len(cells) != len(headers):
                        raise ValueError(f"第 {i+1} 行表格列数不一致")
                    text = "\n".join(f"- {h}：{c}" for h, c in zip(headers, cells))
                    rows.append((cells, Piece(text, i+1, i+1, "table_row")))
            elif line.strip():
                outside.append(Piece(line, i+1, i+1, "section_context"))
        if not rows:
            raise ValueError(f"{section.title} 没有可解析的表格")
        return rows, outside


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def units_from(doc: Handbook) -> list[Unit]:
    units = []
    def add(prefix, key, kind, full=False, atomic=False, context=None):
        s = doc.section(prefix)
        units.append(Unit(key, s.title, kind, s, doc.body(s, full), context or [], atomic))

    add("1. ", "SCOPE-001", "scope", atomic=True)
    add("2. ", "CHEM-001", "chemistry", full=True, atomic=True)
    add("3.1 ", "PROC-001", "process_overview", atomic=True)
    s = doc.section("3.3 ")
    rows, outside = doc.rows(s)
    for cells, body in rows:
        kind = "utility" if cells[0].startswith("UTILITY-") else "stream"
        units.append(Unit(cells[0], f"TEP 流股 {cells[1]}：{cells[2]}", kind, s, body, outside, True))
    for s in doc.sections:
        if "｜EQUIP-" in s.title:
            units.append(Unit(s.title.split("｜")[-1], s.title, "equipment", s, doc.body(s), []))

    vars_section = doc.section("5. ")
    var_context = doc.body(vars_section)
    add("5. ", "VARS-001", "variable_conventions", atomic=True)
    for prefix in ("5.1 ", "5.2 ", "5.3 "):
        s = doc.section(prefix)
        rows, outside = doc.rows(s)
        # 首段是编辑导语；单位约定和来源才需要附到每个变量。
        common = [doc.piece(i, i+1, "units_and_sources")
                  for i in range(vars_section.start+1, vars_section.direct_end)
                  if doc.lines[i].startswith(("**单位约定", "变量表来源"))]
        if not common:
            raise ValueError("变量字典缺少单位/来源约定")
        for cells, body in rows:
            number = int(cells[0].removeprefix("VAR-X"))
            original = f"XMEAS({number})" if number <= 41 else f"XMV({number-41})"
            if cells[1] != f"X{number}" or cells[2] != original or not cells[4]:
                raise ValueError(f"变量 {cells[0]} 的列映射或单位不正确")
            # 只复制该变量相关的单位解释，避免每条温度记录夹带所有量纲。
            relevant = []
            unit_word = ("操纵量" if number > 41 else "液位" if cells[4] == "%"
                         else "kPa(g)" if cells[4] == "kPa(g)" else cells[4])
            for p in common:
                if p.text.startswith("**单位约定"):
                    sentences = re.findall(r"[^。]+。?", p.text.removeprefix("**单位约定：**"))
                    selected = "".join(s for s in sentences if unit_word in s).strip()
                    if selected:
                        relevant.append(Piece(selected,p.start,p.end,"units_and_sources"))
                else:
                    relevant.append(p)
            units.append(Unit(cells[0], f"{cells[1]} / {cells[2]}：{cells[3]}",
                              "variable", s, body, relevant + outside, True))

    add("6.1 ", "DATA-TIMING", "sampling", atomic=True)
    add("6.2 ", "DATA-FILES", "dataset_scope")
    add("6.3 ", "DATA-002", "editorial_guidance", context=[var_context, doc.body(doc.section("6.1 "))])
    add("7. ", "FAULTS-001", "fault_conventions", atomic=True)
    fault_parent = doc.section("7. ")
    # 故障目录第一段是公共解释边界；每个故障自己的来源保持独立。
    boundary = doc.piece(fault_parent.start+1, fault_parent.start+3, "fault_boundary")
    for s in doc.sections:
        if "｜FAULT-IDV" in s.title:
            units.append(Unit(s.title.split("｜")[-1], s.title, "fault", s, doc.body(s), [boundary], True))

    s = doc.section("8. ")
    conflicts, outside = doc.rows(s)
    # 未知项/不纳入本版的内容也单独保留，避免只留下冲突表。
    tail = [p for p in outside if p.text.startswith(("**当前保留", "**不纳入"))]
    if tail:
        p = doc.piece(tail[0].start-1, tail[-1].end)
        units.append(Unit("LIMITS-001", "本知识库的未知项与适用边界", "limitations", s, p, []))
    by_key = {u.key: u for u in units}
    for cells, body in conflicts:
        key = cells[0]
        if key not in CONFLICT_TARGETS:
            raise ValueError(f"新冲突 {key} 尚未配置关联条目，停止以免漏附纠正信息")
        for target in CONFLICT_TARGETS[key]:
            if target not in by_key:
                raise ValueError(f"冲突 {key} 的目标 {target} 不存在")
            by_key[target].context.append(Piece(body.text, body.start, body.end, "source_correction"))
        units.append(Unit(key, f"来源差异 {key}：{cells[2]}", "source_correction", s, body, [], True))

    # 新增章节时要求显式登记规则，不静默跳过。
    handled = {id(u.section) for u in units}
    allowed = {"2.1 ", "2.2 ", "3. ", "3.2 ", "4. ", "6. "}
    for s in doc.sections:
        if s.level == 1 or s.title.startswith(("9. ", "10. ", "S0")):
            continue
        if id(s) not in handled and not any(s.title.startswith(x) for x in allowed):
            raise ValueError(f"未处理的新章节：{s.title}")
    return units


def split_prose(piece: Piece, limit: int) -> list[Piece]:
    """仅长叙述段落细分；表格、列表和代码块不可在内部机械切断。

    先按空行分块，再尝试按完整句子分；不按字符硬截，也不改写。
    上限是软限制：不可拆的结构或单句过长时保留，并在报告中提示。
    """
    if len(piece.text) <= limit:
        return [piece]
    lines = piece.text.splitlines(keepends=True)
    blocks, buf, in_fence, start = [], [], False, piece.start
    for offset, line in enumerate(lines):
        if line.startswith("```"):
            in_fence = not in_fence
        if not line.strip() and not in_fence:
            if buf:
                blocks.append(Piece("".join(buf).strip(), start, piece.start+offset-1))
                buf = []
            start = piece.start+offset+1
        else:
            buf.append(line)
    if buf:
        blocks.append(Piece("".join(buf).strip(), start, piece.end))
    atoms = []
    for block in blocks:
        protected = any(re.match(r"^(\||```|\s*[-*] |\d+\. )", l) for l in block.text.splitlines())
        if len(block.text) > limit and not protected:
            sentences = re.split(r"(?<=[。！？])", block.text)
            offset = 0
            for sentence in sentences:
                if sentence.strip():
                    begin = block.start + block.text[:offset].count("\n")
                    atoms.append(Piece(sentence.strip(), begin, begin+sentence.count("\n")))
                offset += len(sentence)
        else:
            atoms.append(block)
    result, current = [], []
    for atom in atoms:
        if current and sum(len(p.text)+2 for p in current)+len(atom.text) > limit:
            result.append(Piece("\n\n".join(p.text for p in current), current[0].start, current[-1].end))
            current = []
        current.append(atom)
    if current:
        result.append(Piece("\n\n".join(p.text for p in current), current[0].start, current[-1].end))
    return result


def entities(text: str) -> list[str]:
    found = set(re.findall(r"\b(?:XMEAS|XMV|IDV)\(\d+\)|\bX\d+\b", text))
    found = {f"X{int(e[1:])}" if re.fullmatch(r"X\d+", e) else e for e in found}
    # X23–X28 等区间不能只索引两端。
    for a, b in re.findall(r"\bX(\d+)\s*[–—-]\s*X?(\d+)", text):
        if 1 <= int(a) <= int(b) <= 52:
            found.update(f"X{i}" for i in range(int(a), int(b)+1))
    for number in re.findall(r"流\s*(\d+)", text):
        found.add(f"STREAM-{int(number):02}")
    for first, rest in re.findall(r"IDV\((\d+)\)((?:/\(\d+\))+)", text):
        found.update(f"IDV({n})" for n in [first, *re.findall(r"\d+", rest)])
    for a, b in re.findall(r"IDV\((\d+)\)\s*[–—-]\s*(?:IDV)?\((\d+)\)", text):
        if 1 <= int(a) <= int(b) <= 21:
            found.update(f"IDV({n})" for n in range(int(a), int(b)+1))
    return sorted(found)


def build(document: Path, source_path: Path, max_chars=2000):
    if max_chars < 200:
        raise ValueError("--max-chars 至少为 200（字符，不是 token）")
    doc = Handbook(document)
    registry = json.loads(source_path.read_text(encoding="utf-8"))
    if (registry["document_id"], registry["document_version"]) != (doc.meta["document_id"], doc.meta["version"]):
        raise ValueError("来源清单与手册版本不一致")
    sources = {s["source_id"]: s for s in registry["sources"]}
    chunks, warnings = [], []
    units = units_from(doc)
    for unit in units:
        context = list({(p.start, p.end, p.text): p for p in unit.context}.values())
        context_text = "\n\n".join(f"【{ROLE_LABELS.get(p.role, p.role)}】\n{p.text}" for p in context)
        budget = max(1, max_chars-len(unit.title)-len(context_text)-20)
        parts = [unit.body] if unit.atomic else split_prose(unit.body, budget)
        source_text = unit.body.text + "\n" + context_text
        mentions = re.findall(r"\[([^\]]+)\]\(#src-(s\d+)\)", source_text, re.I)
        source_ids = set(re.findall(r"\bS\d{2,}\b", source_text))
        if source_ids - sources.keys():
            raise ValueError(f"{unit.key} 引用了未登记来源：{source_ids-sources.keys()}")
        resolved = [dict(sources[sid], mentions=[label for label, anchor in mentions if anchor.upper()==sid])
                    for sid in sorted(source_ids)]
        for i, part in enumerate(parts, 1):
            suffix = f":p{i:02}" if len(parts)>1 else ""
            content = f"{unit.title}\n\n{part.text}"
            if context_text:
                content += "\n\n【继承的限定与来源】\n"+context_text
            if len(parts)>1:
                content += f"\n\n同一知识单元共 {len(parts)} 段；来源与适用范围以父条目 {unit.key} 为准。"
            # 所有片段中的来源锚点改为真实手册路径，独立显示不产生悬空链接。
            content = re.sub(r"\]\(#src-(s\d+)\)", lambda m:f"]({doc.path}#src-{m[1]})", content)
            for target in re.findall(r"\]\(([^)]+)\)", content):
                if target.startswith(("http:", "https:", "/", "#")):
                    continue
                content = content.replace(f"]({target})", f"]({doc.path.parent / target})")
            lineages = [dict(role=p.role, start_line=p.start, end_line=p.end)
                        for p in [part, *context]]
            if unit.body.role == "table_row":
                header_line = next(i+1 for i in range(unit.section.start+1, unit.section.direct_end)
                                   if doc.lines[i].startswith("|"))
                lineages.append(dict(role="table_header", start_line=header_line, end_line=header_line))
            chunk = {
                "chunk_id": f"{doc.meta['document_id']}:{unit.key}:v{doc.meta['version']}:{VERSION}{suffix}",
                "unit_id": unit.key, "document_id": doc.meta["document_id"],
                "document_version": doc.meta["version"], "chunker_version": VERSION,
                "title": unit.title, "kind": unit.kind, "heading_path": unit.section.path,
                "scope": doc.meta["scope"], "review_status": doc.meta["status"],
                "part": i, "parts": len(parts), "content": content,
                "content_sha256": sha(content), "char_count": len(content),
                "entities": sorted(set([unit.key, *entities(unit.title+"\n"+unit.body.text)])),
                "sources": resolved,
                "provenance": {"document_path": str(doc.path), "document_sha256": sha(doc.raw), "spans": lineages},
            }
            if len(content) > max_chars:
                warnings.append({"chunk_id":chunk["chunk_id"], "chars":len(content),
                                 "reason":"保留不可拆结构或必要上下文，超过字符软上限"})
            chunks.append(chunk)
    validate(chunks, doc)
    counts = Counter(c["kind"] for c in chunks)
    lengths = sorted(c["char_count"] for c in chunks)
    manifest = {
        "document_id":doc.meta["document_id"], "document_version":doc.meta["version"],
        "chunker_version":VERSION, "input_sha256":sha(doc.raw),
        "sources_sha256":sha(source_path.read_text(encoding="utf-8")),
        "max_chars_soft_limit":max_chars, "size_measure":"Unicode characters, not tokens",
        "chunk_count":len(chunks), "unit_count":len(units), "counts_by_kind":dict(counts),
        "char_stats":{"min":lengths[0],"median":lengths[len(lengths)//2],"max":lengths[-1]},
        "checks":{"unique_chunk_ids":True,"variables_52":True,"faults_21":True,
                  "streams_11":True,"utilities_2":True,"equipment_5":True,
                  "fault_boundaries_present":True,"provenance_lines_valid":True},
        "warnings":warnings,
        "excluded":[{"section":"引言、阅读路径、来源登记、交付状态","reason":"不作为领域检索正文；来源登记进入元数据"},
                    {"section":"3.2 Mermaid 结构图","reason":"本轮为文本切分；完整流程文字与流股表已纳入，图保留在原手册"}],
        "status":"本地切分完成，未接入在线问答；尚未做检索效果评测",
    }
    return chunks, manifest


def validate(chunks, doc):
    ids=[c["chunk_id"] for c in chunks]
    if len(ids)!=len(set(ids)):
        raise ValueError("chunk_id 重复")
    expected = {"variable":{f"VAR-X{i:02}" for i in range(1,53)},
                "fault":{f"FAULT-IDV{i:02}" for i in range(1,22)},
                "stream":{f"STREAM-{i:02}" for i in range(1,12)},
                "utility":{"UTILITY-12","UTILITY-13"},
                "equipment":{f"EQUIP-{s}" for s in ["REACTOR","CONDENSER","SEPARATOR","COMPRESSOR","STRIPPER"]}}
    for kind, keys in expected.items():
        if {c["unit_id"] for c in chunks if c["kind"]==kind} != keys:
            raise ValueError(f"{kind} 覆盖检查失败")
    for c in chunks:
        if c["kind"]=="fault" and not all(t in c["content"] for t in ["预设注入", "可观测性", "解释边界"]):
            raise ValueError(f"故障限定被截断：{c['unit_id']}")
        for span in c["provenance"]["spans"]:
            if not 1<=span["start_line"]<=span["end_line"]<=len(doc.lines):
                raise ValueError("来源行号越界")
        if c["kind"] in expected and not c["sources"]:
            raise ValueError(f"{c['unit_id']} 缺少来源")


def preview(chunks, manifest):
    counts = "、".join(f"{KIND_LABELS[k]} {v}" for k,v in manifest["counts_by_kind"].items())
    lines = ["# TEP 切分结果预览", "", f"共 **{len(chunks)} 个 chunk**。下方每个编号条目对应 JSONL 中的一条记录。",
             "", "切分不调用大模型、不改写领域事实；表格行按原表头展开。正文下方保留了继承的单位、边界与来源。",
             "", f"类型统计：{counts}。", "", f"字符数（不是 token）：{manifest['char_stats']}。", "",
             "## 先看三个实际样例", ""]
    for key in ["VAR-X04", "FAULT-IDV07", "VAR-X22"]:
        c=next(c for c in chunks if c["unit_id"]==key)
        lines.extend([f"### 样例：{c['title']}", "", c["content"], "", f"编号：`{c['chunk_id']}`", "",
                      f"关联实体：{', '.join(c['entities'])}", "", f"来源：{', '.join(s['source_id'] for s in c['sources'])}", ""])
    lines.extend(["## 全部切分结果", ""])
    for n,c in enumerate(chunks,1):
        span=c["provenance"]["spans"][0]
        location=f"{c['provenance']['document_path']}:{span['start_line']}"
        lines.extend([f"### {n:03} · {c['title']}", "", f"`{c['chunk_id']}` · {c['char_count']} 字符 · {c['kind']}", "",
                      f"[定位手册原文]({location}) · 原文行 {span['start_line']}–{span['end_line']}", "", c["content"], "",
                      "来源元数据：", ""])
        for s in c["sources"]:
            address=s.get('url') or s.get('path')
            locator='；'.join(s['mentions']) or s.get('locator','')
            lines.append(f"- [{s['source_id']}]({address})：{locator}")
        if not c['sources']:
            lines.append("- 本手册编辑整理的范围或方法说明；通过原文定位追溯，不冒充外部文献结论。")
        lines.extend(["", "---", ""])
    return "\n".join(lines)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,default=BASE/'TEP_SOURCE_MAP.md')
    parser.add_argument('--sources',type=Path,default=BASE/'docs/knowledge_sources.json')
    parser.add_argument('--output-dir',type=Path,default=BASE/'knowledge_build')
    parser.add_argument('--max-chars',type=int,default=2000,help='完整片段的字符软上限；保留原子条目优先')
    args=parser.parse_args()
    try:
        chunks, manifest=build(args.input,args.sources,args.max_chars)
    except (ValueError,KeyError,OSError) as e:
        parser.exit(1,f'切分失败，未发布新产物：{e}\n')
    payload=''.join(json.dumps(c,ensure_ascii=False,sort_keys=True)+'\n' for c in chunks)
    manifest['chunks_sha256']=sha(payload)
    products={'chunks.jsonl':payload,'preview.md':preview(chunks,manifest),
              'manifest.json':json.dumps(manifest,ensure_ascii=False,indent=2)+'\n'}
    out=args.output_dir.resolve()
    if out == args.input.resolve().parent and args.input.name in products:
        parser.exit(1,'输出路径会覆盖输入文件\n')
    out.mkdir(parents=True,exist_ok=True)
    # 所有检查通过后才写；每个文件采用临时文件替换，manifest 最后发布。
    # 下游读者还应核对 manifest 的 chunks_sha256，避免读到更新中的不同批次。
    for name,text in products.items():
        with tempfile.NamedTemporaryFile('w',encoding='utf-8',dir=out,delete=False) as f:
            f.write(text)
            temp=Path(f.name)
        temp.replace(out/name)
    print(json.dumps({'output_dir':str(out),'chunks':len(chunks),'by_kind':manifest['counts_by_kind'],
                      'characters':manifest['char_stats'],'warnings':len(manifest['warnings'])},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
