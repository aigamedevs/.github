# Morrowlight

> Verified game note.

![Morrowlight screenshot](https://raw.githubusercontent.com/Attacktive/morrowlight/main/store/images/morrowlight-garden.webp)

## At a glance

- **Score:** 6.9/10
- **Screenshot rating:** 4.4/10 ([manually reviewed image](https://github.com/Attacktive/morrowlight/blob/main/store/images/morrowlight-garden.webp)). Treat this as visual review only; do not infer a playtest.
- **Model:** GPT-6.1 Sol, GPT-6 Astra
- **Technology:** Kotlin
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/Attacktive/morrowlight](https://github.com/Attacktive/morrowlight)
- **Evidence:** [direct model evidence](https://github.com/Attacktive/morrowlight/commit/37c93f44f260c6ddd7f1ab99b6046b7045480208)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Attacktive/morrowlight/blob/main/store/images/morrowlight-garden.webp) — 📸 4.4/10 · manual visual review · Use this frame for the game-level score. Portrait incremental screen with a glowing tree island and progress panel; minimal.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A native Android incremental game about bringing a floating garden back to life. Start with a single ember, gather Glow, and grow a home for the stars. Commit carries an exact GPT-6.1 Sol / GPT-6 Astra co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Attacktive/morrowlight/blob/main/app/src/main/kotlin/xyz/attacktive/morrowlight/ui/Morrowlight.kt](https://github.com/Attacktive/morrowlight/blob/main/app/src/main/kotlin/xyz/attacktive/morrowlight/ui/Morrowlight.kt)
- [https://github.com/Attacktive/morrowlight/commit/37c93f44f260c6ddd7f1ab99b6046b7045480208](https://github.com/Attacktive/morrowlight/commit/37c93f44f260c6ddd7f1ab99b6046b7045480208)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/Attacktive/morrowlight

[Back to the awesome list](../../README.md)
