# RideIdle

> Verified game note.

![RideIdle screenshot placeholder](rideidle-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Sonnet 5.5
- **Technology:** PHP
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/KenjiWriter/RideIdle](https://github.com/KenjiWriter/RideIdle)
- **Evidence:** [direct model evidence](https://github.com/KenjiWriter/RideIdle/commit/90977e023f4ffb7eff50ad45616d283dbe653502)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Przeglądarkowa gra idle o wyścigach (PWA, później aplikacje mobilne przez Capacitor), zbudowana jako dane sterowany „silnik”, który da się przenieść na inny świat (np. statki kosmiczne). Gracz odbudowuje wraki, kupuje coraz lepsze auta, rywalizuje w… Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/KenjiWriter/RideIdle/blob/main/api/resources/views/welcome.blade.php](https://github.com/KenjiWriter/RideIdle/blob/main/api/resources/views/welcome.blade.php)
- [https://github.com/KenjiWriter/RideIdle/commit/90977e023f4ffb7eff50ad45616d283dbe653502](https://github.com/KenjiWriter/RideIdle/commit/90977e023f4ffb7eff50ad45616d283dbe653502)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/KenjiWriter/RideIdle

[Back to the awesome list](../../README.md)
