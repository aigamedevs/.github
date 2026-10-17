# Trench Dive

> Verified game note.

![Trench Dive screenshot placeholder](trench-dive-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/cwinters410/trench-dive](https://github.com/cwinters410/trench-dive)
- **Evidence:** [direct model evidence](https://github.com/cwinters410/trench-dive/commit/90892ffbd04ef42f2aa352742786a41e86b7dbb9)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A rare-answer trivia game inspired by Krillion. Every prompt has a ranked list of accepted answers. Obvious answers barely get you wet; the rarer your answer, the deeper you dive. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/cwinters410/trench-dive/blob/main/src/prompts.js](https://github.com/cwinters410/trench-dive/blob/main/src/prompts.js)
- [https://github.com/cwinters410/trench-dive/commit/90892ffbd04ef42f2aa352742786a41e86b7dbb9](https://github.com/cwinters410/trench-dive/commit/90892ffbd04ef42f2aa352742786a41e86b7dbb9)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/cwinters410/trench-dive

[Back to the awesome list](../../README.md)
