# Verto

> Verified game note.

![Verto screenshot placeholder](verto-placeholder.svg)

## At a glance

- **Score:** 7.8/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** Unity, C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/swear01/Verto](https://github.com/swear01/Verto)
- **Evidence:** [direct model evidence](https://github.com/swear01/Verto/commit/1aeb93a83303b470333faab7adc839885430b222)
- **Live demo:** [open demo](https://swear01.itch.io/phase)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Verto — a color-phase pixel platformer with an in-game level editor (Unity 6000.4.7f1). The jam version shipped as PHASE: https://swear01.itch.io/phase. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/swear01/Verto/blob/main/Assets/Phase/Runtime/PhaseEditor.cs](https://github.com/swear01/Verto/blob/main/Assets/Phase/Runtime/PhaseEditor.cs)
- [https://github.com/swear01/Verto/commit/1aeb93a83303b470333faab7adc839885430b222](https://github.com/swear01/Verto/commit/1aeb93a83303b470333faab7adc839885430b222)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/swear01/Verto

[Back to the awesome list](../../README.md)
