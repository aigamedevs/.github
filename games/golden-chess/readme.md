# Golden Chess

> Verified game note.

![Golden Chess screenshot placeholder](golden-chess-placeholder.svg)

## At a glance

- **Score:** 8.1/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/ukazyra-collab/golden-chess](https://github.com/ukazyra-collab/golden-chess)
- **Evidence:** [direct model evidence](https://github.com/ukazyra-collab/golden-chess/commit/e7af906ed701fb840926ad293004fd1c7aa69d90)
- **Live demo:** [open demo](https://ukazyra-collab.github.io/golden-chess/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Chess with one golden move per player. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ukazyra-collab/golden-chess/blob/main/index.html](https://github.com/ukazyra-collab/golden-chess/blob/main/index.html)
- [https://github.com/ukazyra-collab/golden-chess/commit/e7af906ed701fb840926ad293004fd1c7aa69d90](https://github.com/ukazyra-collab/golden-chess/commit/e7af906ed701fb840926ad293004fd1c7aa69d90)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/ukazyra-collab/golden-chess

[Back to the awesome list](../../README.md)
