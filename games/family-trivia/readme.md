# Family Trivia

> Verified game note.

![Family Trivia screenshot](https://raw.githubusercontent.com/yeahthisisrob/family-trivia/main/docs/screenshots/01-trivia-flow.png)

## At a glance

- **Score:** 8.2/10
- **Screenshot rating:** 4.6/10 ([manually reviewed image](https://github.com/yeahthisisrob/family-trivia/blob/main/docs/screenshots/01-trivia-flow.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/yeahthisisrob/family-trivia](https://github.com/yeahthisisrob/family-trivia)
- **Evidence:** [direct model evidence](https://github.com/yeahthisisrob/family-trivia/commit/5c37822873db40636e16a61a9f0c05752f6428d7)
- **Live demo:** [open demo](https://github.com/yeahthisisrob/family-trivia#readme)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/yeahthisisrob/family-trivia/blob/main/docs/screenshots/01-trivia-flow.png) — 📸 4.6/10 · manual visual review · Use this frame for the game-level score. Plain mobile trivia category menu; functional, little visual content.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

AI-powered family trivia, daily facts, and mini-games. Built with React, AWS CDK, and Claude on Bedrock. Dedicated to Mom for #MentalHealthMonth & #WordsToRememberForNana. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/yeahthisisrob/family-trivia/blob/main/shared/generated/api-types.ts](https://github.com/yeahthisisrob/family-trivia/blob/main/shared/generated/api-types.ts)
- [https://github.com/yeahthisisrob/family-trivia/commit/5c37822873db40636e16a61a9f0c05752f6428d7](https://github.com/yeahthisisrob/family-trivia/commit/5c37822873db40636e16a61a9f0c05752f6428d7)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/yeahthisisrob/family-trivia

[Back to the awesome list](../../README.md)
