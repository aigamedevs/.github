# AVA Rip Off

> Verified game note.

![AVA Rip Off screenshot](https://raw.githubusercontent.com/Harlock123/AVARipOff/main/Images/AVARipOff-towing.png)

## At a glance

- **Score:** 7.0/10
- **Screenshot rating:** 6.0/10 ([manually reviewed image](https://github.com/Harlock123/AVARipOff/blob/main/Images/AVARipOff-towing.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/Harlock123/AVARipOff](https://github.com/Harlock123/AVARipOff)
- **Evidence:** [direct model evidence](https://github.com/Harlock123/AVARipOff/commit/2a38b1e30aaea3b92805c871f8e5447f5aa1cbb2)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Harlock123/AVARipOff/blob/main/Images/AVARipOff-towing.png) — 📸 6.0/10 · manual visual review · Use this frame for the game-level score. Vector arcade field with fuel canisters, raider tanks and score; crisp retro vector look, sparse.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A colour vector game after the 1980 arcade classic Rip Off: defend eight fuel canisters from raiders that tow them off the screen. C#, .NET 10 and Avalonia. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Harlock123/AVARipOff/blob/main/src/AVARipOff/Engine/GameEngine.Play.cs](https://github.com/Harlock123/AVARipOff/blob/main/src/AVARipOff/Engine/GameEngine.Play.cs)
- [https://github.com/Harlock123/AVARipOff/commit/2a38b1e30aaea3b92805c871f8e5447f5aa1cbb2](https://github.com/Harlock123/AVARipOff/commit/2a38b1e30aaea3b92805c871f8e5447f5aa1cbb2)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/Harlock123/AVARipOff

[Back to the awesome list](../../README.md)
