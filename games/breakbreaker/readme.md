# BreakBreaker

> Verified game note.

![BreakBreaker screenshot placeholder](breakbreaker-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, Three.js, Phaser, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/thlaure/BreakBreaker](https://github.com/thlaure/BreakBreaker)
- **Evidence:** [direct model evidence](https://github.com/thlaure/BreakBreaker/commit/786a05bc48da93d0592b9eb7b7e11db519fe5488)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Jeu d'action arcade en pixel art, vu du dessus (Phaser 4 + TypeScript). Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/thlaure/BreakBreaker/blob/main/src/sim/director.ts](https://github.com/thlaure/BreakBreaker/blob/main/src/sim/director.ts)
- [https://github.com/thlaure/BreakBreaker/commit/786a05bc48da93d0592b9eb7b7e11db519fe5488](https://github.com/thlaure/BreakBreaker/commit/786a05bc48da93d0592b9eb7b7e11db519fe5488)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/thlaure/BreakBreaker

[Back to the awesome list](../../README.md)
