# Wordle

> Verified game note.

![Wordle screenshot placeholder](wordle-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** Rust
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/chuan-khuna/wordle](https://github.com/chuan-khuna/wordle)
- **Evidence:** [direct model evidence](https://github.com/chuan-khuna/wordle/commit/0bfc9712f8787a3a0b4ce1a686bef9988a47bf64)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

An interactive Wordle game you play in the terminal, plus a solver that suggests guesses and explains why. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/chuan-khuna/wordle/blob/main/app/wordle-gpui/src/ui/mod.rs](https://github.com/chuan-khuna/wordle/blob/main/app/wordle-gpui/src/ui/mod.rs)
- [https://github.com/chuan-khuna/wordle/commit/0bfc9712f8787a3a0b4ce1a686bef9988a47bf64](https://github.com/chuan-khuna/wordle/commit/0bfc9712f8787a3a0b4ce1a686bef9988a47bf64)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/chuan-khuna/wordle

[Back to the awesome list](../../README.md)
