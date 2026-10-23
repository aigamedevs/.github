# Kuhhandel Online

> Verified game note.

![Kuhhandel Online screenshot placeholder](kuhhandel-online-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/Krist95/kuhhandel](https://github.com/Krist95/kuhhandel)
- **Evidence:** [direct model evidence](https://github.com/Krist95/kuhhandel/commit/4a3974c11c01287ec0596b62470001fa80867fa7)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

An online version of the card game Kuhhandel (Cow Trading) for 3 to 5 players. It is played on phones in landscape and installs as a PWA. There is one room per deployment. It runs on Cloudflare Workers Free with a single Durable Object (GameRoom, bound as… Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Krist95/kuhhandel/blob/main/src/room.ts](https://github.com/Krist95/kuhhandel/blob/main/src/room.ts)
- [https://github.com/Krist95/kuhhandel/commit/4a3974c11c01287ec0596b62470001fa80867fa7](https://github.com/Krist95/kuhhandel/commit/4a3974c11c01287ec0596b62470001fa80867fa7)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/Krist95/kuhhandel

[Back to the awesome list](../../README.md)
