import json,collections
acc=set(l.strip() for l in open('accept.txt') if l.strip())
ins=json.load(open('inspect.json'))
rq=json.load(open('repo-query-log.json')); cq=json.load(open('commit-query-log.json'))
by=collections.defaultdict(set)
for f in ('repo-searches.jsonl','commit-searches.jsonl'):
  for l in open(f):
    x=json.loads(l); by[x['q']].add(x.get('full_name') or x.get('repo'))
def rows(L): return [{'query':q['query'],'hits':q['hits'],'fetched':q['fetched'],'capped':q['capped'],'verified_yield':len(by[q['query']]&acc)} for q in L]
meta=json.load(open('commit-pool-meta.json')); fresh=json.load(open('commit-pool-fresh.json'))
out={'timezone':'Asia/Phnom_Penh (UTC+7)','window':'2026-10-16..2026-10-17 local; UTC creation floor 2026-10-16T00:00:00Z, ceiling 2026-10-17T01:30:00Z','run_on':'2026-10-17',
 'repository_queries':rows(rq),'commit_queries':rows(cq),
 'commit_pool':{'repositories':len(meta),'fresh_non_fork':len(fresh)},
 'inspected':len(ins),'accepted':len(acc)}
json.dump(out,open('search-results.json','w'),indent=2,ensure_ascii=False)
named={'WollyMonjac/Vahva-Reis':'browser port of an existing game; outside games.json','gretchenboria/jester-deadline':'AI used at runtime only; no tracked authoring evidence',
 'novaki-ai/last-spark':'built by Kimi K3, not a tracked model','hy57in/neighborhood-quest':'not a game (AI neighborhood journaling app)',
 'GreyTheGangalf/arena':'2 KB stub','Ali-sial-786/WordSmith':'no game source in the tree','shnydaone/BTC-Game':'docs only, no game source',
 'billyhetech/awesome-gemini4-argon-videos':'awesome list of videos, not a game; collection candidate for awesomelists.md'}
auto=set(l.strip() for l in open('autodrop.txt') if l.strip())
rej={}
for r in ins:
  if r in acc: continue
  rej[r]=named.get(r) or ('classifier auto-reject: no tracked-model co-author trailer or not a game' if r in auto else 'manual review: port, decomp, mod, tool, non-game, stub, or no tracked-model authoring evidence (see review2.txt)')
json.dump({'accepted':sorted(acc),'rejected':rej,'held':{}},open('candidate-decisions.json','w'),indent=2,ensure_ascii=False)
print(len(acc),len(rej), sum(r['verified_yield'] for r in out['repository_queries']), len(meta),len(fresh))
