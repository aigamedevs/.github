# Amarna Letters

> Verified game note.

![Amarna Letters screenshot placeholder](amarna-letters-placeholder.svg)

## At a glance

- **Score:** 8.0/10
- **Model:** Claude Opus 5.5
- **Technology:** C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/HaakTuah/amarna-letters](https://github.com/HaakTuah/amarna-letters)
- **Evidence:** [direct model evidence](https://github.com/HaakTuah/amarna-letters/commit/12ed860c586f4c241bd1ef03e3ab00ba1582ae0e)
- **Live demo:** [open demo](https://haaktuah.github.io/amarna-letters/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A strategy game of the Late Bronze Age Great Kings, where every word passes through an envoy. C# engine, Blazor WebAssembly, Claude-played kings and envoys. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/HaakTuah/amarna-letters/blob/main/src/Amarna.Llm/Prompts.cs](https://github.com/HaakTuah/amarna-letters/blob/main/src/Amarna.Llm/Prompts.cs)
- [https://github.com/HaakTuah/amarna-letters/commit/12ed860c586f4c241bd1ef03e3ab00ba1582ae0e](https://github.com/HaakTuah/amarna-letters/commit/12ed860c586f4c241bd1ef03e3ab00ba1582ae0e)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/HaakTuah/amarna-letters

[Back to the awesome list](../../README.md)
