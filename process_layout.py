"""Approved compact TEP layout. Coordinates share the existing 8-second animation hooks."""

def render_process_svg():
    svg=['''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1550 920" class="tep-svg" role="group" aria-label="TEP主设备和物流连接">
    <defs>
    <marker id="main-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#969386"/></marker>
    <marker id="return-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#7d886e"/></marker>
    <marker id="product-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#b65e42"/></marker>
    </defs><style>.tep-svg text{font-family:system-ui,-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;fill:#45443e} .tep-svg .pipe{fill:none;stroke-width:3;stroke-linecap:round;stroke-linejoin:round} .tep-svg .main{stroke:#969386;marker-end:url(#main-arrow)} .tep-svg .return{stroke:#7d886e;marker-end:url(#return-arrow)} .tep-svg .product{stroke:#b65e42;marker-end:url(#product-arrow)} .tep-svg .shell{fill:#faf9f5;stroke:#67665f;stroke-width:2.5} .tep-svg .inside{fill:none;stroke:#aaa597;stroke-width:2} .tep-svg .label{font-size:19px} .tep-svg .minor{font-size:17px;fill:#777569} .tep-svg .device-name{font-size:26px;font-weight:600;letter-spacing:.4px} .tep-svg .num{fill:#faf9f5;font-size:20px;font-weight:600} .tep-svg .note{font-size:16px;fill:#888477}</style>
    <rect width="1550" height="920" fill="#faf9f5"/><g transform="translate(-50 0)">
    ''']
    pipe_keys=iter(('feed-a','feed-d','feed-e','mixed','react-out','condensed','gas','recycle','purge','liquid','top-return','strip-feed','product'))
    def pipe(d,kind='main',arrow=True):
     extra='' if arrow else ' style="marker-end:none"'
     key=next(pipe_keys)
     flow_kind='recycle' if kind=='return' else kind
     bridge=f'<path class="tep-pipe-clear" d="{d}"/>' if key=='top-return' else '' 
     svg.append(f'<g class="tep-pipe tep-{flow_kind}" data-pipe="{key}">'
                f'{bridge}'
                f'<path class="pipe {kind}" d="{d}"{extra}/>'
                f'<path class="tep-trace tep-timed" pathLength="1000" d="{d}"/>'
                f'<path class="tep-flow tep-timed" pathLength="1000" d="{d}"/></g>')
    def txt(x,y,s,cl='label',anchor='middle'):
     svg.append(f'<text class="{cl}" x="{x}" y="{y}" text-anchor="{anchor}">{s}</text>')
    def title(x,y,num,name):
     svg.append(f'<rect x="{x}" y="{y-25}" width="42" height="34" rx="7" fill="#7d886e"/>')
     txt(x+21,y,num,'num');txt(x+56,y+1,name,'device-name','start')
    # Material connections; arrows follow physical flow direction.
    pipe('M270 285 H295 Q315 285 315 305 V380 Q315 400 335 400 H350',arrow=False)
    pipe('M270 400 H350',arrow=False)
    pipe('M270 515 H295 Q315 515 315 495 V420 Q315 400 335 400 H350',arrow=False)
    pipe('M350 400 H510')
    pipe('M650 400 H810')
    pipe('M970 400 H1100')
    pipe('M1150 310 V165 Q1150 145 1130 145 H901','return')
    pipe('M799 145 H370 Q350 145 350 165 V400','return')
    pipe('M1150 220 H1530')
    pipe('M1150 490 V600 Q1150 620 1170 620 H1330')
    # Bridge at the liquid line makes the non-connection explicit.
    pipe('M1380 570 V566 Q1380 550 1364 550 H1164 Q1150 524 1136 550 H370 Q350 550 350 530 V400','return')
    pipe('M380 780 H1260 Q1280 780 1280 760 V740 Q1280 720 1300 720 H1330')
    pipe('M1380 760 V790 Q1380 810 1400 810 H1550','product')
    svg.append('<circle cx="1150" cy="220" r="4" fill="#969386"/><circle cx="350" cy="400" r="5" fill="#7d886e"/>')
    # Feeds and mixing junction.
    for y,n,c in [(250,1,'A'),(365,2,'D'),(480,3,'E')]:
     svg.append(f'<rect x="90" y="{y}" width="180" height="70" rx="10" fill="#f1efe6" stroke="#ccc8bb" stroke-width="1.5"/>')
     txt(180,y+42,f'流{n}（{c}原料进料）','minor')
    txt(333,438,'进料汇合','minor','end')
    svg.append('<rect x="90" y="752" width="290" height="56" rx="10" fill="#f1efe6" stroke="#ccc8bb" stroke-width="1.5"/>')
    txt(235,787,'流4（A/C进料，含B）')
    # Keep the separator title gap opaque even when another device is selected.
    svg.append('<rect x="1035" y="239" width="264" height="52" fill="#faf9f5"/>')
    # Reactor.
    svg.append('<g class="tep-equipment" data-equipment="reactor" role="button" tabindex="0" aria-label="了解反应器" aria-pressed="false"><title>反应器：点击查看作用与进出物流</title><rect class="tep-pulse tep-timed" x="492" y="207" width="180" height="305" rx="16"/><rect class="tep-hit" x="492" y="207" width="180" height="305" rx="16"/>')
    
    svg.append('<rect class="shell" x="510" y="300" width="140" height="200" rx="42"/><path class="inside" d="M580 300 V460 M538 365 H604 Q625 365 625 385 Q625 405 604 405 H552 Q530 405 530 427 Q530 449 552 449 H608 M555 460 H605"/>')
    title(492,240,'01','反应器');txt(580,275,'冷却水移热','minor')
    svg.append('</g>')
    # Condenser.
    svg.append('<g class="tep-equipment" data-equipment="condenser" role="button" tabindex="0" aria-label="了解冷凝器" aria-pressed="false"><title>冷凝器：点击查看作用与进出物流</title><rect class="tep-pulse tep-timed" x="796" y="265" width="190" height="190" rx="16"/><rect class="tep-hit" x="796" y="265" width="190" height="190" rx="16"/>')
    
    svg.append('<rect class="shell" x="810" y="360" width="160" height="80" rx="32"/><path class="inside" d="M835 364 V436 M850 364 V436 M930 364 V436 M945 364 V436 M850 382 H930 M850 400 H930 M850 418 H930"/>')
    title(796,301,'02','冷凝器');txt(890,337,'冷却水换热','minor')
    svg.append('</g>')
    # Separator.
    svg.append('<g class="tep-equipment" data-equipment="separator" role="button" tabindex="0" aria-label="了解汽液分离器" aria-pressed="false"><title>汽液分离器：点击查看作用与进出物流</title><rect class="tep-pulse tep-timed" x="1035" y="232" width="264" height="270" rx="16"/><rect class="tep-hit" x="1035" y="232" width="264" height="270" rx="16"/>')
    
    svg.append('<rect class="shell" x="1100" y="310" width="100" height="180" rx="35"/><path d="M1103 417 H1197 V456 Q1197 487 1168 487 H1132 Q1103 487 1103 456Z" fill="#e6e9de"/><path class="inside" d="M1103 417 H1197"/>')
    title(1045,271,'03','汽液分离器')
    svg.append('</g>')
    # Compressor points left in the return direction.
    svg.append('<g class="tep-equipment" data-equipment="compressor" role="button" tabindex="0" aria-label="了解循环压缩机" aria-pressed="false"><title>循环压缩机：点击查看作用与进出物流</title><rect class="tep-pulse tep-timed" x="747" y="28" width="223" height="176" rx="16"/><rect class="tep-hit" x="747" y="28" width="223" height="176" rx="16"/>')
    
    svg.append('<circle class="shell" cx="850" cy="145" r="50"/><path class="inside" d="M872 119 L827 145 L872 171Z"/>')
    title(755,62,'04','循环压缩机')
    svg.append('</g>')
    # Stripper.
    svg.append('<g class="tep-equipment" data-equipment="stripper" role="button" tabindex="0" aria-label="了解汽提塔" aria-pressed="false"><title>汽提塔：点击查看作用与进出物流</title><rect class="tep-pulse tep-timed" x="1290" y="474" width="156" height="297" rx="16"/><rect class="tep-hit" x="1290" y="474" width="156" height="297" rx="16"/>')
    
    svg.append('<rect class="shell" x="1330" y="570" width="100" height="190" rx="30"/><path class="inside" d="M1333 607 H1408 M1352 640 H1427 M1333 673 H1408 M1352 706 H1427 M1344 738 H1416"/>')
    title(1298,507,'05','汽提塔')
    svg.append('</g>')
    svg.append('<path d="M1558 676 H1435" fill="none" stroke="#bca890" stroke-width="2" stroke-dasharray="5 6" marker-end="url(#product-arrow)"/>')
    txt(1510,654,'蒸汽供热','minor')
    # Stream labels are placed in whitespace, independently of equipment headings.
    txt(435,380,'流6（混合进料）','minor')
    txt(730,380,'流7（反应器出料）','minor')
    txt(1035,380,'冷凝后')
    txt(1040,123,'未凝气相','minor')
    txt(565,122,'流8（循环气）')
    txt(1375,202,'流9（排放气）');txt(1542,225,'排放','label','start')
    txt(1240,603,'流10（液相）','minor')
    txt(850,581,'流5（塔顶返回）')
    txt(1417,851,'流11（G/H产品）','label')
    txt(90,896,'示意图省略仪表、泵阀及压缩机旁路。箭头表示物料流向。','note','start')
    svg.append('</g></svg>')
    return ''.join(svg)
