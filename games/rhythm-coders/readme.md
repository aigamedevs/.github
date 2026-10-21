# Rhythm Coders

> Verified game note.

![Rhythm Coders screenshot placeholder](rhythm-coders-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/SametAylak/ludum-dare-60](https://github.com/SametAylak/ludum-dare-60)
- **Evidence:** [direct model evidence](https://github.com/SametAylak/ludum-dare-60/commit/9bc0173e6a7391aea3e6dce0c630a7a8a30372fd)
- **Live demo:** [open demo](https://sametaylak.github.io/ludum-dare-60/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

An Incredibox-style music game where old computer parts are the band. Drag a hard drive, floppy drive, modem, CRT monitor or speech chip onto the desk and each one adds its own loop to the mix. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/SametAylak/ludum-dare-60/blob/main/js/bonus/boot/music.js](https://github.com/SametAylak/ludum-dare-60/blob/main/js/bonus/boot/music.js)
- [https://github.com/SametAylak/ludum-dare-60/commit/9bc0173e6a7391aea3e6dce0c630a7a8a30372fd](https://github.com/SametAylak/ludum-dare-60/commit/9bc0173e6a7391aea3e6dce0c630a7a8a30372fd)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/SametAylak/ludum-dare-60

[Back to the awesome list](../../README.md)
