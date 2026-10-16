import json,re,subprocess,sys
f=json.load(open('commit-pool-fresh.json'))
G=re.compile(r'(?i)game|play|arcade|puzzle|shoot|rpg|platform|tetris|snake|chess|rac(e|ing)|dungeon|rogue|tower|surviv|quest|kart|pong|invader|breakout|craft|battle|card|clicker|idle|runner|zombie|jump|maze|sudoku|poker|golf|soccer|football|wars?\b|hero|legend|tycoon|dino|bird|kingdom|space|pixel|tank|fight|block|monster|pet|farm|world|adventure|escape|mine')
B=re.compile(r'(?i)\bmod\b|mods\b|launcher|dashboard|mcp|tracker|\bapi\b|benchmark|tool|wiki|server|discord|bot\b|plugin|portfolio|landing|website')
short=[r for r,v in f.items() if G.search(r+' '+(v['meta']['description'] or '')) and not B.search(r+' '+(v['meta']['description'] or ''))]
extra=['Torchwood4201/Wormhole','oscarqht/pikmin-rush-by-opus-5.5','oscarqht/pikmin-rush-by-gemini-4','testingyoubob/Star-Trek-StarFleet-Command-game-','The-Focus-AI/brutism-gemini-4-test','Nightmoods/Circular-maze-generator-by-Gemini-4-Argon','Patcher786/GPT-6-Astra','danieldownes/PizzaWorm','hashbrownprime/Gemini-4-','chillqoder/Gemini-4-Argon','danieldownes/AtomicBomberman','aratane/koipond-gemini-4-argon','aakashg/argon-five-builds','padmashri23/Gemini4_Argon_test','Emily2040/chrono-analogue-1974-synth-studio']
repos=extra+[r for r in short if r not in extra]
print(len(repos),file=sys.stderr)
res={}
for i in range(0,len(repos),8):
  chunk=repos[i:i+8];parts=[]
  for j,r in enumerate(chunk):
    o,n=r.split('/',1)
    parts.append(f'''r{j}: repository(owner:{json.dumps(o)}, name:{json.dumps(n)}){{nameWithOwner createdAt databaseId description homepageUrl stargazerCount isFork primaryLanguage{{name}} defaultBranchRef{{name target{{... on Commit{{history(first:100){{nodes{{oid message committedDate}}}}}}}}}}
      readme: object(expression:"HEAD:README.md"){{... on Blob{{text}}}}
      tree: object(expression:"HEAD:"){{... on Tree{{entries{{name type}}}}}} }}''')
  q='query{'+' '.join(parts)+'}'
  p=subprocess.run(['gh','api','graphql','-f',f'query={q}'],capture_output=True,text=True)
  d=json.loads(p.stdout or '{}').get('data') or {}
  for j,r in enumerate(chunk):
    v=d.get(f'r{j}')
    if not v: print('miss',r,file=sys.stderr); continue
    br=v['defaultBranchRef'] or {}
    commits=((br.get('target') or {}).get('history') or {}).get('nodes',[])
    res[r]=dict(id=v['databaseId'],created=v['createdAt'],desc=v['description'],home=v['homepageUrl'],stars=v['stargazerCount'],lang=(v['primaryLanguage'] or {}).get('name'),branch=br.get('name'),
      readme=((v.get('readme') or {}).get('text') or '')[:4000],tree=[e['name']+('/' if e['type']=='tree' else '') for e in ((v.get('tree') or {}).get('entries') or [])],
      commits=[dict(sha=c['oid'],msg=c['message'][:500],date=c['committedDate']) for c in commits])
json.dump(res,open('inspect.json','w'),indent=1)
print(len(res),file=sys.stderr)
