# Riftbrand

> Verified game note.

![Riftbrand screenshot placeholder](riftbrand-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, PixiJS, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/oe7set/riftbrand](https://github.com/oe7set/riftbrand)
- **Evidence:** [direct model evidence](https://github.com/oe7set/riftbrand/commit/eefafccb5cf7f27ddc96989f729c504c592a8f2f)
- **Live demo:** [open demo](https://oe7set.github.io/riftbrand/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

2D-Action-Roguelike für den Browser: mobile-first (Touch), aber auch mit Tastatur/Maus und Gamepad spielbar. Neon-Vektor-Look, TypeScript, PixiJS v8, deterministischer Simulationskern. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/oe7set/riftbrand/blob/ccr-44cded7b-e91ufi/src/app/game.ts](https://github.com/oe7set/riftbrand/blob/ccr-44cded7b-e91ufi/src/app/game.ts)
- [https://github.com/oe7set/riftbrand/commit/eefafccb5cf7f27ddc96989f729c504c592a8f2f](https://github.com/oe7set/riftbrand/commit/eefafccb5cf7f27ddc96989f729c504c592a8f2f)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/oe7set/riftbrand

[Back to the awesome list](../../README.md)
