# Sensory Town

> Verified game note.

![Sensory Town screenshot placeholder](sensory-town-placeholder.svg)

## At a glance

- **Score:** 8.1/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/darthreckoner/sensory-town](https://github.com/darthreckoner/sensory-town)
- **Evidence:** [direct model evidence](https://github.com/darthreckoner/sensory-town/commit/bfa8f53e5f9c08518024720ef9edbd1b6694b694)
- **Live demo:** [open demo](https://darthreckoner.github.io/sensory-town/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Sensory Town — a cozy offline 3D toy town for iPad (dress up, drive, build, squish, slime, wax cracking). Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/darthreckoner/sensory-town/blob/main/src/scenes/BuildScene.ts](https://github.com/darthreckoner/sensory-town/blob/main/src/scenes/BuildScene.ts)
- [https://github.com/darthreckoner/sensory-town/commit/bfa8f53e5f9c08518024720ef9edbd1b6694b694](https://github.com/darthreckoner/sensory-town/commit/bfa8f53e5f9c08518024720ef9edbd1b6694b694)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/darthreckoner/sensory-town

[Back to the awesome list](../../README.md)
