# Advanced Sudoku

> Verified game note.

![Advanced Sudoku screenshot placeholder](advanced-sudoku-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/brunogutierre/AdvancedSudoku](https://github.com/brunogutierre/AdvancedSudoku)
- **Evidence:** [direct model evidence](https://github.com/brunogutierre/AdvancedSudoku/commit/ed9f0b63305da36615a743671bfa23d2cc085b31)
- **Live demo:** [open demo](https://brunogutierre.github.io/AdvancedSudoku/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Modern Sudoku PWA in Angular 22: technique-graded puzzles, teaching hints, daily challenge, offline, 4 languages. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/brunogutierre/AdvancedSudoku/blob/main/src/app/features/play/play.spec.ts](https://github.com/brunogutierre/AdvancedSudoku/blob/main/src/app/features/play/play.spec.ts)
- [https://github.com/brunogutierre/AdvancedSudoku/commit/ed9f0b63305da36615a743671bfa23d2cc085b31](https://github.com/brunogutierre/AdvancedSudoku/commit/ed9f0b63305da36615a743671bfa23d2cc085b31)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/brunogutierre/AdvancedSudoku

[Back to the awesome list](../../README.md)
