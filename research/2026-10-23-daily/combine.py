# Combine the Oct 22 and Oct 23 fresh pools, dedupe against games.json and earlier decisions, keep co-author-confirmed repos.
import json,re
known={g['github_url'].casefold().rstrip('/') for g in json.load(open('../../games.json'))}
prev=set()
for d in ('2026-10-16-daily','2026-10-17-daily','2026-10-21-daily'):
  p=json.load(open(f'../{d}/candidate-decisions.json'))
  prev|={k.lower() for k in list(p['held'])+list(p['rejected'])+p['accepted']}
a=json.load(open('../2026-10-22-daily/commit-pool-fresh.json')); b=json.load(open('commit-pool-fresh.json'))
allp={}
for src in (a,b):
  for r,v in src.items():
    e=allp.setdefault(r,dict(meta=v['meta'],commits=[]))
    seen={c['sha'] for c in e['commits']}
    e['commits']+= [c for c in v['commits'] if c['sha'] is None or c['sha'] not in seen]
PAT=re.compile(r'(?i)claude[ -]opus[ -]5\.5|opus[ -]5\.5|sonnet[ -]5\.5|fable[ -]5|claude[ -]fable|gpt-?6\.1[ -]?sol|gpt-?6[ -]astra|gemini[ -]4[ -]argon')
stats=dict(union=len(allp),known=0,prev=0)
co=[];nonco=[]
for r,v in sorted(allp.items(),key=lambda x:x[1]['meta']['createdAt']):
  if ('https://github.com/'+r).casefold() in known: stats['known']+=1; continue
  if r.lower() in prev: stats['prev']+=1; continue
  ok=any(c['sha'] is None or any(l.strip().lower().startswith('co-authored-by') and PAT.search(l) for l in c['msg'].splitlines()) for c in v['commits'])
  (co if ok else nonco).append(r)
open('combined-co.txt','w').write('\n'.join(co)+'\n'); open('combined-nonco.txt','w').write('\n'.join(nonco)+'\n')
json.dump(allp,open('combined-pool.json','w'),indent=1)
stats.update(co=len(co),nonco=len(nonco)); print(stats)
