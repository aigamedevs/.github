# ฟังแป๊บ — เกมทายเพลงไทย (MVP)

> Verified game note.

![ฟังแป๊บ — เกมทายเพลงไทย (MVP) screenshot placeholder](mvp-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/PuviwatS/fang-paep](https://github.com/PuviwatS/fang-paep)
- **Evidence:** [direct model evidence](https://github.com/PuviwatS/fang-paep/commit/8b9f63e860cd188bbe88e44e0e669623eebde717)
- **Live demo:** [open demo](https://fang-paep.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

เกมแนว Songless สำหรับเพลงไทย ฟังท่อนสั้น 0.5 วินาที ทายผิดหรือกดข้ามจะได้ฟังยาวขึ้น. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/PuviwatS/fang-paep/blob/main/src/lib/storage.ts](https://github.com/PuviwatS/fang-paep/blob/main/src/lib/storage.ts)
- [https://github.com/PuviwatS/fang-paep/commit/8b9f63e860cd188bbe88e44e0e669623eebde717](https://github.com/PuviwatS/fang-paep/commit/8b9f63e860cd188bbe88e44e0e669623eebde717)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/PuviwatS/fang-paep

[Back to the awesome list](../../README.md)
