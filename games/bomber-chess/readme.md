# Bomber-Chess

> Verified game note.

![Bomber-Chess screenshot placeholder](bomber-chess-placeholder.svg)

## At a glance

- **Score:** 6.8/10
- **Model:** Claude Fable 5.1
- **Technology:** JavaScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/JorSanders/bomber-chess](https://github.com/JorSanders/bomber-chess)
- **Evidence:** [direct model evidence](https://github.com/JorSanders/bomber-chess/commit/108a5d57ee5a5f2125f3df12fb7c8cd8b8e165d6)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Bomberman on a chess board: the bombs are chess pieces and blow up the squares they attack. Commit carries an exact Claude Fable 5.1 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/JorSanders/bomber-chess/blob/main/src/game.js](https://github.com/JorSanders/bomber-chess/blob/main/src/game.js)
- [https://github.com/JorSanders/bomber-chess/commit/108a5d57ee5a5f2125f3df12fb7c8cd8b8e165d6](https://github.com/JorSanders/bomber-chess/commit/108a5d57ee5a5f2125f3df12fb7c8cd8b8e165d6)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/JorSanders/bomber-chess

[Back to the awesome list](../../README.md)
