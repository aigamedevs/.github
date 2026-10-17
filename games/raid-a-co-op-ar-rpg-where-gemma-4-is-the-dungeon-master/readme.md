# Raid — a co-op AR RPG where Gemma 4 is the dungeon master

> Verified game note.

![Raid — a co-op AR RPG where Gemma 4 is the dungeon master screenshot](https://raw.githubusercontent.com/hocmemini/gemma-raid/main/docs/screenshots/lobby.png)

## At a glance

- **Score:** 7.3/10
- **Screenshot rating:** 3.8/10 ([manually reviewed image](https://github.com/hocmemini/gemma-raid/blob/main/docs/screenshots/lobby.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Fable 5.1
- **Technology:** Kotlin
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/hocmemini/gemma-raid](https://github.com/hocmemini/gemma-raid)
- **Evidence:** [direct model evidence](https://github.com/hocmemini/gemma-raid/commit/04ac5d240c847ca5105780f3f102e43242a217dc)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/hocmemini/gemma-raid/blob/main/docs/screenshots/lobby.png) — 📸 3.8/10 · manual visual review · Use this frame for the game-level score. Dark mobile setup screen with small text and one button; little visual content.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Co-op AR RPG where Gemma 4 runs on your phone as the dungeon master. Offline, peer-to-peer, open weights. Commit carries an exact Claude Fable 5.1 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/hocmemini/gemma-raid/blob/main/android/app/src/main/kotlin/com/hocmemini/raid/GameSession.kt](https://github.com/hocmemini/gemma-raid/blob/main/android/app/src/main/kotlin/com/hocmemini/raid/GameSession.kt)
- [https://github.com/hocmemini/gemma-raid/commit/04ac5d240c847ca5105780f3f102e43242a217dc](https://github.com/hocmemini/gemma-raid/commit/04ac5d240c847ca5105780f3f102e43242a217dc)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/hocmemini/gemma-raid

[Back to the awesome list](../../README.md)
