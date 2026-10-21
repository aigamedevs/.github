# Roguelites

> Top-list entry: **today** (#10).

![Roguelites screenshot](https://raw.githubusercontent.com/MundaPlus/roguelites/main/docs/demo.gif)

## At a glance

- **Score:** 8.4/10
- **Screenshot rating:** 4.0/10 ([manually reviewed image](https://github.com/MundaPlus/roguelites/blob/main/docs/demo.gif)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/MundaPlus/roguelites](https://github.com/MundaPlus/roguelites)
- **Evidence:** [direct model evidence](https://github.com/MundaPlus/roguelites/commit/ef11b71308e8fafb5cfa82a4329ddd5514074186)
- **Live demo:** [open demo](https://mundaplus.github.io/roguelites/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/MundaPlus/roguelites/blob/main/docs/demo.gif) — 📸 4.0/10 · manual visual review · Use this frame for the game-level score. Launcher grid of roguelite game tiles; a menu, not gameplay.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

60 small web roguelite games: 50 classic play styles and 10 new concepts. Play in the browser on PC and phone. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/MundaPlus/roguelites/blob/main/neon-depths/src/game.ts](https://github.com/MundaPlus/roguelites/blob/main/neon-depths/src/game.ts)
- [https://github.com/MundaPlus/roguelites/commit/ef11b71308e8fafb5cfa82a4329ddd5514074186](https://github.com/MundaPlus/roguelites/commit/ef11b71308e8fafb5cfa82a4329ddd5514074186)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/MundaPlus/roguelites

[Back to the awesome list](../../README.md)
