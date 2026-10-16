# CarRace

> Verified game note.

![CarRace screenshot placeholder](carrace-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-16
- **Repository:** [https://github.com/alexander-uspenskiy/CarRace](https://github.com/alexander-uspenskiy/CarRace)
- **Evidence:** [direct model evidence](https://github.com/alexander-uspenskiy/CarRace/commit/9814f3281b74eacf91fbfc498f0b51da684e346e)
- **Live demo:** [open demo](https://alexander-uspenskiy.github.io/CarRace/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Formula-style Three.js racing game with three circuits, a 20-car grid, upgrades and Hall of Fame. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected only; no playtest.

### Gameplay source

- [https://github.com/alexander-uspenskiy/CarRace/blob/main/src/render/geomUtil.js](https://github.com/alexander-uspenskiy/CarRace/blob/main/src/render/geomUtil.js)
- [https://github.com/alexander-uspenskiy/CarRace/commit/9814f3281b74eacf91fbfc498f0b51da684e346e](https://github.com/alexander-uspenskiy/CarRace/commit/9814f3281b74eacf91fbfc498f0b51da684e346e)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-15..2026-10-16 (6-hour UTC partitions) joined to repositories created after 2026-10-14T17:00Z; https://github.com/alexander-uspenskiy/CarRace

[Back to the awesome list](../../README.md)
