# Run Out

> Verified game note.

![Run Out screenshot placeholder](run-out-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5
- **Technology:** HTML, JavaScript, Canvas, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-16
- **Repository:** [https://github.com/NiceWorkLad/pool-game](https://github.com/NiceWorkLad/pool-game)
- **Evidence:** [direct model evidence](https://github.com/NiceWorkLad/pool-game/commit/fc02ca02d8a28f30edb0b481d89f2851d3d8f7c1)
- **Live demo:** [open demo](https://pool.whittleadams.com)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Single-page pool game with 8-ball puzzles, a Learn mode, Survival, Blackout and two-player 8-ball, plus levels and XP. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected only; no playtest.

### Gameplay source

- [https://github.com/NiceWorkLad/pool-game/blob/main/index.html](https://github.com/NiceWorkLad/pool-game/blob/main/index.html)
- [https://github.com/NiceWorkLad/pool-game/commit/fc02ca02d8a28f30edb0b481d89f2851d3d8f7c1](https://github.com/NiceWorkLad/pool-game/commit/fc02ca02d8a28f30edb0b481d89f2851d3d8f7c1)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-15..2026-10-16 (6-hour UTC partitions) joined to repositories created after 2026-10-14T17:00Z; https://github.com/NiceWorkLad/pool-game

[Back to the awesome list](../../README.md)
