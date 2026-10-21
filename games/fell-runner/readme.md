# Fell Runner

> Verified game note.

![Fell Runner screenshot](https://raw.githubusercontent.com/rmcrkd/fell-runner/main/docs/gameplay.gif)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 6.5/10 ([manually reviewed image](https://github.com/rmcrkd/fell-runner/blob/main/docs/gameplay.gif)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/rmcrkd/fell-runner](https://github.com/rmcrkd/fell-runner)
- **Evidence:** [direct model evidence](https://github.com/rmcrkd/fell-runner/commit/44598cfba9d5021a9a70098a58a1c352cbd6a430)
- **Live demo:** [open demo](https://rmcrkd.github.io/fell-runner/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/rmcrkd/fell-runner/blob/main/docs/gameplay.gif) — 📸 6.5/10 · manual visual review · Use this frame for the game-level score. Rainy side-scrolling fell platformer with stone pillars, timer and wind callout; good atmosphere, small player.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A Celeste-style speedrunning platformer over three notorious Lake District fells, with real routes, seeded weather, wind physics, ghosts and full accessibility. Free to play in your browser. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/rmcrkd/fell-runner/blob/main/src/main.js](https://github.com/rmcrkd/fell-runner/blob/main/src/main.js)
- [https://github.com/rmcrkd/fell-runner/commit/44598cfba9d5021a9a70098a58a1c352cbd6a430](https://github.com/rmcrkd/fell-runner/commit/44598cfba9d5021a9a70098a58a1c352cbd6a430)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/rmcrkd/fell-runner

[Back to the awesome list](../../README.md)
