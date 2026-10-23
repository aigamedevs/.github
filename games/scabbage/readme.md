# Scabbage

> Verified game note.

![Scabbage screenshot](https://raw.githubusercontent.com/jmeekerdev/scabbage/main/docs/screenshots/blocks.jpg)

## At a glance

- **Score:** 7.7/10
- **Screenshot rating:** 5.5/10 ([manually reviewed image](https://github.com/jmeekerdev/scabbage/blob/main/docs/screenshots/blocks.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/jmeekerdev/scabbage](https://github.com/jmeekerdev/scabbage)
- **Evidence:** [direct model evidence](https://github.com/jmeekerdev/scabbage/commit/86625ff2b1f0707822ebfabee5c026ee5530b4f0)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/jmeekerdev/scabbage/blob/main/docs/screenshots/blocks.jpg) — 📸 5.5/10 · manual visual review · Use this frame for the game-level score. Block palette overlay on voxel world

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A family voxel game that runs in the browser. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jmeekerdev/scabbage/blob/main/server/internal/pb/scabbage/v1/net.pb.go](https://github.com/jmeekerdev/scabbage/blob/main/server/internal/pb/scabbage/v1/net.pb.go)
- [https://github.com/jmeekerdev/scabbage/commit/86625ff2b1f0707822ebfabee5c026ee5530b4f0](https://github.com/jmeekerdev/scabbage/commit/86625ff2b1f0707822ebfabee5c026ee5530b4f0)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/jmeekerdev/scabbage

[Back to the awesome list](../../README.md)
