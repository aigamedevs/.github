# Pac-Man (1980) Recreation

> Verified game note.

![Pac-Man (1980) Recreation screenshot](https://raw.githubusercontent.com/davidkolche/pacman/main/assets/screenshot.png)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 5.8/10 ([manually reviewed image](https://github.com/davidkolche/pacman/blob/main/assets/screenshot.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/davidkolche/pacman](https://github.com/davidkolche/pacman)
- **Evidence:** [direct model evidence](https://github.com/davidkolche/pacman/commit/314aec0f70df6066c1e71b7fbf30d10dd338d5ed)
- **Live demo:** [open demo](https://davidkolche.github.io/pacman/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/davidkolche/pacman/blob/main/assets/screenshot.png) — 📸 5.8/10 · manual visual review · Use this frame for the game-level score. Faithful Pac-Man maze with ghosts, pellets and READY text; crisp but a straight recreation.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A recreation of the 1980 arcade Pac-Man in vanilla JavaScript and HTML5 Canvas. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/davidkolche/pacman/blob/main/js/constants.js](https://github.com/davidkolche/pacman/blob/main/js/constants.js)
- [https://github.com/davidkolche/pacman/commit/314aec0f70df6066c1e71b7fbf30d10dd338d5ed](https://github.com/davidkolche/pacman/commit/314aec0f70df6066c1e71b7fbf30d10dd338d5ed)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/davidkolche/pacman

[Back to the awesome list](../../README.md)
