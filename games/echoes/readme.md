# ECHOES

> Verified game note.

![ECHOES screenshot](https://raw.githubusercontent.com/dustinpolkrst/echoes/main/docs/media/ferry-playthrough.gif)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 5.2/10 ([manually reviewed image](https://github.com/dustinpolkrst/echoes/blob/main/docs/media/ferry-playthrough.gif)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Lua
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/dustinpolkrst/echoes](https://github.com/dustinpolkrst/echoes)
- **Evidence:** [direct model evidence](https://github.com/dustinpolkrst/echoes/commit/a72332d030c0462d2f2255c0c7c0d44859cea161)
- **Live demo:** [open demo](https://dustinpolkrst.github.io/echoes/)
- **Additional live link:** [open demo](https://dustinpolkrst.github.io/echoes/play/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/dustinpolkrst/echoes/blob/main/docs/media/ferry-playthrough.gif) — 📸 5.2/10 · manual visual review · Use this frame for the game-level score. Small dark side-view platformer room with candles and a glowing portal; readable but low detail.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Echoes: a LÖVE puzzle platformer where you ride replays of your past self, plus a dev blog of how it was built with Claude Code. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/dustinpolkrst/echoes/blob/main/game/dev/solutions/act5.lua](https://github.com/dustinpolkrst/echoes/blob/main/game/dev/solutions/act5.lua)
- [https://github.com/dustinpolkrst/echoes/commit/a72332d030c0462d2f2255c0c7c0d44859cea161](https://github.com/dustinpolkrst/echoes/commit/a72332d030c0462d2f2255c0c7c0d44859cea161)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/dustinpolkrst/echoes

[Back to the awesome list](../../README.md)
