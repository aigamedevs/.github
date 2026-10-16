# Clown Squad

> Verified game note.

![Clown Squad screenshot placeholder](clown-squad-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** C#, Godot, Desktop
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-16
- **Repository:** [https://github.com/eddiedonesit/ClownSquad](https://github.com/eddiedonesit/ClownSquad)
- **Evidence:** [direct model evidence](https://github.com/eddiedonesit/ClownSquad/commit/8c8a7d7c1b99d536476b969f73bebffb4c93043a)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Godot C# game with an HD-2D world map and fighter actors (PlayerFighter.cs, WorldMap3D.cs) plus generated art and music pipelines; no README. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected only; no playtest.

### Gameplay source

- [https://github.com/eddiedonesit/ClownSquad/blob/master/tools/gen_cast_hd.py](https://github.com/eddiedonesit/ClownSquad/blob/master/tools/gen_cast_hd.py)
- [https://github.com/eddiedonesit/ClownSquad/commit/8c8a7d7c1b99d536476b969f73bebffb4c93043a](https://github.com/eddiedonesit/ClownSquad/commit/8c8a7d7c1b99d536476b969f73bebffb4c93043a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-15..2026-10-16 (6-hour UTC partitions) joined to repositories created after 2026-10-14T17:00Z; https://github.com/eddiedonesit/ClownSquad

[Back to the awesome list](../../README.md)
