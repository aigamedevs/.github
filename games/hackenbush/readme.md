# Hackenbush

> Verified game note.

![Hackenbush screenshot](https://raw.githubusercontent.com/sen-ltd/hackenbush/main/assets/screenshot.png)

## At a glance

- **Score:** 6.8/10
- **Screenshot rating:** 5.0/10 ([manually reviewed image](https://github.com/sen-ltd/hackenbush/blob/main/assets/screenshot.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/sen-ltd/hackenbush](https://github.com/sen-ltd/hackenbush)
- **Evidence:** [direct model evidence](https://github.com/sen-ltd/hackenbush/commit/11d13f3e7dc779bf35fe05700d9e9dd18914fffb)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/sen-ltd/hackenbush/blob/main/assets/screenshot.png) — 📸 5.0/10 · manual visual review · Use this frame for the game-level score. Hackenbush drawing beside value panel; functional dark UI.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Blue-Red-Green Hackenbush with an exact game-value engine: draw anything and get its canonical value (3/4, 2, ↑, {0 \| 6, 7}), every cut marked win/lose. Checked against Berlekamp's rule (8.4M stalks), the fusion principle (329,711 graphs) and plain search… Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/sen-ltd/hackenbush/blob/main/src/main.ts](https://github.com/sen-ltd/hackenbush/blob/main/src/main.ts)
- [https://github.com/sen-ltd/hackenbush/commit/11d13f3e7dc779bf35fe05700d9e9dd18914fffb](https://github.com/sen-ltd/hackenbush/commit/11d13f3e7dc779bf35fe05700d9e9dd18914fffb)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/sen-ltd/hackenbush

[Back to the awesome list](../../README.md)
