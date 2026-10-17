# Music Memory

> Verified game note.

![Music Memory screenshot placeholder](music-memory-placeholder.svg)

## At a glance

- **Score:** 6.9/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/thomaswiener/music-memory](https://github.com/thomaswiener/music-memory)
- **Evidence:** [direct model evidence](https://github.com/thomaswiener/music-memory/commit/1b6730c62e1a4aa46fd9d8c8f204c22b5974089c)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A memory match game played by ear. Flip two tiles, each plays a short Spotify snippet, and pair the ones that sound the same. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/thomaswiener/music-memory/blob/main/src/lib/spotify.js](https://github.com/thomaswiener/music-memory/blob/main/src/lib/spotify.js)
- [https://github.com/thomaswiener/music-memory/commit/1b6730c62e1a4aa46fd9d8c8f204c22b5974089c](https://github.com/thomaswiener/music-memory/commit/1b6730c62e1a4aa46fd9d8c8f204c22b5974089c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/thomaswiener/music-memory

[Back to the awesome list](../../README.md)
