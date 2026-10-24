# King's Cup

> Verified game note.

![King's Cup screenshot placeholder](king-s-cup-placeholder.svg)

## At a glance

- **Score:** 6.9/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-24
- **Repository:** [https://github.com/ngfamclam-cpu/kings-cup](https://github.com/ngfamclam-cpu/kings-cup)
- **Evidence:** [direct model evidence](https://github.com/ngfamclam-cpu/kings-cup/commit/8be8550f03fda6f32e9c7aac3e5241f9ff469db7)
- **Live demo:** [open demo](https://ngfamclam-cpu.github.io/kings-cup/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

King's Cup without a deck of cards: web app + Android APK. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ngfamclam-cpu/kings-cup/blob/main/www/app.js](https://github.com/ngfamclam-cpu/kings-cup/blob/main/www/app.js)
- [https://github.com/ngfamclam-cpu/kings-cup/commit/8be8550f03fda6f32e9c7aac3e5241f9ff469db7](https://github.com/ngfamclam-cpu/kings-cup/commit/8be8550f03fda6f32e9c7aac3e5241f9ff469db7)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; https://github.com/ngfamclam-cpu/kings-cup

[Back to the awesome list](../../README.md)
