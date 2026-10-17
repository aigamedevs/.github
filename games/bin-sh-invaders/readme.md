# bin/sh Invaders

> Verified game note.

![bin/sh Invaders screenshot](https://raw.githubusercontent.com/th-in-gs/sh_invaders/main/mac_screenshot.png)

## At a glance

- **Score:** 7.0/10
- **Screenshot rating:** 5.0/10 ([manually reviewed image](https://github.com/th-in-gs/sh_invaders/blob/main/mac_screenshot.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** Shell
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/th-in-gs/sh_invaders](https://github.com/th-in-gs/sh_invaders)
- **Evidence:** [direct model evidence](https://github.com/th-in-gs/sh_invaders/commit/00000010a7432d193979186bb6d0bc38b45660ed)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/th-in-gs/sh_invaders/blob/main/mac_screenshot.png) — 📸 5.0/10 · manual visual review · Use this frame for the game-level score. Terminal Space Invaders with coloured invader rows, bunkers and score line; faithful and readable, very minimal.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

!/bin/sh Invaders: Space Invaders written in unnecessarily pure old-school POSIX shell. As faithful to the 1978 arcade game as a grid of characters allows. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/th-in-gs/sh_invaders/blob/main/sh_invaders.sh](https://github.com/th-in-gs/sh_invaders/blob/main/sh_invaders.sh)
- [https://github.com/th-in-gs/sh_invaders/commit/00000010a7432d193979186bb6d0bc38b45660ed](https://github.com/th-in-gs/sh_invaders/commit/00000010a7432d193979186bb6d0bc38b45660ed)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/th-in-gs/sh_invaders

[Back to the awesome list](../../README.md)
