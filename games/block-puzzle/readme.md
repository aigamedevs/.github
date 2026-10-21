# Block Puzzle

> Verified game note.

![Block Puzzle screenshot](https://raw.githubusercontent.com/uchedavid50-oss/blockpuzzle/main/docs/screens/gameplay.png)

## At a glance

- **Score:** 7.7/10
- **Screenshot rating:** 5.2/10 ([manually reviewed image](https://github.com/uchedavid50-oss/blockpuzzle/blob/main/docs/screens/gameplay.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Sonnet 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/uchedavid50-oss/blockpuzzle](https://github.com/uchedavid50-oss/blockpuzzle)
- **Evidence:** [direct model evidence](https://github.com/uchedavid50-oss/blockpuzzle/commit/5b94247f90b24747300f784342bd24987533019b)
- **Live demo:** [open demo](https://blockpuzzle-three.vercel.app)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/uchedavid50-oss/blockpuzzle/blob/main/docs/screens/gameplay.png) — 📸 5.2/10 · manual visual review · Use this frame for the game-level score. Portrait 8x8 block puzzle with colourful blocks, score and tray; clean but standard.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Original 8x8 drag-and-drop block puzzle. Vite + TypeScript + Canvas 2D, installable PWA. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/uchedavid50-oss/blockpuzzle/blob/main/src/mapView.ts](https://github.com/uchedavid50-oss/blockpuzzle/blob/main/src/mapView.ts)
- [https://github.com/uchedavid50-oss/blockpuzzle/commit/5b94247f90b24747300f784342bd24987533019b](https://github.com/uchedavid50-oss/blockpuzzle/commit/5b94247f90b24747300f784342bd24987533019b)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/uchedavid50-oss/blockpuzzle

[Back to the awesome list](../../README.md)
