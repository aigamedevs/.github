# Rusty Rex

> Verified game note.

![Rusty Rex screenshot](https://raw.githubusercontent.com/yamz8/rusty-rex/master/docs/demo.gif)

## At a glance

- **Score:** 7.2/10
- **Screenshot rating:** 4.0/10 ([manually reviewed image](https://github.com/yamz8/rusty-rex/blob/master/docs/demo.gif)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Rust
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/yamz8/rusty-rex](https://github.com/yamz8/rusty-rex)
- **Evidence:** [direct model evidence](https://github.com/yamz8/rusty-rex/commit/5a57af789cfc4334fa0a44a574effb7282de32f5)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/yamz8/rusty-rex/blob/master/docs/demo.gif) — 📸 4.0/10 · manual visual review · Use this frame for the game-level score. Monochrome Chrome-dino style runner; minimal by design.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

The Chrome offline dinosaur game, rebuilt in Rust with macroquad for Omarchy. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/yamz8/rusty-rex/blob/master/src/game.rs](https://github.com/yamz8/rusty-rex/blob/master/src/game.rs)
- [https://github.com/yamz8/rusty-rex/commit/5a57af789cfc4334fa0a44a574effb7282de32f5](https://github.com/yamz8/rusty-rex/commit/5a57af789cfc4334fa0a44a574effb7282de32f5)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/yamz8/rusty-rex

[Back to the awesome list](../../README.md)
