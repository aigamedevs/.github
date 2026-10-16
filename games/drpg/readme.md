# Drpg

> Verified game note.

![Drpg screenshot placeholder](drpg-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-16
- **Repository:** [https://github.com/ywf2661/Drpg](https://github.com/ywf2661/Drpg)
- **Evidence:** [direct model evidence](https://github.com/ywf2661/Drpg/commit/75e4454ba1814d54ea6019a793511f44ff9ddf7a)
- **Live demo:** [open demo](https://ywf2661.github.io/Drpg/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Diablo 1-style 2.5D web action RPG: descend five random dungeon floors by torchlight and defeat the minotaur; skills, HUD and world sim in src/. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected only; no playtest.

### Gameplay source

- [https://github.com/ywf2661/Drpg/blob/main/tools/sprites.py](https://github.com/ywf2661/Drpg/blob/main/tools/sprites.py)
- [https://github.com/ywf2661/Drpg/commit/75e4454ba1814d54ea6019a793511f44ff9ddf7a](https://github.com/ywf2661/Drpg/commit/75e4454ba1814d54ea6019a793511f44ff9ddf7a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-15..2026-10-16 (6-hour UTC partitions) joined to repositories created after 2026-10-14T17:00Z; https://github.com/ywf2661/Drpg

[Back to the awesome list](../../README.md)
