# The Last Musketeer Standing

> Verified game note.

![The Last Musketeer Standing screenshot placeholder](the-last-musketeer-standing-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** Unity, C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/gabercmatej/Last-Musketeer-standing-game-](https://github.com/gabercmatej/Last-Musketeer-standing-game-)
- **Evidence:** [direct model evidence](https://github.com/gabercmatej/Last-Musketeer-standing-game-/commit/aa7494f68d39f7a3188c6552ac30bf03f82b3614)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A simultaneous-turn musketeer brawler made for Los Cuatro Mosqueteros: Matej, Matic, Aljaž and Nik. Everyone plans their moves in secret, everything resolves at the same time, and the last musketeer standing wins. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/gabercmatej/Last-Musketeer-standing-game-/blob/main/Assets/_Project/Scripts/Sim/Bots/BotPlanner.cs](https://github.com/gabercmatej/Last-Musketeer-standing-game-/blob/main/Assets/_Project/Scripts/Sim/Bots/BotPlanner.cs)
- [https://github.com/gabercmatej/Last-Musketeer-standing-game-/commit/aa7494f68d39f7a3188c6552ac30bf03f82b3614](https://github.com/gabercmatej/Last-Musketeer-standing-game-/commit/aa7494f68d39f7a3188c6552ac30bf03f82b3614)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/gabercmatej/Last-Musketeer-standing-game-

[Back to the awesome list](../../README.md)
