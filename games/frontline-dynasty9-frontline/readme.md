# Frontline

> Verified game note.

![Frontline screenshot](https://raw.githubusercontent.com/Dynasty9/Frontline/main/docs/screenshots/battle.jpg)

## At a glance

- **Score:** 8.0/10
- **Screenshot rating:** 7.2/10 ([manually reviewed image](https://github.com/Dynasty9/Frontline/blob/main/docs/screenshots/battle.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/Dynasty9/Frontline](https://github.com/Dynasty9/Frontline)
- **Evidence:** [direct model evidence](https://github.com/Dynasty9/Frontline/commit/77b8b1ce5026c7030f6eb6b37bcf1d8c60a104d9)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Dynasty9/Frontline/blob/main/docs/screenshots/battle.jpg) — 📸 7.2/10 · manual visual review · Use this frame for the game-level score. Squad RTS battlefield with buildings, fires, trees and a unit list HUD; detailed terrain, dense interface.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Squad-level military RTS in Godot 4: soldiers who think, squad tactics, armour, boats and helicopters on a 1 km battlefield. Co-op and PvP. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Dynasty9/Frontline/blob/main/scripts/game/vehicles/vm_core.gd](https://github.com/Dynasty9/Frontline/blob/main/scripts/game/vehicles/vm_core.gd)
- [https://github.com/Dynasty9/Frontline/commit/77b8b1ce5026c7030f6eb6b37bcf1d8c60a104d9](https://github.com/Dynasty9/Frontline/commit/77b8b1ce5026c7030f6eb6b37bcf1d8c60a104d9)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/Dynasty9/Frontline

[Back to the awesome list](../../README.md)
