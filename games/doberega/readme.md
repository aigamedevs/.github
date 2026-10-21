# Doberega — тиша та спокій

> Verified game note.

![Doberega — тиша та спокій screenshot placeholder](doberega-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/denislinnik948-lgtm/doberega](https://github.com/denislinnik948-lgtm/doberega)
- **Evidence:** [direct model evidence](https://github.com/denislinnik948-lgtm/doberega/commit/752046e508280f44e25052b073947458fef2e631)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A small, dependency-free canvas prototype for a calm lake scene rendered as a regular ASCII character field. The screen grid and distant forest glyphs are generated on resize or when character spacing changes. Water animation is a separate mathematical model,… Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/denislinnik948-lgtm/doberega/blob/main/src/canvas-renderer.js](https://github.com/denislinnik948-lgtm/doberega/blob/main/src/canvas-renderer.js)
- [https://github.com/denislinnik948-lgtm/doberega/commit/752046e508280f44e25052b073947458fef2e631](https://github.com/denislinnik948-lgtm/doberega/commit/752046e508280f44e25052b073947458fef2e631)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/denislinnik948-lgtm/doberega

[Back to the awesome list](../../README.md)
