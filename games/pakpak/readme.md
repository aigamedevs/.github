# PakPak

> Verified game note.

![PakPak screenshot](https://raw.githubusercontent.com/deguzmanshanmichael/pakpakGame/main/site/img/collection.png)

## At a glance

- **Score:** 7.4/10
- **Screenshot rating:** 5.0/10 ([manually reviewed image](https://github.com/deguzmanshanmichael/pakpakGame/blob/main/site/img/collection.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Kotlin, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/deguzmanshanmichael/pakpakGame](https://github.com/deguzmanshanmichael/pakpakGame)
- **Evidence:** [direct model evidence](https://github.com/deguzmanshanmichael/pakpakGame/commit/8eacf897d6bb013115893a52bdd952321e90b77c)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/deguzmanshanmichael/pakpakGame/blob/main/site/img/collection.png) — 📸 5.0/10 · manual visual review · Use this frame for the game-level score. Pixel collection book grid on narrow phone screen.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

An original pixel-art flapping game for Android and iOS with Endless and Adventure modes, a 133-piece collection book, and an online layer for friends, messages and trading. The online layer runs on a small Node.js backend. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/deguzmanshanmichael/pakpakGame/blob/main/mobile/shared/src/commonMain/kotlin/com/shan/pakpak/scenes/PlayScene.kt](https://github.com/deguzmanshanmichael/pakpakGame/blob/main/mobile/shared/src/commonMain/kotlin/com/shan/pakpak/scenes/PlayScene.kt)
- [https://github.com/deguzmanshanmichael/pakpakGame/commit/8eacf897d6bb013115893a52bdd952321e90b77c](https://github.com/deguzmanshanmichael/pakpakGame/commit/8eacf897d6bb013115893a52bdd952321e90b77c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/deguzmanshanmichael/pakpakGame

[Back to the awesome list](../../README.md)
