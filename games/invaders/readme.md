# Invaders

> Verified game note.

![Invaders screenshot](https://raw.githubusercontent.com/cocodedk/invaders/main/og.png)

## At a glance

- **Score:** 7.8/10
- **Screenshot rating:** 5.5/10 ([manually reviewed image](https://github.com/cocodedk/invaders/blob/main/og.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/cocodedk/invaders](https://github.com/cocodedk/invaders)
- **Evidence:** [direct model evidence](https://github.com/cocodedk/invaders/commit/1a66326020cf791a85b941de3e26efa491d5053c)
- **Live demo:** [open demo](https://invaders.cocode.dk)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/cocodedk/invaders/blob/main/og.png) — 📸 5.5/10 · manual visual review · Use this frame for the game-level score. Title banner with logo, tagline and four small level thumbnails; promotional, discounted.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A cinematic arcade shooter for the browser: 8 worlds, 40 levels, and a trailer cut from your own run. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/cocodedk/invaders/blob/main/src/fx/react-world.js](https://github.com/cocodedk/invaders/blob/main/src/fx/react-world.js)
- [https://github.com/cocodedk/invaders/commit/1a66326020cf791a85b941de3e26efa491d5053c](https://github.com/cocodedk/invaders/commit/1a66326020cf791a85b941de3e26efa491d5053c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/cocodedk/invaders

[Back to the awesome list](../../README.md)
