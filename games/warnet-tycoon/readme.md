# Warnet Tycoon

> Verified game note.

![Warnet Tycoon screenshot placeholder](warnet-tycoon-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/RafiAlaydrus/WarnetTycoon](https://github.com/RafiAlaydrus/WarnetTycoon)
- **Evidence:** [direct model evidence](https://github.com/RafiAlaydrus/WarnetTycoon/commit/a903ee559ed16c840f03a6b859004f984308e944)
- **Live demo:** [open demo](https://rafialaydrus.github.io/WarnetTycoon/)
- **Additional live link:** [open demo](https://rafialaydrus.github.io/WarnetTycoon/?debug=1)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

An idle and management game about running an Indonesian internet cafe. It is a static site (HTML, CSS, JS, no build step, no network calls) that installs on an iPhone as a home-screen app and runs with no connection at all. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/RafiAlaydrus/WarnetTycoon/blob/main/game.js](https://github.com/RafiAlaydrus/WarnetTycoon/blob/main/game.js)
- [https://github.com/RafiAlaydrus/WarnetTycoon/commit/a903ee559ed16c840f03a6b859004f984308e944](https://github.com/RafiAlaydrus/WarnetTycoon/commit/a903ee559ed16c840f03a6b859004f984308e944)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/RafiAlaydrus/WarnetTycoon

[Back to the awesome list](../../README.md)
