# HorrorStudio

> Verified game note.

![HorrorStudio screenshot placeholder](horrorstudio-placeholder.svg)

## At a glance

- **Score:** 7.9/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5, Claude Fable 5.1
- **Technology:** Unreal Engine, C++
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/tsukibii/HorrorEngine](https://github.com/tsukibii/HorrorEngine)
- **Evidence:** [direct model evidence](https://github.com/tsukibii/HorrorEngine/commit/ad52c48172e2cf2658ffc2b0b8a27d3b1ea15e4c)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

One Unreal project where all our horror games live, with Claude as co-lead engineer. You write a rough story;. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 / Claude Fable 5.1 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/tsukibii/HorrorEngine/blob/main/tools/director/app.js](https://github.com/tsukibii/HorrorEngine/blob/main/tools/director/app.js)
- [https://github.com/tsukibii/HorrorEngine/commit/ad52c48172e2cf2658ffc2b0b8a27d3b1ea15e4c](https://github.com/tsukibii/HorrorEngine/commit/ad52c48172e2cf2658ffc2b0b8a27d3b1ea15e4c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/tsukibii/HorrorEngine

[Back to the awesome list](../../README.md)
