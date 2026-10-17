# Gnomes vs Goblins

> Verified game note.

![Gnomes vs Goblins screenshot placeholder](gnomes-vs-goblins-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Sonnet 5.5
- **Technology:** TypeScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/kllloh/gnome-strike](https://github.com/kllloh/gnome-strike)
- **Evidence:** [direct model evidence](https://github.com/kllloh/gnome-strike/commit/262ece52696e830b3f8503a7abbe42354eca77af)
- **Live demo:** [open demo](https://kllloh.github.io/gnome-strike/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Gnomes vs Goblins: a blocky browser FPS in a destructible English back garden. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/kllloh/gnome-strike/blob/main/src/bots.ts](https://github.com/kllloh/gnome-strike/blob/main/src/bots.ts)
- [https://github.com/kllloh/gnome-strike/commit/262ece52696e830b3f8503a7abbe42354eca77af](https://github.com/kllloh/gnome-strike/commit/262ece52696e830b3f8503a7abbe42354eca77af)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/kllloh/gnome-strike

[Back to the awesome list](../../README.md)
