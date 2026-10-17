# California Drive

> Verified game note.

![California Drive screenshot](https://raw.githubusercontent.com/roszhan2684/california-drive/main/docs/media/la-day-clear.jpg)

## At a glance

- **Score:** 7.8/10
- **Screenshot rating:** 6.8/10 ([manually reviewed image](https://github.com/roszhan2684/california-drive/blob/main/docs/media/la-day-clear.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/roszhan2684/california-drive](https://github.com/roszhan2684/california-drive)
- **Evidence:** [direct model evidence](https://github.com/roszhan2684/california-drive/commit/63f6bcfd1f9ce048755470dad36fc4ffe4ece884)
- **Live demo:** [open demo](https://roszhan2684.github.io/california-drive/)
- **Additional live link:** [open demo](https://california-drive.vercel.app)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/roszhan2684/california-drive/blob/main/docs/media/la-day-clear.jpg) — 📸 6.8/10 · manual visual review · Use this frame for the game-level score. Third-person 3D drive on a city avenue with towers, trees and an orange sports car; clean lighting, simple geometry.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Accountless browser open-world California driving game built from open map data. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/roszhan2684/california-drive/blob/main/src/world/chunkGen.ts](https://github.com/roszhan2684/california-drive/blob/main/src/world/chunkGen.ts)
- [https://github.com/roszhan2684/california-drive/commit/63f6bcfd1f9ce048755470dad36fc4ffe4ece884](https://github.com/roszhan2684/california-drive/commit/63f6bcfd1f9ce048755470dad36fc4ffe4ece884)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/roszhan2684/california-drive

[Back to the awesome list](../../README.md)
