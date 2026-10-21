# Balloon Stack

> Verified game note.

![Balloon Stack screenshot](https://raw.githubusercontent.com/lewisca/Balloon-Stack/main/docs/screenshot.png)

## At a glance

- **Score:** 7.3/10
- **Screenshot rating:** 3.6/10 ([manually reviewed image](https://github.com/lewisca/Balloon-Stack/blob/main/docs/screenshot.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/lewisca/Balloon-Stack](https://github.com/lewisca/Balloon-Stack)
- **Evidence:** [direct model evidence](https://github.com/lewisca/Balloon-Stack/commit/d78a12e5377a3de02aceec445e83f5e0acf82c04)
- **Live demo:** [open demo](https://lewisca.github.io/Balloon-Stack/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/lewisca/Balloon-Stack/blob/main/docs/screenshot.png) — 📸 3.6/10 · manual visual review · Use this frame for the game-level score. Balloon stacking tree on a mostly text panel UI; small playfield.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Balloon stacking game. Basically a reverse jenga. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/lewisca/Balloon-Stack/blob/main/index.html](https://github.com/lewisca/Balloon-Stack/blob/main/index.html)
- [https://github.com/lewisca/Balloon-Stack/commit/d78a12e5377a3de02aceec445e83f5e0acf82c04](https://github.com/lewisca/Balloon-Stack/commit/d78a12e5377a3de02aceec445e83f5e0acf82c04)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/lewisca/Balloon-Stack

[Back to the awesome list](../../README.md)
