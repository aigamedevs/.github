# AVA Jet Set Willy

> Verified game note.

![AVA Jet Set Willy screenshot](https://raw.githubusercontent.com/Harlock123/AVAJetSetWilly/main/Images/AVAJetSetWilly-bathroom.png)

## At a glance

- **Score:** 7.1/10
- **Screenshot rating:** 5.4/10 ([manually reviewed image](https://github.com/Harlock123/AVAJetSetWilly/blob/main/Images/AVAJetSetWilly-bathroom.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/Harlock123/AVAJetSetWilly](https://github.com/Harlock123/AVAJetSetWilly)
- **Evidence:** [direct model evidence](https://github.com/Harlock123/AVAJetSetWilly/commit/4d458ec4af1e4fcc2e5785872d9748e7f47d2ca5)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Harlock123/AVAJetSetWilly/blob/main/Images/AVAJetSetWilly-bathroom.png) — 📸 5.4/10 · manual visual review · Use this frame for the game-level score. ZX-style mansion room with platforms, collectibles and status bar; faithful retro, flat.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A flip-screen platformer round a mansion: put every item away before midnight, in the style of Matthew Smith's 1984 Jet Set Willy. .NET 10 + Avalonia. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Harlock123/AVAJetSetWilly/blob/main/src/AVAJetSetWilly/Views/GameCanvas.Draw.cs](https://github.com/Harlock123/AVAJetSetWilly/blob/main/src/AVAJetSetWilly/Views/GameCanvas.Draw.cs)
- [https://github.com/Harlock123/AVAJetSetWilly/commit/4d458ec4af1e4fcc2e5785872d9748e7f47d2ca5](https://github.com/Harlock123/AVAJetSetWilly/commit/4d458ec4af1e4fcc2e5785872d9748e7f47d2ca5)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/Harlock123/AVAJetSetWilly

[Back to the awesome list](../../README.md)
