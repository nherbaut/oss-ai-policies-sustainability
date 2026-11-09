// Execute the exact inline workflow script against mocked GitHub APIs.
const {test} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const yaml = fs.readFileSync(path.join(__dirname, '../../.github/workflows/coding-session-pr.yml'), 'utf8');
const source = yaml.split('          script: |\n')[1].split('\n').map(line => line.slice(12)).join('\n');
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
const execute = new AsyncFunction('github', 'context', 'core', source);

function harness() {
  const state = {
    head: 'a'.repeat(40), branch: 'coding/alice/session', remoteHead: null, truncated: false, integrated: null,
    manifest: {version: 1, id: '1'.repeat(32), project: 'data/coding.qda', coder: 'Alice',
      branch: 'coding/alice/session', base: '0'.repeat(40), completed_at: '2026-11-09T10:00:00Z',
      summary: {'code_text:add': 2}},
    prs: [], created: [], updated: [], converted: [], messages: []
  };
  state.files = [{filename: 'data/coding.qda/data.qda', status: 'modified'},
    {filename: `coding/sessions/${state.manifest.id}.json`, status: 'added'}];
  const github = {rest: {
    repos: {
      getBranch: async () => ({data: {commit: {sha: state.remoteHead || state.head}}}),
      compareCommitsWithBasehead: async () => ({data: {status: 'ahead', files: state.files}}),
      getContent: async () => {
        if (!state.integrated) throw Object.assign(new Error('Not found'), {status: 404});
        return {data: {content: Buffer.from(JSON.stringify(state.integrated)).toString('base64')}};
      }
    },
    git: {
      getCommit: async () => ({data: {tree: {sha: 'root-tree'}}}),
      getTree: async () => ({data: {truncated: state.truncated,
        tree: [{type: 'blob', path: `coding/sessions/${state.manifest.id}.json`, sha: 'manifest-blob'}]}}),
      getBlob: async () => ({data: {encoding: 'base64', content: Buffer.from(JSON.stringify(state.manifest)).toString('base64')}})
    },
    pulls: {
      list: () => {},
      create: async args => {
        state.created.push(args);
        const pr = {number: 42, state: 'open', draft: args.draft, node_id: 'pr-node', body: args.body};
        state.prs.push(pr);
        return {data: pr};
      },
      update: async args => {state.updated.push(args); return {data: args};}
    }
  },
    paginate: async () => state.prs,
    graphql: async (query, args) => {state.converted.push(args); return {};}
  };
  return {state, run: () => execute(github,
    {repo: {owner: 'team', repo: 'research'}, ref: `refs/heads/${state.branch}`, sha: state.head},
    {info: message => state.messages.push(message)})};
}

test('creates one draft PR and refreshes the same PR for a newer push', async () => {
  const {state, run} = harness();
  await run();
  assert.equal(state.created.length, 1);
  assert.equal(state.created[0].draft, true);
  assert.equal(state.created[0].base, 'master');
  assert.ok(state.created[0].body.includes(`"head":"${state.head}"`));
  state.head = 'b'.repeat(40);
  await run();
  assert.equal(state.created.length, 1);
  assert.equal(state.updated.length, 1);
  assert.equal(state.updated[0].pull_number, 42);
  assert.ok(state.updated[0].body.includes(`"head":"${state.head}"`));
});

test('returns an existing notification to draft before updating it', async () => {
  const {state, run} = harness();
  state.prs.push({number: 7, state: 'open', draft: false, node_id: 'ready-pr'});
  await run();
  assert.deepEqual(state.converted, [{id: 'ready-pr'}]);
  assert.equal(state.updated[0].pull_number, 7);
  assert.equal(state.created.length, 0);
});

test('never reopens a closed notification', async () => {
  const {state, run} = harness();
  state.prs.push({number: 7, state: 'closed'});
  await run();
  assert.equal(state.created.length + state.updated.length, 0);
});

test('skips an older push superseded by a newer branch head', async () => {
  const {state, run} = harness();
  state.remoteHead = 'b'.repeat(40);
  await run();
  assert.equal(state.created.length, 0);
  assert.match(state.messages[0], /superseded/);
});

test('skips integrated snapshots and rejects reused session IDs', async () => {
  const {state, run} = harness();
  state.integrated = {submission: state.head};
  await run();
  assert.equal(state.created.length, 0);
  state.integrated.submission = 'c'.repeat(40);
  await assert.rejects(run(), /different snapshot/);
});

test('rejects unrelated files and malformed manifests', async () => {
  const {state, run} = harness();
  state.files.push({filename: 'scripts/untrusted.sh', status: 'added'});
  await assert.rejects(run(), /may change only/);
  state.files.pop();
  state.manifest.coder = 'default';
  await assert.rejects(run(), /Invalid completed/);
  assert.equal(state.created.length, 0);
});

test('rejects missing session manifests and truncated repository trees', async () => {
  const {state, run} = harness();
  state.manifest.branch = 'coding/other/session';
  await assert.rejects(run(), /exactly one/);
  state.manifest.branch = state.branch;
  state.truncated = true;
  await assert.rejects(run(), /truncated/);
  state.truncated = false;
  state.manifest.summary = {'unexpected:operation': 1};
  await assert.rejects(run(), /Invalid completed/);
});

test('lists changed corpus files with snapshot links and per-file counts', async () => {
  const {state, run} = harness();
  state.manifest.changed_documents = ['one.md','policy two.md'].map(name => ({name,
    path:`data/coding.qda/documents/${name}`,cases:['Example'],changes:{'code_text:add':1}}));
  await run();
  const body = state.created[0].body;
  assert.ok(body.includes('Corpus files with coding changes'));
  assert.ok(body.includes('[one.md]'));
  assert.ok(body.includes(`[policy two.md](https://github.com/team/research/blob/${state.head}/data/coding.qda/documents/policy%20two.md)`));
  assert.ok(body.includes('coded passages added: 1'));
});

test('rejects inaccurate per-file counts and invalid corpus paths', async () => {
  const {state, run} = harness();
  state.manifest.changed_documents = [{name:'one.md',path:'data/coding.qda/documents/one.md',
    cases:['Example'],changes:{'code_text:add':1}}];
  await assert.rejects(run(),/counts do not match/);
  state.manifest.changed_documents[0].changes['code_text:add'] = 2;
  state.manifest.changed_documents[0].path = 'data/coding.qda/documents/../secret';
  await assert.rejects(run(),/Invalid corpus-file/);
  assert.equal(state.created.length,0);
});

test('large file lists stay within PR body limits and link to the full manifest', async () => {
  const {state, run} = harness();
  state.manifest.summary = {'code_text:add':201};
  state.manifest.changed_documents = Array.from({length:201},(_,i) => ({name:`document-${i}.md`,
    path:`data/coding.qda/documents/document-${i}.md`,cases:[],changes:{'code_text:add':1}}));
  await run();
  const body=state.created[0].body;
  assert.ok(body.length<65536);
  assert.ok(body.includes('additional files'));
  assert.ok(body.includes(`[full file list](https://github.com/team/research/blob/${state.head}/coding/sessions/${state.manifest.id}.json)`));
});

test('codebook sessions list proposals and accept the synchronized registry path', async () => {
  const {state, run} = harness();
  state.manifest.codebook_version = 1;
  state.manifest.codebook_context = {shared: {revision: 'd'.repeat(64)}, history: [{master: 'e'.repeat(40)}]};
  state.manifest.codebook_proposals = [{id: '11111111-1111-4111-8111-111111111111',
    before: null, after: {kind: 'code', name: 'Emergent sustainability'}}];
  state.files.push({filename: 'coding/codebook.json', status: 'modified'});
  await run();
  assert.match(state.created[0].body, /Emergent sustainability/);
  assert.match(state.created[0].body, /Explicit synchronizations: 1/);
  state.manifest.codebook_context.shared.revision = 'invalid';
  await assert.rejects(run(), /Invalid codebook/);
});

test('an unfinished synchronization checkpoint does not create a notification PR', async () => {
  const {state, run} = harness();
  delete state.manifest.completed_at;
  await run();
  assert.equal(state.created.length, 0);
  assert.match(state.messages[0], /Active synchronization checkpoint/);
});
