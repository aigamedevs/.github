# Pixel War

> Verified game note.

![Pixel War screenshot placeholder](pixel-war-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** Roblox, Luau
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/bradhunt5/pixel-war](https://github.com/bradhunt5/pixel-war)
- **Evidence:** [direct model evidence](https://github.com/bradhunt5/pixel-war/commit/22919796ba37266378a99cfde4269b5705596193)
- **Live demo:** [open demo](https://bradhunt5.github.io/pixel-war/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Pixel War: a territory-conquest strategy game for phones (installable PWA). Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/bradhunt5/pixel-war/blob/main/game.js](https://github.com/bradhunt5/pixel-war/blob/main/game.js)
- [https://github.com/bradhunt5/pixel-war/commit/22919796ba37266378a99cfde4269b5705596193](https://github.com/bradhunt5/pixel-war/commit/22919796ba37266378a99cfde4269b5705596193)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/bradhunt5/pixel-war

[Back to the awesome list](../../README.md)
