# 岩瀬酒造 蔵元カードゲーム（仮）

> Verified game note.

![岩瀬酒造 蔵元カードゲーム（仮） screenshot placeholder](game-kenchasonakai-iwanoi-card-game-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5, Claude Fable 5.1
- **Technology:** TypeScript, Phaser, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/kenchasonakai/iwanoi-card-game](https://github.com/kenchasonakai/iwanoi-card-game)
- **Evidence:** [direct model evidence](https://github.com/kenchasonakai/iwanoi-card-game/commit/a676cd16457eb0acb50559b2336280e74bb93a49)
- **Live demo:** [open demo](https://kenchasonakai.github.io/iwanoi-card-game/)
- **Additional live link:** [open demo](https://kenchasonakai.github.io/iwanoi-card-game/guide/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

岩瀬酒造（千葉県御宿町、銘柄「岩の井」）の酒造りを、1 人で遊ぶカードゲームです。ハッカソンの題材として作ります。. Commit carries an exact Claude Opus 5.5 / Claude Fable 5.1 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/kenchasonakai/iwanoi-card-game/blob/main/src/scenes/BoardScene.ts](https://github.com/kenchasonakai/iwanoi-card-game/blob/main/src/scenes/BoardScene.ts)
- [https://github.com/kenchasonakai/iwanoi-card-game/commit/a676cd16457eb0acb50559b2336280e74bb93a49](https://github.com/kenchasonakai/iwanoi-card-game/commit/a676cd16457eb0acb50559b2336280e74bb93a49)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/kenchasonakai/iwanoi-card-game

[Back to the awesome list](../../README.md)
