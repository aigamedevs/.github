# Word Shooter

> Verified game note.

![Word Shooter screenshot placeholder](word-shooter-placeholder.svg)

## At a glance

- **Score:** 8.0/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Phaser, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/phamhieus/english-games](https://github.com/phamhieus/english-games)
- **Evidence:** [direct model evidence](https://github.com/phamhieus/english-games/commit/6c30047f8f9a710f93f03fc69f2053e938a023b4)
- **Live demo:** [open demo](https://word-shooter-sage.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A cute, soft bubble-shooter style game for memorising English vocabulary. Balloons with words float down. Type the English word and press Enter, and the little cannon pops the balloon. It runs entirely in the browser (data in IndexedDB); optionally players… Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/phamhieus/english-games/blob/main/worker/worker-configuration.d.ts](https://github.com/phamhieus/english-games/blob/main/worker/worker-configuration.d.ts)
- [https://github.com/phamhieus/english-games/commit/6c30047f8f9a710f93f03fc69f2053e938a023b4](https://github.com/phamhieus/english-games/commit/6c30047f8f9a710f93f03fc69f2053e938a023b4)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/phamhieus/english-games

[Back to the awesome list](../../README.md)
