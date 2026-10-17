# Ruler of the Plane

> Verified game note.

![Ruler of the Plane screenshot](https://raw.githubusercontent.com/ls11ae/ruler-of-the-plane/main/docs/look/start-map.webp)

## At a glance

- **Score:** 7.8/10
- **Screenshot rating:** 6.0/10 ([manually reviewed image](https://github.com/ls11ae/ruler-of-the-plane/blob/main/docs/look/start-map.webp)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Unity, C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/ls11ae/ruler-of-the-plane](https://github.com/ls11ae/ruler-of-the-plane)
- **Evidence:** [direct model evidence](https://github.com/ls11ae/ruler-of-the-plane/commit/b9d4fc9134b48431a3ed3740c51786c5938d08e4)
- **Live demo:** [open demo](https://ls11ae.github.io/ruler-of-the-plane/)
- **Additional live link:** [open demo](https://kbuchin.github.io/ruler/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/ls11ae/ruler-of-the-plane/blob/main/docs/look/start-map.webp) — 📸 6.0/10 · manual visual review · Use this frame for the game-level score. Hand-drawn parchment world map menu linking geometry games; charming, but a menu.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Geometry games for the TU Dortmund open house – web edition of Ruler of the Plane. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ls11ae/ruler-of-the-plane/blob/main/src/ui/games/voronoi/index.tsx](https://github.com/ls11ae/ruler-of-the-plane/blob/main/src/ui/games/voronoi/index.tsx)
- [https://github.com/ls11ae/ruler-of-the-plane/commit/b9d4fc9134b48431a3ed3740c51786c5938d08e4](https://github.com/ls11ae/ruler-of-the-plane/commit/b9d4fc9134b48431a3ed3740c51786c5938d08e4)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/ls11ae/ruler-of-the-plane

[Back to the awesome list](../../README.md)
