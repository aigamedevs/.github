# Tamtech WEM Crossword

> Verified game note.

![Tamtech WEM Crossword screenshot placeholder](tamtech-wem-crossword-placeholder.svg)

## At a glance

- **Score:** 6.9/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/jordanlcn/crossword-game](https://github.com/jordanlcn/crossword-game)
- **Evidence:** [direct model evidence](https://github.com/jordanlcn/crossword-game/commit/a7cfe06b37bc32436604e4bdc0f682b769958adf)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Live multiplayer crossword (Node.js + WebSocket). 60 words from words.json (built from the Excel file), one puzzle per room, one player per team. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jordanlcn/crossword-game/blob/main/server.js](https://github.com/jordanlcn/crossword-game/blob/main/server.js)
- [https://github.com/jordanlcn/crossword-game/commit/a7cfe06b37bc32436604e4bdc0f682b769958adf](https://github.com/jordanlcn/crossword-game/commit/a7cfe06b37bc32436604e4bdc0f682b769958adf)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/jordanlcn/crossword-game

[Back to the awesome list](../../README.md)
