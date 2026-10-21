# Who did that?

> Verified game note.

![Who did that? screenshot placeholder](who-did-that-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/trickzyinsanity/who-did-that](https://github.com/trickzyinsanity/who-did-that)
- **Evidence:** [direct model evidence](https://github.com/trickzyinsanity/who-did-that/commit/ced38d61ee7bc01ac413a659e9a1820ccfa25b59)
- **Live demo:** [open demo](https://who-did-that.onrender.com)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Party game: everyone writes an anecdote, the group guesses who wrote it (EN/FR). Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/trickzyinsanity/who-did-that/blob/main/public/app.js](https://github.com/trickzyinsanity/who-did-that/blob/main/public/app.js)
- [https://github.com/trickzyinsanity/who-did-that/commit/ced38d61ee7bc01ac413a659e9a1820ccfa25b59](https://github.com/trickzyinsanity/who-did-that/commit/ced38d61ee7bc01ac413a659e9a1820ccfa25b59)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/trickzyinsanity/who-did-that

[Back to the awesome list](../../README.md)
