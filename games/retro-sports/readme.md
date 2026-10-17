# RETRO SPORTS

> Verified game note.

![RETRO SPORTS screenshot](https://raw.githubusercontent.com/helico-tech/retro-sports/main/docs/screenshots/super-shot.png)

## At a glance

- **Score:** 7.8/10
- **Screenshot rating:** 7.6/10 ([manually reviewed image](https://github.com/helico-tech/retro-sports/blob/main/docs/screenshots/super-shot.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Rust
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/helico-tech/retro-sports](https://github.com/helico-tech/retro-sports)
- **Evidence:** [direct model evidence](https://github.com/helico-tech/retro-sports/commit/a4baa08f5d413d5cf2741c53e09fe3f21ca79deb)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/helico-tech/retro-sports/blob/main/docs/screenshots/super-shot.png) — 📸 7.6/10 · manual visual review · Use this frame for the game-level score. Pixel-art beach dodgeball match at sunset with team bars, timer and palm trees; vibrant 16-bit style, readable action.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Whimsical 16-bit sports games on Helico Island: dodgeball, frisbee dogs, Dutch headwind cycling, trail running, hang gliding. Rust, all art and sound generated in code. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/helico-tech/retro-sports/blob/main/src/games/tegenwind/race.rs](https://github.com/helico-tech/retro-sports/blob/main/src/games/tegenwind/race.rs)
- [https://github.com/helico-tech/retro-sports/commit/a4baa08f5d413d5cf2741c53e09fe3f21ca79deb](https://github.com/helico-tech/retro-sports/commit/a4baa08f5d413d5cf2741c53e09fe3f21ca79deb)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/helico-tech/retro-sports

[Back to the awesome list](../../README.md)
