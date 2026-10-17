# Drakonix Picross

> Verified game note.

![Drakonix Picross screenshot](https://raw.githubusercontent.com/meltingscales/DrakonixPicrossAndroid/main/screenshots/play/gallery-1.png)

## At a glance

- **Score:** 6.9/10
- **Screenshot rating:** 5.4/10 ([manually reviewed image](https://github.com/meltingscales/DrakonixPicrossAndroid/blob/main/screenshots/play/gallery-1.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Fable 5.1
- **Technology:** Kotlin
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/meltingscales/DrakonixPicrossAndroid](https://github.com/meltingscales/DrakonixPicrossAndroid)
- **Evidence:** [direct model evidence](https://github.com/meltingscales/DrakonixPicrossAndroid/commit/61ace8a60722396c4da2fcab466feeb85b922ebb)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/meltingscales/DrakonixPicrossAndroid/blob/main/screenshots/play/gallery-1.png) — 📸 5.4/10 · manual visual review · Use this frame for the game-level score. Picross gallery of solved pixel images; neat, not gameplay.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Simple Android picross (nonogram) game. No ads, no BS. Just a fun puzzle game. Commit carries an exact Claude Opus 5.5 / Claude Fable 5.1 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/meltingscales/DrakonixPicrossAndroid/blob/main/app/src/main/java/systems/drakonix/picross/PicrossView.kt](https://github.com/meltingscales/DrakonixPicrossAndroid/blob/main/app/src/main/java/systems/drakonix/picross/PicrossView.kt)
- [https://github.com/meltingscales/DrakonixPicrossAndroid/commit/61ace8a60722396c4da2fcab466feeb85b922ebb](https://github.com/meltingscales/DrakonixPicrossAndroid/commit/61ace8a60722396c4da2fcab466feeb85b922ebb)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/meltingscales/DrakonixPicrossAndroid

[Back to the awesome list](../../README.md)
