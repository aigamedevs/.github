# AutoGame · 像素游戏厅

> Verified game note.

![AutoGame · 像素游戏厅 screenshot](https://raw.githubusercontent.com/YichiCS/AutoGame/main/docs/hub.png)

## At a glance

- **Score:** 8.1/10
- **Screenshot rating:** 4.2/10 ([manually reviewed image](https://github.com/YichiCS/AutoGame/blob/main/docs/hub.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/YichiCS/AutoGame](https://github.com/YichiCS/AutoGame)
- **Evidence:** [direct model evidence](https://github.com/YichiCS/AutoGame/commit/2c1c9969f615b8175899c6880591fe19cf016403)
- **Live demo:** [open demo](https://yichics.github.io/AutoGame/)
- **Additional live link:** [open demo](https://yichics.github.io/AutoGame/games/research-simulator/)
- **Additional live link:** [open demo](https://yichics.github.io/AutoGame/games/pixel-baseball/dist/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/YichiCS/AutoGame/blob/main/docs/hub.png) — 📸 4.2/10 · manual visual review · Use this frame for the game-level score. Portal page with game cards and thumbnails; a menu rather than gameplay.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

像素风小游戏合集。打开网页、挑一个游戏、点一下就开始玩；所有游戏的存档在同一个地方管理。. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/YichiCS/AutoGame/blob/main/games/research-simulator/js/ui/ui.js](https://github.com/YichiCS/AutoGame/blob/main/games/research-simulator/js/ui/ui.js)
- [https://github.com/YichiCS/AutoGame/commit/2c1c9969f615b8175899c6880591fe19cf016403](https://github.com/YichiCS/AutoGame/commit/2c1c9969f615b8175899c6880591fe19cf016403)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/YichiCS/AutoGame

[Back to the awesome list](../../README.md)
