# Zombie Survival Shooter

> Verified game note.

![Zombie Survival Shooter screenshot](https://raw.githubusercontent.com/ahmedayadeng-lang/zombie-survival-shooter/main/docs/screenshot.png)

## At a glance

- **Score:** 6.6/10
- **Screenshot rating:** 3.4/10 ([manually reviewed image](https://github.com/ahmedayadeng-lang/zombie-survival-shooter/blob/main/docs/screenshot.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Python
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/ahmedayadeng-lang/zombie-survival-shooter](https://github.com/ahmedayadeng-lang/zombie-survival-shooter)
- **Evidence:** [direct model evidence](https://github.com/ahmedayadeng-lang/zombie-survival-shooter/commit/3994c7145d2823ea6fb5c6c82debee789191e1d2)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/ahmedayadeng-lang/zombie-survival-shooter/blob/main/docs/screenshot.png) — 📸 3.4/10 · manual visual review · Use this frame for the game-level score. Top-down orange field with small zombies and a player blob; flat and low detail.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Top-down 2D zombie survival shooter in Python/Pygame: 4 weapons, animated sprites, chasing enemy AI, procedural maps and sound. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ahmedayadeng-lang/zombie-survival-shooter/blob/main/player.py](https://github.com/ahmedayadeng-lang/zombie-survival-shooter/blob/main/player.py)
- [https://github.com/ahmedayadeng-lang/zombie-survival-shooter/commit/3994c7145d2823ea6fb5c6c82debee789191e1d2](https://github.com/ahmedayadeng-lang/zombie-survival-shooter/commit/3994c7145d2823ea6fb5c6c82debee789191e1d2)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/ahmedayadeng-lang/zombie-survival-shooter

[Back to the awesome list](../../README.md)
