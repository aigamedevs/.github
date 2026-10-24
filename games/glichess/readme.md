# Glichess

> Verified game note.

![Glichess screenshot](https://raw.githubusercontent.com/govindpvenu/glichess/main/docs/demo.gif)

## At a glance

- **Score:** 7.2/10
- **Screenshot rating:** 3.6/10 ([manually reviewed image](https://github.com/govindpvenu/glichess/blob/main/docs/demo.gif)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-24
- **Repository:** [https://github.com/govindpvenu/glichess](https://github.com/govindpvenu/glichess)
- **Evidence:** [direct model evidence](https://github.com/govindpvenu/glichess/commit/ac2f365e2e6faa95c49fc4f52b22c73cf53d51e2)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/govindpvenu/glichess/blob/main/docs/demo.gif) — 📸 3.6/10 · manual visual review · Use this frame for the game-level score. Dark landing page for an online chess site; mostly empty UI.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Realtime chess with built-in video, voice and chat. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/govindpvenu/glichess/blob/main/apps/server/src/game/manager.ts](https://github.com/govindpvenu/glichess/blob/main/apps/server/src/game/manager.ts)
- [https://github.com/govindpvenu/glichess/commit/ac2f365e2e6faa95c49fc4f52b22c73cf53d51e2](https://github.com/govindpvenu/glichess/commit/ac2f365e2e6faa95c49fc4f52b22c73cf53d51e2)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; https://github.com/govindpvenu/glichess

[Back to the awesome list](../../README.md)
