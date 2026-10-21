# Bane Remastered

> Verified game note.

![Bane Remastered screenshot](https://raw.githubusercontent.com/Empatixx/Bane-remastered/master/media/biome-sewer.png)

## At a glance

- **Score:** 8.2/10
- **Screenshot rating:** 6.4/10 ([manually reviewed image](https://github.com/Empatixx/Bane-remastered/blob/master/media/biome-sewer.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** Rust
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/Empatixx/Bane-remastered](https://github.com/Empatixx/Bane-remastered)
- **Evidence:** [direct model evidence](https://github.com/Empatixx/Bane-remastered/commit/ff9e86a32944a7a8ef02617f31e5ea1d3e8f23ff)
- **Live demo:** [open demo](https://empatixx.github.io/Bane-remastered/docs)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Empatixx/Bane-remastered/blob/master/media/biome-sewer.png) — 📸 6.4/10 · manual visual review · Use this frame for the game-level score. Top-down hand-drawn dungeon with slime, bats, hero and gun HUD; coherent dark style.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Watch the trailer in full quality. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Empatixx/Bane-remastered/blob/master/rust/app/src/scenes/cinematic.rs](https://github.com/Empatixx/Bane-remastered/blob/master/rust/app/src/scenes/cinematic.rs)
- [https://github.com/Empatixx/Bane-remastered/commit/ff9e86a32944a7a8ef02617f31e5ea1d3e8f23ff](https://github.com/Empatixx/Bane-remastered/commit/ff9e86a32944a7a8ef02617f31e5ea1d3e8f23ff)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/Empatixx/Bane-remastered

[Back to the awesome list](../../README.md)
