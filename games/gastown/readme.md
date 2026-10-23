# Gastown

> Verified game note.

![Gastown screenshot](https://raw.githubusercontent.com/nulljosh/gastown/main/screenshots/gastown-2.jpg)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 4.5/10 ([manually reviewed image](https://github.com/nulljosh/gastown/blob/main/screenshots/gastown-2.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** Swift, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/nulljosh/gastown](https://github.com/nulljosh/gastown)
- **Evidence:** [direct model evidence](https://github.com/nulljosh/gastown/commit/e9437d096483fd017c2ea392b3b49ecae87c68c5)
- **Live demo:** [open demo](https://gastown.jaybulb.com)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/nulljosh/gastown/blob/main/screenshots/gastown-2.jpg) — 📸 4.5/10 · manual visual review · Use this frame for the game-level score. Dark top-down colony grid with tiny units; hard to read.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A Vancouver colony game: send a crew, build machines that run themselves, raise the Gastown Steam Clock. Mac, iPhone, iPad and the web. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/nulljosh/gastown/blob/main/Sources/Game/Scenes/GameScene.swift](https://github.com/nulljosh/gastown/blob/main/Sources/Game/Scenes/GameScene.swift)
- [https://github.com/nulljosh/gastown/commit/e9437d096483fd017c2ea392b3b49ecae87c68c5](https://github.com/nulljosh/gastown/commit/e9437d096483fd017c2ea392b3b49ecae87c68c5)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/nulljosh/gastown

[Back to the awesome list](../../README.md)
