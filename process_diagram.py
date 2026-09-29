"""TEP 结构导览：依据知识手册 PROC-001 / STREAM-001，动画不编码实时工况。"""
import json
from process_layout import render_process_svg


# 8秒是一轮讲解的节奏，并非实际停留时间或流速。
FLOW_TIMING = {
    'feed-a': (0.05, 1.0), 'feed-d': (0.05, 1.0), 'feed-e': (0.05, 1.0),
    'mixed': (0.95, 1.35), 'react-out': (2.0, 2.65), 'condensed': (3.0, 3.55),
    'gas': (4.0, 4.45), 'recycle': (4.7, 5.9), 'purge': (4.0, 5.0),
    'liquid': (4.1, 4.85), 'strip-feed': (4.0, 4.85),
    'top-return': (5.5, 6.7), 'product': (6.0, 7.2),
}
DEVICE_TIMING = {'reactor': (1.35, 2.15), 'condenser': (2.65, 3.2),
                 'separator': (3.55, 4.3), 'compressor': (4.45, 5.0), 'stripper': (4.85, 6.2)}

EXPLANATIONS = {
    'overview': {'title': '原料、产物与工艺流程', 'eyebrow': 'PROCESS OVERVIEW',
                 'body': 'TEP模拟用A、C、D、E四种原料生产G、H两种液体产品，同时产生副产物F，系统中还含惰性组分B。A–H是模型中的化学组分代号，不能直接对应到具体商品名称。',
                 'note': '工艺流程：原料混合后进入反应器，出料经冷凝器冷却，再由汽液分离器分成气、液两相。部分气体经压缩机循环，另一部分排放；液体进入汽提塔，塔顶物料返回进料端，塔底输出G/H产品混合物。流4的新鲜A/C混合进料先进入汽提塔。', 'pipes': [], 'nodes': []},
    'reactor': {'title': '反应器：原料发生化学反应', 'eyebrow': '01 / FEED & REACTION',
                'body': 'A、D、E 三路新鲜进料与流5、流8两路返回物料汇合，形成流6。反应器中发生放热反应，冷却水隔着换热面带走热量；含产品和未反应组分的物料经流7进入冷凝器。',
                'note': '相关测量：X6 总进料流量 · X7 压力 · X8 液位 · X9 温度。',
                'pipes': ['feed-a','feed-d','feed-e','mixed','react-out','recycle','top-return'], 'nodes': ['reactor']},
    'condenser': {'title': '冷凝器：冷却反应器出料', 'eyebrow': '02 / COOLING & CONDENSATION',
                  'body': '冷凝器接收反应器的流7出料，通过独立冷却水侧换热，使可凝组分形成液相，再送入汽液分离器。冷凝器负责换热和相变，后面的分离器负责气液分相。',
                  'note': '相关测量：X22 冷凝冷却系统的冷却水出口温度；冷却水不与工艺物料混合。',
                  'pipes': ['react-out','condensed'], 'nodes': ['condenser','separator']},
    'separator': {'title': '汽液分离器：分开气体和液体', 'eyebrow': '03 / VAPOUR–LIQUID SEPARATION',
                  'body': '汽液分离器接收冷凝后的物料。未凝气相进入循环及排放支路，液相经流10进入汽提塔继续处理。这里的液体还不是最终产品。',
                  'note': '相关测量：X11 温度 · X12 液位 · X13 压力 · X14 液相流量。',
                  'pipes': ['condensed','gas','purge','liquid'], 'nodes': ['separator']},
    'compressor': {'title': '循环压缩机：将气体送回进料端', 'eyebrow': '04 / RECYCLE & PURGE',
                   'body': '分离器气相的一部分经循环压缩机返回进料混合处，形成流8；另一部分经流9排出系统。循环帮助回收物料，排放为惰性组分、副产物等提供出口。图中省略了压缩机旁路细节。',
                   'note': '相关测量：X5 循环流量 · X20 压缩机功率 · X10 排放流量。',
                   'pipes': ['gas','recycle','purge'], 'nodes': ['compressor','separator']},
    'stripper': {'title': '汽提塔：回收反应物并输出产品', 'eyebrow': '05 / STRIPPING & PRODUCT',
                 'body': '流10液相和流4的新鲜 A/C 混合进料进入汽提塔，在供热条件下回收残余反应物。塔顶流5返回进料混合处，塔底流11输出含 G/H 的产品混合物，后续精制不在本基准内。',
                 'note': '相关测量：X4 新鲜混合进料流量 · X16 塔压力 · X17 产品流量 · X18 塔温度。',
                 'pipes': ['liquid','strip-feed','top-return','product'], 'nodes': ['stripper']},
}


def render_process_diagram():
    tabs=''.join(f'<button type="button" data-process-step="{key}" aria-pressed="{"true" if key=="overview" else "false"}">{label}</button>'
                 for key,label in [('overview','总览'),('reactor','01 进料与反应'),('condenser','02 冷凝'),('separator','03 分相'),('compressor','04 循环'),('stripper','05 汽提与产品')])
    overview=EXPLANATIONS['overview']
    data=json.dumps(EXPLANATIONS,ensure_ascii=False).replace('<','\\u003c')
    return f'''<section id="tep-process" class="tep-process" aria-labelledby="tep-process-title" data-running="false">
<div class="tep-topline"><span class="tep-kicker">TENNESSEE EASTMAN PROCESS</span><span class="tep-disclaimer">8 秒流程演示 · 非实时工况</span></div>
<div class="tep-title-row"><h2 id="tep-process-title">TEP 过程介绍</h2><button type="button" id="tep-motion" aria-pressed="false" disabled>播放演示</button></div>
<p class="tep-intro">TEP（Tennessee Eastman Process，田纳西伊斯曼过程）是Eastman Chemical公司的J. J. Downs和E. F. Vogel提出的化工过程仿真模型，详细发表于1993年。它为过程控制研究提供统一的测试对象，本项目用它演示故障诊断。点击下图设备可查看作用和物流连接。</p>
<div class="tep-legend"><span><i class="tep-line-main"></i>主流程</span><span><i class="tep-line-recycle"></i>返回物流</span><span><i class="tep-line-product"></i>产品输出</span><button type="button" id="tep-zoom" aria-pressed="false" disabled>放大阅读</button></div>
<div class="tep-canvas" tabindex="0" role="region" aria-label="TEP工艺结构图，放大后可左右滚动">
{render_process_svg()}</div>
<div class="tep-timeline" aria-hidden="true"><span class="tep-timed"></span></div>
<div class="tep-timeline-labels" aria-hidden="true"><span>原料进入</span><span>反应 · 冷凝</span><span>分相 · 汽提</span><span>产品输出 ↻</span></div>
<div class="tep-steps" role="group" aria-label="选择流程步骤">{tabs}</div>
<div class="tep-explanation" aria-live="polite" aria-atomic="true"><span id="tep-caption-kicker" class="tep-kicker">{overview['eyebrow']}</span><h3 id="tep-caption-title">{overview['title']}</h3><p id="tep-caption-body">{overview['body']}</p><p id="tep-caption-note" class="tep-caption-note">{overview['note']}</p></div>
<div class="process-next"><button id="tep-ask" type="button" data-question="TEP的主要设备和工作流程是什么？">向助手询问TEP流程 ↗</button><a href="#diagnosis">进入IDV(7)故障诊断 →</a></div>
<p class="tep-source">参考：<a href="https://users.abo.fi/khaggblo/RS/Downs.pdf" target="_blank" rel="noopener">Downs &amp; Vogel（1993），A plant-wide industrial process control problem</a>；知识手册 §2–4及论文图2.3。图中箭头表示物料流向。</p>
<script type="application/json" id="tep-process-data">{data}</script>
</section>'''


PROCESS_CSS = '''
.tep-process{--tep-paper:#faf9f5;--tep-ink:#30302e;--tep-muted:#67665f;--tep-border:#e3e0d6;--tep-accent:#b65e42;background:var(--tep-paper);color:var(--tep-ink);border:1px solid var(--tep-border);border-radius:20px;padding:28px 26px 18px;margin:20px 0 30px;overflow:hidden}
.tep-topline,.tep-title-row,.tep-legend{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}.tep-kicker{font-size:10px;letter-spacing:1.6px;color:var(--tep-muted)}.tep-disclaimer{font-size:11px;color:var(--tep-muted)}.tep-title-row{margin-top:14px}.tep-process h2{font-family:Georgia,"Songti SC","SimSun",serif;font-size:27px;font-weight:500;line-height:1.4;margin:0}.tep-intro{font-size:14px;color:var(--tep-muted);margin:10px 0 22px;line-height:1.7}
.tep-process button{font-size:12px;min-height:36px;padding:8px 11px;border:1px solid var(--tep-border);background:transparent;color:var(--tep-ink);border-radius:8px;transition:background .2s,border-color .2s}.tep-process button:hover{background:#eeece3;border-color:#c9c5b9}.tep-process button:focus-visible,.tep-canvas:focus-visible{outline:2px solid var(--tep-accent);outline-offset:3px}.tep-process button:disabled{cursor:default}
.tep-legend{justify-content:flex-start;gap:16px;font-size:11px;color:var(--tep-muted)}.tep-legend span{display:flex;align-items:center;gap:7px}.tep-legend i{width:20px;height:2px;display:inline-block;background:#8b887f}.tep-legend .tep-line-recycle{background:#71816a}.tep-legend .tep-line-product{background:#be684b}.tep-legend button{margin-left:auto;font-size:11px;min-height:30px;padding:5px 9px}
.tep-canvas{overflow:auto;margin:12px -6px 0;scrollbar-width:thin;scrollbar-color:#b8b4a8 transparent}.tep-svg{width:100%;height:auto;display:block;overflow:visible}.tep-process.is-enlarged .tep-svg{min-width:1500px}.tep-svg text{font-family:system-ui,-apple-system,"Microsoft YaHei",sans-serif;fill:var(--tep-ink);font-size:18px}.tep-svg .tep-stream-label{font-size:17px;fill:var(--tep-muted);paint-order:stroke;stroke:var(--tep-paper);stroke-width:6px;stroke-linejoin:round}.tep-pipe{color:#8b887f;transition:opacity .35s}.tep-recycle{color:#71816a}.tep-product{color:#be684b}.tep-pipe-clear{fill:none;stroke:var(--tep-paper);stroke-width:9px}.tep-pipe-base{fill:none;stroke:currentColor;stroke-width:2;opacity:.6;stroke-linejoin:round}.tep-trace{fill:none;stroke:currentColor;stroke-width:3;stroke-dasharray:1000;stroke-dashoffset:1000;opacity:0;pointer-events:none}.tep-flow{fill:none;stroke:#b65e42;stroke-width:5;stroke-linecap:round;stroke-dasharray:40 1960;stroke-dashoffset:40;opacity:0;pointer-events:none}.tep-timed{animation-duration:8s;animation-timing-function:linear;animation-iteration-count:infinite;animation-play-state:paused}.tep-process[data-running="true"] .tep-timed{animation-play-state:running}.tep-pulse{fill:#f2e5d4;stroke:#c99277;stroke-width:1.5;opacity:0;pointer-events:none}.tep-process.has-focus .tep-pulse{display:none}.tep-product-finish{animation-name:tep-product-done}@keyframes tep-product-done{0%,86%,100%{fill:#faf9f5;stroke:#b8b3a6}90%,95%{fill:#edd6c2;stroke:#b65e42}}.tep-timeline{height:2px;background:#e4e0d5;margin-top:8px;overflow:hidden}.tep-timeline span{display:block;width:100%;height:100%;background:#b65e42;transform-origin:left;transform:scaleX(0);animation-name:tep-progress}.tep-timeline-labels{display:flex;justify-content:space-between;gap:8px;font-size:10px;color:#77746b;margin:9px 0 17px}@keyframes tep-progress{to{transform:scaleX(1)}}
.tep-equipment{cursor:pointer;outline:none;transition:opacity .35s}.tep-hit{fill:transparent;stroke:transparent;stroke-width:1.5;transition:fill .25s,stroke .25s}.tep-equipment:hover .tep-hit,.tep-equipment:focus-visible .tep-hit{fill:#efede5;stroke:#c4bfb0}.tep-equipment.is-selected .tep-hit{fill:#f1e8dd;stroke:#c99277}.tep-vessel{fill:var(--tep-paper);stroke:#5e5d59;stroke-width:2}.tep-internal{fill:none;stroke:#aaa598;stroke-width:1.7;stroke-linecap:round}.tep-liquid-fill{fill:#e8e7da}.tep-svg .tep-device-label{font-size:20px;font-weight:500}.tep-svg .tep-device-number{font-size:12px;fill:#969185;letter-spacing:1px}.tep-process.has-focus .tep-pipe:not(.is-related){opacity:.16}.tep-process.has-focus .tep-equipment:not(.is-related){opacity:.38}.tep-pipe.is-related .tep-pipe-base{stroke-width:2.5}.tep-boundaries{fill:var(--tep-paper);stroke:#b8b3a6;stroke-width:1.5}.tep-boundaries text{stroke:none}.tep-boundaries circle{fill:#8b887f;stroke:none}.tep-utilities{fill:none;stroke:#c4bfb1;stroke-width:1.3;stroke-dasharray:3 4}.tep-utilities text{stroke:none;fill:#77746b;font-size:15px}.tep-svg .tep-minor-label{font-size:15px;fill:#77746b}
.tep-steps{display:flex;flex-wrap:wrap;gap:7px;padding:16px 0;border-top:1px solid var(--tep-border)}.tep-steps button[aria-pressed="true"]{background:#30302e;border-color:#30302e;color:#faf9f5}.tep-explanation{border-left:2px solid var(--tep-accent);padding:3px 0 3px 18px;margin:10px 0 20px;min-height:172px}.tep-explanation h3{font-family:Georgia,"Songti SC","SimSun",serif;font-size:21px;font-weight:500;margin:8px 0;line-height:1.4}.tep-explanation p{font-size:14px;line-height:1.8;margin:0}.tep-explanation .tep-caption-note{font-size:12px;color:var(--tep-muted);margin-top:9px}.tep-source{font-size:11px!important;color:#77746b;line-height:1.6!important;margin:0;padding-top:14px;border-top:1px solid var(--tep-border)}
@media(max-width:600px){.tep-process{padding:20px 16px 16px}.tep-topline{gap:6px}.tep-title-row{align-items:flex-start}.tep-process h2{font-size:23px}.tep-disclaimer{font-size:10px}.tep-title-row button{font-size:11px}.tep-legend{gap:10px}.tep-legend button{margin-left:0}.tep-explanation{min-height:240px;padding-left:13px}.tep-explanation h3{font-size:19px}.tep-steps button{min-height:40px}.tep-intro{margin-bottom:16px}}
@media(prefers-reduced-motion:reduce){.tep-process *, .tep-process *::before{transition:none!important}}
'''


# 各线路共用8秒时钟；每轮依次到达设备，末尾留0.8秒让画面静下来。
for _key, (_start, _end) in FLOW_TIMING.items():
    _a, _b = _start / 8 * 100, _end / 8 * 100
    PROCESS_CSS += (
        f'.tep-pipe[data-pipe="{_key}"] .tep-trace{{animation-name:tep-trace-{_key}}}'
        f'@keyframes tep-trace-{_key}{{'
        f'0%,{_a:.3f}%{{stroke-dashoffset:1000;opacity:0}}'
        f'{_a+.01:.3f}%{{stroke-dashoffset:1000;opacity:.85}}'
        f'{_b:.3f}%,94%{{stroke-dashoffset:0;opacity:.85}}'
        f'98%,100%{{stroke-dashoffset:0;opacity:0}}}}'
        f'.tep-pipe[data-pipe="{_key}"] .tep-flow{{animation-name:tep-flow-{_key}}}'
        f'@keyframes tep-flow-{_key}{{'
        f'0%,{_a:.3f}%{{stroke-dashoffset:40;opacity:0}}'
        f'{_a+.01:.3f}%{{stroke-dashoffset:40;opacity:.95}}'
        f'{_b:.3f}%{{stroke-dashoffset:-1000;opacity:.95}}'
        f'{_b+.01:.3f}%,100%{{stroke-dashoffset:-1000;opacity:0}}}}'
    )
for _key, (_start, _end) in DEVICE_TIMING.items():
    _a, _b = _start / 8 * 100, _end / 8 * 100
    PROCESS_CSS += (
        f'.tep-equipment[data-equipment="{_key}"] .tep-pulse{{animation-name:tep-unit-{_key}}}'
        f'@keyframes tep-unit-{_key}{{0%,{_a:.3f}%{{opacity:0}}'
        f'{_a+2:.3f}%,{_b:.3f}%{{opacity:1}}{_b+3:.3f}%,100%{{opacity:0}}}}'
    )


PROCESS_JS = '''
(() => {
  const panel = document.getElementById('tep-process');
  if (!panel) return;
  const explanations = JSON.parse(document.getElementById('tep-process-data').textContent);
  const motion = document.getElementById('tep-motion');
  const zoom = document.getElementById('tep-zoom');
  const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
  let wantsMotion = !preference.matches;
  let inView = true;
  function updateMotion() {
    panel.dataset.running = String(wantsMotion && inView && !document.hidden);
    motion.textContent = wantsMotion ? '暂停演示' : '播放演示';
    motion.setAttribute('aria-pressed', String(wantsMotion));
  }
  motion.disabled = false;
  zoom.disabled = false;
  motion.addEventListener('click', () => { wantsMotion = !wantsMotion; updateMotion(); });
  preference.addEventListener('change', () => { wantsMotion = !preference.matches; updateMotion(); });
  document.addEventListener('visibilitychange', updateMotion);
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(entries => { inView = entries[0].isIntersecting; updateMotion(); }, {threshold:0}).observe(panel);
  }
  zoom.addEventListener('click', () => {
    const enlarged = panel.classList.toggle('is-enlarged');
    zoom.textContent = enlarged ? '适配全图' : '放大阅读';
    zoom.setAttribute('aria-pressed', String(enlarged));
  });
  function selectStep(key) {
    const info = explanations[key];
    if (!info) return;
    panel.classList.toggle('has-focus', key !== 'overview');
    panel.querySelectorAll('[data-pipe]').forEach(el => el.classList.toggle('is-related', info.pipes.includes(el.dataset.pipe)));
    panel.querySelectorAll('[data-equipment]').forEach(el => {
      el.classList.toggle('is-related', info.nodes.includes(el.dataset.equipment));
      el.classList.toggle('is-selected', el.dataset.equipment === key);
      el.setAttribute('aria-pressed', String(el.dataset.equipment === key));
    });
    panel.querySelectorAll('[data-process-step]').forEach(el => el.setAttribute('aria-pressed', String(el.dataset.processStep === key)));
    document.getElementById('tep-caption-kicker').textContent = info.eyebrow;
    document.getElementById('tep-caption-title').textContent = info.title;
    document.getElementById('tep-caption-body').textContent = info.body;
    document.getElementById('tep-caption-note').textContent = info.note;
    const subjects = {reactor:'反应器',condenser:'冷凝器',separator:'汽液分离器',compressor:'循环压缩机',stripper:'汽提塔'};
    const ask = document.getElementById('tep-ask');
    ask.dataset.question = subjects[key] ? subjects[key] + '有什么作用？' : 'TEP的主要设备和工作流程是什么？';
    ask.textContent = subjects[key] ? '向助手询问' + subjects[key] + ' ↗' : '向助手询问TEP流程 ↗';
  }
  panel.addEventListener('click', event => {
    const target = event.target.closest('[data-process-step], [data-equipment]');
    if (target) selectStep(target.dataset.processStep || target.dataset.equipment);
  });
  panel.addEventListener('keydown', event => {
    const target = event.target.closest('[data-equipment]');
    if (target && (event.key === 'Enter' || event.key === ' ')) { event.preventDefault(); selectStep(target.dataset.equipment); }
  });
  updateMotion();
})();
'''
