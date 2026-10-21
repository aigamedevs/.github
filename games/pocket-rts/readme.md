# Pocket RTS

> Verified game note.

![Pocket RTS screenshot placeholder](pocket-rts-placeholder.svg)

## At a glance

- **Score:** 8.0/10
- **Model:** Claude Opus 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/cavaleirobrancopensante/PocketRTS](https://github.com/cavaleirobrancopensante/PocketRTS)
- **Evidence:** [direct model evidence](https://github.com/cavaleirobrancopensante/PocketRTS/commit/3dc62e733a9c18ea6047a442ca1fe25e81bb7c21)
- **Live demo:** [open demo](https://cavaleirobrancopensante.github.io/PocketRTS/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A StarCraft / Beyond All Reason style real-time strategy game for phones and the browser, made in Godot 4.7 with NES-style pixel art. Play a skirmish with up to four players: 1v1, 2v2, you against two or three computers, or a free-for-all. Each slot picks a… Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/cavaleirobrancopensante/PocketRTS/blob/main/tools/music/compose.py](https://github.com/cavaleirobrancopensante/PocketRTS/blob/main/tools/music/compose.py)
- [https://github.com/cavaleirobrancopensante/PocketRTS/commit/3dc62e733a9c18ea6047a442ca1fe25e81bb7c21](https://github.com/cavaleirobrancopensante/PocketRTS/commit/3dc62e733a9c18ea6047a442ca1fe25e81bb7c21)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/cavaleirobrancopensante/PocketRTS

[Back to the awesome list](../../README.md)
