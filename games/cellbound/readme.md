# Cellbound

> Verified game note.

![Cellbound screenshot](https://raw.githubusercontent.com/playingpossumm/cellbound/main/docs/laptop.png)

## At a glance

- **Score:** 7.7/10
- **Screenshot rating:** 5.6/10 ([manually reviewed image](https://github.com/playingpossumm/cellbound/blob/main/docs/laptop.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-24
- **Repository:** [https://github.com/playingpossumm/cellbound](https://github.com/playingpossumm/cellbound)
- **Evidence:** [direct model evidence](https://github.com/playingpossumm/cellbound/commit/988490eb2791e7770f84277a8835760eef4abad0)
- **Live demo:** [open demo](https://cellbound-sudoku.vercel.app)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/playingpossumm/cellbound/blob/main/docs/laptop.png) — 📸 5.6/10 · manual visual review · Use this frame for the game-level score. Dark variant sudoku board with killer-cage lines and keypad; elegant and readable.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Variant sudoku in the browser: a daily puzzle, roguelite runs, fog, free play and lessons, in six looks. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/playingpossumm/cellbound/blob/main/src/game/store.ts](https://github.com/playingpossumm/cellbound/blob/main/src/game/store.ts)
- [https://github.com/playingpossumm/cellbound/commit/988490eb2791e7770f84277a8835760eef4abad0](https://github.com/playingpossumm/cellbound/commit/988490eb2791e7770f84277a8835760eef4abad0)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; https://github.com/playingpossumm/cellbound

[Back to the awesome list](../../README.md)
