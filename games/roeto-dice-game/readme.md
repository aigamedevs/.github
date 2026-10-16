# Roeto Dice Game

> Verified game note.

![Roeto Dice Game screenshot placeholder](roeto-dice-game-placeholder.svg)

## At a glance

- **Score:** 6.9/10
- **Model:** Claude Sonnet 5.5
- **Technology:** TypeScript, React, Node.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-16
- **Repository:** [https://github.com/levikore/roeto-dice-game](https://github.com/levikore/roeto-dice-game)
- **Evidence:** [direct model evidence](https://github.com/levikore/roeto-dice-game/commit/de5987e9b70cb86af29921f2c88134280f730c11)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Two-player dice game (roll, hold, double six loses the round) with rules enforced by an authenticated backend. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected only; no playtest.

### Gameplay source

- [https://github.com/levikore/roeto-dice-game/blob/main/server/src/game/service.ts](https://github.com/levikore/roeto-dice-game/blob/main/server/src/game/service.ts)
- [https://github.com/levikore/roeto-dice-game/commit/de5987e9b70cb86af29921f2c88134280f730c11](https://github.com/levikore/roeto-dice-game/commit/de5987e9b70cb86af29921f2c88134280f730c11)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-15..2026-10-16 (6-hour UTC partitions) joined to repositories created after 2026-10-14T17:00Z; https://github.com/levikore/roeto-dice-game

[Back to the awesome list](../../README.md)
