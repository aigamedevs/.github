# AVA Rolling Thunder

> Verified game note.

![AVA Rolling Thunder screenshot](https://raw.githubusercontent.com/Harlock123/AVARollingThunder/main/Images/AVARollingThunder-gunfight.png)

## At a glance

- **Score:** 7.2/10
- **Screenshot rating:** 5.8/10 ([manually reviewed image](https://github.com/Harlock123/AVARollingThunder/blob/main/Images/AVARollingThunder-gunfight.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/Harlock123/AVARollingThunder](https://github.com/Harlock123/AVARollingThunder)
- **Evidence:** [direct model evidence](https://github.com/Harlock123/AVARollingThunder/commit/6f4b3ff34aefc91e6a0c9da3593f255bedcc826f)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Harlock123/AVARollingThunder/blob/main/Images/AVARollingThunder-gunfight.png) — 📸 5.8/10 · manual visual review · Use this frame for the game-level score. Side-view corridor shooter with doors, enemies, bullets and status bar; tidy flat retro art.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A recreation of Rolling Thunder (Namco arcade, 1986) in .NET 10 and Avalonia. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Harlock123/AVARollingThunder/blob/main/src/AVARollingThunder/Views/GameCanvas.Figures.cs](https://github.com/Harlock123/AVARollingThunder/blob/main/src/AVARollingThunder/Views/GameCanvas.Figures.cs)
- [https://github.com/Harlock123/AVARollingThunder/commit/6f4b3ff34aefc91e6a0c9da3593f255bedcc826f](https://github.com/Harlock123/AVARollingThunder/commit/6f4b3ff34aefc91e6a0c9da3593f255bedcc826f)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/Harlock123/AVARollingThunder

[Back to the awesome list](../../README.md)
