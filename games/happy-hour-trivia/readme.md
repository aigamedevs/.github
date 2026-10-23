# Happy Hour Trivia

> Verified game note.

![Happy Hour Trivia screenshot placeholder](happy-hour-trivia-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Sonnet 5.5
- **Technology:** PHP
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/mavrck/happy-hour-trivia](https://github.com/mavrck/happy-hour-trivia)
- **Evidence:** [direct model evidence](https://github.com/mavrck/happy-hour-trivia/commit/15d973c875fd3777e76639daff228dcf4eedd16a)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A Kahoot-style trivia game for team events. Everyone joins from their phone, the host drives the game, and a shared screen shows the questions, the leaderboard, and a final podium. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/mavrck/happy-hour-trivia/blob/main/database/data/questions.php](https://github.com/mavrck/happy-hour-trivia/blob/main/database/data/questions.php)
- [https://github.com/mavrck/happy-hour-trivia/commit/15d973c875fd3777e76639daff228dcf4eedd16a](https://github.com/mavrck/happy-hour-trivia/commit/15d973c875fd3777e76639daff228dcf4eedd16a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/mavrck/happy-hour-trivia

[Back to the awesome list](../../README.md)
