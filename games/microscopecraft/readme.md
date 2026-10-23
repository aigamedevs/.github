# MicroscopeCraft

> Verified game note.

![MicroscopeCraft screenshot](https://raw.githubusercontent.com/yijiang1/MicroscopeCraft/main/docs/thumbnail.png)

## At a glance

- **Score:** 7.9/10
- **Screenshot rating:** 6.2/10 ([manually reviewed image](https://github.com/yijiang1/MicroscopeCraft/blob/main/docs/thumbnail.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/yijiang1/MicroscopeCraft](https://github.com/yijiang1/MicroscopeCraft)
- **Evidence:** [direct model evidence](https://github.com/yijiang1/MicroscopeCraft/commit/5c154630854f5f06168ad34929bd690e94ec31b5)
- **Live demo:** [open demo](https://yijiang1.github.io/MicroscopeCraft/)
- **Additional live link:** [open demo](https://llmhackathon.github.io/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/yijiang1/MicroscopeCraft/blob/main/docs/thumbnail.png) — 📸 6.2/10 · manual visual review · Use this frame for the game-level score. Pixel-title promo with 3D microscope building and scale icons.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

You start on a university campus with nothing but your own eyes. Gather sand, iron and copper, craft your first hand lens, and look again: the leaf in front of you suddenly has veins. Keep building, from a compound microscope to fluorescence, a transmission… Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/yijiang1/MicroscopeCraft/blob/main/src/world/campus.ts](https://github.com/yijiang1/MicroscopeCraft/blob/main/src/world/campus.ts)
- [https://github.com/yijiang1/MicroscopeCraft/commit/5c154630854f5f06168ad34929bd690e94ec31b5](https://github.com/yijiang1/MicroscopeCraft/commit/5c154630854f5f06168ad34929bd690e94ec31b5)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/yijiang1/MicroscopeCraft

[Back to the awesome list](../../README.md)
