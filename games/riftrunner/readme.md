# Riftrunner

> Verified game note.

![Riftrunner screenshot](https://raw.githubusercontent.com/underscoreloG/riftrunner/main/screenshots/gameplay.png)

## At a glance

- **Score:** 7.4/10
- **Screenshot rating:** 6.6/10 ([manually reviewed image](https://github.com/underscoreloG/riftrunner/blob/main/screenshots/gameplay.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/underscoreloG/riftrunner](https://github.com/underscoreloG/riftrunner)
- **Evidence:** [direct model evidence](https://github.com/underscoreloG/riftrunner/commit/7c8c7d73d57ebf58ae84cefbaca1a5d5f159fa75)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/underscoreloG/riftrunner/blob/main/screenshots/gameplay.png) — 📸 6.6/10 · manual visual review · Use this frame for the game-level score. Space shmup with a dense neon bullet spread, explosions, nebula and score HUD; flashy but busy.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A roguelite vertical shoot-'em-up in the spirit of Tyrian, shipped as one standalone HTML file. No engine, no libraries, no external assets: every sprite is drawn procedurally on a canvas and every sound is generated with WebAudio. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/underscoreloG/riftrunner/blob/main/riftrunner.html](https://github.com/underscoreloG/riftrunner/blob/main/riftrunner.html)
- [https://github.com/underscoreloG/riftrunner/commit/7c8c7d73d57ebf58ae84cefbaca1a5d5f159fa75](https://github.com/underscoreloG/riftrunner/commit/7c8c7d73d57ebf58ae84cefbaca1a5d5f159fa75)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/underscoreloG/riftrunner

[Back to the awesome list](../../README.md)
