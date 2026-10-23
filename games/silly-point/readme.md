# Silly Point

> Verified game note.

![Silly Point screenshot](https://raw.githubusercontent.com/ahab94/silly-point/main/docs/media/cover-drive.gif)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 6.0/10 ([manually reviewed image](https://github.com/ahab94/silly-point/blob/main/docs/media/cover-drive.gif)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/ahab94/silly-point](https://github.com/ahab94/silly-point)
- **Evidence:** [direct model evidence](https://github.com/ahab94/silly-point/commit/f9415248f61f5313a4ce2e7f57df49696fb86e40)
- **Live demo:** [open demo](https://ahab94.github.io/silly-point/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/ahab94/silly-point/blob/main/docs/media/cover-drive.gif) — 📸 6.0/10 · manual visual review · Use this frame for the game-level score. First-person batting view of a stadium; clear 3D scene.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A 3D cricket batting game about all the strange things a cricket ball does: swing, reverse swing, cracked pitches, reviews. Play in the browser. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ahab94/silly-point/blob/main/scripts/game.gd](https://github.com/ahab94/silly-point/blob/main/scripts/game.gd)
- [https://github.com/ahab94/silly-point/commit/f9415248f61f5313a4ce2e7f57df49696fb86e40](https://github.com/ahab94/silly-point/commit/f9415248f61f5313a4ce2e7f57df49696fb86e40)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/ahab94/silly-point

[Back to the awesome list](../../README.md)
