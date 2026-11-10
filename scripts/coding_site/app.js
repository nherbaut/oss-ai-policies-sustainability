/* Plain DOM rendering: corpus text and memos are never interpreted as HTML. */
(() => {
  'use strict';
  const data = window.CODING_DATA;
  const $ = id => document.getElementById(id);
  const codes = new Map(data.codes.map(code => [code.id, code]));
  const state = { code: null, document: null };
  const collator = new Intl.Collator('en', { numeric: true, sensitivity: 'base' });
  const sorted = items => [...items].sort((a, b) => collator.compare(a.name, b.name));
  const color = code => /^#[0-9a-f]{6}$/i.test(code?.color || '') ? code.color : '#d9e9c5';
  function element(tag, text, className) {
    const node = document.createElement(tag);
    if (text !== undefined) node.textContent = text;
    if (className) node.className = className;
    return node;
  }
  function matchingCoding(coding) {
    return (state.code === null || coding.code === state.code) && (!$('coder').value || coding.owner === $('coder').value);
  }
  function matchingAnnotation(annotation) {
    return state.code === null && (!$('coder').value || annotation.owner === $('coder').value);
  }
  const counts = new Map();
  for (const doc of data.documents) {
    for (const coding of doc.codings) counts.set(coding.code, (counts.get(coding.code) || 0) + 1);
  }
  const s = data.summary;
  $('summary').textContent = `${s.documents} documents · ${s.codes} codes · ${s.categories} categories · ${s.codings} coded passages · ${s.annotations} annotations`;
  const owners = new Set(data.documents.flatMap(doc => [...doc.codings, ...doc.annotations].map(item => item.owner)));
  for (const owner of [...owners].sort(collator.compare)) {
    const option = element('option', owner || 'Unattributed');
    option.value = owner;
    // Empty attribution is displayed in passages but is not a distinct filter.
    if (owner) $('coder').append(option);
  }

  function addMemo(parent, memo) {
    if (!memo) return;
    const details = element('details');
    details.append(element('summary', 'Memo'), element('p', memo, 'memo'));
    parent.append(details);
  }
  function codeBranch(parent, code) {
    const group = element('div', undefined, 'tree-group');
    const button = element('button', `${code.name} (${counts.get(code.id) || 0})`, 'code-button');
    button.type = 'button';
    button.style.setProperty('--code-color', color(code));
    button.dataset.code = code.id;
    button.setAttribute('aria-pressed', String(state.code === code.id));
    button.addEventListener('click', () => { state.code = code.id; update(); });
    group.append(button);
    addMemo(group, code.memo);
    for (const child of sorted(data.codes.filter(c => c.parent === code.id))) codeBranch(group, child);
    parent.append(group);
  }
  function categoryBranch(parent, category) {
    const details = element('details', undefined, 'tree-group');
    details.open = true;
    details.append(element('summary', category.name));
    addMemo(details, category.memo);
    for (const child of sorted(data.categories.filter(c => c.parent === category.id))) categoryBranch(details, child);
    for (const code of sorted(data.codes.filter(c => c.category === category.id && c.parent === null))) codeBranch(details, code);
    parent.append(details);
  }
  for (const category of sorted(data.categories.filter(c => c.parent === null))) categoryBranch($('code-tree'), category);
  for (const code of sorted(data.codes.filter(c => c.category === null && c.parent === null))) codeBranch($('code-tree'), code);

  function showDocument(doc) {
    $('empty').hidden = Boolean(doc);
    $('document-view').hidden = !doc;
    if (!doc) return;
    $('entity').textContent = doc.entity || 'Corpus';
    $('document-title').textContent = doc.name;
    const selected = doc.codings.filter(matchingCoding);
    const annotations = doc.annotations.filter(matchingAnnotation);
    $('document-info').textContent = `${selected.length} / ${doc.codings.length} coded passages · ${annotations.length} / ${doc.annotations.length} annotations`;
    $('document-memo').textContent = [...doc.paths, doc.memo].filter(Boolean).join('\n\n');
    $('provenance').hidden = !$('document-memo').textContent;
    const items = [
      ...selected.map(c => ({ ...c, kind: 'coding', anchor: `coding-${c.id}` })),
      ...annotations.map(a => ({ ...a, kind: 'annotation', anchor: `annotation-${a.id}` }))
    ].sort((a, b) => a.start - b.start || a.end - b.end || collator.compare(a.anchor, b.anchor));
    const fragment = document.createDocumentFragment();
    for (const item of items) {
      const code = codes.get(item.code);
      const card = element('div', undefined, 'passage');
      card.id = item.anchor;
      card.style.setProperty('--code-color', color(code));
      card.append(element('h4', `${code ? code.name : 'Annotation'}${item.important ? ' · Important' : ''}`));
      card.append(element('p', `${item.owner || 'Unattributed'} · ${item.date || 'Date unavailable'}`, 'hint'));
      card.append(element('blockquote', doc.text.slice(item.start, item.end)));
      if (item.memo) card.append(element('p', item.memo, 'memo'));
      const back = element('a', 'View in text');
      back.href = `#text-${item.anchor}`;
      card.append(back);
      fragment.append(card);
    }
    if (!items.length) fragment.append(element('p', 'No passages match the filters.', 'hint'));
    $('passages').replaceChildren(fragment);
    renderText(doc.text, items);
  }

  function renderText(text, items) {
    // Split at every boundary: each segment retains all overlapping interpretations.
    const events = new Map();
    for (const item of items) {
      for (const position of [item.start, item.end]) {
        if (!events.has(position)) events.set(position, { starts: [], ends: [] });
      }
      events.get(item.start).starts.push(item);
      events.get(item.end).ends.push(item);
    }
    const positions = [...new Set([0, text.length, ...events.keys()])].sort((a, b) => a - b);
    const active = new Map();
    const fragment = document.createDocumentFragment();
    for (let i = 0; i < positions.length - 1; i++) {
      const start = positions[i], end = positions[i + 1];
      const event = events.get(start);
      if (event) {
        for (const item of event.ends) active.delete(item.anchor);
        for (const item of event.starts) {
          active.set(item.anchor, item);
          const marker = element('span');
          marker.id = `text-${item.anchor}`;
          fragment.append(marker);
        }
      }
      if (!active.size) { fragment.append(document.createTextNode(text.slice(start, end))); continue; }
      const entries = [...active.values()];
      const target = entries[0];
      const link = element('a', text.slice(start, end), 'highlight');
      if (entries.length > 1) link.classList.add('overlap');
      if (entries.some(item => item.kind === 'annotation')) link.classList.add('annotation');
      const palette = [...new Set(entries.filter(item => item.kind === 'coding').map(item => color(codes.get(item.code))))];
      if (palette.length === 1) link.style.backgroundColor = palette[0];
      if (palette.length > 1) link.style.backgroundImage = `linear-gradient(135deg, ${palette.map((c, n) => `${c} ${n * 100 / palette.length}%, ${c} ${(n + 1) * 100 / palette.length}%`).join(', ')})`;
      link.href = `#${target.anchor}`;
      link.title = entries.map(item => `${codes.get(item.code)?.name || 'Annotation'} — ${item.owner || 'Unattributed'}`).join('\n');
      link.addEventListener('click', () => {
        // Mark every interpretation of a shared segment without changing their order.
        for (const card of $('passages').children) card.classList.toggle('selected', entries.some(item => item.anchor === card.id));
      });
      fragment.append(link);
    }
    $('document-text').replaceChildren(fragment);
  }

  function update() {
    const query = $('search').value.trim().toLocaleLowerCase('en');
    const filtered = data.documents.filter(doc => {
      if (query && ![doc.entity, doc.name, ...doc.paths, ...doc.cases, doc.text].some(text => text.toLocaleLowerCase('en').includes(query))) return false;
      if ($('coded-only').checked && !doc.codings.some(matchingCoding)) return false;
      if (state.code !== null && !doc.codings.some(matchingCoding)) return false;
      if ($('coder').value && !doc.codings.some(matchingCoding) && !doc.annotations.some(matchingAnnotation)) return false;
      return true;
    });
    if (!filtered.some(doc => doc.id === state.document)) state.document = filtered[0]?.id ?? null;
    $('code-filter').textContent = state.code === null ? '' : `· ${codes.get(state.code).name}`;
    $('all-codes').setAttribute('aria-pressed', String(state.code === null));
    for (const button of document.querySelectorAll('[data-code]')) button.setAttribute('aria-pressed', String(Number(button.dataset.code) === state.code));
    $('document-count').textContent = `(${filtered.length} / ${data.documents.length})`;
    const fragment = document.createDocumentFragment();
    for (const doc of filtered) {
      const button = element('button', undefined, 'document-button');
      button.type = 'button';
      button.setAttribute('aria-pressed', String(doc.id === state.document));
      button.append(element('strong', doc.entity || 'No project'), element('span', doc.name));
      button.append(element('small', `${doc.codings.filter(matchingCoding).length} coded passages · ${doc.annotations.filter(matchingAnnotation).length} annotations`));
      button.addEventListener('click', () => { state.document = doc.id; update(); });
      fragment.append(button);
    }
    if (!filtered.length) fragment.append(element('p', 'No documents match the filters.', 'hint'));
    $('documents').replaceChildren(fragment);
    showDocument(filtered.find(doc => doc.id === state.document));
  }
  let searchTimer;
  $('search').addEventListener('input', () => { clearTimeout(searchTimer); searchTimer = setTimeout(update, 150); });
  for (const id of ['coder', 'coded-only']) $(id).addEventListener('change', update);
  $('all-codes').addEventListener('click', () => { state.code = null; update(); });
  $('reset').addEventListener('click', () => {
    $('search').value = ''; $('coder').value = ''; $('coded-only').checked = false;
    state.code = null;
    update();
  });
  update();
})();
