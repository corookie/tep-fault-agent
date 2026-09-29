const form = document.getElementById('question-form');
const log = document.getElementById('chat-log');
const deployment = window.TEP_DEPLOYMENT || {};
function apiUrl(path) {
  return (deployment.apiBase || '') + path;
}
let lastQuestion = '';
const resetButton = document.getElementById('reset-chat');
resetButton.addEventListener('click', () => {
  lastQuestion = '';
  log.replaceChildren();
  addMessage('assistant', '你好，我是TEP智能助手，可以回答工艺流程、变量含义和预设故障相关问题。例如：IDV(7)是什么故障？');
});
function addMessage(role, content, sources = []) {
  const bubble = document.createElement('div');
  bubble.className = 'message ' + role;
  bubble.textContent = content;
  if (sources.length) {
    addSources(bubble, sources);
  }
  log.appendChild(bubble);
  log.scrollTop = log.scrollHeight;
  return bubble;
}
function addSources(bubble, sources) {
  const details = document.createElement('details');
  details.className = 'sources';
  const heading = document.createElement('summary');
  heading.textContent = '查看依据（' + sources.length + '）';
  const list = document.createElement('ul');
  for (const source of sources) {
    const item = document.createElement('li');
    const title = document.createElement('div');
    title.textContent = (source.marker || '') + ' ' + (source.title || source.id);
    const location = document.createElement('small');
    location.textContent = source.source + ' · 知识手册 v' + source.document_version;
    const excerpt = document.createElement('p');
    excerpt.style.whiteSpace = 'pre-wrap';
    excerpt.textContent = source.content || '';
    item.append(title, location, excerpt);
    list.appendChild(item);
  }
  details.append(heading, list);
  bubble.appendChild(details);
}
if (deployment.staticMode && !deployment.apiBase) {
  log.replaceChildren();
  addMessage('assistant', '在线知识问答需要独立后端。本页面可直接体验工艺动画和故障诊断；完整问答可在本地运行源码。');
  form.elements.question.disabled = true;
  form.elements.question.placeholder = '公开预览暂未启用在线问答';
  form.querySelector('button[type="submit"]').disabled = true;
}
form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const question = form.elements.question.value.trim();
  if (!question) return;
  const button = form.querySelector('button');
  if (button.disabled) return;
  button.disabled = true;
  resetButton.disabled = true;
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 45000);
  addMessage('user', question);
  form.elements.question.value = '';
  const reply = addMessage('assistant', '正在查找资料并生成回答…');
  reply.classList.add('loading');
  try {
    if (deployment.staticMode && !deployment.apiBase) {
      throw new Error('GitHub Pages 目前仅提供工艺图和故障诊断演示。在线知识问答需要部署独立的安全后端。');
    }
    const response = await fetch(apiUrl('/api/ask'), {
      method: 'POST',
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
      body: new URLSearchParams({question, previous_question: lastQuestion}),
      signal: controller.signal,
      cache: 'no-store'
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || '问答失败，请重试');
    reply.classList.remove('loading');
    reply.textContent = data.answer;
    if (data.sources && data.sources.length) {
      addSources(reply, data.sources);
    }
    if (data.query && data.query.context_used && data.status === 'answered') {
      const interpretation = document.createElement('small');
      interpretation.textContent = '本次理解为：' + data.query.resolved_query;
      reply.appendChild(interpretation);
    }
    lastQuestion = data.next_question || '';
  } catch (error) {
    lastQuestion = '';
    reply.classList.remove('loading');
    reply.classList.add('error');
    reply.textContent = error.name === 'AbortError' ? '等待回答超时，请重试。' : (error.message || '问答失败，请重试');
  } finally {
    clearTimeout(timer);
    button.disabled = false;
    resetButton.disabled = false;
    form.elements.question.focus();
    log.scrollTop = log.scrollHeight;
  }
});
const diagnoseForm = document.getElementById('diagnose-form');
const diagnosisOutput = document.getElementById('diagnose-output');
const diagnosisStatus = document.getElementById('diagnose-status');
const emptyDiagnosis = document.getElementById('diagnose-empty');
emptyDiagnosis.hidden = Boolean(diagnosisOutput.textContent.trim());
function setDiagnosisStatus(text, error = false) {
  diagnosisStatus.textContent = text;
  diagnosisStatus.hidden = !text;
  diagnosisStatus.classList.toggle('error', error);
}
diagnoseForm.addEventListener('change', () => {
  if (diagnosisOutput.textContent.trim()) setDiagnosisStatus('参数已调整。点击“开始诊断”更新结果；下方仍是上一次诊断结果。');
});
diagnoseForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  const button = diagnoseForm.querySelector('button');
  if (button.disabled) return;
  const body = new URLSearchParams(new FormData(diagnoseForm));
  const controls = [...diagnoseForm.querySelectorAll('button, select')];
  controls.forEach(el => el.disabled = true);
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 45000);
  const output = diagnosisOutput;
  output.classList.add('is-loading');
  output.setAttribute('aria-busy', 'true');
  setDiagnosisStatus(deployment.staticMode
    ? '正在加载该参数组合的预计算诊断结果…'
    : '正在进行格兰杰因果检验，计算根源变量排名和候选传播路径…');
  try {
    const response = deployment.staticMode
      ? await fetch(`./diagnosis/${body.get('samples')}-${body.get('lag')}.json`, {signal: controller.signal, cache: 'no-store'})
      : await fetch(apiUrl('/api/diagnose'), {method: 'POST', body, signal: controller.signal, cache: 'no-store'});
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || '诊断失败');
    // HTML仅来自本服务的转义模板和诊断数值，不使用模型生成的HTML。
    output.innerHTML = data.html;
    emptyDiagnosis.hidden = true;
    setDiagnosisStatus('');
    output.scrollIntoView({behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block:'start'});
  } catch (error) {
    setDiagnosisStatus(error.name === 'AbortError' ? '分析超时，请重试。' : (error.message || '诊断失败，请重试'), true);
  } finally {
    clearTimeout(timer);
    controls.forEach(el => el.disabled = false);
    output.classList.remove('is-loading');
    output.setAttribute('aria-busy', 'false');
  }
});
// 委托到固定容器，新分析替换结果后不携带旧路径状态。
document.getElementById('diagnose-output').addEventListener('click', (event) => {
  const option = event.target.closest('.path-option');
  const reset = event.target.closest('.path-reset');
  if (!option && !reset) return;
  const scope = (option || reset).closest('.path-explorer');
  const active = option && option.getAttribute('aria-pressed') !== 'true';
  const nodes = active ? JSON.parse(option.dataset.pathNodes) : [];
  const nodeSet = new Set(nodes);
  const pairSet = new Set(nodes.slice(1).map((target, i) => nodes[i] + '>' + target));
  for (const edge of scope.querySelectorAll('.graph-edge')) {
    const selected = pairSet.has(edge.dataset.source + '>' + edge.dataset.target);
    edge.classList.toggle('path-active', Boolean(active && selected));
    edge.classList.toggle('path-muted', Boolean(active && !selected));
  }
  for (const node of scope.querySelectorAll('.graph-node')) {
    node.classList.toggle('path-active', Boolean(active && nodeSet.has(node.dataset.node)));
    node.classList.toggle('path-muted', Boolean(active && !nodeSet.has(node.dataset.node)));
  }
  for (const button of scope.querySelectorAll('.path-option')) {
    button.setAttribute('aria-pressed', String(Boolean(active && button === option)));
  }
  scope.querySelector('.path-reset').disabled = !active;
  scope.querySelector('.path-status').textContent = active
    ? '已选：' + nodes.join(' → ') + '。暖橙色为所选路径；其余关系已淡化。'
    : '当前显示全部关系，尚未选择路径。';
  if (active && window.innerWidth < 980) {
    scope.querySelector('.network-plot').scrollIntoView({block:'center', behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'});
  }
});

// 选题只填入编辑区，由用户决定发送；不会自动消耗模型额度。
document.addEventListener('click', event => {
  const sample = event.target.closest('[data-question]');
  if (sample) {
    if (form.querySelector('button[type="submit"]').disabled) return;
    form.elements.question.value = sample.dataset.question;
    const target = window.innerWidth < 700 ? form : document.getElementById('knowledge');
    target.scrollIntoView({block: window.innerWidth < 700 ? 'center' : 'start', behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'});
    form.elements.question.focus({preventScroll:true});
  }
  const zoom = event.target.closest('.graph-zoom');
  if (zoom) {
    const enlarged = zoom.closest('.path-explorer').classList.toggle('is-enlarged');
    zoom.setAttribute('aria-pressed', String(enlarged));
    zoom.textContent = enlarged ? '适配全图' : '放大图示';
  }
});
form.elements.question.addEventListener('keydown', event => {
  if (event.key === 'Enter' && !event.shiftKey && !event.isComposing) {
    event.preventDefault();
    form.requestSubmit();
  }
});
// 三个工作区共享一条导航，滚动和点击使用相同的当前区状态。
const navLinks = [...document.querySelectorAll('.main-nav a')];
let navScheduled = false;
function updateNavigation() {
  let current = navLinks[0];
  for (const link of navLinks) {
    if (document.querySelector(link.getAttribute('href')).getBoundingClientRect().top <= 160) current = link;
  }
  navLinks.forEach(link => {
    if (link === current) link.setAttribute('aria-current','location');
    else link.removeAttribute('aria-current');
  });
  navScheduled = false;
}
window.addEventListener('scroll', () => {
  if (!navScheduled) { navScheduled = true; requestAnimationFrame(updateNavigation); }
}, {passive:true});
updateNavigation();
