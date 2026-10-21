# ARAM: Mayhem

> Verified game note.

![ARAM: Mayhem screenshot placeholder](aram-mayhem-placeholder.svg)

## At a glance

- **Score:** 7.8/10
- **Model:** Claude Opus 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/ancientmodern/aram-mayhem](https://github.com/ancientmodern/aram-mayhem)
- **Evidence:** [direct model evidence](https://github.com/ancientmodern/aram-mayhem/commit/8e3149ed307b3dcd8bdc0e7624a69b668114b021)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Single-player League of Legends ARAM (Howling Abyss) recreation in Godot 4 — 1 player vs 9 bots, driven by League's own game data through custom VFX, animation and HUD runtimes. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ancientmodern/aram-mayhem/blob/main/src/vfx/lol_vfx.gd](https://github.com/ancientmodern/aram-mayhem/blob/main/src/vfx/lol_vfx.gd)
- [https://github.com/ancientmodern/aram-mayhem/commit/8e3149ed307b3dcd8bdc0e7624a69b668114b021](https://github.com/ancientmodern/aram-mayhem/commit/8e3149ed307b3dcd8bdc0e7624a69b668114b021)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/ancientmodern/aram-mayhem

[Back to the awesome list](../../README.md)
