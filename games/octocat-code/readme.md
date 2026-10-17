# OctoCat-Code

> Verified game note.

![OctoCat-Code screenshot placeholder](octocat-code-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/INDFORGE-Studio/OctoCat-Code](https://github.com/INDFORGE-Studio/OctoCat-Code)
- **Evidence:** [direct model evidence](https://github.com/INDFORGE-Studio/OctoCat-Code/commit/261a3998fd7b13a58bffceab18767907c9b19eeb)
- **Live demo:** [open demo](https://squidfunk.github.io/mkdocs-material/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Jeu d'aventure rétro 2D pour apprendre à programmer — le site est le jeu (MkDocs + KAPLAY.js). Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/INDFORGE-Studio/OctoCat-Code/blob/main/docs/javascripts/engine.js](https://github.com/INDFORGE-Studio/OctoCat-Code/blob/main/docs/javascripts/engine.js)
- [https://github.com/INDFORGE-Studio/OctoCat-Code/commit/261a3998fd7b13a58bffceab18767907c9b19eeb](https://github.com/INDFORGE-Studio/OctoCat-Code/commit/261a3998fd7b13a58bffceab18767907c9b19eeb)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/INDFORGE-Studio/OctoCat-Code

[Back to the awesome list](../../README.md)
