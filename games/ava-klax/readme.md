# AVA Klax

> Verified game note.

![AVA Klax screenshot](https://raw.githubusercontent.com/Harlock123/AVAKlax/main/Images/AVAKlax-play.png)

## At a glance

- **Score:** 7.1/10
- **Screenshot rating:** 6.2/10 ([manually reviewed image](https://github.com/Harlock123/AVAKlax/blob/main/Images/AVAKlax-play.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/Harlock123/AVAKlax](https://github.com/Harlock123/AVAKlax)
- **Evidence:** [direct model evidence](https://github.com/Harlock123/AVAKlax/commit/99f2cedae6de542db0edd6e479b61668a641dacd)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Harlock123/AVAKlax/blob/main/Images/AVAKlax-play.png) — 📸 6.2/10 · manual visual review · Use this frame for the game-level score. Klax-style perspective conveyor with coloured tiles, bin grid and goal panels; clean neon arcade layout.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A recreation of Klax (Atari Games arcade, 1989) in .NET 10 and Avalonia. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Harlock123/AVAKlax/blob/main/src/AVAKlax/Views/GameCanvas.Draw.cs](https://github.com/Harlock123/AVAKlax/blob/main/src/AVAKlax/Views/GameCanvas.Draw.cs)
- [https://github.com/Harlock123/AVAKlax/commit/99f2cedae6de542db0edd6e479b61668a641dacd](https://github.com/Harlock123/AVAKlax/commit/99f2cedae6de542db0edd6e479b61668a641dacd)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/Harlock123/AVAKlax

[Back to the awesome list](../../README.md)
