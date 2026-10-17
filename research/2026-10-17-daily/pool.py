import json,subprocess
known={g['github_url'].casefold().rstrip('/') for g in json.load(open('../../games.json'))}
pool={}
for l in open('commit-searches.jsonl'):
  d=json.loads(l)
  if d['fork']: continue
  pool.setdefault(d['repo'],[]).append(d)
repos=[r for r in pool if ('https://github.com/'+r).casefold() not in known and not r.startswith('TheClockwyrks/')]
print('pool',len(pool),'unknown',len(repos))
meta={}
for i in range(0,len(repos),50):
  chunk=repos[i:i+50]; parts=[]
  for j,r in enumerate(chunk):
    o,n=r.split('/',1)
    parts.append(f'r{j}: repository(owner:{json.dumps(o)}, name:{json.dumps(n)}){{nameWithOwner createdAt isFork description homepageUrl databaseId stargazerCount primaryLanguage{{name}} defaultBranchRef{{name}}}}')
  q='query{'+' '.join(parts)+'}'
  res=subprocess.run(['gh','api','graphql','-f',f'query={q}'],capture_output=True,text=True)
  d=json.loads(res.stdout or '{}').get('data') or {}
  for j,r in enumerate(chunk):
    v=d.get(f'r{j}')
    if v: meta[r]=v
json.dump(meta,open('commit-pool-meta.json','w'),indent=1)
fresh={r:v for r,v in meta.items() if v['createdAt']>='2026-10-16T00:00:00Z' and not v['isFork']}
json.dump({r:dict(meta=fresh[r],commits=[dict(sha=c['sha'],msg=c['msg'][:300],q=c['q']) for c in pool[r]]) for r in fresh},open('commit-pool-fresh.json','w'),indent=1)
print('fresh',len(fresh))
for r,v in sorted(fresh.items(),key=lambda x:x[1]['createdAt']):
  m=pool[r][0]['msg'].split('\n')[0][:90]
  print(r,'|',v['createdAt'][5:16],'|',(v['primaryLanguage'] or {}).get('name'),'|',(v['description'] or '')[:90],'|',m)
