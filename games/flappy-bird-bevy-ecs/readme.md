# Flappy Bird (Bevy ECS)

> Verified game note.

![Flappy Bird (Bevy ECS) screenshot placeholder](flappy-bird-bevy-ecs-placeholder.svg)

## At a glance

- **Score:** 6.5/10
- **Model:** Claude Opus 5.5
- **Technology:** Rust
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/twigmytwig/flappy-bird-bevy-ecs](https://github.com/twigmytwig/flappy-bird-bevy-ecs)
- **Evidence:** [direct model evidence](https://github.com/twigmytwig/flappy-bird-bevy-ecs/commit/026833effa1865b8f21502159fb98c6094d73bc7)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Flappy Bird clone built with Rust and Bevy's ECS. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/twigmytwig/flappy-bird-bevy-ecs/blob/main/src/bird.rs](https://github.com/twigmytwig/flappy-bird-bevy-ecs/blob/main/src/bird.rs)
- [https://github.com/twigmytwig/flappy-bird-bevy-ecs/commit/026833effa1865b8f21502159fb98c6094d73bc7](https://github.com/twigmytwig/flappy-bird-bevy-ecs/commit/026833effa1865b8f21502159fb98c6094d73bc7)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/twigmytwig/flappy-bird-bevy-ecs

[Back to the awesome list](../../README.md)
