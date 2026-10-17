# AVA Castles of Dr. Creep

> Verified game note.

![AVA Castles of Dr. Creep screenshot](https://raw.githubusercontent.com/Harlock123/AVACastlesOfDrCreep/main/Images/AVACastlesOfDrCreep-gatehouse.png)

## At a glance

- **Score:** 7.2/10
- **Screenshot rating:** 5.4/10 ([manually reviewed image](https://github.com/Harlock123/AVACastlesOfDrCreep/blob/main/Images/AVACastlesOfDrCreep-gatehouse.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/Harlock123/AVACastlesOfDrCreep](https://github.com/Harlock123/AVACastlesOfDrCreep)
- **Evidence:** [direct model evidence](https://github.com/Harlock123/AVACastlesOfDrCreep/commit/4e53c48e6ef2838eda54871db45860597b1fafc6)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Harlock123/AVACastlesOfDrCreep/blob/main/Images/AVACastlesOfDrCreep-gatehouse.png) — 📸 5.4/10 · manual visual review · Use this frame for the game-level score. Dark castle room with ladder, door and tiny character; faithful but sparse.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

AVA Castles of Dr. Creep: a puzzle-platformer of castle escapes after the 1984 C64 classic. Seven castles, a synthesised speaking welcome, two players. C# / .NET 10 / Avalonia. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Harlock123/AVACastlesOfDrCreep/blob/main/src/AVACastlesOfDrCreep/Views/GameCanvas.Draw.cs](https://github.com/Harlock123/AVACastlesOfDrCreep/blob/main/src/AVACastlesOfDrCreep/Views/GameCanvas.Draw.cs)
- [https://github.com/Harlock123/AVACastlesOfDrCreep/commit/4e53c48e6ef2838eda54871db45860597b1fafc6](https://github.com/Harlock123/AVACastlesOfDrCreep/commit/4e53c48e6ef2838eda54871db45860597b1fafc6)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/Harlock123/AVACastlesOfDrCreep

[Back to the awesome list](../../README.md)
