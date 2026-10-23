# Kasserine

> Verified game note.

![Kasserine screenshot placeholder](kasserine-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Opus 5.5
- **Technology:** Java
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/saedarm/Kasserine](https://github.com/saedarm/Kasserine)
- **Evidence:** [direct model evidence](https://github.com/saedarm/Kasserine/commit/cb3980dfd72ac8ee10bd9d1c190851ef7b27c80d)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A greybox twin-stick action roguelike set in Tunisia, February 1943. You're one GI holding the south mouth of a canyon while the Afrika Korps pushes down it. A desktop game built with libGDX for Windows, Mac and Linux. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/saedarm/Kasserine/blob/main/core/src/main/java/com/saedarm/kasserine/Kasserine.java](https://github.com/saedarm/Kasserine/blob/main/core/src/main/java/com/saedarm/kasserine/Kasserine.java)
- [https://github.com/saedarm/Kasserine/commit/cb3980dfd72ac8ee10bd9d1c190851ef7b27c80d](https://github.com/saedarm/Kasserine/commit/cb3980dfd72ac8ee10bd9d1c190851ef7b27c80d)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/saedarm/Kasserine

[Back to the awesome list](../../README.md)
