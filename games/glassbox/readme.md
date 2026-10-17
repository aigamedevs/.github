# Glassbox

> Verified game note.

![Glassbox screenshot](https://raw.githubusercontent.com/AbrahamCain/glassbox/main/docs/screenshot.png)

## At a glance

- **Score:** 7.0/10
- **Screenshot rating:** 5.6/10 ([manually reviewed image](https://github.com/AbrahamCain/glassbox/blob/main/docs/screenshot.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/AbrahamCain/glassbox](https://github.com/AbrahamCain/glassbox)
- **Evidence:** [direct model evidence](https://github.com/AbrahamCain/glassbox/commit/bff094bde5c57a5f4c02ed4c4c64b8f13f55b1b6)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/AbrahamCain/glassbox/blob/main/docs/screenshot.png) — 📸 5.6/10 · manual visual review · Use this frame for the game-level score. Layer-stack visualisation with quest list and question panel; educational, text-heavy.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A game for exploring the inside of a vision-language model: climb its layers, cast interventions, bet on the outcome. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/AbrahamCain/glassbox/blob/main/godot/scripts/main.gd](https://github.com/AbrahamCain/glassbox/blob/main/godot/scripts/main.gd)
- [https://github.com/AbrahamCain/glassbox/commit/bff094bde5c57a5f4c02ed4c4c64b8f13f55b1b6](https://github.com/AbrahamCain/glassbox/commit/bff094bde5c57a5f4c02ed4c4c64b8f13f55b1b6)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/AbrahamCain/glassbox

[Back to the awesome list](../../README.md)
