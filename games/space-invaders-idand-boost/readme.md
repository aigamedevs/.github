# Space Invaders (idand-boost)

> Verified game note.

![Space Invaders (idand-boost) screenshot placeholder](space-invaders-idand-boost-placeholder.svg)

## At a glance

- **Score:** 6.9/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/idand-boost/space-invaders-monday-sdk](https://github.com/idand-boost/space-invaders-monday-sdk)
- **Evidence:** [direct model evidence](https://github.com/idand-boost/space-invaders-monday-sdk/commit/28010acdd5c65588c2b91971225702a4eea493ab)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A Space Invaders clone built with TypeScript + Vite, using React purely as the renderer. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/idand-boost/space-invaders-monday-sdk/blob/main/src/game/engine.ts](https://github.com/idand-boost/space-invaders-monday-sdk/blob/main/src/game/engine.ts)
- [https://github.com/idand-boost/space-invaders-monday-sdk/commit/28010acdd5c65588c2b91971225702a4eea493ab](https://github.com/idand-boost/space-invaders-monday-sdk/commit/28010acdd5c65588c2b91971225702a4eea493ab)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/idand-boost/space-invaders-monday-sdk

[Back to the awesome list](../../README.md)
