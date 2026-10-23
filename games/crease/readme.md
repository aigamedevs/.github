# Crease

> Verified game note.

![Crease screenshot placeholder](crease-placeholder.svg)

## At a glance

- **Score:** 7.9/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Three.js, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/anand1296/Crease](https://github.com/anand1296/Crease)
- **Evidence:** [direct model evidence](https://github.com/anand1296/Crease/commit/3533d9edeb032f2816fd3537e4100e5fda418e18)
- **Live demo:** [open demo](https://crease-orcin.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A browser-based 3D cricket game, built with React, TypeScript and Three.js. Inspired by the depth and replayability of classic cricket games: batting that rewards timing and shot selection, bowling with real variation, and an opponent that plays the ball… Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/anand1296/Crease/blob/main/src/game/scenes/MatchView.tsx](https://github.com/anand1296/Crease/blob/main/src/game/scenes/MatchView.tsx)
- [https://github.com/anand1296/Crease/commit/3533d9edeb032f2816fd3537e4100e5fda418e18](https://github.com/anand1296/Crease/commit/3533d9edeb032f2816fd3537e4100e5fda418e18)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/anand1296/Crease

[Back to the awesome list](../../README.md)
