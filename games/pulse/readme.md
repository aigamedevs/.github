# Pulse

> Verified game note.

![Pulse screenshot](https://raw.githubusercontent.com/shwan-ps5/pulse/main/docs/media/pulse-fractal-triangle.jpg)

## At a glance

- **Score:** 7.7/10
- **Screenshot rating:** 7.0/10 ([manually reviewed image](https://github.com/shwan-ps5/pulse/blob/main/docs/media/pulse-fractal-triangle.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Sonnet 5.5
- **Technology:** C++
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/shwan-ps5/pulse](https://github.com/shwan-ps5/pulse)
- **Evidence:** [direct model evidence](https://github.com/shwan-ps5/pulse/commit/948a7c09fa03259062cada9f0d0b6d7a7678fb5e)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/shwan-ps5/pulse/blob/main/docs/media/pulse-fractal-triangle.jpg) — 📸 7.0/10 · manual visual review · Use this frame for the game-level score. Neon rhythm lane with a glowing triangle target, coloured arrows, light beams and cubes; vivid and kinetic.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Beat Saber-style rhythm game for PS VR2 and Sense controllers on a jailbroken PS5: any MP3 becomes note maps. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/shwan-ps5/pulse/blob/main/render/fontatlas.h](https://github.com/shwan-ps5/pulse/blob/main/render/fontatlas.h)
- [https://github.com/shwan-ps5/pulse/commit/948a7c09fa03259062cada9f0d0b6d7a7678fb5e](https://github.com/shwan-ps5/pulse/commit/948a7c09fa03259062cada9f0d0b6d7a7678fb5e)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/shwan-ps5/pulse

[Back to the awesome list](../../README.md)
