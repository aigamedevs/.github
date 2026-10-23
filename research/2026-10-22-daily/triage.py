import json,re
d=json.load(open('inspect.json')); ev=json.load(open('evidence.json'))
POS=re.compile(r'(?i)\b(game|games|gameplay|playable|arcade|platformer|shooter|roguelike|roguelite|rpg|puzzle game|tower defen[cs]e|dungeon crawler|survival game|endless runner|idle game|clicker|high ?score|boss fight|enemies|power-?ups?|levels?|lives|game over|controls|wasd|arrow keys|spacebar|mouse to aim|joystick|mini-?games?)\b')
NEG=re.compile(r'(?i)\b(save editor|mod manager|launcher|discord bot|telegram bot|api|sdk|library|framework|cli|mcp server|dashboard|analytics|tracker|stats|scraper|backend|server only|template|boilerplate|starter|benchmark harness|wiki|documentation|portfolio|landing page|crm|saas|extension|plugin|companion app|tool(s|kit)?|helper|calculator|overlay|bot|engine)\b')
rows=[]
for r,v in d.items():
  e=ev[r]
  if not e['co']: tag='X'
  else: tag=','.join(sorted(e['co']))
  text=(r.split('/')[1]+' '+(v['desc'] or '')+' '+v['readme'][:3000])
  p=len(POS.findall(text)); n=len(NEG.findall(r.split('/')[1]+' '+(v['desc'] or '')+' '+v['readme'][:800]))
  rows.append((r,p,n,tag,v))
json.dump([(r,p,n,t) for r,p,n,t,_ in rows],open('triage.json','w'))
import collections
print(collections.Counter(min(p,6) for r,p,n,t,v in rows))
print(sum(1 for r,p,n,t,v in rows if t=='X'))
