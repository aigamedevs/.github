# City Grid

> Verified game note.

![City Grid screenshot placeholder](city-grid-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/hectorei19/city-grid](https://github.com/hectorei19/city-grid)
- **Evidence:** [direct model evidence](https://github.com/hectorei19/city-grid/commit/20a95a737e2dc348d4f33a5d43b8e13bd4d37a75)
- **Live demo:** [open demo](https://hectorei19.github.io/country-grid/)
- **Additional live link:** [open demo](https://hectorei19.github.io/city-grid/)
- **Additional live link:** [open demo](https://hectorei19.github.io/geo-games/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Geography grid game with cities: name a city that matches each row and column (the 195 national capitals, one per country). A sister of Country Grid, same game and same look, with cities instead of countries. Every grid is checked so it can always be… Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/hectorei19/city-grid/blob/claude/city-cross-8cg8rw/index.html](https://github.com/hectorei19/city-grid/blob/claude/city-cross-8cg8rw/index.html)
- [https://github.com/hectorei19/city-grid/commit/20a95a737e2dc348d4f33a5d43b8e13bd4d37a75](https://github.com/hectorei19/city-grid/commit/20a95a737e2dc348d4f33a5d43b8e13bd4d37a75)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/hectorei19/city-grid

[Back to the awesome list](../../README.md)
