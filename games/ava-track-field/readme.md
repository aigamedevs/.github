# AVA Track & Field

> Verified game note.

![AVA Track & Field screenshot](https://raw.githubusercontent.com/Harlock123/AVATrackAndField/main/Images/AVATrackAndField-dash.png)

## At a glance

- **Score:** 7.2/10
- **Screenshot rating:** 6.4/10 ([manually reviewed image](https://github.com/Harlock123/AVATrackAndField/blob/main/Images/AVATrackAndField-dash.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/Harlock123/AVATrackAndField](https://github.com/Harlock123/AVATrackAndField)
- **Evidence:** [direct model evidence](https://github.com/Harlock123/AVATrackAndField/commit/b3cbff44e164329f2b7204b692788f60991d581a)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Harlock123/AVATrackAndField/blob/main/Images/AVATrackAndField-dash.png) — 📸 6.4/10 · manual visual review · Use this frame for the game-level score. Track and Field sprint with a packed stadium crowd, scoreboard and speed bar; faithful, lively retro scene.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A recreation of Track & Field (Konami arcade, 1983) in .NET 10 and Avalonia. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Harlock123/AVATrackAndField/blob/main/src/AVATrackAndField/Views/GameCanvas.Draw.cs](https://github.com/Harlock123/AVATrackAndField/blob/main/src/AVATrackAndField/Views/GameCanvas.Draw.cs)
- [https://github.com/Harlock123/AVATrackAndField/commit/b3cbff44e164329f2b7204b692788f60991d581a](https://github.com/Harlock123/AVATrackAndField/commit/b3cbff44e164329f2b7204b692788f60991d581a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/Harlock123/AVATrackAndField

[Back to the awesome list](../../README.md)
