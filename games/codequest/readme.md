# CodeQuest

> Verified game note.

![CodeQuest screenshot](https://raw.githubusercontent.com/mason-keiser/code-quest/master/docs/screenshots/host-lobby.png)

## At a glance

- **Score:** 7.1/10
- **Screenshot rating:** 4.5/10 ([manually reviewed image](https://github.com/mason-keiser/code-quest/blob/master/docs/screenshots/host-lobby.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/mason-keiser/code-quest](https://github.com/mason-keiser/code-quest)
- **Evidence:** [direct model evidence](https://github.com/mason-keiser/code-quest/commit/3b342f117046380c79ec92501ccce9ecf0c0f19e)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/mason-keiser/code-quest/blob/master/docs/screenshots/host-lobby.png) — 📸 4.5/10 · manual visual review · Use this frame for the game-level score. Quiz host lobby with game PIN; plain web UI.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

🔗 Live demo: add your Vercel URL here. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/mason-keiser/code-quest/blob/master/src/components/QuizEditor.tsx](https://github.com/mason-keiser/code-quest/blob/master/src/components/QuizEditor.tsx)
- [https://github.com/mason-keiser/code-quest/commit/3b342f117046380c79ec92501ccce9ecf0c0f19e](https://github.com/mason-keiser/code-quest/commit/3b342f117046380c79ec92501ccce9ecf0c0f19e)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/mason-keiser/code-quest

[Back to the awesome list](../../README.md)
