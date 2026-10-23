# World Conquest

> Verified game note.

![World Conquest screenshot](https://raw.githubusercontent.com/foster-curtis/world-conquest/main/tools/map-build/preview.png)

## At a glance

- **Score:** 7.3/10
- **Screenshot rating:** 5.0/10 ([manually reviewed image](https://github.com/foster-curtis/world-conquest/blob/main/tools/map-build/preview.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/foster-curtis/world-conquest](https://github.com/foster-curtis/world-conquest)
- **Evidence:** [direct model evidence](https://github.com/foster-curtis/world-conquest/commit/29617aab78bbf6f3abfdd56b3171efcaa0941014)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/foster-curtis/world-conquest/blob/main/tools/map-build/preview.png) — 📸 5.0/10 · manual visual review · Use this frame for the game-level score. Flat colour-coded world map board with clean territory borders; readable but sparse, no units or HUD visible.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

An online copycat of Risk. Pass and play and online are available, synchronous or asynchronous. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/foster-curtis/world-conquest/blob/main/packages/engine/src/decide.ts](https://github.com/foster-curtis/world-conquest/blob/main/packages/engine/src/decide.ts)
- [https://github.com/foster-curtis/world-conquest/commit/29617aab78bbf6f3abfdd56b3171efcaa0941014](https://github.com/foster-curtis/world-conquest/commit/29617aab78bbf6f3abfdd56b3171efcaa0941014)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/foster-curtis/world-conquest

[Back to the awesome list](../../README.md)
