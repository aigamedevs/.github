import json,collections
acc=set(l.strip() for l in open('accept.txt') if l.strip())
ins=json.load(open('inspect.json')); tri={r:(p,n,t) for r,p,n,t in json.load(open('triage.json'))}
rq=json.load(open('../2026-10-20-daily/repo-query-log.json'))+json.load(open('repo-query-log.json'))
cq=json.load(open('../2026-10-20-daily/commit-query-log.json'))+json.load(open('commit-query-log.json'))
by=collections.defaultdict(set)
for f in ('../2026-10-20-daily/repo-searches.jsonl','repo-searches.jsonl','../2026-10-20-daily/commit-searches.jsonl','commit-searches.jsonl'):
  for l in open(f):
    x=json.loads(l); by[x['q']].add(x.get('full_name') or x.get('repo'))
def rows(L): return [{'query':q['query'],'hits':q['hits'],'fetched':q['fetched'],'capped':q['capped'],'verified_yield':len(by[q['query']]&acc)} for q in L]
meta=json.load(open('commit-pool-meta.json')); fresh=json.load(open('commit-pool-fresh.json'))
out={'timezone':'Asia/Phnom_Penh (UTC+7)','window':'2026-10-17..2026-10-21 local; UTC creation floor 2026-10-17T00:00:00Z, commit and repository search 2026-10-17T01:00Z..2026-10-21T01:00Z (Oct 17-20 searches ran on 2026-10-20, Oct 20-21 on 2026-10-21)','run_on':'2026-10-21',
 'repository_queries':rows(rq),'commit_queries':rows(cq),
 'commit_pool':{'repositories':len(meta),'fresh_non_fork':len(fresh),'prefiltered_for_trailer_and_game_signal':sum(1 for _ in open('pool-co.txt'))},
 'inspected':len(ins),'accepted':len(acc)}
json.dump(out,open('search-results.json','w'),indent=2,ensure_ascii=False)
L=lambda f:{l.strip() for l in open(f) if l.strip()}
ra,rb,nc=L('A-reject.txt'),L('B-reject.txt'),L('nocode.txt')
rej={}
for r in ins:
  if r in acc: continue
  p,n,t=tri[r]
  if r in nc: why='no source code in the tree'
  elif r=='grootbot-dev/awesome-opus-5.5-games': why='this catalog itself; not a game'
  elif t=='X': why='no tracked-model co-author trailer in the last 100 commits'
  elif r in ra or r in rb: why='manual review: port, recomp, decomp, mod, tool, companion, portal, non-game, stub, or reimplementation of an existing game'
  else: why='weak game signal in README and description (fewer than two game terms); not reviewed further this pass'
  rej[r]=why
json.dump({'accepted':sorted(acc),'rejected':rej,'held':{}},open('candidate-decisions.json','w'),indent=2,ensure_ascii=False)
print(len(acc),len(rej),collections.Counter(rej.values()).most_common())
