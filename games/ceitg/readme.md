# CeitG

> Verified game note.

![CeitG screenshot](https://raw.githubusercontent.com/faithere1/CeitG/main/docs/gameplay.png)

## At a glance

- **Score:** 6.8/10
- **Screenshot rating:** 4.0/10 ([manually reviewed image](https://github.com/faithere1/CeitG/blob/main/docs/gameplay.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Roblox, Luau
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/faithere1/CeitG](https://github.com/faithere1/CeitG)
- **Evidence:** [direct model evidence](https://github.com/faithere1/CeitG/commit/4d69390df5c74ea0204c8df73658684f3b9c134c)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/faithere1/CeitG/blob/main/docs/gameplay.png) — 📸 4.0/10 · manual visual review · Use this frame for the game-level score. Flat top-down tag field with labelled circles for players and a timer bar; readable but very sparse.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Tiny 2D LAN tag game for the classroom (Windows & macOS). Cross the field 3 times, don't get tagged. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/faithere1/CeitG/blob/main/draw.go](https://github.com/faithere1/CeitG/blob/main/draw.go)
- [https://github.com/faithere1/CeitG/commit/4d69390df5c74ea0204c8df73658684f3b9c134c](https://github.com/faithere1/CeitG/commit/4d69390df5c74ea0204c8df73658684f3b9c134c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/faithere1/CeitG

[Back to the awesome list](../../README.md)
