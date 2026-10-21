# VEXEL – Protokoll Null

> Verified game note.

![VEXEL – Protokoll Null screenshot placeholder](vexel-protokoll-null-placeholder.svg)

## At a glance

- **Score:** 8.1/10
- **Model:** Claude Opus 5.5
- **Technology:** C
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/patrickmoosmaier/Vexel](https://github.com/patrickmoosmaier/Vexel)
- **Evidence:** [direct model evidence](https://github.com/patrickmoosmaier/Vexel/commit/fed19e99d7c2e222f86a48a37d28fff216272e65)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Ein eigenständiges Monster-Sammel-RPG für den DS (Homebrew-ROM VEXEL.nds), läuft im Delta-Emulator. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/patrickmoosmaier/Vexel/blob/main/source/gen_mon.c](https://github.com/patrickmoosmaier/Vexel/blob/main/source/gen_mon.c)
- [https://github.com/patrickmoosmaier/Vexel/commit/fed19e99d7c2e222f86a48a37d28fff216272e65](https://github.com/patrickmoosmaier/Vexel/commit/fed19e99d7c2e222f86a48a37d28fff216272e65)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/patrickmoosmaier/Vexel

[Back to the awesome list](../../README.md)
