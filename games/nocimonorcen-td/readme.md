# Nocimonorcen TD

> Verified game note.

![Nocimonorcen TD screenshot placeholder](nocimonorcen-td-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Phaser, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/SinisterN/Nocimonorcen](https://github.com/SinisterN/Nocimonorcen)
- **Evidence:** [direct model evidence](https://github.com/SinisterN/Nocimonorcen/commit/96cfb329622ca0b865924457f22cd0106c30433e)
- **Live demo:** [open demo](https://sinistern.github.io/Nocimonorcen/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Isometric tower defense with puzzle-driven upgrades. Built with Phaser 4, TypeScript and Vite. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/SinisterN/Nocimonorcen/blob/main/src/scenes/GameScene.ts](https://github.com/SinisterN/Nocimonorcen/blob/main/src/scenes/GameScene.ts)
- [https://github.com/SinisterN/Nocimonorcen/commit/96cfb329622ca0b865924457f22cd0106c30433e](https://github.com/SinisterN/Nocimonorcen/commit/96cfb329622ca0b865924457f22cd0106c30433e)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/SinisterN/Nocimonorcen

[Back to the awesome list](../../README.md)
