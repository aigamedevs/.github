# Make Ten

> Verified game note.

![Make Ten screenshot placeholder](make-ten-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Sonnet 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/koushikreddy510/make-ten](https://github.com/koushikreddy510/make-ten)
- **Evidence:** [direct model evidence](https://github.com/koushikreddy510/make-ten/commit/0d337049757431d1cdb8489f3ea256dba83aa695)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A number puzzle game built with Expo (React Native) and TypeScript. Select tiles that add up to 10 to clear them, chain clears for combos, and reach each level's target score before the moves or the clock run out. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/koushikreddy510/make-ten/blob/main/src/features/game/engine.ts](https://github.com/koushikreddy510/make-ten/blob/main/src/features/game/engine.ts)
- [https://github.com/koushikreddy510/make-ten/commit/0d337049757431d1cdb8489f3ea256dba83aa695](https://github.com/koushikreddy510/make-ten/commit/0d337049757431d1cdb8489f3ea256dba83aa695)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/koushikreddy510/make-ten

[Back to the awesome list](../../README.md)
