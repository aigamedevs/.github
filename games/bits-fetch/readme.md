# Bits Fetch

> Verified game note.

![Bits Fetch screenshot](https://raw.githubusercontent.com/ddjess/bits-fetch/main/docs/screenshots/charge.png)

## At a glance

- **Score:** 6.7/10
- **Screenshot rating:** 5.6/10 ([manually reviewed image](https://github.com/ddjess/bits-fetch/blob/main/docs/screenshots/charge.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/ddjess/bits-fetch](https://github.com/ddjess/bits-fetch)
- **Evidence:** [direct model evidence](https://github.com/ddjess/bits-fetch/commit/0b0e90b986d5afe4d16be5b870800a80b1361f71)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/ddjess/bits-fetch/blob/main/docs/screenshots/charge.png) — 📸 5.6/10 · manual visual review · Use this frame for the game-level score. 8-bit fetch scene with dog, thrown bone arc, hills and power bar; simple retro art.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

8-bit fetch game that sends traces, logs, custom metrics and RUM to Datadog. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ddjess/bits-fetch/blob/main/static/game.js](https://github.com/ddjess/bits-fetch/blob/main/static/game.js)
- [https://github.com/ddjess/bits-fetch/commit/0b0e90b986d5afe4d16be5b870800a80b1361f71](https://github.com/ddjess/bits-fetch/commit/0b0e90b986d5afe4d16be5b870800a80b1361f71)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/ddjess/bits-fetch

[Back to the awesome list](../../README.md)
