# Carla's Video Poker Game

> Verified game note.

![Carla's Video Poker Game screenshot](https://raw.githubusercontent.com/kendallmark3/video-poker/main/screenshots/r9-wide.png)

## At a glance

- **Score:** 6.8/10
- **Screenshot rating:** 6.3/10 ([manually reviewed image](https://github.com/kendallmark3/video-poker/blob/main/screenshots/r9-wide.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/kendallmark3/video-poker](https://github.com/kendallmark3/video-poker)
- **Evidence:** [direct model evidence](https://github.com/kendallmark3/video-poker/commit/01b68bc16749562e579049ca296621d5be17d38c)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/kendallmark3/video-poker/blob/main/screenshots/r9-wide.png) — 📸 6.3/10 · manual visual review · Use this frame for the game-level score. Neon video poker table with pay table, five card slots and bet buttons; polished casino UI, static.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A Jacks or Better video poker machine for the browser, built with React. It was built in small, verified steps from intent files, then attacked with an adversarial test suite to find what breaks. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/kendallmark3/video-poker/blob/main/src/App.jsx](https://github.com/kendallmark3/video-poker/blob/main/src/App.jsx)
- [https://github.com/kendallmark3/video-poker/commit/01b68bc16749562e579049ca296621d5be17d38c](https://github.com/kendallmark3/video-poker/commit/01b68bc16749562e579049ca296621d5be17d38c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/kendallmark3/video-poker

[Back to the awesome list](../../README.md)
