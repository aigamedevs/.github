# Burn Rate

> Verified game note.

![Burn Rate screenshot](https://raw.githubusercontent.com/wowlocal/burn-rate/main/docs/screenshots/founders.png)

## At a glance

- **Score:** 7.1/10
- **Screenshot rating:** 5.6/10 ([manually reviewed image](https://github.com/wowlocal/burn-rate/blob/main/docs/screenshots/founders.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Python
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-24
- **Repository:** [https://github.com/wowlocal/burn-rate](https://github.com/wowlocal/burn-rate)
- **Evidence:** [direct model evidence](https://github.com/wowlocal/burn-rate/commit/1faff16a530d1e34657aed0578dbbcdbb7349d80)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/wowlocal/burn-rate/blob/main/docs/screenshots/founders.png) — 📸 5.6/10 · manual visual review · Use this frame for the game-level score. Pixel character-select grid of founder portraits; lively art, menu screen.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

An experimental 2D brawler on the Randori engine: fictional Silicon Valley AI-startup founders fight. Art made with Codex CLI image generation, sounds and music synthesized. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/wowlocal/burn-rate/blob/main/tools/content/interface.py](https://github.com/wowlocal/burn-rate/blob/main/tools/content/interface.py)
- [https://github.com/wowlocal/burn-rate/commit/1faff16a530d1e34657aed0578dbbcdbb7349d80](https://github.com/wowlocal/burn-rate/commit/1faff16a530d1e34657aed0578dbbcdbb7349d80)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; https://github.com/wowlocal/burn-rate

[Back to the awesome list](../../README.md)
