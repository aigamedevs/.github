# STARFALL

> Verified game note.

![STARFALL screenshot](https://raw.githubusercontent.com/hiradbaba/starfall/main/docs/media/gameplay.gif)

## At a glance

- **Score:** 7.2/10
- **Screenshot rating:** 3.8/10 ([manually reviewed image](https://github.com/hiradbaba/starfall/blob/main/docs/media/gameplay.gif)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/hiradbaba/starfall](https://github.com/hiradbaba/starfall)
- **Evidence:** [direct model evidence](https://github.com/hiradbaba/starfall/commit/d61da61aa775520a0758b710e4409e4a18a32e0c)
- **Live demo:** [open demo](https://hiradbaba.github.io/starfall/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/hiradbaba/starfall/blob/main/docs/media/gameplay.gif) — 📸 3.8/10 · manual visual review · Use this frame for the game-level score. Sparse vector-style space shooter with a few small ships on black and a thin score line.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

remake of the old cpp star wars game that I had for my bachelors in 2019. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/hiradbaba/starfall/blob/main/src/screens/play.ts](https://github.com/hiradbaba/starfall/blob/main/src/screens/play.ts)
- [https://github.com/hiradbaba/starfall/commit/d61da61aa775520a0758b710e4409e4a18a32e0c](https://github.com/hiradbaba/starfall/commit/d61da61aa775520a0758b710e4409e4a18a32e0c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/hiradbaba/starfall

[Back to the awesome list](../../README.md)
