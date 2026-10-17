# Blind Tape

> Verified game note.

![Blind Tape screenshot placeholder](blind-tape-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/lanwakacsus/blind-tape](https://github.com/lanwakacsus/blind-tape)
- **Evidence:** [direct model evidence](https://github.com/lanwakacsus/blind-tape/commit/814c300356e59d32ebf113aafc81c45f87248913)
- **Live demo:** [open demo](https://blind-tape-psi.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Real-time trading game with a built-in backtester and a daily challenge. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/lanwakacsus/blind-tape/blob/main/src/ui/play.ts](https://github.com/lanwakacsus/blind-tape/blob/main/src/ui/play.ts)
- [https://github.com/lanwakacsus/blind-tape/commit/814c300356e59d32ebf113aafc81c45f87248913](https://github.com/lanwakacsus/blind-tape/commit/814c300356e59d32ebf113aafc81c45f87248913)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/lanwakacsus/blind-tape

[Back to the awesome list](../../README.md)
