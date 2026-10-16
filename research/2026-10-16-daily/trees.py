import json,subprocess,re
d=json.load(open('inspect.json'))
out={}
for r in [l.strip() for l in open('cands.txt') if l.strip()]:
  br=(d.get(r) or {}).get('branch') or 'HEAD'
  p=subprocess.run(['gh','api',f'repos/{r}/git/trees/{br}?recursive=1'],capture_output=True,text=True)
  try: t=json.loads(p.stdout)
  except: t={}
  files=[(e['path'],e.get('size',0)) for e in t.get('tree',[]) if e['type']=='blob']
  code=[(f,s) for f,s in files if re.search(r'\.(html?|js|mjs|ts|tsx|jsx|gd|cs|java|rs|py|swift|lua|luau|kt|cpp|c|qml|php|svelte|vue)$',f,re.I) and not re.search(r'node_modules|vendor/|\.min\.|dist/|build/|test',f)]
  code.sort(key=lambda x:-x[1])
  out[r]=dict(branch=br,nfiles=len(files),code_bytes=sum(s for _,s in code),top=code[:6])
  print(r,br,len(files),sum(s for _,s in code),[f"{f}:{s//1000}k" for f,s in code[:4]],flush=True)
json.dump(out,open('trees.json','w'),indent=1)
