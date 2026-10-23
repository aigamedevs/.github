# Tank Tangle

> Verified game note.

![Tank Tangle screenshot placeholder](tank-tangle-placeholder.svg)

## At a glance

- **Score:** 8.0/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/bradwindy/tanktangle](https://github.com/bradwindy/tanktangle)
- **Evidence:** [direct model evidence](https://github.com/bradwindy/tanktangle/commit/729a264f52216b5a46b77883990b9d378ed57033)
- **Live demo:** [open demo](https://tanktangle.bradwindy.workers.dev)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Retro pixel maze tank battles for 2 to 12 players, in the browser. Share a link, ricochet, blow up the walls. Cloudflare Workers + Durable Objects. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/bradwindy/tanktangle/blob/main/worker-configuration.d.ts](https://github.com/bradwindy/tanktangle/blob/main/worker-configuration.d.ts)
- [https://github.com/bradwindy/tanktangle/commit/729a264f52216b5a46b77883990b9d378ed57033](https://github.com/bradwindy/tanktangle/commit/729a264f52216b5a46b77883990b9d378ed57033)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/bradwindy/tanktangle

[Back to the awesome list](../../README.md)
