# Endfall

> Verified game note.

![Endfall screenshot placeholder](endfall-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/mazzucci/endfall](https://github.com/mazzucci/endfall)
- **Evidence:** [direct model evidence](https://github.com/mazzucci/endfall/commit/30d0bf71f0bb1b8f79f241f4199173857a7569a3)
- **Live demo:** [open demo](https://mazzucci.github.io/endfall/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A browser real-time strategy game in the 1998 mold: mine shards and ether, build supply, raise an army, and level. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/mazzucci/endfall/blob/main/crates/endfall-sim/src/world.rs](https://github.com/mazzucci/endfall/blob/main/crates/endfall-sim/src/world.rs)
- [https://github.com/mazzucci/endfall/commit/30d0bf71f0bb1b8f79f241f4199173857a7569a3](https://github.com/mazzucci/endfall/commit/30d0bf71f0bb1b8f79f241f4199173857a7569a3)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/mazzucci/endfall

[Back to the awesome list](../../README.md)
