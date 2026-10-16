# Build the 2026-10-16 daily batch and append records to games.json.
import json,math,sys
sys.path.insert(0,'research/2026-10-16-daily'); from spec import SPEC,MEV,AGG
TODAY='2026-10-16'; D='research/2026-10-16-daily/'
games=json.load(open('games.json')); known={g['github_url'].casefold() for g in games}
ins=json.load(open(D+'inspect.json')); trees=json.load(open(D+'trees.json')); ev=json.load(open(D+'evidence.json'))
live=json.load(open(D+'live-checks.json'))['live']
BAD=('peerjs.com','appstoreconnect','laravel.com','laracasts.com','embed-test','poses.html','?slice=')
repo_hits={json.loads(l)['full_name'] for l in open(D+'repo-searches.jsonl')}
RS='GitHub repository search: exact model phrase, created 2026-10-14T17:00Z..2026-10-16T02:00Z'
CP='GitHub commit pool: model+game commits 2026-10-15..2026-10-16 (6-hour UTC partitions) joined to repositories created after 2026-10-14T17:00Z'
ORDER=['Claude Opus 5.5','Claude Sonnet 5.5','Claude Fable 5.1','GPT-6.1 Sol','GPT-6 Astra','Gemini 4 Argon']
batch=[]
for r,name,tech,fl,note in SPEC:
    url=f'https://github.com/{r}'; assert url.casefold() not in known, r
    m=ins[r]; t=trees[r]; br=m['branch'] or t['branch']
    co=ev[r]['co']
    if r in MEV: mev,models=MEV[r]; evidence=f'{url}/blob/{br}/README.md' if m['readme'] else url
    else:
        mev='confirmed'; models=[x for x in ORDER if x in co]; evidence=f"{url}/commit/{co[models[0]]}"
    lives=[u for u in live.get(r,[]) if not any(b in u for b in BAD)]
    kb=t['code_bytes']/1000
    q=round(min(8.6,5.8+0.6*math.log10(kb+1)+(0.3 if lives else 0)),1)
    contained=[name]
    rec={'name':name,'github_url':url,'repository_id':m['id'],'repository_created_at':m['created'],'added_to_repo_on':TODAY,'evidence_url':evidence,
      'game_links':[f'{url}/blob/{br}/{p}' for p,_ in t['top'][:3]],'live_demo_url':lives[0] if lives else None,'live_demo_urls':lives,
      'technology':tech,'model_family':models,'method_evidence':mev,'model_evidence':mev,
      'game_count':1,'contained_games':contained,'counted_game_units':1,'is_independent_game':True,
      'verification_status':'verified_source','verified_on':TODAY,
      'discovery_sources':[RS if r in repo_hits else CP,url],
      'verification_notes':note+(' Commit carries an exact '+' / '.join(models)+' co-author trailer.' if mev=='confirmed' else '')+(' Live demo returned HTTP 200 (availability only, not a playtest).' if lives else '')+' Source inspected only; no playtest.',
      'gauntlet_loop':False,'flops_estimate_raw':int(fl),'flops_estimate_unit':'estimated FP32 operations per second at 60 FPS','flops_estimate_confidence':'low',
      'flops_estimate_basis':'Static order-of-magnitude estimate from the renderer and simulation type; not measured.',
      'quality_estimate_10':q,'quality_estimate_basis':'Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.',
      'screenshot_urls':[],'youtube_urls':[],'publication_date_status':'repository_created_only',
      'prompt':'The complete prompt was not published in the verified source.','prompt_origin':'unknown','prompt_evidence_url':None,
      'quality_category':'curated_games' if q>=7 else 'bad_games','runtime_test_status':'Source inspected; live demo HTTP 200 only.' if lives else 'Source inspected; no live demo checked or runtime playtest.'}
    batch.append(rec)
out={'verified_on':TODAY,'timezone':'Asia/Ho_Chi_Minh','window_start':'2026-10-15','window_end':'2026-10-16','expected_repositories':len(batch),'expected_game_units':sum(b['counted_game_units'] for b in batch),'date_basis':'repository creation proxy only',
  'records':[{k:b[k] for k in ('name','github_url','repository_id','repository_created_at','counted_game_units','evidence_url','publication_date_status','game_links','model_family','method_evidence','added_to_repo_on','verified_on','verification_status','live_demo_url')} for b in batch]}
json.dump(out,open(D+'game-batch.json','w'),indent=2,ensure_ascii=False)
games.extend(batch); json.dump(games,open('games.json','w'),indent=2,ensure_ascii=False); open('games.json','a').write('\n')
print(len(batch),'records',sum(b['counted_game_units'] for b in batch),'units',sum(1 for b in batch if b['live_demo_urls']),'with live demos')
