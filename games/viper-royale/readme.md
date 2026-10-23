# Viper Royale

> Verified game note.

![Viper Royale screenshot placeholder](viper-royale-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/hnsik/viper](https://github.com/hnsik/viper)
- **Evidence:** [direct model evidence](https://github.com/hnsik/viper/commit/524a81d17d02302473c4d3b3441359cd40385b9c)
- **Live demo:** [open demo](https://viper-ashen.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Project: a slither.io-style snake game in a single index.html (HTML5 canvas, no dependencies). Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/hnsik/viper/blob/main/index.html](https://github.com/hnsik/viper/blob/main/index.html)
- [https://github.com/hnsik/viper/commit/524a81d17d02302473c4d3b3441359cd40385b9c](https://github.com/hnsik/viper/commit/524a81d17d02302473c4d3b3441359cd40385b9c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/hnsik/viper

[Back to the awesome list](../../README.md)
