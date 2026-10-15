# Build the 2026-10-15 daily batch and append records to games.json.
import json,re,subprocess,sys
sys.path.insert(0,'research/2026-10-15-daily'); from spec import SPEC
TODAY='2026-10-15'
games=json.load(open('games.json')); known={g['github_url'].casefold() for g in games}
i1=json.load(open('research/2026-10-15-daily/inspect1.json'))
pool={json.loads(l)['repo']:json.loads(l) for l in open('research/2026-10-15-daily/pool-inspect.jsonl')}
trail=re.compile(r'(?i)co-authored-by:\s*(claude (opus|sonnet|fable) [0-9.]+|gpt-6)|gpt-6(\.1)?[- ](sol|astra)')
def http_ok(u):
    p=subprocess.run(['curl','-s','-o','/dev/null','-w','%{http_code}','-L','--max-time','20',u],capture_output=True,text=True)
    return p.stdout.strip()=='200'
batch=[]
for sp in SPEC:
    r=sp['repo']
    if r in i1:
        m=i1[r]; rid=m['id']; created=m['created_at']; br=m['branch']
        ev=next((f"https://github.com/{r}/commit/{c['sha']}" for c in m['commits'] if trail.search(c['msg'])),None)
        src_files=[p for p in m['paths'] if re.search(r'\.(html|js|ts|gd|java|rs|py|swift|cs|luau)$',p) and 'node_modules' not in p][:3]
    else:
        m=pool[r]; rid=m['id']; created=m['created_at']; br=m['branch']
        ev=next(iter(m['ev'].values()),None) if m['ev'] else None
        src_files=m['src'][:3]
    url=f'https://github.com/{r}'
    assert url.casefold() not in known, r
    if sp['mev'] in ('confirmed','directory-method') and ev is None: print('WARN no trailer ev',r)
    evidence=ev if (sp['mev']=='confirmed' and ev) else f'{url}/blob/{br}/README.md' if (r in i1 and i1[r]['readme']) or (r in pool and pool[r]['readme']) else url
    if sp['mev']=='directory-method' and ev: evidence=ev
    lives=[u for u in sp.get('live',[]) if http_ok(u)]
    contained=sp.get('contained',[sp['name']])
    rec={'name':sp['name'],'github_url':url,'repository_id':rid,'repository_created_at':created,'added_to_repo_on':TODAY,'evidence_url':evidence,
      'game_links':[f'{url}/blob/{br}/{p}' for p in src_files],'live_demo_url':lives[0] if lives else None,'live_demo_urls':lives,
      'technology':sp['tech'],'model_family':sp['models'],'method_evidence':sp['mev'],'model_evidence':sp['mev'],
      'game_count':len(contained),'contained_games':contained,'counted_game_units':len(contained),'is_independent_game':True,
      'verification_status':'verified_source','verified_on':TODAY,
      'discovery_sources':[sp['src'],url]+sp.get('extra_src',[]),'verification_notes':sp['note']+(' Live demo returned HTTP 200 (availability only, not a playtest).' if lives else '')+' Source inspected only; no playtest.',
      'gauntlet_loop':False,'flops_estimate_raw':int(sp['fl']),'flops_estimate_unit':'estimated FP32 operations per second at 60 FPS','flops_estimate_confidence':'low',
      'flops_estimate_basis':'Static order-of-magnitude estimate from the renderer and simulation type; not measured.',
      'quality_estimate_10':sp['q'],'quality_estimate_basis':'Estimated from README, source tree and commit history; no runtime playtest.',
      'screenshot_urls':[],'youtube_urls':[],'publication_date_status':'repository_created_only',
      'prompt':'The complete prompt was not published in the verified source.','prompt_origin':'unknown','prompt_evidence_url':None,
      'quality_category':'curated_games' if sp['q']>=7 else 'bad_games','runtime_test_status':'Source inspected; live demo HTTP 200 only.' if lives else 'Source inspected; no live demo checked or runtime playtest.'}
    batch.append(rec)
json.dump(batch,open('research/2026-10-15-daily/game-batch.json','w'),indent=2,ensure_ascii=False)
games.extend(batch); json.dump(games,open('games.json','w'),indent=2,ensure_ascii=False); open('games.json','a').write('\n')
print(len(batch),'records',sum(b['counted_game_units'] for b in batch),'units', sum(1 for b in batch if b['live_demo_urls']),'with live demos')
