# Vol Game

> Verified game note.

![Vol Game screenshot placeholder](vol-game-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/poctave/vol-game](https://github.com/poctave/vol-game)
- **Evidence:** [direct model evidence](https://github.com/poctave/vol-game/commit/156cbf7a3ac765bb63c9f8046067417f57f1f5c6)
- **Live demo:** [open demo](https://poctave.github.io/vol-game/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Typed options-strategy game in the browser: name, price, build and draw option strategies and Greeks. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/poctave/vol-game/blob/main/js/views/terminal-options.js](https://github.com/poctave/vol-game/blob/main/js/views/terminal-options.js)
- [https://github.com/poctave/vol-game/commit/156cbf7a3ac765bb63c9f8046067417f57f1f5c6](https://github.com/poctave/vol-game/commit/156cbf7a3ac765bb63c9f8046067417f57f1f5c6)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/poctave/vol-game

[Back to the awesome list](../../README.md)
