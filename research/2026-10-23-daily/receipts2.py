# Receipts for the combined 2026-10-22 + 2026-10-23 daily pass.
import json,collections
D22='../2026-10-22-daily/'
by=collections.defaultdict(set)
for f in (D22+'repo-searches.jsonl','repo-searches.jsonl',D22+'commit-searches.jsonl','commit-searches.jsonl'):
  for l in open(f):
    try: x=json.loads(l)
    except ValueError: continue  # partial last line from the time-limited run
    by[x['q']].add((x.get('full_name') or x.get('repo') or '').lower())
man=json.load(open('manual-decisions.json')); auto=json.load(open('auto-rejects.json'))
dup={l.strip() for l in open('id-dup-rejects.txt') if l.strip()}
acc=sorted(r for r,v in man.items() if v['decision']=='accept' and r not in dup)
accl={r.lower() for r in acc}
def rows(L,day): return [{'run_on':day,'query':q['query'],'hits':q['hits'],'fetched':q['fetched'],'capped':q['capped'],'verified_yield':len(by[q['query']]&accl)} for q in L]
rq=rows(json.load(open(D22+'repo-query-log.json')),'2026-10-22')+rows(json.load(open('repo-query-log.json')),'2026-10-23')
cq=rows(json.load(open(D22+'commit-query-log.json')),'2026-10-22')+rows(json.load(open('commit-query-log.json')),'2026-10-23')
nonco=sum(1 for l in open('combined-nonco.txt') if l.strip()); co=sum(1 for l in open('combined-co.txt') if l.strip())
out={'timezone':'Asia/Phnom_Penh (UTC+7)',
 'window':'commit and repository search 2026-10-21T01:00Z..2026-10-23T01:00Z (2026-10-21 08:00..2026-10-23 08:00 local); batch window 2026-10-20..2026-10-23 local by repository creation proxy',
 'run_on':'searches 2026-10-22 and 2026-10-23 (both runs hit the 50-minute limit before committing); verification completed 2026-10-23 from the saved pools without re-running searches',
 'repository_queries':rq,'commit_queries':cq,
 'commit_pool':{'oct22_fresh_non_fork':len(json.load(open(D22+'commit-pool-fresh.json'))),'oct23_fresh_non_fork':len(json.load(open('commit-pool-fresh.json'))),
   'combined_after_dedupe_against_catalog_and_prior_decisions':co+nonco,'with_tracked_model_trailer':co,'without_trailer_not_inspected':nonco},
 'inspected':co,'manually_reviewed':len(man),'auto_rejected':len(auto),'accepted':len(acc)}
json.dump(out,open('search-results.json','w'),indent=2,ensure_ascii=False)
rej={}
for r,v in man.items():
  if v['decision']!='accept': rej[r]='manual review ('+v['batch']+'): port, recomp, decomp, remake, mod, tool, launcher, site, portfolio, platform, template, AI bot, non-game, or no README with unclear content'
for r in dup: rej[r]='duplicate repository id of an already-catalogued game (mirror)'
rej.update(auto)
json.dump({'accepted':acc,'rejected':rej,'held':{}},open('candidate-decisions.json','w'),indent=2,ensure_ascii=False)
print(len(acc),len(rej),len(rq),len(cq),sum(q['capped'] for q in cq),collections.Counter(rej.values()).most_common(6))
