# Swooping Simulator

> Verified game note.

![Swooping Simulator screenshot](https://raw.githubusercontent.com/wizzard262/swooping-simulator/main/screenshots/01-first-build.png)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 5.5/10 ([manually reviewed image](https://github.com/wizzard262/swooping-simulator/blob/main/screenshots/01-first-build.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/wizzard262/swooping-simulator](https://github.com/wizzard262/swooping-simulator)
- **Evidence:** [direct model evidence](https://github.com/wizzard262/swooping-simulator/commit/6bf3e5a67d610732be93d0dc169b803cd6479917)
- **Live demo:** [open demo](https://wizzard262.github.io/swooping-simulator/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/wizzard262/swooping-simulator/blob/main/screenshots/01-first-build.png) — 📸 5.5/10 · manual visual review · Use this frame for the game-level score. Bright pixel suburb with sun and magpie; simple but clean.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Fly an Australian magpie over an Aussie suburb: a pixel-art Flappy Bird style game in one HTML page. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/wizzard262/swooping-simulator/blob/main/index.html](https://github.com/wizzard262/swooping-simulator/blob/main/index.html)
- [https://github.com/wizzard262/swooping-simulator/commit/6bf3e5a67d610732be93d0dc169b803cd6479917](https://github.com/wizzard262/swooping-simulator/commit/6bf3e5a67d610732be93d0dc169b803cd6479917)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/wizzard262/swooping-simulator

[Back to the awesome list](../../README.md)
