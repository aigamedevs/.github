# Chess Lab

> Verified game note.

![Chess Lab screenshot placeholder](chess-lab-placeholder.svg)

## At a glance

- **Score:** 6.4/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/AarinSingh1/chess-lab](https://github.com/AarinSingh1/chess-lab)
- **Evidence:** [direct model evidence](https://github.com/AarinSingh1/chess-lab/commit/21adcb6630713792b5f565a6710d7a2152698b45)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Browser chess game built from scratch in vanilla JS — one feature PR per day. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/AarinSingh1/chess-lab/blob/main/src/engine.js](https://github.com/AarinSingh1/chess-lab/blob/main/src/engine.js)
- [https://github.com/AarinSingh1/chess-lab/commit/21adcb6630713792b5f565a6710d7a2152698b45](https://github.com/AarinSingh1/chess-lab/commit/21adcb6630713792b5f565a6710d7a2152698b45)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/AarinSingh1/chess-lab

[Back to the awesome list](../../README.md)
