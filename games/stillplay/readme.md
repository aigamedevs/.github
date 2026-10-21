# stillplay.

> Verified game note.

![stillplay. screenshot](https://raw.githubusercontent.com/btahir/stillplay/main/docs/media/stillplay-loop.webp)

## At a glance

- **Score:** 7.7/10
- **Screenshot rating:** 6.0/10 ([manually reviewed image](https://github.com/btahir/stillplay/blob/main/docs/media/stillplay-loop.webp)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/btahir/stillplay](https://github.com/btahir/stillplay)
- **Evidence:** [direct model evidence](https://github.com/btahir/stillplay/commit/43be54b22708f57c7154361556021fce0547d5c5)
- **Live demo:** [open demo](https://stillplay.shiptiffin.app)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/btahir/stillplay/blob/main/docs/media/stillplay-loop.webp) — 📸 6.0/10 · manual visual review · Use this frame for the game-level score. Close-up solitaire tableau with crisp classic card faces on green felt; faithful and clean but simple.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Minesweeper, FreeCell, Solitaire, Spider and Hearts, rebuilt for the browser. C rules compiled to WebAssembly, offline, no installs, no accounts. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/btahir/stillplay/blob/main/src/hearts-ui.js](https://github.com/btahir/stillplay/blob/main/src/hearts-ui.js)
- [https://github.com/btahir/stillplay/commit/43be54b22708f57c7154361556021fce0547d5c5](https://github.com/btahir/stillplay/commit/43be54b22708f57c7154361556021fce0547d5c5)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/btahir/stillplay

[Back to the awesome list](../../README.md)
