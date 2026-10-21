# Life of Colors

> Verified game note.

![Life of Colors screenshot placeholder](life-of-colors-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/PalinkasAljoscha/LifeOfColors_game](https://github.com/PalinkasAljoscha/LifeOfColors_game)
- **Evidence:** [direct model evidence](https://github.com/PalinkasAljoscha/LifeOfColors_game/commit/c99bb3e38030c1bff2be31f7c2d81b71399381b0)
- **Live demo:** [open demo](https://palinkasaljoscha.github.io/LifeOfColors_game/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A logic puzzle with secret rules. When you tap a cell, its new colour depends on the colours of its. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/PalinkasAljoscha/LifeOfColors_game/blob/main/src/telemetry/telemetry.js](https://github.com/PalinkasAljoscha/LifeOfColors_game/blob/main/src/telemetry/telemetry.js)
- [https://github.com/PalinkasAljoscha/LifeOfColors_game/commit/c99bb3e38030c1bff2be31f7c2d81b71399381b0](https://github.com/PalinkasAljoscha/LifeOfColors_game/commit/c99bb3e38030c1bff2be31f7c2d81b71399381b0)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/PalinkasAljoscha/LifeOfColors_game

[Back to the awesome list](../../README.md)
