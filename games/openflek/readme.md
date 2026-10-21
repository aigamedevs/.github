# OpenFlek

> Verified game note.

![OpenFlek screenshot](https://raw.githubusercontent.com/radcliffkey/openflek/main/docs/card_sheet.png)

## At a glance

- **Score:** 7.2/10
- **Screenshot rating:** 4.0/10 ([manually reviewed image](https://github.com/radcliffkey/openflek/blob/main/docs/card_sheet.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Rust
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/radcliffkey/openflek](https://github.com/radcliffkey/openflek)
- **Evidence:** [direct model evidence](https://github.com/radcliffkey/openflek/commit/842eafc0750f02991ad81335b3055d745f9a61c8)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/radcliffkey/openflek/blob/main/docs/card_sheet.png) — 📸 4.0/10 · manual visual review · Use this frame for the game-level score. Grid of the game's playing-card faces on green; shows art assets rather than a game in progress.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Open source implementation of Flek! mariáš game. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/radcliffkey/openflek/blob/main/src/game/ai.rs](https://github.com/radcliffkey/openflek/blob/main/src/game/ai.rs)
- [https://github.com/radcliffkey/openflek/commit/842eafc0750f02991ad81335b3055d745f9a61c8](https://github.com/radcliffkey/openflek/commit/842eafc0750f02991ad81335b3055d745f9a61c8)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/radcliffkey/openflek

[Back to the awesome list](../../README.md)
