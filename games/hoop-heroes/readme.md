# Hoop Heroes

> Verified game note.

![Hoop Heroes screenshot placeholder](hoop-heroes-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/laizk/hoop-heroes](https://github.com/laizk/hoop-heroes)
- **Evidence:** [direct model evidence](https://github.com/laizk/hoop-heroes/commit/b8db7a940f658f5c4b1a007ed28da712dd4ce5f5)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Chibi 3D arcade basketball in the browser (Three.js + Blender). Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/laizk/hoop-heroes/blob/main/src/game/match.js](https://github.com/laizk/hoop-heroes/blob/main/src/game/match.js)
- [https://github.com/laizk/hoop-heroes/commit/b8db7a940f658f5c4b1a007ed28da712dd4ce5f5](https://github.com/laizk/hoop-heroes/commit/b8db7a940f658f5c4b1a007ed28da712dd4ce5f5)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/laizk/hoop-heroes

[Back to the awesome list](../../README.md)
