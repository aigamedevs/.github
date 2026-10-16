# QUIZ KNIGHTS

> Verified game note.

![QUIZ KNIGHTS screenshot placeholder](quiz-knights-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Svelte, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-16
- **Repository:** [https://github.com/MiyazakiSora1234/quiz-knights](https://github.com/MiyazakiSora1234/quiz-knights)
- **Evidence:** [direct model evidence](https://github.com/MiyazakiSora1234/quiz-knights/commit/fb9277fdaf80f3524cbe8926c38be8f80409d952)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Job-based battle game linked to buzzer quizzes with remote participation; rules engine with fuzz tests and a room server. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected only; no playtest.

### Gameplay source

- [https://github.com/MiyazakiSora1234/quiz-knights/blob/main/app/src/lib/engine/battle.js](https://github.com/MiyazakiSora1234/quiz-knights/blob/main/app/src/lib/engine/battle.js)
- [https://github.com/MiyazakiSora1234/quiz-knights/commit/fb9277fdaf80f3524cbe8926c38be8f80409d952](https://github.com/MiyazakiSora1234/quiz-knights/commit/fb9277fdaf80f3524cbe8926c38be8f80409d952)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-15..2026-10-16 (6-hour UTC partitions) joined to repositories created after 2026-10-14T17:00Z; https://github.com/MiyazakiSora1234/quiz-knights

[Back to the awesome list](../../README.md)
