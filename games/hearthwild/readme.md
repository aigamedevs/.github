# Hearthwild

> Verified game note.

![Hearthwild screenshot](https://raw.githubusercontent.com/hobsojam/survival/main/docs/art-review/branch-pile-followup/game.png)

## At a glance

- **Score:** 7.4/10
- **Screenshot rating:** 6.0/10 ([manually reviewed image](https://github.com/hobsojam/survival/blob/main/docs/art-review/branch-pile-followup/game.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Flutter, Dart
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/hobsojam/survival](https://github.com/hobsojam/survival)
- **Evidence:** [direct model evidence](https://github.com/hobsojam/survival/commit/9a47aabe774cdc91ee44f1afcff1cf23b9910a11)
- **Live demo:** [open demo](https://hobsojam.github.io/survival/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/hobsojam/survival/blob/main/docs/art-review/branch-pile-followup/game.png) — 📸 6.0/10 · manual visual review · Use this frame for the game-level score. Top-down pixel camp clearing in forest; clean tiles.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Hearthwild, a cozy single-player browser survival game. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/hobsojam/survival/blob/main/src/ui/App.ts](https://github.com/hobsojam/survival/blob/main/src/ui/App.ts)
- [https://github.com/hobsojam/survival/commit/9a47aabe774cdc91ee44f1afcff1cf23b9910a11](https://github.com/hobsojam/survival/commit/9a47aabe774cdc91ee44f1afcff1cf23b9910a11)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/hobsojam/survival

[Back to the awesome list](../../README.md)
