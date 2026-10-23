# Tap Duel

> Verified game note.

![Tap Duel screenshot placeholder](tap-duel-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Opus 5.5
- **Technology:** Flutter, Dart
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/TechNaom/tap-duel](https://github.com/TechNaom/tap-duel)
- **Evidence:** [direct model evidence](https://github.com/TechNaom/tap-duel/commit/cd7bbf77e8d3f52b10e9ecb05b6fbf798cdf6ddf)
- **Live demo:** [open demo](https://technaom.github.io/tap-duel/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Two-player tap race game in Flutter - Kohli vs Rohit, first to 1000. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/TechNaom/tap-duel/blob/main/lib/ui/player_panel.dart](https://github.com/TechNaom/tap-duel/blob/main/lib/ui/player_panel.dart)
- [https://github.com/TechNaom/tap-duel/commit/cd7bbf77e8d3f52b10e9ecb05b6fbf798cdf6ddf](https://github.com/TechNaom/tap-duel/commit/cd7bbf77e8d3f52b10e9ecb05b6fbf798cdf6ddf)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/TechNaom/tap-duel

[Back to the awesome list](../../README.md)
