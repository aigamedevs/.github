# דובב (Simon)

> Verified game note.

![דובב (Simon) screenshot placeholder](simon-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/dovevgit/simon-game](https://github.com/dovevgit/simon-game)
- **Evidence:** [direct model evidence](https://github.com/dovevgit/simon-game/commit/0ed1ad664bf29e898f8ac91d3e2e6b9c0ad6306a)
- **Live demo:** [open demo](https://dovevgit.github.io/simon-game/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

simon sound and color old school game. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/dovevgit/simon-game/blob/main/src/game/useGame.ts](https://github.com/dovevgit/simon-game/blob/main/src/game/useGame.ts)
- [https://github.com/dovevgit/simon-game/commit/0ed1ad664bf29e898f8ac91d3e2e6b9c0ad6306a](https://github.com/dovevgit/simon-game/commit/0ed1ad664bf29e898f8ac91d3e2e6b9c0ad6306a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/dovevgit/simon-game

[Back to the awesome list](../../README.md)
