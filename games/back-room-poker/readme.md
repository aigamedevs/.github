# Back Room Poker

> Verified game note.

![Back Room Poker screenshot placeholder](back-room-poker-placeholder.svg)

## At a glance

- **Score:** 7.8/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/Frigiduss/backroom-poker](https://github.com/Frigiduss/backroom-poker)
- **Evidence:** [direct model evidence](https://github.com/Frigiduss/backroom-poker/commit/190a93d279c030457e2ce6de1f9e132677ee9f6b)
- **Live demo:** [open demo](https://frigiduss.github.io/backroom-poker/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A browser poker game against computer opponents. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Frigiduss/backroom-poker/blob/main/supabase/functions/poker-table/index.ts](https://github.com/Frigiduss/backroom-poker/blob/main/supabase/functions/poker-table/index.ts)
- [https://github.com/Frigiduss/backroom-poker/commit/190a93d279c030457e2ce6de1f9e132677ee9f6b](https://github.com/Frigiduss/backroom-poker/commit/190a93d279c030457e2ce6de1f9e132677ee9f6b)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/Frigiduss/backroom-poker

[Back to the awesome list](../../README.md)
