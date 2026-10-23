# Saultsteroids

> Verified game note.

![Saultsteroids screenshot placeholder](saultsteroids-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/saultcollege/saultsteroids](https://github.com/saultcollege/saultsteroids)
- **Evidence:** [direct model evidence](https://github.com/saultcollege/saultsteroids/commit/7fae8e3813367811f970217fc2fecbf375f1e7cd)
- **Live demo:** [open demo](https://saultcollege.github.io/saultsteroids/)
- **Additional live link:** [open demo](https://saultcollege.github.io/saultsteroids/?kiosk)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A Sault College take on Asteroids, built with LittleJS. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/saultcollege/saultsteroids/blob/main/src/game.js](https://github.com/saultcollege/saultsteroids/blob/main/src/game.js)
- [https://github.com/saultcollege/saultsteroids/commit/7fae8e3813367811f970217fc2fecbf375f1e7cd](https://github.com/saultcollege/saultsteroids/commit/7fae8e3813367811f970217fc2fecbf375f1e7cd)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/saultcollege/saultsteroids

[Back to the awesome list](../../README.md)
