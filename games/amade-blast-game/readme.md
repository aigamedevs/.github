# amade-blast-game

> Verified game note.

![amade-blast-game screenshot placeholder](amade-blast-game-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** Java, React
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/datazuul/amade-blast-game](https://github.com/datazuul/amade-blast-game)
- **Evidence:** [direct model evidence](https://github.com/datazuul/amade-blast-game/commit/12eeffa38c6de5b87f916085103245b57fd6177c)
- **Live demo:** [open demo](https://datazuul.github.io/amade-game-engine/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

The keys can be changed in ~/.config/amadeos/blast/blast.properties, with the names Java gives them, several separated by spaces. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/datazuul/amade-blast-game/blob/main/src/main/java/eu/amadeos/games/blast/ui/game/BlastPainter.java](https://github.com/datazuul/amade-blast-game/blob/main/src/main/java/eu/amadeos/games/blast/ui/game/BlastPainter.java)
- [https://github.com/datazuul/amade-blast-game/commit/12eeffa38c6de5b87f916085103245b57fd6177c](https://github.com/datazuul/amade-blast-game/commit/12eeffa38c6de5b87f916085103245b57fd6177c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/datazuul/amade-blast-game

[Back to the awesome list](../../README.md)
