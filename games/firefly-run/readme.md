# Firefly Run

> Verified game note.

![Firefly Run screenshot placeholder](firefly-run-placeholder.svg)

## At a glance

- **Score:** 6.7/10
- **Model:** Claude Opus 5.5
- **Technology:** HTML, JavaScript, Canvas, Browser, Capacitor
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-16
- **Repository:** [https://github.com/AhmedShela/firefly-run](https://github.com/AhmedShela/firefly-run)
- **Evidence:** [direct model evidence](https://github.com/AhmedShela/firefly-run/commit/90ed38134cb0d7420b2b5013219c7b4edebc07f1)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Web game wrapped with Capacitor for iOS and Android; the game itself is in www/index.html and www/game.js. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected only; no playtest.

### Gameplay source

- [https://github.com/AhmedShela/firefly-run/blob/main/www/game.js](https://github.com/AhmedShela/firefly-run/blob/main/www/game.js)
- [https://github.com/AhmedShela/firefly-run/commit/90ed38134cb0d7420b2b5013219c7b4edebc07f1](https://github.com/AhmedShela/firefly-run/commit/90ed38134cb0d7420b2b5013219c7b4edebc07f1)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-15..2026-10-16 (6-hour UTC partitions) joined to repositories created after 2026-10-14T17:00Z; https://github.com/AhmedShela/firefly-run

[Back to the awesome list](../../README.md)
