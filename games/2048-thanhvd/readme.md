# 2048 (thanhvd)

> Verified game note.

![2048 (thanhvd) screenshot placeholder](2048-thanhvd-placeholder.svg)

## At a glance

- **Score:** 6.6/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-24
- **Repository:** [https://github.com/thanhvd/game-2048](https://github.com/thanhvd/game-2048)
- **Evidence:** [direct model evidence](https://github.com/thanhvd/game-2048/commit/6d8fa5e873f8e2105709250d7ff7e2e7a9937399)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

The sliding-tile puzzle 2048 for the browser, built with React, TypeScript and MUI. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/thanhvd/game-2048/blob/main/src/App.tsx](https://github.com/thanhvd/game-2048/blob/main/src/App.tsx)
- [https://github.com/thanhvd/game-2048/commit/6d8fa5e873f8e2105709250d7ff7e2e7a9937399](https://github.com/thanhvd/game-2048/commit/6d8fa5e873f8e2105709250d7ff7e2e7a9937399)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; https://github.com/thanhvd/game-2048

[Back to the awesome list](../../README.md)
