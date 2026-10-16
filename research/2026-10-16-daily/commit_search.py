import json,subprocess,time
M=["Opus 5.5","Sonnet 5.5","gpt-6.1-sol","GPT-6 Astra","Claude Fable","Gemini 4 Argon"]
W=[]
for day in ("2026-10-15","2026-10-16"):
  for a,b in (("00:00:00","05:59:59"),("06:00:00","11:59:59"),("12:00:00","17:59:59"),("18:00:00","23:59:59")):
    if day=="2026-10-16" and a>"02": continue
    W.append(f"{day}T{a}Z..{day}T{b}Z")
out=open('commit-searches.jsonl','w');log=[]
for m in M:
  for w in W:
    q=f'"{m}" game committer-date:{w}'
    total=0;n=0
    for page in (1,2,3):
      r=subprocess.run(['gh','api','-X','GET','search/commits','-f',f'q={q}','-f','per_page=100','-f',f'page={page}'],capture_output=True,text=True)
      if r.returncode: print('ERR',q,r.stderr[:200]); time.sleep(30); break
      d=json.loads(r.stdout); total=d['total_count']
      for it in d['items']:
        n+=1; out.write(json.dumps(dict(q=q,repo=it['repository']['full_name'],fork=it['repository']['fork'],sha=it['sha'],msg=it['commit']['message'][:600]))+'\n')
      time.sleep(2.2)
      if n>=total or len(d['items'])<100: break
    log.append(dict(query=q,hits=total,fetched=n,capped=total>n))
    print(q,total,n,flush=True)
json.dump(log,open('commit-query-log.json','w'),indent=1)
