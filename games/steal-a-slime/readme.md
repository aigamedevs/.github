# Steal a Slime! — движок «фабрики плейсов»

> Verified game note.

![Steal a Slime! — движок «фабрики плейсов» screenshot placeholder](steal-a-slime-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** Roblox, Luau
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/ddepqwee/steal-a-slime](https://github.com/ddepqwee/steal-a-slime)
- **Evidence:** [direct model evidence](https://github.com/ddepqwee/steal-a-slime/commit/ffff7f9dc166c3fdda6a86456ee0f5f29514bff9)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Игра целиком в коде: карта, слаймы, UI, экономика, монетизация. Новый плейс на этом движке =. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ddepqwee/steal-a-slime/blob/main/src/client/HUD.luau](https://github.com/ddepqwee/steal-a-slime/blob/main/src/client/HUD.luau)
- [https://github.com/ddepqwee/steal-a-slime/commit/ffff7f9dc166c3fdda6a86456ee0f5f29514bff9](https://github.com/ddepqwee/steal-a-slime/commit/ffff7f9dc166c3fdda6a86456ee0f5f29514bff9)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/ddepqwee/steal-a-slime

[Back to the awesome list](../../README.md)
