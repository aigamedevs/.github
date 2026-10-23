# Partial Annihilation

> Verified game note.

![Partial Annihilation screenshot](https://raw.githubusercontent.com/BrianChase515/partial-annihilation/main/screenshots/arena.gif)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 5.3/10 ([manually reviewed image](https://github.com/BrianChase515/partial-annihilation/blob/main/screenshots/arena.gif)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Lua, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/BrianChase515/partial-annihilation](https://github.com/BrianChase515/partial-annihilation)
- **Evidence:** [direct model evidence](https://github.com/BrianChase515/partial-annihilation/commit/a42c52df55ff3e66d0e9c9e476d17e682a25737a)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/BrianChase515/partial-annihilation/blob/main/screenshots/arena.gif) — 📸 5.3/10 · manual visual review · Use this frame for the game-level score. RTS arena view with selection ring; plain map

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Lightweight land/sea/air RTS for Mac (LÖVE). Shapes as units, 4 players with teams, AI difficulty 1-10 + personalities, select-half, retreat-until-repaired, veterancy. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/BrianChase515/partial-annihilation/blob/main/docs/love.js](https://github.com/BrianChase515/partial-annihilation/blob/main/docs/love.js)
- [https://github.com/BrianChase515/partial-annihilation/commit/a42c52df55ff3e66d0e9c9e476d17e682a25737a](https://github.com/BrianChase515/partial-annihilation/commit/a42c52df55ff3e66d0e9c9e476d17e682a25737a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/BrianChase515/partial-annihilation

[Back to the awesome list](../../README.md)
