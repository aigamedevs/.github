# The Glitch Arcade

> Verified game note.

![The Glitch Arcade screenshot](https://raw.githubusercontent.com/glitchless-gg/glitch-arcade/main/assets/screenshots/blastpit-game.png)

## At a glance

- **Score:** 7.9/10
- **Screenshot rating:** 6.2/10 ([manually reviewed image](https://github.com/glitchless-gg/glitch-arcade/blob/main/assets/screenshots/blastpit-game.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-24
- **Repository:** [https://github.com/glitchless-gg/glitch-arcade](https://github.com/glitchless-gg/glitch-arcade)
- **Evidence:** [direct model evidence](https://github.com/glitchless-gg/glitch-arcade/commit/1d59d70f4afc26235da5ed314bb31894ab648d0c)
- **Live demo:** [open demo](https://www.glitchless.gg)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/glitchless-gg/glitch-arcade/blob/main/assets/screenshots/blastpit-game.png) — 📸 6.2/10 · manual visual review · Use this frame for the game-level score. Neon 3D arena shooter view with enemies and weapon HUD; energetic but busy.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Small Three.js games in different genres, instrumented with Glitchless: each tracks its own genre, ships with planted problems, and has its own dashboard. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/glitchless-gg/glitch-arcade/blob/main/games/gemfall/src/main.js](https://github.com/glitchless-gg/glitch-arcade/blob/main/games/gemfall/src/main.js)
- [https://github.com/glitchless-gg/glitch-arcade/commit/1d59d70f4afc26235da5ed314bb31894ab648d0c](https://github.com/glitchless-gg/glitch-arcade/commit/1d59d70f4afc26235da5ed314bb31894ab648d0c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; https://github.com/glitchless-gg/glitch-arcade

[Back to the awesome list](../../README.md)
