"""从同一份诊断边表生成矩阵、网络和候选路径；不调用模型、不新增因果边。"""
import math
import json
from collections import deque
from html import escape

NAMES = {'X4':'混合进料流量','X7':'反应器压力','X13':'分离器压力','X16':'汽提塔压力',
         'X20':'压缩机功率','X45':'流4操纵量','X46':'压缩机循环阀'}


def graph_data(result, max_paths=24):
    variables = list(result['variables'])
    edges = [e for e in result['edges'] if e['selected']]
    pairs = {(e['source'], e['target']) for e in edges}
    adjacency = {v: [w for w in variables if (v,w) in pairs] for v in variables}
    matrix = [[int((source,target) in pairs) if source != target else None
               for source in variables] for target in variables]
    # 互相可达的节点属于同一强连通分量，不能把其中任意节点强行当唯一根源。
    reach = {}
    for v in variables:
        seen = set(); todo = list(adjacency[v])
        while todo:
            w = todo.pop()
            if w in seen: continue
            seen.add(w); todo.extend(adjacency[w])
        reach[v] = seen
    groups = []; assigned = set()
    for v in variables:
        if v in assigned: continue
        group = [w for w in variables if w == v or (w in reach[v] and v in reach[w])]
        assigned.update(group)
        if len(group) > 1: groups.append(group)
    candidates = [v for v in result['candidates'] if v in adjacency]
    # 每个起点按长度从短到长生成路径，再轮流取一条，避免截断只保留第一个起点。
    def paths_from(start):
        queue = deque([[start]])
        while queue:
            path = queue.popleft()
            next_nodes = [w for w in adjacency[path[-1]] if w not in path]
            if not next_nodes:
                if len(path)>1:
                    yield {'nodes':path, 'termination':'feedback' if adjacency[path[-1]] else 'terminal'}
            else:
                queue.extend(path+[w] for w in next_nodes)
    if max_paths < 1:
        raise ValueError('max_paths必须为正数')
    pending = [iter(paths_from(v)) for v in candidates]
    paths = []; seen_paths = set()
    while pending and len(paths) <= max_paths:
        active = []
        for iterator in pending:
            path = next(iterator, None)
            if path is None: continue
            active.append(iterator)
            key = tuple(path['nodes'])
            if key not in seen_paths:
                seen_paths.add(key); paths.append(path)
            if len(paths)>max_paths: break
        pending = active
    return {'variables':variables, 'edges':edges, 'matrix':matrix, 'feedback_groups':groups,
            'candidates':candidates, 'paths':paths[:max_paths], 'paths_truncated':len(paths)>max_paths,
            'isolated':[v for v in variables if not any(v in (e['source'],e['target']) for e in edges)]}


def matrix_svg(data):
    n=len(data['variables']); cell=54; left=108; top=24; width=left+n*cell+24; height=top+n*cell+98
    out=[f'<svg viewBox="0 0 {width} {height}" role="img" aria-label="格兰杰关系矩阵：列为驱动变量，行为结果变量" xmlns="http://www.w3.org/2000/svg">',
         '<title>格兰杰关系矩阵：1表示本次筛选通过，0表示未通过；对角线不检验</title>']
    for i,v in enumerate(data['variables']):
        out += [f'<text x="{left+i*cell+cell/2}" y="{top+n*cell+28}" text-anchor="middle" font-size="15">{escape(v)}</text>',
                f'<text x="{left-12}" y="{top+i*cell+cell/2+5}" text-anchor="end" font-size="15">{escape(v)}</text>']
    for row,target in enumerate(data['variables']):
        for col,source in enumerate(data['variables']):
            value=data['matrix'][row][col]; color='#b65e42' if value else '#eeece3' if value is None else '#e6e7da'
            label='—' if value is None else str(value)
            out.append(f'<g><title>{escape(source)} → {escape(target)}：{label}</title><rect x="{left+col*cell}" y="{top+row*cell}" width="{cell}" height="{cell}" fill="{color}" stroke="#faf9f5"/>'
                       f'<text x="{left+col*cell+cell/2}" y="{top+row*cell+cell/2+5}" text-anchor="middle" font-size="16" fill="{"white" if value else "#5e5d59"}">{label}</text></g>')
    out += [f'<text x="{left+n*cell/2}" y="{height-20}" text-anchor="middle" font-size="15">驱动变量（列）</text>',
            f'<text transform="translate(28 {top+n*cell/2}) rotate(-90)" text-anchor="middle" font-size="15">结果变量（行）</text>', '</svg>']
    return ''.join(out)


def network_svg(data):
    nodes=data['variables']; n=len(nodes)
    pos={v:(430+255*math.cos(-math.pi/2+i*2*math.pi/n),330+220*math.sin(-math.pi/2+i*2*math.pi/n)) for i,v in enumerate(nodes)}
    pairs={(e['source'],e['target']) for e in data['edges']}
    out=['<svg viewBox="0 0 860 660" role="img" aria-label="格兰杰因果关系图" xmlns="http://www.w3.org/2000/svg">',
         '<title>有向关系图；橄榄色虚线表示两个变量互为格兰杰因果，不代表已核实的物理控制回路</title>', '<defs>']
    for kind,color in [('edge','#9a968b'),('candidate','#b65e42'),('cycle','#7d886e'),('active','#b65e42')]:
        out.append(f'<marker id="arrow-{kind}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{color}"/></marker>')
    out.append('</defs>')
    for e in data['edges']:
        source,target=e['source'],e['target']; x,y=pos[source]; xx,yy=pos[target]
        dx,dy=xx-x,yy-y; length=math.hypot(dx,dy); ux,uy=dx/length,dy/length
        start=(x+32*ux,y+32*uy); end=(xx-36*ux,yy-36*uy)
        reciprocal=(target,source) in pairs
        kind='cycle' if reciprocal else 'candidate' if source in data['candidates'] else 'edge'
        color={'cycle':'#7d886e','candidate':'#b65e42','edge':'#9a968b'}[kind]
        if reciprocal:
            cx,cy=(x+xx)/2-uy*28,(y+yy)/2+ux*28
            d=f'M {start[0]:.2f} {start[1]:.2f} Q {cx:.2f} {cy:.2f} {end[0]:.2f} {end[1]:.2f}'
        else:d=f'M {start[0]:.2f} {start[1]:.2f} L {end[0]:.2f} {end[1]:.2f}'
        dash='stroke-dasharray="6 4"' if reciprocal else ''
        out.append(f'<path class="graph-edge" data-source="{escape(source)}" data-target="{escape(target)}" d="{d}" fill="none" stroke="{color}" stroke-width="2" {dash} marker-end="url(#arrow-{kind})"><title>{escape(source)} → {escape(target)}；预测误差降低 {e["improvement"]:.1%}；q={e["q_value"]:.4g}</title></path>')
    for v,(x,y) in pos.items():
        candidate=v in data['candidates']; color='#b65e42' if candidate else '#67665f'
        # 标签放在圆环外侧；连线在圆环内部，背景片进一步保护文字。
        if abs(y-330)>185:
            lx,ly,anchor=x,y+(-52 if y<330 else 56),'middle'
        else:
            lx,ly,anchor=x+(48 if x>430 else -48),y+5,('start' if x>430 else 'end')
        name=NAMES.get(v,v); label_width=len(name)*14+18
        left=lx-9 if anchor=='start' else lx-label_width+9 if anchor=='end' else lx-label_width/2
        out.append(f'<g class="graph-node" data-node="{escape(v)}"><title>{escape(v)}：{escape(name)}</title>'
                   f'<circle cx="{x:.2f}" cy="{y:.2f}" r="28" fill="{"#f2e5d9" if candidate else "#faf9f5"}" stroke="{color}" stroke-width="{2.5 if candidate else 1.5}"/>'
                   f'<text x="{x:.2f}" y="{y+5:.2f}" text-anchor="middle" fill="{color}" font-size="18">{escape(v)}</text>'
                   f'<rect class="node-label-bg" x="{left:.2f}" y="{ly-17:.2f}" width="{label_width}" height="25" rx="5" fill="#f7f6f0"/>'
                   f'<text class="node-name" x="{lx:.2f}" y="{ly:.2f}" text-anchor="{anchor}" fill="#5e5d59" font-size="14">{escape(name)}</text></g>')
    if data['edges']:
        out.append('<g class="graph-line-key" aria-label="实线表示变量间单向因果关系">'
                   '<path d="M 34 633 H 66" fill="none" stroke="#9a968b" stroke-width="2"/>'
                   '<text x="76" y="637" fill="#67665f" font-size="12">实线：变量间单向因果关系</text></g>')
    if any((target,source) in pairs for source,target in pairs):
        out.append('<g class="graph-cycle-key" aria-label="虚线表示变量间双向因果关系，互为因果">'
                   '<path d="M 330 633 H 362" fill="none" stroke="#7d886e" stroke-width="2" stroke-dasharray="6 4"/>'
                   '<text x="372" y="637" fill="#67665f" font-size="12">虚线：变量间双向因果关系，互为因果</text></g>')
    out.append('</svg>');return ''.join(out)


def render_graphs(result):
    data=graph_data(result)
    items=[]
    for index,p in enumerate(data['paths'],1):
        label=escape(' → '.join(p['nodes']))
        nodes=escape(json.dumps(p['nodes']), quote=True)
        note='<small>遇到统计反馈，停止展开</small>' if p['termination']=='feedback' else ''
        items.append(f'<li><button type="button" class="path-option" data-path-nodes="{nodes}" aria-pressed="false"><span class="path-number" aria-hidden="true">{index:02}</span><span>{label}</span></button>{note}</li>')
    paths='<ol class="path-list">'+''.join(items[:3])+'</ol>' if items else ''
    if len(items)>3:
        paths+='<details class="more-paths"><summary>展开其余候选路径（'+str(len(items)-3)+'条）</summary><ol class="path-list" start="4">'+''.join(items[3:])+'</ol></details>'
    if not data['edges']:message='当前窗口没有筛出关系，无法据此给出候选传播路径。可以增加采样点数后重新诊断。'
    elif not data['candidates']:message='已检出格兰杰因果关系，但没有变量满足根源排名条件，因此不强行指定根源变量。'
    else:message='点击路径，高亮图中对应的变量和箭头。再次点击取消。'
    cycles='；'.join('、'.join(g) for g in data['feedback_groups']) or '未发现'
    truncated='<p class="path-status">最多保留24条，轮流覆盖候选起点，不按可信度排序。</p>' if data['paths_truncated'] else ''
    network=('<section class="card path-explorer"><div class="result-heading"><div><h2>格兰杰因果关系图</h2></div><button type="button" class="graph-zoom" aria-pressed="false">放大图示</button></div>'
             '<div class="graph-legend"><span><i class="legend-node"></i>可能的根源变量</span><span>A → B：A是B的格兰杰因，B是A的格兰杰果。</span></div>'
             '<p class="plot-hint">可放大图示并左右滑动查看细节。</p><div class="network-layout"><div class="network-plot">'+network_svg(data)+'</div>'
             '<aside class="path-sidebar"><h3>候选故障传播路径</h3><p>'+message+'</p>'+
             ('<button type="button" class="path-reset" disabled>显示全部关系</button><p class="path-status" role="status">当前显示全部关系，尚未选择路径。</p>' if items else '')+paths+truncated+
             ('<p class="path-status">先展示3条路径，可展开其余路径。显示顺序不代表可信度。</p>' if items else '')+'</aside></div>'
             '<p class="feedback-note">包含循环关系的变量组：'+escape(cycles)+'。候选路径由图中的箭头连接得到，需结合工艺验证是否为实际故障传播路径。</p></section>')
    matrix=('<details class="card evidence-section"><summary>查看格兰杰因果关系矩阵</summary><div class="matrix-and-guide"><div class="matrix-plot">'+matrix_svg(data)+'</div>'
            '<div class="matrix-guide"><h3>按“列 → 行”读图</h3><p>列为驱动变量，行为结果变量。与上方有向图使用同一份结果。</p>'
            '<div class="matrix-key"><span><i class="selected">1</i> 筛选通过</span><span><i>0</i> 未通过</span></div><p>例如，若X4列、X20行为1，表示筛出了X4 → X20。0不等于证明没有因果关系；对角线不检验。</p></div></div></details>')
    return network+matrix
