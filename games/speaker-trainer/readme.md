# Speaker Trainer

> Verified game note.

![Speaker Trainer screenshot](https://raw.githubusercontent.com/danielmazh/speaker-trainer/main/docs/design/02-home.png)

## At a glance

- **Score:** 7.7/10
- **Screenshot rating:** 4.5/10 ([manually reviewed image](https://github.com/danielmazh/speaker-trainer/blob/main/docs/design/02-home.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/danielmazh/speaker-trainer](https://github.com/danielmazh/speaker-trainer)
- **Evidence:** [direct model evidence](https://github.com/danielmazh/speaker-trainer/commit/50b8c6f19604530f5f19932a26d575d8b5c1eb94)
- **Live demo:** [open demo](https://danielmazh.github.io/speaker-trainer/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/danielmazh/speaker-trainer/blob/main/docs/design/02-home.png) — 📸 4.5/10 · manual visual review · Use this frame for the game-level score. Mobile home screen UI for lessons; app-like, little game visual.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Mobile game that trains spoken English for technical talks. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/danielmazh/speaker-trainer/blob/main/js/content.js](https://github.com/danielmazh/speaker-trainer/blob/main/js/content.js)
- [https://github.com/danielmazh/speaker-trainer/commit/50b8c6f19604530f5f19932a26d575d8b5c1eb94](https://github.com/danielmazh/speaker-trainer/commit/50b8c6f19604530f5f19932a26d575d8b5c1eb94)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/danielmazh/speaker-trainer

[Back to the awesome list](../../README.md)
