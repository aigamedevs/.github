# Tidewater (island horror game)

> Verified game note.

![Tidewater (island horror game) screenshot placeholder](tidewater-island-horror-game-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Sonnet 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/upenthiran93/godot_horrogame_island](https://github.com/upenthiran93/godot_horrogame_island)
- **Evidence:** [direct model evidence](https://github.com/upenthiran93/godot_horrogame_island/commit/12b64583d917b8fee94d93d92b79de594f586845)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A first-person island horror game in Godot 4.7, built previs-first: story in story/, auto-playing chapter playblasts in previs/, level blockouts in game/levels/, and a 3D story map in game/map/. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/upenthiran93/godot_horrogame_island/blob/main/tools/build_chapters.gd](https://github.com/upenthiran93/godot_horrogame_island/blob/main/tools/build_chapters.gd)
- [https://github.com/upenthiran93/godot_horrogame_island/commit/12b64583d917b8fee94d93d92b79de594f586845](https://github.com/upenthiran93/godot_horrogame_island/commit/12b64583d917b8fee94d93d92b79de594f586845)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/upenthiran93/godot_horrogame_island

[Back to the awesome list](../../README.md)
