# Topo Heli

> Verified game note.

![Topo Heli screenshot placeholder](topo-heli-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/RedNoos/topo-heli](https://github.com/RedNoos/topo-heli)
- **Evidence:** [direct model evidence](https://github.com/RedNoos/topo-heli/commit/7e0e47317979994c0beea0e5266135fc7512794d)
- **Live demo:** [open demo](https://rednoos.github.io/topo-heli/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Browser topography game: fly a helicopter to cities, mountains, rivers and lakes (Serbia, Netherlands, Europe). Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/RedNoos/topo-heli/blob/main/scripts/build-physical.mjs](https://github.com/RedNoos/topo-heli/blob/main/scripts/build-physical.mjs)
- [https://github.com/RedNoos/topo-heli/commit/7e0e47317979994c0beea0e5266135fc7512794d](https://github.com/RedNoos/topo-heli/commit/7e0e47317979994c0beea0e5266135fc7512794d)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/RedNoos/topo-heli

[Back to the awesome list](../../README.md)
