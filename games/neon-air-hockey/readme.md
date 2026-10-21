# Neon Air Hockey

> Verified game note.

![Neon Air Hockey screenshot placeholder](neon-air-hockey-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/VicArr786/HockeygameApple](https://github.com/VicArr786/HockeygameApple)
- **Evidence:** [direct model evidence](https://github.com/VicArr786/HockeygameApple/commit/a3c8b6bc70524b3c1933b85a789e3b5a6cbfb598)
- **Live demo:** [open demo](https://hockeygame-one.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Arcade air hockey for iPhone and iPad (Android works too). Drag your paddle. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/VicArr786/HockeygameApple/blob/main/src/screens/GameScreen.tsx](https://github.com/VicArr786/HockeygameApple/blob/main/src/screens/GameScreen.tsx)
- [https://github.com/VicArr786/HockeygameApple/commit/a3c8b6bc70524b3c1933b85a789e3b5a6cbfb598](https://github.com/VicArr786/HockeygameApple/commit/a3c8b6bc70524b3c1933b85a789e3b5a6cbfb598)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/VicArr786/HockeygameApple

[Back to the awesome list](../../README.md)
