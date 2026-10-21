# Deepward

> Verified game note.

![Deepward screenshot placeholder](deepward-placeholder.svg)

## At a glance

- **Score:** 7.8/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** JavaScript, Three.js, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/leehj825/Deepward](https://github.com/leehj825/Deepward)
- **Evidence:** [direct model evidence](https://github.com/leehj825/Deepward/commit/0b52d232db7c6d73365270ad971fb48d93e4ca74)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A quarter-view 3D action dungeon crawler that runs in the browser (Three.js r128, no build step). No town, no army: the whole game is the fight. Every enemy attack is telegraphed, and each dungeon tier demands a skill the last one didn't: spacing, then… Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/leehj825/Deepward/blob/main/js/anims.js](https://github.com/leehj825/Deepward/blob/main/js/anims.js)
- [https://github.com/leehj825/Deepward/commit/0b52d232db7c6d73365270ad971fb48d93e4ca74](https://github.com/leehj825/Deepward/commit/0b52d232db7c6d73365270ad971fb48d93e4ca74)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/leehj825/Deepward

[Back to the awesome list](../../README.md)
