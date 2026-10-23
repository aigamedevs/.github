# Mexica Chess

> Verified game note.

![Mexica Chess screenshot](https://raw.githubusercontent.com/alrc21/mexica-chess/main/public/stills/templo-mayor.jpg)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 6.5/10 ([manually reviewed image](https://github.com/alrc21/mexica-chess/blob/main/public/stills/templo-mayor.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/alrc21/mexica-chess](https://github.com/alrc21/mexica-chess)
- **Evidence:** [direct model evidence](https://github.com/alrc21/mexica-chess/commit/12f17c6053ed97f766a0e036cfbb3df9143c0b59)
- **Live demo:** [open demo](https://mexica-chess.vercel.app)
- **Additional live link:** [open demo](https://mexica-chess.vercel.app/about)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/alrc21/mexica-chess/blob/main/public/stills/templo-mayor.jpg) — 📸 6.5/10 · manual visual review · Use this frame for the game-level score. Torch-lit 3D stone chess board before a pyramid; strong atmosphere.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A chess set carved in volcanic stone, played in 3D in the browser. An Alia Studio experiment: Blender, three.js, Stockfish. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/alrc21/mexica-chess/blob/main/src/stage.ts](https://github.com/alrc21/mexica-chess/blob/main/src/stage.ts)
- [https://github.com/alrc21/mexica-chess/commit/12f17c6053ed97f766a0e036cfbb3df9143c0b59](https://github.com/alrc21/mexica-chess/commit/12f17c6053ed97f766a0e036cfbb3df9143c0b59)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/alrc21/mexica-chess

[Back to the awesome list](../../README.md)
