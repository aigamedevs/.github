# Spellmerge

> Verified game note.

![Spellmerge screenshot placeholder](spellmerge-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/peterdk31/spellmerge](https://github.com/peterdk31/spellmerge)
- **Evidence:** [direct model evidence](https://github.com/peterdk31/spellmerge/commit/d90375eb12608c28db17a7107d912f6324783107)
- **Live demo:** [open demo](https://peterdk31.github.io/spellmerge/)
- **Additional live link:** [open demo](https://peterdk31.github.io/spellmerge/play/)
- **Additional live link:** [open demo](https://peterdk31.github.io/spellmerge/nightly/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Merge spells. Cause chaos. Together. A 1-4 player co-op roguelite built by Claude and the community. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/peterdk31/spellmerge/blob/main/ci/smbot/session.py](https://github.com/peterdk31/spellmerge/blob/main/ci/smbot/session.py)
- [https://github.com/peterdk31/spellmerge/commit/d90375eb12608c28db17a7107d912f6324783107](https://github.com/peterdk31/spellmerge/commit/d90375eb12608c28db17a7107d912f6324783107)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/peterdk31/spellmerge

[Back to the awesome list](../../README.md)
