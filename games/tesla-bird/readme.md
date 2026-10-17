# Tesla Bird

> Verified game note.

![Tesla Bird screenshot](https://raw.githubusercontent.com/troshkinpavel/tesla-bird/main/docs/gameplay.gif)

## At a glance

- **Score:** 7.3/10
- **Screenshot rating:** 5.0/10 ([manually reviewed image](https://github.com/troshkinpavel/tesla-bird/blob/main/docs/gameplay.gif)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/troshkinpavel/tesla-bird](https://github.com/troshkinpavel/tesla-bird)
- **Evidence:** [direct model evidence](https://github.com/troshkinpavel/tesla-bird/commit/607b24c4a57758996f3118e48d37444ad29290c0)
- **Live demo:** [open demo](https://troshkinpavel.github.io/tesla-bird/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/troshkinpavel/tesla-bird/blob/main/docs/gameplay.gif) — 📸 5.0/10 · manual visual review · Use this frame for the game-level score. Night city title card with Tesla Bird logo and controls hint; menu only.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Flappy-Bird-style pixel-art game inspired by the new Tesla Roadster's thruster-powered flight at its Oct 16, 2026 unveiling: fly the Roadster through Starship rocket pillars. Vanilla JS + canvas, night/day themes, fills any screen. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/troshkinpavel/tesla-bird/blob/main/flappy-assets/script/app.2dba3964ec8b.js](https://github.com/troshkinpavel/tesla-bird/blob/main/flappy-assets/script/app.2dba3964ec8b.js)
- [https://github.com/troshkinpavel/tesla-bird/commit/607b24c4a57758996f3118e48d37444ad29290c0](https://github.com/troshkinpavel/tesla-bird/commit/607b24c4a57758996f3118e48d37444ad29290c0)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/troshkinpavel/tesla-bird

[Back to the awesome list](../../README.md)
