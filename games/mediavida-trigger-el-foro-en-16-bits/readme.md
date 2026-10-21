# Mediavida Trigger ⏳: el foro, en 16 bits.

> Verified game note.

![Mediavida Trigger ⏳: el foro, en 16 bits. screenshot](https://raw.githubusercontent.com/rechedev9/mediavida-trigger/main/docs/assets/screens.png)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 6.2/10 ([manually reviewed image](https://github.com/rechedev9/mediavida-trigger/blob/main/docs/assets/screens.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/rechedev9/mediavida-trigger](https://github.com/rechedev9/mediavida-trigger)
- **Evidence:** [direct model evidence](https://github.com/rechedev9/mediavida-trigger/commit/610628726a1f1b7a72b82ca16e98df5d3f42986a)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/rechedev9/mediavida-trigger/blob/main/docs/assets/screens.png) — 📸 6.2/10 · manual visual review · Use this frame for the game-level score. Composite of 16-bit RPG screens: town map, party stats and dialogue; detailed retro art but a collage.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Chrono Trigger style fan RPG set in the Mediavida forum. Browser game in TypeScript. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/rechedev9/mediavida-trigger/blob/main/art/src/enemies/lagvos.ts](https://github.com/rechedev9/mediavida-trigger/blob/main/art/src/enemies/lagvos.ts)
- [https://github.com/rechedev9/mediavida-trigger/commit/610628726a1f1b7a72b82ca16e98df5d3f42986a](https://github.com/rechedev9/mediavida-trigger/commit/610628726a1f1b7a72b82ca16e98df5d3f42986a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/rechedev9/mediavida-trigger

[Back to the awesome list](../../README.md)
