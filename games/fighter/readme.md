# Fighter

> Verified game note.

![Fighter screenshot placeholder](fighter-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-24
- **Repository:** [https://github.com/Firex2200/fighter](https://github.com/Firex2200/fighter)
- **Evidence:** [direct model evidence](https://github.com/Firex2200/fighter/commit/e7c33316b63f88eaa8c8b0562a4302bac642cbb5)
- **Live demo:** [open demo](https://firex2200.github.io/fighter/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Smash-style browser fighting game starring Rook Ashvane. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Firex2200/fighter/blob/main/src/render/rook3d.js](https://github.com/Firex2200/fighter/blob/main/src/render/rook3d.js)
- [https://github.com/Firex2200/fighter/commit/e7c33316b63f88eaa8c8b0562a4302bac642cbb5](https://github.com/Firex2200/fighter/commit/e7c33316b63f88eaa8c8b0562a4302bac642cbb5)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; https://github.com/Firex2200/fighter

[Back to the awesome list](../../README.md)
