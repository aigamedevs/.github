# ReTzar

> Verified game note.

![ReTzar screenshot](https://raw.githubusercontent.com/ColCarlo/ReTzar/main/screenshots/1-castle-and-army.jpg)

## At a glance

- **Score:** 7.9/10
- **Screenshot rating:** 7.0/10 ([manually reviewed image](https://github.com/ColCarlo/ReTzar/blob/main/screenshots/1-castle-and-army.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Rust
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/ColCarlo/ReTzar](https://github.com/ColCarlo/ReTzar)
- **Evidence:** [direct model evidence](https://github.com/ColCarlo/ReTzar/commit/693e0af6a8b24b2fd8bf8fdc636c0dd8afb0b46f)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/ColCarlo/ReTzar/blob/main/screenshots/1-castle-and-army.jpg) — 📸 7.0/10 · manual visual review · Use this frame for the game-level score. Classic RTS base with detailed medieval buildings, units, walls and a side command panel; dense, coherent sprite art.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Fan remake of the classic RTS Tzar: The Burden of the Crown, rebuilt in Rust and Bevy. Needs your own copy of the game (GOG, Steam or CD). Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ColCarlo/ReTzar/blob/main/src/gameplay.rs](https://github.com/ColCarlo/ReTzar/blob/main/src/gameplay.rs)
- [https://github.com/ColCarlo/ReTzar/commit/693e0af6a8b24b2fd8bf8fdc636c0dd8afb0b46f](https://github.com/ColCarlo/ReTzar/commit/693e0af6a8b24b2fd8bf8fdc636c0dd8afb0b46f)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/ColCarlo/ReTzar

[Back to the awesome list](../../README.md)
