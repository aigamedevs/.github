# Vocabulary Quiz Show

> Verified game note.

![Vocabulary Quiz Show screenshot placeholder](vocabulary-quiz-show-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Sonnet 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/Ponta-English-Teacher/vocabulary-quiz-show](https://github.com/Ponta-English-Teacher/vocabulary-quiz-show)
- **Evidence:** [direct model evidence](https://github.com/Ponta-English-Teacher/vocabulary-quiz-show/commit/10a3946a6611a3b6f7f15894c36d0fe557cb478b)
- **Live demo:** [open demo](https://vocabulary-quiz-show.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Two-player, face-to-face English vocabulary quiz. One student is the Giver (sees the word, explains it aloud); the other is the Taker (asks questions, types/dictates a guess). Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Ponta-English-Teacher/vocabulary-quiz-show/blob/main/src/lib/studio/ai/prompts.ts](https://github.com/Ponta-English-Teacher/vocabulary-quiz-show/blob/main/src/lib/studio/ai/prompts.ts)
- [https://github.com/Ponta-English-Teacher/vocabulary-quiz-show/commit/10a3946a6611a3b6f7f15894c36d0fe557cb478b](https://github.com/Ponta-English-Teacher/vocabulary-quiz-show/commit/10a3946a6611a3b6f7f15894c36d0fe557cb478b)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/Ponta-English-Teacher/vocabulary-quiz-show

[Back to the awesome list](../../README.md)
