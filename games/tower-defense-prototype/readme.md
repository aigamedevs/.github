# Tower Defense prototype

> Verified game note.

![Tower Defense prototype screenshot placeholder](tower-defense-prototype-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Opus 5.5
- **Technology:** Unity, C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/MagicMiikka/TowerDefense](https://github.com/MagicMiikka/TowerDefense)
- **Evidence:** [direct model evidence](https://github.com/MagicMiikka/TowerDefense/commit/934dfc7356422e71f96b37217c97f73cf011b5df)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A compact-grid mazing roguelite where the enemy evolves to counter your build. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/MagicMiikka/TowerDefense/blob/main/Packages/com.tdgame.core/Runtime/Sim/SiteSim.cs](https://github.com/MagicMiikka/TowerDefense/blob/main/Packages/com.tdgame.core/Runtime/Sim/SiteSim.cs)
- [https://github.com/MagicMiikka/TowerDefense/commit/934dfc7356422e71f96b37217c97f73cf011b5df](https://github.com/MagicMiikka/TowerDefense/commit/934dfc7356422e71f96b37217c97f73cf011b5df)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/MagicMiikka/TowerDefense

[Back to the awesome list](../../README.md)
