# Chroma Lines

> Verified game note.

![Chroma Lines screenshot placeholder](chroma-lines-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Phaser, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/mikeylambo/Chroma-Lines](https://github.com/mikeylambo/Chroma-Lines)
- **Evidence:** [direct model evidence](https://github.com/mikeylambo/Chroma-Lines/commit/99e9a1bf7f3a4b0991d52d3ee742cfc851e24d1a)
- **Live demo:** [open demo](https://chroma-lines-chi.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Arrow-escape logic puzzle on the SLU web shell (vendored, built from mikeylambo/Web-Game-Shell-v1.02 source). Phaser 3 board, DOM UI, WebAudio synth. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/mikeylambo/Chroma-Lines/blob/claude/tender-newton-bci6su/src/view/BoardScene.ts](https://github.com/mikeylambo/Chroma-Lines/blob/claude/tender-newton-bci6su/src/view/BoardScene.ts)
- [https://github.com/mikeylambo/Chroma-Lines/commit/99e9a1bf7f3a4b0991d52d3ee742cfc851e24d1a](https://github.com/mikeylambo/Chroma-Lines/commit/99e9a1bf7f3a4b0991d52d3ee742cfc851e24d1a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/mikeylambo/Chroma-Lines

[Back to the awesome list](../../README.md)
