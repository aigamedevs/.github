# Blindspot

> Verified game note.

![Blindspot screenshot placeholder](blindspot-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Sonnet 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/MeetThakur/blindspot](https://github.com/MeetThakur/blindspot)
- **Evidence:** [direct model evidence](https://github.com/MeetThakur/blindspot/commit/c49fe0e7bcc09736f695e4767ac3094eb0fe0357)
- **Live demo:** [open demo](https://blindspot.pages.dev)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A real-time party game for 2–5 friends in the browser, made for playing on a Discord call. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/MeetThakur/blindspot/blob/main/client/src/screens/Game.tsx](https://github.com/MeetThakur/blindspot/blob/main/client/src/screens/Game.tsx)
- [https://github.com/MeetThakur/blindspot/commit/c49fe0e7bcc09736f695e4767ac3094eb0fe0357](https://github.com/MeetThakur/blindspot/commit/c49fe0e7bcc09736f695e4767ac3094eb0fe0357)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/MeetThakur/blindspot

[Back to the awesome list](../../README.md)
