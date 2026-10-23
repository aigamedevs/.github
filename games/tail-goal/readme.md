# TAIL GOAL

> Verified game note.

![TAIL GOAL screenshot placeholder](tail-goal-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/YashNirwan/tail-goal](https://github.com/YashNirwan/tail-goal)
- **Evidence:** [direct model evidence](https://github.com/YashNirwan/tail-goal/commit/a4e4ca90c88ddabc95a696999e99333ce63fd6cf)
- **Live demo:** [open demo](https://tail-goal.bc-server.workers.dev)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Score in their goal. Yours follows you. 2-4 player online car-football (three.js + Cloudflare Workers), built with OpenAI Codex + Claude. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/YashNirwan/tail-goal/blob/main/protos/tail-goal/render3d.ts](https://github.com/YashNirwan/tail-goal/blob/main/protos/tail-goal/render3d.ts)
- [https://github.com/YashNirwan/tail-goal/commit/a4e4ca90c88ddabc95a696999e99333ce63fd6cf](https://github.com/YashNirwan/tail-goal/commit/a4e4ca90c88ddabc95a696999e99333ce63fd6cf)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/YashNirwan/tail-goal

[Back to the awesome list](../../README.md)
