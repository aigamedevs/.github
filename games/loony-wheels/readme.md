# Loony Wheels

> Verified game note.

![Loony Wheels screenshot placeholder](loony-wheels-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/deathangel4290/Loony](https://github.com/deathangel4290/Loony)
- **Evidence:** [direct model evidence](https://github.com/deathangel4290/Loony/commit/e80be4f2d7e232a532963b1cb3dd368f775d4dc8)
- **Live demo:** [open demo](https://deathangel4290.github.io/Loony/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A 2D physics hill-driving game for iOS. Drive as far as you can across six worlds (including a low-gravity moon), flip for coins, manage fuel, upgrade seven very different vehicles and chase your best distance. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/deathangel4290/Loony/blob/claude/mobile-car-game/src/game/GameView.ts](https://github.com/deathangel4290/Loony/blob/claude/mobile-car-game/src/game/GameView.ts)
- [https://github.com/deathangel4290/Loony/commit/e80be4f2d7e232a532963b1cb3dd368f775d4dc8](https://github.com/deathangel4290/Loony/commit/e80be4f2d7e232a532963b1cb3dd368f775d4dc8)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/deathangel4290/Loony

[Back to the awesome list](../../README.md)
