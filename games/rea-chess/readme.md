# REA Chess

> Verified game note.

![REA Chess screenshot placeholder](rea-chess-placeholder.svg)

## At a glance

- **Score:** 8.2/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/paulofcmello/rea-chess](https://github.com/paulofcmello/rea-chess)
- **Evidence:** [direct model evidence](https://github.com/paulofcmello/rea-chess/commit/4b0a91c0d736bc3072ab1348047073fd5eb5c212)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A local, single-player take on chess.com's puzzles and bots. No accounts, no multiplayer. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/paulofcmello/rea-chess/blob/main/.rea/scripts/files/origins/1e76d9acdaa1d09f7881b8ef8a593a6b926a3cd57d263a84ce6cf6edf900e283/r2/client-packages/puzzles/2026.10.3/shared.eager.CZJHaxB19i.chunk.js](https://github.com/paulofcmello/rea-chess/blob/main/.rea/scripts/files/origins/1e76d9acdaa1d09f7881b8ef8a593a6b926a3cd57d263a84ce6cf6edf900e283/r2/client-packages/puzzles/2026.10.3/shared.eager.CZJHaxB19i.chunk.js)
- [https://github.com/paulofcmello/rea-chess/commit/4b0a91c0d736bc3072ab1348047073fd5eb5c212](https://github.com/paulofcmello/rea-chess/commit/4b0a91c0d736bc3072ab1348047073fd5eb5c212)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/paulofcmello/rea-chess

[Back to the awesome list](../../README.md)
