# AVA X-COM

> Verified game note.

![AVA X-COM screenshot](https://raw.githubusercontent.com/Harlock123/AVAXCom/main/Images/AVAXCom-geoscape.png)

## At a glance

- **Score:** 7.5/10
- **Screenshot rating:** 6.4/10 ([manually reviewed image](https://github.com/Harlock123/AVAXCom/blob/main/Images/AVAXCom-geoscape.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** C#, React
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/Harlock123/AVAXCom](https://github.com/Harlock123/AVAXCom)
- **Evidence:** [direct model evidence](https://github.com/Harlock123/AVAXCom/commit/4072e07f41185c735e65a76773dd016b373f3a11)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Harlock123/AVAXCom/blob/main/Images/AVAXCom-geoscape.png) — 📸 6.4/10 · manual visual review · Use this frame for the game-level score. Geoscape globe with UFO interception alert, clock and command menu; faithful X-COM style layout.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A UFO defence strategy game in the style of X-COM: UFO Defense (MicroProse, 1994), in .NET 10 and Avalonia. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Harlock123/AVAXCom/blob/main/src/AVAXCom/Engine/Campaign.cs](https://github.com/Harlock123/AVAXCom/blob/main/src/AVAXCom/Engine/Campaign.cs)
- [https://github.com/Harlock123/AVAXCom/commit/4072e07f41185c735e65a76773dd016b373f3a11](https://github.com/Harlock123/AVAXCom/commit/4072e07f41185c735e65a76773dd016b373f3a11)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/Harlock123/AVAXCom

[Back to the awesome list](../../README.md)
