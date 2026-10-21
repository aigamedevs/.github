# Color Magic

> Verified game note.

![Color Magic screenshot placeholder](color-magic-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/TimLeitch/color-match-game](https://github.com/TimLeitch/color-match-game)
- **Evidence:** [direct model evidence](https://github.com/TimLeitch/color-match-game/commit/c662659d6bf2ba4bc0a674dc40f2414c4edf3403)
- **Live demo:** [open demo](https://timleitch.github.io/color-match-game/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A dumpster-and-conveyor color sorter for Kaotic Gaming. Tap a dumpster to pick up its next color stack, then tap where it should go — send it down the track, or swap fronts when a send has no room. A level is cleared when every dumpster holds a single color. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/TimLeitch/color-match-game/blob/main/game.js](https://github.com/TimLeitch/color-match-game/blob/main/game.js)
- [https://github.com/TimLeitch/color-match-game/commit/c662659d6bf2ba4bc0a674dc40f2414c4edf3403](https://github.com/TimLeitch/color-match-game/commit/c662659d6bf2ba4bc0a674dc40f2414c4edf3403)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/TimLeitch/color-match-game

[Back to the awesome list](../../README.md)
