# Bắt Bài

> Verified game note.

![Bắt Bài screenshot placeholder](bat-bai-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-24
- **Repository:** [https://github.com/dopg-vbee/bat-bai](https://github.com/dopg-vbee/bat-bai)
- **Evidence:** [direct model evidence](https://github.com/dopg-vbee/bat-bai/commit/814ddfd6f508126d604dff52e2499fb15a420cee)
- **Live demo:** [open demo](https://batbai.onrender.com)
- **Additional live link:** [open demo](https://googlefonts.github.io/noto-emoji-animation/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Bắt Bài – game party nghe lời đoán tên bài hát, chơi realtime qua trình duyệt. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/dopg-vbee/bat-bai/blob/main/src/server/game/room.ts](https://github.com/dopg-vbee/bat-bai/blob/main/src/server/game/room.ts)
- [https://github.com/dopg-vbee/bat-bai/commit/814ddfd6f508126d604dff52e2499fb15a420cee](https://github.com/dopg-vbee/bat-bai/commit/814ddfd6f508126d604dff52e2499fb15a420cee)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; https://github.com/dopg-vbee/bat-bai

[Back to the awesome list](../../README.md)
