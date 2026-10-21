# RE: flappy

> Verified game note.

![RE: flappy screenshot](https://raw.githubusercontent.com/PChanida-B/RE-flappy/main/_docs/demo.gif)

## At a glance

- **Score:** 6.7/10
- **Screenshot rating:** 4.6/10 ([manually reviewed image](https://github.com/PChanida-B/RE-flappy/blob/main/_docs/demo.gif)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/PChanida-B/RE-flappy](https://github.com/PChanida-B/RE-flappy)
- **Evidence:** [direct model evidence](https://github.com/PChanida-B/RE-flappy/commit/5c95aa5d414fd031ffecc5cc8afe144a944a6c62)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/PChanida-B/RE-flappy/blob/main/_docs/demo.gif) — 📸 4.6/10 · manual visual review · Use this frame for the game-level score. Portrait Flappy Bird get-ready screen with bird, ground and pipes absent; plain.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Running the game is as simple as. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/PChanida-B/RE-flappy/blob/main/js/FlappyBirdScene.js](https://github.com/PChanida-B/RE-flappy/blob/main/js/FlappyBirdScene.js)
- [https://github.com/PChanida-B/RE-flappy/commit/5c95aa5d414fd031ffecc5cc8afe144a944a6c62](https://github.com/PChanida-B/RE-flappy/commit/5c95aa5d414fd031ffecc5cc8afe144a944a6c62)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/PChanida-B/RE-flappy

[Back to the awesome list](../../README.md)
