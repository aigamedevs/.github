# AVA Dune II

> Verified game note.

![AVA Dune II screenshot](https://raw.githubusercontent.com/Harlock123/AVADune2/main/Images/AVADune2-title.png)

## At a glance

- **Score:** 7.4/10
- **Screenshot rating:** 5.4/10 ([manually reviewed image](https://github.com/Harlock123/AVADune2/blob/main/Images/AVADune2-title.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/Harlock123/AVADune2](https://github.com/Harlock123/AVADune2)
- **Evidence:** [direct model evidence](https://github.com/Harlock123/AVADune2/commit/3c5806c25ef9c43ff81f07c44d9fad7955852240)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Harlock123/AVADune2/blob/main/Images/AVADune2-title.png) — 📸 5.4/10 · manual visual review · Use this frame for the game-level score. Desert title screen with a sandworm and campaign menu; a title card.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A real-time strategy game in the style of Dune II (Westwood, 1992), in .NET 10 and Avalonia. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Harlock123/AVADune2/blob/main/src/AVADune2/Engine/GameEngine.cs](https://github.com/Harlock123/AVADune2/blob/main/src/AVADune2/Engine/GameEngine.cs)
- [https://github.com/Harlock123/AVADune2/commit/3c5806c25ef9c43ff81f07c44d9fad7955852240](https://github.com/Harlock123/AVADune2/commit/3c5806c25ef9c43ff81f07c44d9fad7955852240)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/Harlock123/AVADune2

[Back to the awesome list](../../README.md)
