# Kibitz

> Verified game note.

![Kibitz screenshot placeholder](kibitz-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/pc-style/kibitz](https://github.com/pc-style/kibitz)
- **Evidence:** [direct model evidence](https://github.com/pc-style/kibitz/commit/9c47d65a026167759e8fef724663af50801d2bcb)
- **Live demo:** [open demo](https://kibitz-review.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Free chess game review in the browser: chess.com-style grades, accuracy, a coach, Best and Retry. Stockfish runs on your device. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/pc-style/kibitz/blob/main/site/src/ui/review.tsx](https://github.com/pc-style/kibitz/blob/main/site/src/ui/review.tsx)
- [https://github.com/pc-style/kibitz/commit/9c47d65a026167759e8fef724663af50801d2bcb](https://github.com/pc-style/kibitz/commit/9c47d65a026167759e8fef724663af50801d2bcb)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/pc-style/kibitz

[Back to the awesome list](../../README.md)
