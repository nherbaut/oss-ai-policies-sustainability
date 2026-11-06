"""Build a conservative full-corpus first pass and validate exact evidence.

No language-model calls. Positive codes come from annotations.py or the pilot's
explicitly retained annotations. Automated candidates remain visibly provisional.
"""
import csv
import hashlib
import io
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from annotations import POLICY, GENERAL, PURPOSE, PURPOSE_DESCRIPTIONS, PURPOSE_CASE_STATUS

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DATASET = ROOT / 'data/281/dataset1-multiple-ai-policies.csv'
SOURCES = json.loads((HERE / 'source-manifest.json').read_text())
DOCS = json.loads((HERE / 'documents.json').read_text())
EVIDENCE = []


def sha(b): return hashlib.sha256(b).hexdigest()


def table_read(path):
    with path.open(newline='', encoding='utf-8-sig') as f: return list(csv.reader(f))


def write_csv(path, rows):
    with path.open('w', newline='', encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)


def quality(text):
    if not text.strip(): return 'empty_text'
    if re.fullmatch(r'[.\w/-]+\.(md|rst)',text.strip()): return 'path_stub'
    if re.search(r'Cookie monster!|Making sure you.re not a bot|Access Denied|Just a moment\.\.\.|Enable JavaScript and cookies to continue',text,re.I): return 'bot_or_access_page'
    if re.search(r'Impossible d.ouvrir|doesn.t have JavaScript enabled|version of (?:the|your) browser.{0,40}no longer supported',text,re.I): return 'rendering_problem_requires_review'
    return 'text_available'


def record(entity, path, excerpt, rqs, dimensions, basis, rationale, scope='AI policy', source_url='', source_id='', uncertainty='Provisional AI-assisted first-pass interpretation; independent review required.'):
    text=(ROOT/path).read_text()
    assert excerpt in text, (entity,path,excerpt)
    if not path.startswith('data/281/policies/'):
        # Keep quoted external material brief; full fetched text is available as
        # a source snapshot. Local user-supplied extracts are not truncated here.
        same_source=[e for e in EVIDENCE if e['source_url']==source_url and not e['source_path'].startswith('data/281/policies/')]
        remaining=25-sum(len(e['excerpt'].split()) for e in same_source)
        if remaining<=0:
            return same_source[0]
        words=list(re.finditer(r'\S+',excerpt))
        if len(words)>remaining:excerpt=excerpt[:words[remaining-1].end()]
    offset=text.index(excerpt)
    item={'evidence_id':f'C{len(EVIDENCE)+1:04d}','entity':entity,'rqs':rqs,'scope':scope,
          'basis':basis,'dimensions':dimensions,'excerpt':excerpt,'source_path':path,
          'source_sha256':sha((ROOT/path).read_bytes()),'line_start':text[:offset].count('\n')+1,
          'line_end':text[:offset+len(excerpt)].count('\n')+1,'source_url':source_url,
          'source_id':source_id,'rationale':rationale,'uncertainty':uncertainty}
    EVIDENCE.append(item)
    return item


def locate(entity, needle, purposes=False):
    if purposes:
        candidates=[{'path':s['snapshot'],'source_url':s['url'],'source_id':s['id']} for s in SOURCES
                    if s['entity']==entity and s['role']=='purpose_statement_candidate' and s['status']=='downloaded']
    else: candidates=[d for d in DOCS if d['entity']==entity]
    pattern=re.compile(r'\s+'.join(re.escape(p) for p in needle.split()))
    for doc in candidates:
        text=(ROOT/doc['path']).read_text();match=pattern.search(text)
        if match:return doc,match.group()
    return None,None


def inherit_pilot():
    with (ROOT/'analysis/feasibility-pilot/evidence.csv').open(newline='') as f: prior=list(csv.DictReader(f))
    for e in prior:
        if e['basis']=='unusable_extraction':continue
        if e['source_id']=='21-policy-raw':continue # User has now supplied the actual local document.
        if not (ROOT/e['source_path']).exists() or e['excerpt'] not in (ROOT/e['source_path']).read_text():continue
        record(e['entity'],e['source_path'],e['excerpt'],e['rqs'],e['dimensions'],e['basis'],e['rationale'],
               scope=e['scope'],source_url=e['source_url'],source_id=e['source_id'],uncertainty=e['uncertainty'])


def add_annotations():
    errors=[]
    for entries,purposes,scope in [(POLICY,False,'AI policy'),(GENERAL,False,'General contribution guidance'),(PURPOSE,True,'Purpose/support context')]:
        for entity,needle,dims,why in entries:
            doc,quote=locate(entity,needle,purposes)
            if doc is None:errors.append((entity,needle));continue
            basis=PURPOSE_CASE_STATUS.get(entity,'interpreted_dimension') if purposes else 'interpreted_dimension'
            actual_scope='Purpose/principles passage' if purposes and entity in PURPOSE_CASE_STATUS else scope
            record(entity,doc['path'],quote,'RQ1' if purposes else 'RQ2;RQ3',dims,basis,why,
                   scope=actual_scope,source_url=doc.get('source_url',''),source_id=doc.get('source_id') or 'local-snapshot')
    if errors:
        print('UNMATCHED ANNOTATIONS:',json.dumps(errors,indent=2,ensure_ascii=False))
        raise SystemExit(1)


def paragraphs(text):
    return [m.group().strip() for m in re.finditer(r'\S[^\n]*(?:\n(?!\s*\n)[^\n]*)*',text)]


def purpose_candidate(source):
    text=(ROOT/source['snapshot']).read_text()
    if quality(text)!='text_available': return None
    options=[]
    name=source['entity'].split('/')[-1].lower()
    name_pattern=re.compile(r'[- _]?'.join(re.escape(part) for part in re.split('[-_]',name)),re.I)
    for n,p in enumerate(paragraphs(text)):
        plain=re.sub(r'\s+',' ',re.sub(r'<[^>]+>','',p)).strip()
        if len(plain)<45 or len(p)>4000:continue
        if p.startswith(('#','- ','* ','!','```','[!','<!--')):continue
        if re.search(r'<(?:img|picture|source)\b|^>\s*\[!',p,re.I):continue
        if re.search(r'copyright|all rights reserved|permission is hereby|unless required by applicable law|without warranties|as is.{0,20}basis|license.{0,30}warranty',plain,re.I):continue
        if plain.count('https://')>4:continue
        if re.search(r'\b(is|provides?|aims?|goals?|mission|purpose|designed|helps?|enables?|build|develops?)\b',plain,re.I):
            score=10 if re.search(r'\b(our mission|mission is|we aim|our goal|aims to|purpose is)\b',plain,re.I) else 0
            if name_pattern.search(plain) and re.search(r'\b(is|provides?|designed|framework|library|language|tool|engine|server|application)\b',plain,re.I):score+=20
            if re.search(r'^\s*(If |Unless |Please |For |To install|Support|You can|Documentation|Most documentation)',plain,re.I):score-=15
            options.append((score,-n,p))
    return max(options)[2] if options else None


def attach_sources(table):
    col=table[0].index('supplementary_material')
    for row in table[1:]:
        records=json.loads(row[col] or '[]')
        for source in SOURCES:
            if source['entity']!=row[0]:continue
            record_source={k:v for k,v in source.items() if k not in ('entity','candidate_urls')}
            record_source['used_as_evidence']=any(e['source_id']==source['id'] for e in EVIDENCE)
            if source['status']=='downloaded':record_source['content_quality']=quality((ROOT/source['snapshot']).read_text())
            # Preserve all prior records and provenance; merge only this source/version.
            existing=next((r for r in records if (r.get('url'),r.get('version'))==(source.get('url'),source.get('version'))),None)
            if existing:
                existing.update(record_source)
            else:records.append(record_source)
        if row[0]=='Forgejo':
            for path in sorted((ROOT/'data/281/policies/Forgejo').glob('*.md')):
                key='manual-forgejo-'+path.stem
                item={'id':key,'title':'Forgejo: user-retrieved '+path.stem,'role':'user_supplied_policy',
                      'url':row[9] if path.stem=='ai_policy' else None,
                      'accessed_at':None,'version':None,'status':'user_supplied',
                      'snapshot':str(path.relative_to(ROOT)),'sha256':sha(path.read_bytes()),
                      'notes':'Manually retrieved by user. Retrieval date and contributing-file URL were not supplied; not inferred.'}
                records=[r for r in records if r.get('id')!=key];records.append(item)
        row[col]=json.dumps(records,ensure_ascii=False,separators=(',',':'))


def main():
    table=table_read(DATASET);original=[r[:32] for r in table]
    baseline=json.loads((HERE/'baseline.json').read_text())
    assert sha(json.dumps(original,ensure_ascii=False).encode())==baseline['original_cells_sha256']
    inherit_pilot();add_annotations()
    cases=[]
    for n,row in enumerate(table[1:],1):
        entity=row[0];docs=[d for d in DOCS if d['entity']==entity]
        good=[d for d in docs if quality((ROOT/d['path']).read_text())=='text_available']
        issues=[d['path']+': '+quality((ROOT/d['path']).read_text()) for d in docs if quality((ROOT/d['path']).read_text())!='text_available']
        ev=[e for e in EVIDENCE if e['entity']==entity]
        policy=[e for e in ev if e['scope'] in ('AI policy','Supplementary contribution policy','Supplementary governance policy','Project-purpose statement embedded in AI policy')]
        positive=[e for e in policy if e['dimensions']]
        purposes=[e for e in ev if e['scope']=='Purpose/principles passage']
        sources=[s for s in SOURCES if s['entity']==entity and s['role']=='purpose_statement_candidate']
        available=[s for s in sources if s['status']=='downloaded' and quality((ROOT/s['snapshot']).read_text())=='text_available']
        purpose_status='insufficient_purpose_evidence'
        purpose_ids=[]
        if purposes:
            purpose_status=purposes[0]['basis'];purpose_ids=[e['evidence_id'] for e in purposes]
        else:
            for source in available:
                if entity in PURPOSE_DESCRIPTIONS:
                    doc,quote=locate(entity,PURPOSE_DESCRIPTIONS[entity],purposes=True)
                    if doc and doc['path']!=source['snapshot']:continue
                else:quote=purpose_candidate(source)
                if quote:
                    # This is a source-review candidate, never a positive semantic code.
                    if len(quote.split())>25:
                        words=list(re.finditer(r'\S+',quote));quote=quote[:words[24].end()]
                    e=record(entity,source['snapshot'],quote,'RQ1','','purpose_passage_candidate',
                             'Automatically located introductory/mission-like passage. No affirmative sustainability code is assigned by this extraction.',
                             scope='Purpose source candidate',source_url=source['url'],source_id=source['id'],
                             uncertainty='Source-level availability checked; passage selection and purpose relevance require independent review.')
                    purpose_ids=[e['evidence_id']];purpose_status='source_available_no_positive_purpose_code';break
        if any('environmental' in e['dimensions'].split(';') for e in policy):status='explicit_environmental_concern'
        elif any(e['basis']=='explicit_sustainability' for e in policy):status='explicit_sustainability_ai'
        elif positive:status='implicit_concern_ai'
        elif not good:status='insufficient_policy_evidence'
        elif any(e['dimensions'] for e in ev if e['scope']=='General contribution guidance'):status='general_context_only'
        else:status='no_sustainability_specific_code_established'
        if entity=='NLnet' and not good:status='insufficient_policy_evidence'
        policy_excerpt_ids=[e['evidence_id'] for e in policy]
        # Provide an exact scope/permission excerpt for otherwise unclassified cases.
        if not policy_excerpt_ids and good:
            for doc in good:
                text=(ROOT/doc['path']).read_text();lines=text.splitlines()
                options=[]
                for a,b in doc['ai_ranges']:
                    for p in paragraphs('\n'.join(lines[a:b])):
                        if re.search(r'\b(AI|LLMs?|generative|coding agents?)\b',p,re.I) and len(p)>35 and not p.startswith(('#','<','- [','!')):
                            options.append(p)
                if options:
                    quote=options[0]
                    if len(quote)>1000:quote=quote[:1000]
                    e=record(entity,doc['path'],quote,'RQ2','','scope_evidence_only',
                             'Confirms AI-related text is present; this passage is not coded as sustainability evidence.',
                             source_url=doc['source_url'],source_id=doc.get('source_id') or 'local-snapshot')
                    policy_excerpt_ids.append(e['evidence_id']);break
        if not policy_excerpt_ids and good:
            # A heading can establish scope even when the following rule avoids
            # repeating "AI" (e.g. "Don't commit code you couldn't ...").
            for doc in good:
                text=(ROOT/doc['path']).read_text();lines=text.splitlines()
                for a,b in doc['ai_ranges']:
                    block='\n'.join(lines[a:b]).strip()
                    if not re.search(r'\b(AI|LLMs?|generative|coding agents?)\b',block,re.I):continue
                    quote=block[:1000]
                    if quote not in text:continue
                    e=record(entity,doc['path'],quote,'RQ2','','scope_evidence_only',
                             'AI-related heading or section establishes scope only; no sustainability interpretation is inferred.',
                             source_url=doc['source_url'],source_id=doc.get('source_id') or 'local-snapshot')
                    policy_excerpt_ids.append(e['evidence_id']);break
                if policy_excerpt_ids:break
        if not policy_excerpt_ids:
            issues.append('No substantive AI-policy scope excerpt established; policy availability/role requires review.')
            if not positive:status='insufficient_policy_evidence'
        if entity=='halo-dev/halo' and purpose_status=='insufficient_purpose_evidence':
            issues.append('Purpose README is predominantly Chinese; no English/French purpose passage established. Do not infer or silently translate purpose.')
        dims=sorted({d for e in positive for d in e['dimensions'].split(';') if d})
        cases.append({'entity':entity,'csv_row':n+1,'review_status':'provisional_AI_assisted_first_pass',
                      'rq1_status':purpose_status,'rq1_evidence_ids':';'.join(purpose_ids),
                      'rq1_source_urls':';'.join(s['url'] for s in available),
                      'rq2_status':status,'rq2_evidence_ids':';'.join(policy_excerpt_ids),
                      'rq3_ai_dimension_candidates':';'.join(dims),
                      'rq4_classification':'insufficient_evidence',
                      'rq4_reason':'No critical-natural-capital/non-substitutability framework established in the reviewed AI-policy material; neither weak nor strong is inferred.',
                      'documents_available':len(docs),'usable_documents':len(good),
                      'quality_flags':' | '.join(issues),
                      'notes':'No positive code is evidence not established in this first pass, not evidence of absence. Source availability, adoption and interpretation require independent review.'})
    write_csv(HERE/'cases.csv',cases);write_csv(HERE/'evidence.csv',EVIDENCE)
    # Every candidate gets a disposition, including rejected/generic material.
    candidates=json.loads((HERE/'candidates.json').read_text())
    for c in candidates:
        matches=[e for e in EVIDENCE if e['entity']==c['entity'] and e['source_path']==c['path'] and
                 e['basis']!='scope_evidence_only' and (e['excerpt'] in c['excerpt'] or c['excerpt'] in e['excerpt'])]
        c['disposition']='supports_recorded_annotation' if matches else 'not_used_as_positive_evidence'
        c['evidence_ids']=';'.join(e['evidence_id'] for e in matches)
        c['review_note']='Candidates are search hits, not codes; no positive inference from an unselected hit. Some are generic rules, boilerplate or outside the AI subsection.'
    write_csv(HERE/'candidate-review.csv',candidates)
    # Freeze a text copy of each document used by evidence, and redirect ledger links
    # to those immutable copies while preserving the original location separately.
    frozen=HERE/'frozen';frozen.mkdir(exist_ok=True)
    for e in EVIDENCE:
        target=frozen/(e['source_sha256']+'.md')
        if not target.exists():target.write_bytes((ROOT/e['source_path']).read_bytes())
        e['frozen_path']=str(target.relative_to(ROOT))
    write_csv(HERE/'evidence.csv',EVIDENCE)
    readable=['# Whole-corpus evidence ledger','','Exact source excerpts; codes remain provisional. Negative/uncoded cases are not claims of absence.','']
    for e in EVIDENCE:
        readable.extend([f"## {e['evidence_id']}",'',f"**{e['entity']}** — {e['rqs']}; {e['scope']}; {e['basis']}",'',
                         '> '+e['excerpt'].replace('\n','\n> '),'',
                         f"Source: [{e['source_path']}, line {e['line_start']}](<../../{e['source_path']}#L{e['line_start']}>). [Frozen text](<../../{e['frozen_path']}>).",'',
                         f"Dimensions: {e['dimensions'] or 'none assigned'}. {e['rationale']}",'',f"Uncertainty: {e['uncertainty']}",''])
    (HERE/'evidence.md').write_text('\n'.join(readable))
    attach_sources(table)
    assert [r[:32] for r in table]==original
    output=io.StringIO(newline='');csv.writer(output,lineterminator='\n').writerows(table)
    if DATASET.read_bytes()!=output.getvalue().encode():DATASET.write_bytes(output.getvalue().encode())
    # Keep document quality and original hashes visible, including empty/path-only files.
    inventory=[]
    for d in DOCS:
        copy=dict(d);copy['content_quality']=quality((ROOT/d['path']).read_text());copy['ai_ranges']=json.dumps(copy['ai_ranges']);inventory.append(copy)
    write_csv(HERE/'inventory.csv',inventory)
    summary={'entities':len(cases),'local_files':len(list((ROOT/'data/281/policies').rglob('*.md'))),
             'documents_including_supplements':len(DOCS),'evidence_rows':len(EVIDENCE),
             'rq1_counts':dict(Counter(c['rq1_status'] for c in cases)),
             'rq2_counts':dict(Counter(c['rq2_status'] for c in cases)),
             'rq3_entity_counts':dict(Counter(d for c in cases for d in c['rq3_ai_dimension_candidates'].split(';') if d)),
             'rq4_counts':dict(Counter(c['rq4_classification'] for c in cases)),
             'source_records':len(SOURCES),'source_status_counts':dict(Counter(s['status'] for s in SOURCES)),
             'document_quality_counts':dict(Counter(d['content_quality'] for d in inventory)),
             'entities_with_quality_flags':sum(bool(c['quality_flags']) for c in cases),
             'baseline_original_cells_sha256':baseline['original_cells_sha256']}
    (HERE/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    validate()
    print(json.dumps(summary,indent=2))


def validate():
    table=table_read(DATASET);baseline=json.loads((HERE/'baseline.json').read_text())
    expected=baseline['dataset_entries']
    assert len(table)==expected+1 and len({r[0] for r in table[1:]})==expected
    assert all(len(r)==len(table[0]) for r in table)
    assert sha(json.dumps([r[:32] for r in table],ensure_ascii=False).encode())==baseline['original_cells_sha256']
    attached={r[0]:json.loads(r[table[0].index('supplementary_material')]) for r in table[1:]}
    for s in SOURCES:
        assert any(r.get('url')==s['url'] and r.get('version')==s.get('version') for r in attached[s['entity']])
        if s.get('raw_snapshot'):assert sha((ROOT/s['raw_snapshot']).read_bytes())==s['sha256']
    for e in EVIDENCE:
        text=(ROOT/e['source_path']).read_text()
        assert sha((ROOT/e['source_path']).read_bytes())==e['source_sha256']
        assert e['excerpt'] in '\n'.join(text.splitlines()[e['line_start']-1:e['line_end']])
        assert sha((ROOT/e['frozen_path']).read_bytes())==e['source_sha256']
    assert len({e['evidence_id'] for e in EVIDENCE})==len(EVIDENCE)


if __name__=='__main__':main()
