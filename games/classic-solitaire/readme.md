# Classic Solitaire

> Verified game note.

![Classic Solitaire screenshot](https://raw.githubusercontent.com/Beebopcat/classic-solitaire/main/docs/media/redesign-table-desktop.webp)

## At a glance

- **Score:** 6.9/10
- **Screenshot rating:** 5.0/10 ([manually reviewed image](https://github.com/Beebopcat/classic-solitaire/blob/main/docs/media/redesign-table-desktop.webp)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/Beebopcat/classic-solitaire](https://github.com/Beebopcat/classic-solitaire)
- **Evidence:** [direct model evidence](https://github.com/Beebopcat/classic-solitaire/commit/4569e6bff7e645966680b28c02f27e5a100993d8)
- **Live demo:** [open demo](https://beebopcat.github.io/classic-solitaire/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Beebopcat/classic-solitaire/blob/main/docs/media/redesign-table-desktop.webp) — 📸 5.0/10 · manual visual review · Use this frame for the game-level score. Klondike table, plain and functional.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Classic Solitaire - Klondike solitaire for the browser. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Beebopcat/classic-solitaire/blob/main/solitaire.js](https://github.com/Beebopcat/classic-solitaire/blob/main/solitaire.js)
- [https://github.com/Beebopcat/classic-solitaire/commit/4569e6bff7e645966680b28c02f27e5a100993d8](https://github.com/Beebopcat/classic-solitaire/commit/4569e6bff7e645966680b28c02f27e5a100993d8)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/Beebopcat/classic-solitaire

[Back to the awesome list](../../README.md)
