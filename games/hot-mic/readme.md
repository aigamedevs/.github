# Hot Mic

> Verified game note.

![Hot Mic screenshot placeholder](hot-mic-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/KenLDubois/hot-mic-game](https://github.com/KenLDubois/hot-mic-game)
- **Evidence:** [direct model evidence](https://github.com/KenLDubois/hot-mic-game/commit/90d90f78f298f21bef2a844b52fdef2db6b4dce4)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

An online multiplayer game that tests your music knowledge! Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/KenLDubois/hot-mic-game/blob/main/apps/server/src/room.ts](https://github.com/KenLDubois/hot-mic-game/blob/main/apps/server/src/room.ts)
- [https://github.com/KenLDubois/hot-mic-game/commit/90d90f78f298f21bef2a844b52fdef2db6b4dce4](https://github.com/KenLDubois/hot-mic-game/commit/90d90f78f298f21bef2a844b52fdef2db6b4dce4)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/KenLDubois/hot-mic-game

[Back to the awesome list](../../README.md)
