# Neuro Reflex

> Verified game note.

![Neuro Reflex screenshot placeholder](neuro-reflex-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-16
- **Repository:** [https://github.com/paatsinsuwan/neuro-reflex-game](https://github.com/paatsinsuwan/neuro-reflex-game)
- **Evidence:** [direct model evidence](https://github.com/paatsinsuwan/neuro-reflex-game/commit/5a96a54149bafee46701ad4c752e71c1cdd2724f)
- **Live demo:** [open demo](https://paatsinsuwan.github.io/neuro-reflex-game/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Stroop-effect reaction game: press the colour matching the ink or the word before the timer runs out; game hook and charts in js/. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected only; no playtest.

### Gameplay source

- [https://github.com/paatsinsuwan/neuro-reflex-game/blob/main/js/hooks/useStroopGame.js](https://github.com/paatsinsuwan/neuro-reflex-game/blob/main/js/hooks/useStroopGame.js)
- [https://github.com/paatsinsuwan/neuro-reflex-game/commit/5a96a54149bafee46701ad4c752e71c1cdd2724f](https://github.com/paatsinsuwan/neuro-reflex-game/commit/5a96a54149bafee46701ad4c752e71c1cdd2724f)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-15..2026-10-16 (6-hour UTC partitions) joined to repositories created after 2026-10-14T17:00Z; https://github.com/paatsinsuwan/neuro-reflex-game

[Back to the awesome list](../../README.md)
