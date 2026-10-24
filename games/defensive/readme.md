# Defensive

> Verified game note.

![Defensive screenshot placeholder](defensive-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-24
- **Repository:** [https://github.com/dkeslowitz-afk/Defensive](https://github.com/dkeslowitz-afk/Defensive)
- **Evidence:** [direct model evidence](https://github.com/dkeslowitz-afk/Defensive/commit/fb558b8aba7a56a4d40d93b63c7eb6f8deb0876c)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A mobile-first tower defense game. Plain HTML/CSS/JS + canvas, no build step. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/dkeslowitz-afk/Defensive/blob/main/js/ui.js](https://github.com/dkeslowitz-afk/Defensive/blob/main/js/ui.js)
- [https://github.com/dkeslowitz-afk/Defensive/commit/fb558b8aba7a56a4d40d93b63c7eb6f8deb0876c](https://github.com/dkeslowitz-afk/Defensive/commit/fb558b8aba7a56a4d40d93b63c7eb6f8deb0876c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; https://github.com/dkeslowitz-afk/Defensive

[Back to the awesome list](../../README.md)
