# Brawler

> Verified game note.

![Brawler screenshot](https://raw.githubusercontent.com/cgsereggela/Brawler/master/docs/media/chaos.gif)

## At a glance

- **Score:** 7.7/10
- **Screenshot rating:** 6.0/10 ([manually reviewed image](https://github.com/cgsereggela/Brawler/blob/master/docs/media/chaos.gif)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/cgsereggela/Brawler](https://github.com/cgsereggela/Brawler)
- **Evidence:** [direct model evidence](https://github.com/cgsereggela/Brawler/commit/bd31135251c20c014506bb20ddf136254d16b582)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/cgsereggela/Brawler/blob/master/docs/media/chaos.gif) — 📸 6.0/10 · manual visual review · Use this frame for the game-level score. Purple cave arena with platforms, four-player HUD and a highlighted player; clear, moody 2D layout.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A ROUNDS-style 2–8 player platform shooter: lose a round, pick a card, come back stronger. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/cgsereggela/Brawler/blob/master/godot/scripts/Main.Checks.cs](https://github.com/cgsereggela/Brawler/blob/master/godot/scripts/Main.Checks.cs)
- [https://github.com/cgsereggela/Brawler/commit/bd31135251c20c014506bb20ddf136254d16b582](https://github.com/cgsereggela/Brawler/commit/bd31135251c20c014506bb20ddf136254d16b582)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/cgsereggela/Brawler

[Back to the awesome list](../../README.md)
