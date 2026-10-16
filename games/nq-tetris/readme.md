# NQ Tetris

> Verified game note.

![NQ Tetris screenshot placeholder](nq-tetris-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Fable 5.1
- **Technology:** JavaScript, Canvas, PHP, Laravel
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-16
- **Repository:** [https://github.com/nikniq/nq-tetris](https://github.com/nikniq/nq-tetris)
- **Evidence:** [direct model evidence](https://github.com/nikniq/nq-tetris/commit/914a943563043fa39b97508986b3d467bcb4b9ab)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Canvas Tetris served by Laravel with register and login (public_html/js/tetris.js ~42 KB). Commit carries an exact Claude Fable 5.1 co-author trailer. Source inspected only; no playtest.

### Gameplay source

- [https://github.com/nikniq/nq-tetris/blob/main/public_html/js/tetris.js](https://github.com/nikniq/nq-tetris/blob/main/public_html/js/tetris.js)
- [https://github.com/nikniq/nq-tetris/commit/914a943563043fa39b97508986b3d467bcb4b9ab](https://github.com/nikniq/nq-tetris/commit/914a943563043fa39b97508986b3d467bcb4b9ab)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-15..2026-10-16 (6-hour UTC partitions) joined to repositories created after 2026-10-14T17:00Z; https://github.com/nikniq/nq-tetris

[Back to the awesome list](../../README.md)
