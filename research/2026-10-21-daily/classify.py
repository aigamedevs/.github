import json,re
d=json.load(open('inspect.json'))
prevset=set()
for dd in ('2026-10-16-daily','2026-10-17-daily'):
  prev=json.load(open(f'../{dd}/candidate-decisions.json'))
  prevset|={k.lower() for k in list(prev['held'])+list(prev['rejected'])+prev['accepted']}
known={g['github_url'].casefold() for g in json.load(open('../../games.json'))}
PAT=[('Claude Opus 5.5',r'claude[ -]opus[ -]5\.5|opus[ -]5\.5'),('Claude Sonnet 5.5',r'sonnet[ -]5\.5'),('Claude Fable 5.1',r'fable[ -]5(\.1)?|claude[ -]fable'),
('GPT-6.1 Sol',r'gpt-?6\.1[ -]?sol'),('GPT-6 Astra',r'gpt-?6[ -]astra'),('Gemini 4 Argon',r'gemini[ -]4[ -]argon')]
ev={}
for r,v in d.items():
  co={};anyc={}
  for c in reversed(v['commits']):
    for line in c['msg'].splitlines():
      L=line.lower()
      for name,p in PAT:
        if re.search(p,L):
          anyc.setdefault(name,c['sha'])
          if L.strip().startswith('co-authored-by:'): co.setdefault(name,c['sha'])
  ev[r]=dict(co=co,any=anyc)
json.dump(ev,open('evidence.json','w'),indent=1)
rows=[]
for r,v in d.items():
  if ('https://github.com/'+r).casefold() in known or r.lower() in prevset: continue
  if v.get('fork'): continue
  e=ev[r]
  tag=','.join(k.split()[-2][:3]+k.split()[-1] for k in e['co']) or ('ANY:'+','.join(e['any']) if e['any'] else 'NONE')
  rd=re.sub(r'<[^>]+>|!\[[^\]]*\]\([^)]*\)|\s+',' ',v['readme'])[:230]
  rows.append(f"{r} [{tag}] {v['lang']} c{len(v['commits'])} | {(v['desc'] or '')[:100]} | {rd} | {' '.join(v['tree'][:12])}")
open('review.txt','w').write('\n'.join(rows))
print(len(rows), sum(1 for x in rows if '[NONE]' in x), sum(1 for x in rows if 'ANY:' in x))
