# Hearthvale

> Verified game note.

![Hearthvale screenshot](https://raw.githubusercontent.com/jaybecina/hearthvale/main/docs/media/spring.png)

## At a glance

- **Score:** 7.3/10
- **Screenshot rating:** 6.0/10 ([manually reviewed image](https://github.com/jaybecina/hearthvale/blob/main/docs/media/spring.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-24
- **Repository:** [https://github.com/jaybecina/hearthvale](https://github.com/jaybecina/hearthvale)
- **Evidence:** [direct model evidence](https://github.com/jaybecina/hearthvale/commit/cccac9453c7f566016907a3e138327437492f7a4)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/jaybecina/hearthvale/blob/main/docs/media/spring.png) — 📸 6.0/10 · manual visual review · Use this frame for the game-level score. Cozy 3D farm plot with a house corner, crops and hotbar HUD; clean but plain.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Hearthvale: a cozy 3D farming-life game for the browser and phones. Clear grandpa's farm, grow 8 crops through 4 seasons and weather, and save the valley. React Three Fiber + a pure, tested TypeScript rules engine. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jaybecina/hearthvale/blob/main/apps/web/src/ui/screens/SaveSlots.tsx](https://github.com/jaybecina/hearthvale/blob/main/apps/web/src/ui/screens/SaveSlots.tsx)
- [https://github.com/jaybecina/hearthvale/commit/cccac9453c7f566016907a3e138327437492f7a4](https://github.com/jaybecina/hearthvale/commit/cccac9453c7f566016907a3e138327437492f7a4)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; https://github.com/jaybecina/hearthvale

[Back to the awesome list](../../README.md)
