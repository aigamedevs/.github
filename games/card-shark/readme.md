# Card Shark

> Verified game note.

![Card Shark screenshot placeholder](card-shark-placeholder.svg)

## At a glance

- **Score:** 6.7/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/MoneyGotLonger/card-shark](https://github.com/MoneyGotLonger/card-shark)
- **Evidence:** [direct model evidence](https://github.com/MoneyGotLonger/card-shark/commit/e315ea99b89444ced6c1abd5979f293a4208ee58)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Head-to-head trading card price game. Two players see the same 6 pairs of cards and pick which is worth more (or less). Highest score wins, and wins and losses move you up a ranked ladder. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/MoneyGotLonger/card-shark/blob/main/src/screens/MatchScreen.tsx](https://github.com/MoneyGotLonger/card-shark/blob/main/src/screens/MatchScreen.tsx)
- [https://github.com/MoneyGotLonger/card-shark/commit/e315ea99b89444ced6c1abd5979f293a4208ee58](https://github.com/MoneyGotLonger/card-shark/commit/e315ea99b89444ced6c1abd5979f293a4208ee58)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/MoneyGotLonger/card-shark

[Back to the awesome list](../../README.md)
