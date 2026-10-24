# Zhirui Sucks At Cards

> Verified game note.

![Zhirui Sucks At Cards screenshot placeholder](zhirui-sucks-at-cards-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-24
- **Repository:** [https://github.com/lohhaoyuan/bridge](https://github.com/lohhaoyuan/bridge)
- **Evidence:** [direct model evidence](https://github.com/lohhaoyuan/bridge/commit/c3579e7bc8dfeb387b3d121dc40a25a2435214f1)
- **Live demo:** [open demo](https://draysucksatbridge.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Vue 3 + Vite frontend, Express API, Turso (hosted SQLite) database. Deploys to Vercel. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/lohhaoyuan/bridge/blob/main/server/app.js](https://github.com/lohhaoyuan/bridge/blob/main/server/app.js)
- [https://github.com/lohhaoyuan/bridge/commit/c3579e7bc8dfeb387b3d121dc40a25a2435214f1](https://github.com/lohhaoyuan/bridge/commit/c3579e7bc8dfeb387b3d121dc40a25a2435214f1)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; https://github.com/lohhaoyuan/bridge

[Back to the awesome list](../../README.md)
