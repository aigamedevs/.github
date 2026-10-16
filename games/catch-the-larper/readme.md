# Catch The Larper

> Verified game note.

![Catch The Larper screenshot placeholder](catch-the-larper-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, React, Node.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-16
- **Repository:** [https://github.com/ShinjiK1/Social-Deduction-Game-NLP-Project](https://github.com/ShinjiK1/Social-Deduction-Game-NLP-Project)
- **Evidence:** [direct model evidence](https://github.com/ShinjiK1/Social-Deduction-Game-NLP-Project/commit/2997547713b69ee582dd8574956681fe19de2a93)
- **Live demo:** [open demo](https://catchthelarper.com)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Online social-deduction word game (client plus room server): everyone but the larper gets the secret word, players give short hints and vote; hint data is also collected for a classifier. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected only; no playtest.

### Gameplay source

- [https://github.com/ShinjiK1/Social-Deduction-Game-NLP-Project/blob/main/server/src/rooms.js](https://github.com/ShinjiK1/Social-Deduction-Game-NLP-Project/blob/main/server/src/rooms.js)
- [https://github.com/ShinjiK1/Social-Deduction-Game-NLP-Project/commit/2997547713b69ee582dd8574956681fe19de2a93](https://github.com/ShinjiK1/Social-Deduction-Game-NLP-Project/commit/2997547713b69ee582dd8574956681fe19de2a93)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-15..2026-10-16 (6-hour UTC partitions) joined to repositories created after 2026-10-14T17:00Z; https://github.com/ShinjiK1/Social-Deduction-Game-NLP-Project

[Back to the awesome list](../../README.md)
