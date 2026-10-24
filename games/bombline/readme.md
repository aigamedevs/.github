# BombLine

> Verified game note.

![BombLine screenshot placeholder](bombline-placeholder.svg)

## At a glance

- **Score:** 6.8/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-24
- **Repository:** [https://github.com/JakaMale/BombLine](https://github.com/JakaMale/BombLine)
- **Evidence:** [direct model evidence](https://github.com/JakaMale/BombLine/commit/60e499b9516e2d8879cb2ef9693c99e756ae5902)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Local Dots & Boxes game for 2–4 players, built with Angular 17. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/JakaMale/BombLine/blob/main/src/app/game/game-engine.ts](https://github.com/JakaMale/BombLine/blob/main/src/app/game/game-engine.ts)
- [https://github.com/JakaMale/BombLine/commit/60e499b9516e2d8879cb2ef9693c99e756ae5902](https://github.com/JakaMale/BombLine/commit/60e499b9516e2d8879cb2ef9693c99e756ae5902)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; https://github.com/JakaMale/BombLine

[Back to the awesome list](../../README.md)
