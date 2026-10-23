# Song Guessr

> Verified game note.

![Song Guessr screenshot placeholder](song-guessr-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/michael-lundsgaard/song-guessr](https://github.com/michael-lundsgaard/song-guessr)
- **Evidence:** [direct model evidence](https://github.com/michael-lundsgaard/song-guessr/commit/9d0436c01c610f6e0e275f856fb5854595b988d0)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A home-made Hitster: manage your own song library from Spotify, organise it into collections, and play Hitster-style games from it on the PC. See ROADMAP.md for what's next. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/michael-lundsgaard/song-guessr/blob/main/src/i18n.ts](https://github.com/michael-lundsgaard/song-guessr/blob/main/src/i18n.ts)
- [https://github.com/michael-lundsgaard/song-guessr/commit/9d0436c01c610f6e0e275f856fb5854595b988d0](https://github.com/michael-lundsgaard/song-guessr/commit/9d0436c01c610f6e0e275f856fb5854595b988d0)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/michael-lundsgaard/song-guessr

[Back to the awesome list](../../README.md)
