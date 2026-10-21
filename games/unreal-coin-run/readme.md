# unreal-coin-run

> Verified game note.

![unreal-coin-run screenshot placeholder](unreal-coin-run-placeholder.svg)

## At a glance

- **Score:** 6.8/10
- **Model:** Claude Sonnet 5.5
- **Technology:** Unreal Engine, C++
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/Sup3rMar10/unreal-coin-run](https://github.com/Sup3rMar10/unreal-coin-run)
- **Evidence:** [direct model evidence](https://github.com/Sup3rMar10/unreal-coin-run/commit/965966fef821439ed95115aaacb8a1193842f6f3)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Small Unreal Engine 5.5 arcade game (Coin Run) in C++ with an engine-free, unit-tested rules core. Never opened in Unreal; see README and STEPS.md. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Sup3rMar10/unreal-coin-run/blob/main/Source/CoinRun/Game/CoinRunDirector.cpp](https://github.com/Sup3rMar10/unreal-coin-run/blob/main/Source/CoinRun/Game/CoinRunDirector.cpp)
- [https://github.com/Sup3rMar10/unreal-coin-run/commit/965966fef821439ed95115aaacb8a1193842f6f3](https://github.com/Sup3rMar10/unreal-coin-run/commit/965966fef821439ed95115aaacb8a1193842f6f3)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/Sup3rMar10/unreal-coin-run

[Back to the awesome list](../../README.md)
