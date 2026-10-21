# Stick Soldiers

> Verified game note.

![Stick Soldiers screenshot placeholder](stick-soldiers-placeholder.svg)

## At a glance

- **Score:** 7.9/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/Dec3ptor/StickFighters](https://github.com/Dec3ptor/StickFighters)
- **Evidence:** [direct model evidence](https://github.com/Dec3ptor/StickFighters/commit/b37ca09a458674dd0551dd8de1c35e46e26e748e)
- **Live demo:** [open demo](https://dec3ptor.github.io/StickFighters/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A browser remake of Stick Soldiers II (Whitespace Unlimited, 2003): a side-on, black-and-white stick-figure shooter where you grab weapons, armour and jetpacks lying around the map and frag your way to the limit. Now with online multiplayer, eight game modes… Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Dec3ptor/StickFighters/blob/main/web/src/editor.js](https://github.com/Dec3ptor/StickFighters/blob/main/web/src/editor.js)
- [https://github.com/Dec3ptor/StickFighters/commit/b37ca09a458674dd0551dd8de1c35e46e26e748e](https://github.com/Dec3ptor/StickFighters/commit/b37ca09a458674dd0551dd8de1c35e46e26e748e)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/Dec3ptor/StickFighters

[Back to the awesome list](../../README.md)
