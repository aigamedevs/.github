# Mister Mole

> Verified game note.

![Mister Mole screenshot](https://raw.githubusercontent.com/BillYLZ/r3f-mister-mole/main/docs/mister-mole.png)

## At a glance

- **Score:** 7.1/10
- **Screenshot rating:** 7.0/10 ([manually reviewed image](https://github.com/BillYLZ/r3f-mister-mole/blob/main/docs/mister-mole.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Three.js, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/BillYLZ/r3f-mister-mole](https://github.com/BillYLZ/r3f-mister-mole)
- **Evidence:** [direct model evidence](https://github.com/BillYLZ/r3f-mister-mole/commit/23944404290346e2d5075c52d89efe9eecc28ae1)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/BillYLZ/r3f-mister-mole/blob/main/docs/mister-mole.png) — 📸 7.0/10 · manual visual review · Use this frame for the game-level score. 3D digging mine with dirt blocks, boulders, gems and score HUD; solid lighting and readability.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

1980'lerin klasik maden oyunlarından esinlenen, React Three Fiber ile yazılmış 3B bir maden oyunu. Grafikler, sesler ve mağaralar bu projeye özgüdür; hiçbir oyundan varlık kopyalanmamıştır. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/BillYLZ/r3f-mister-mole/blob/main/src/v2/SceneV2.tsx](https://github.com/BillYLZ/r3f-mister-mole/blob/main/src/v2/SceneV2.tsx)
- [https://github.com/BillYLZ/r3f-mister-mole/commit/23944404290346e2d5075c52d89efe9eecc28ae1](https://github.com/BillYLZ/r3f-mister-mole/commit/23944404290346e2d5075c52d89efe9eecc28ae1)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/BillYLZ/r3f-mister-mole

[Back to the awesome list](../../README.md)
