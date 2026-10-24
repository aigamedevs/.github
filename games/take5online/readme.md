# take5online

> Verified game note.

![take5online screenshot placeholder](take5online-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-24
- **Repository:** [https://github.com/max-mayorov/take5online](https://github.com/max-mayorov/take5online)
- **Evidence:** [direct model evidence](https://github.com/max-mayorov/take5online/commit/998bf471789f82328500822cb4835441d5cbafb0)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A private website for playing 6 nimmt! (aka Take 5) live with friends, hosted on Cloudflare at https://take5.mayorov.dev. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/max-mayorov/take5online/blob/main/apps/worker/src/room.ts](https://github.com/max-mayorov/take5online/blob/main/apps/worker/src/room.ts)
- [https://github.com/max-mayorov/take5online/commit/998bf471789f82328500822cb4835441d5cbafb0](https://github.com/max-mayorov/take5online/commit/998bf471789f82328500822cb4835441d5cbafb0)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; https://github.com/max-mayorov/take5online

[Back to the awesome list](../../README.md)
