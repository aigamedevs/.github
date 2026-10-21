# Sorcerer's Maze PC port

> Verified game note.

![Sorcerer's Maze PC port screenshot placeholder](sorcerer-s-maze-pc-port-placeholder.svg)

## At a glance

- **Score:** 8.1/10
- **Model:** Claude Opus 5.5
- **Technology:** C
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/Bitsandbreakpoints/sorcerers-maze-psx-pc-recomp](https://github.com/Bitsandbreakpoints/sorcerers-maze-psx-pc-recomp)
- **Evidence:** [direct model evidence](https://github.com/Bitsandbreakpoints/sorcerers-maze-psx-pc-recomp/commit/82e2aef4ba9e124721c9805369894be30e24446a)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Native Windows port of the PlayStation game Sorcerer's Maze - bring your own disc. No game files included. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Bitsandbreakpoints/sorcerers-maze-psx-pc-recomp/blob/main/source/third_party/libchdr/deps/zstd-1.5.7/zstddeclib.c](https://github.com/Bitsandbreakpoints/sorcerers-maze-psx-pc-recomp/blob/main/source/third_party/libchdr/deps/zstd-1.5.7/zstddeclib.c)
- [https://github.com/Bitsandbreakpoints/sorcerers-maze-psx-pc-recomp/commit/82e2aef4ba9e124721c9805369894be30e24446a](https://github.com/Bitsandbreakpoints/sorcerers-maze-psx-pc-recomp/commit/82e2aef4ba9e124721c9805369894be30e24446a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/Bitsandbreakpoints/sorcerers-maze-psx-pc-recomp

[Back to the awesome list](../../README.md)
