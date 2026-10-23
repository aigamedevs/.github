# Revlotto

> Verified game note.

![Revlotto screenshot placeholder](revlotto-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Phaser, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/dashaunb123/revlotto](https://github.com/dashaunb123/revlotto)
- **Evidence:** [direct model evidence](https://github.com/dashaunb123/revlotto/commit/6f994e3ed25d50effe3792a365b46e52e5ba95af)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A browser drag-racing roguelike. Build a car from 12 part slots and a hand of powerups, then race it by timing your launch and shifts. Beat the target time, get paid, shop, snowball. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/dashaunb123/revlotto/blob/main/src/scenes/ShopScene.ts](https://github.com/dashaunb123/revlotto/blob/main/src/scenes/ShopScene.ts)
- [https://github.com/dashaunb123/revlotto/commit/6f994e3ed25d50effe3792a365b46e52e5ba95af](https://github.com/dashaunb123/revlotto/commit/6f994e3ed25d50effe3792a365b46e52e5ba95af)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/dashaunb123/revlotto

[Back to the awesome list](../../README.md)
