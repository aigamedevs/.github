# Mine Clone

> Verified game note.

![Mine Clone screenshot](https://raw.githubusercontent.com/Githyot/mine-clone/main/docs/screenshots/demo.png)

## At a glance

- **Score:** 7.5/10
- **Screenshot rating:** 6.2/10 ([manually reviewed image](https://github.com/Githyot/mine-clone/blob/main/docs/screenshots/demo.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Fable 5.1
- **Technology:** Rust
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/Githyot/mine-clone](https://github.com/Githyot/mine-clone)
- **Evidence:** [direct model evidence](https://github.com/Githyot/mine-clone/commit/82db5ea09a2c155a4fc77c87c451795116c922f3)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Githyot/mine-clone/blob/main/docs/screenshots/demo.png) — 📸 6.2/10 · manual visual review · Use this frame for the game-level score. Voxel world with a wooden house, rainbow wool blocks, water and a hotbar; familiar block style, plain scene.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A Minecraft-like block game written in Rust, built for speed. Rendering uses wgpu on. Commit carries an exact Claude Opus 5.5 / Claude Fable 5.1 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Githyot/mine-clone/blob/main/crates/game/src/main.rs](https://github.com/Githyot/mine-clone/blob/main/crates/game/src/main.rs)
- [https://github.com/Githyot/mine-clone/commit/82db5ea09a2c155a4fc77c87c451795116c922f3](https://github.com/Githyot/mine-clone/commit/82db5ea09a2c155a4fc77c87c451795116c922f3)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/Githyot/mine-clone

[Back to the awesome list](../../README.md)
