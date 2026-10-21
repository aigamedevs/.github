# CHONK DOOM

> Verified game note.

![CHONK DOOM screenshot](https://raw.githubusercontent.com/goums/chonk-doom/main/docs/img/agent-frame.jpg)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 6.0/10 ([manually reviewed image](https://github.com/goums/chonk-doom/blob/main/docs/img/agent-frame.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/goums/chonk-doom](https://github.com/goums/chonk-doom)
- **Evidence:** [direct model evidence](https://github.com/goums/chonk-doom/commit/a7e70492c98309155e44e9c3e0d2a3cc2c88ee5b)
- **Live demo:** [open demo](https://goums.github.io/chonk-doom/)
- **Additional live link:** [open demo](https://goums.github.io/chonk-doom/about.html)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/goums/chonk-doom/blob/main/docs/img/agent-frame.jpg) — 📸 6.0/10 · manual visual review · Use this frame for the game-level score. First-person retro corridor with a hamster enemy, cat face health bar and weapon HUD; charming but blocky.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

CHONK DOOM: a retro DOOM-like FPS starring Le Chonk, played by Mistral Large 4 (Le Chonk challenge entry). Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/goums/chonk-doom/blob/main/src/game/world.ts](https://github.com/goums/chonk-doom/blob/main/src/game/world.ts)
- [https://github.com/goums/chonk-doom/commit/a7e70492c98309155e44e9c3e0d2a3cc2c88ee5b](https://github.com/goums/chonk-doom/commit/a7e70492c98309155e44e9c3e0d2a3cc2c88ee5b)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/goums/chonk-doom

[Back to the awesome list](../../README.md)
