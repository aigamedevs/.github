# Riftcast

> Verified game note.

![Riftcast screenshot](https://raw.githubusercontent.com/iamboosted/riftcast/master/screenshots/combat-high.jpg)

## At a glance

- **Score:** 7.7/10
- **Screenshot rating:** 7.6/10 ([manually reviewed image](https://github.com/iamboosted/riftcast/blob/master/screenshots/combat-high.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Three.js, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/iamboosted/riftcast](https://github.com/iamboosted/riftcast)
- **Evidence:** [direct model evidence](https://github.com/iamboosted/riftcast/commit/105c2d1b2caa595c9df77029a953c36c1faf4afc)
- **Live demo:** [open demo](https://iamboosted.github.io/riftcast/)
- **Additional live link:** [open demo](https://iamboosted.github.io/riftcast/vfx-gallery/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/iamboosted/riftcast/blob/master/screenshots/combat-high.jpg) — 📸 7.6/10 · manual visual review · Use this frame for the game-level score. Third-person arena spell fight with a glowing frost burst, orange sky, floating rocks and a clean health/spell HUD; strong lighting, coherent stylized 3D.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A zero-asset 3D co-op elemental mage roguelite for 1–4 players, running in the browser on Three.js WebGPURenderer + TSL (with automatic WebGL2 fallback). Every mesh, texture, particle sprite, shader and sound is generated at runtime. It loads instantly, needs… Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/iamboosted/riftcast/blob/master/src/vfx/fx.ts](https://github.com/iamboosted/riftcast/blob/master/src/vfx/fx.ts)
- [https://github.com/iamboosted/riftcast/commit/105c2d1b2caa595c9df77029a953c36c1faf4afc](https://github.com/iamboosted/riftcast/commit/105c2d1b2caa595c9df77029a953c36c1faf4afc)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/iamboosted/riftcast

[Back to the awesome list](../../README.md)
