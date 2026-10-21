# Petals & Bones

> Verified game note.

![Petals & Bones screenshot](https://raw.githubusercontent.com/alexzfe/skull-web-game/main/docs/screenshot.png)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 4.0/10 ([manually reviewed image](https://github.com/alexzfe/skull-web-game/blob/main/docs/screenshot.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/alexzfe/skull-web-game](https://github.com/alexzfe/skull-web-game)
- **Evidence:** [direct model evidence](https://github.com/alexzfe/skull-web-game/commit/e5908e573337df35860297b296e5ad9c25b09fc5)
- **Live demo:** [open demo](https://skull.xlobax.com)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/alexzfe/skull-web-game/blob/main/docs/screenshot.png) — 📸 4.0/10 · manual visual review · Use this frame for the game-level score. Neon title menu for host, join and bots; menu only.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Petals & Bones — a free online version of the bluffing party game Skull. Play with friends or bots in your browser. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/alexzfe/skull-web-game/blob/main/qa/mp-e2e.mjs](https://github.com/alexzfe/skull-web-game/blob/main/qa/mp-e2e.mjs)
- [https://github.com/alexzfe/skull-web-game/commit/e5908e573337df35860297b296e5ad9c25b09fc5](https://github.com/alexzfe/skull-web-game/commit/e5908e573337df35860297b296e5ad9c25b09fc5)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/alexzfe/skull-web-game

[Back to the awesome list](../../README.md)
