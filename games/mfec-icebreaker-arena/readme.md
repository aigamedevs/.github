# MFEC IceBreaker Arena

> Verified game note.

![MFEC IceBreaker Arena screenshot](https://raw.githubusercontent.com/sakanarm/IcebreakerArena/main/docs/screenshots/14-stage-lobby.png)

## At a glance

- **Score:** 7.5/10
- **Screenshot rating:** 3.8/10 ([manually reviewed image](https://github.com/sakanarm/IcebreakerArena/blob/main/docs/screenshots/14-stage-lobby.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-21
- **Repository:** [https://github.com/sakanarm/IcebreakerArena](https://github.com/sakanarm/IcebreakerArena)
- **Evidence:** [direct model evidence](https://github.com/sakanarm/IcebreakerArena/commit/8ebba0a3a505e9f303fd14f1fb234949a74766f2)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/sakanarm/IcebreakerArena/blob/main/docs/screenshots/14-stage-lobby.png) — 📸 3.8/10 · manual visual review · Use this frame for the game-level score. Join-code lobby with a large PIN, QR code and a cloud of player names; a lobby screen, not gameplay.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

เกม Icebreaker / Quiz แบบเล่นสดสำหรับทีม MFEC ผู้จัดสร้างคำถามเองแบ่งเป็นหลายด่าน เปิดห้องขึ้นจอใหญ่ ทุกคนสแกน QR แล้วตอบจากมือถือของตัวเอง แข่งเก็บแต้มแบบเรียลไทม์จนถึงโพเดียม. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/sakanarm/IcebreakerArena/blob/main/apps/web/src/components/editor/EditorApp.tsx](https://github.com/sakanarm/IcebreakerArena/blob/main/apps/web/src/components/editor/EditorApp.tsx)
- [https://github.com/sakanarm/IcebreakerArena/commit/8ebba0a3a505e9f303fd14f1fb234949a74766f2](https://github.com/sakanarm/IcebreakerArena/commit/8ebba0a3a505e9f303fd14f1fb234949a74766f2)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-17T01:00Z..2026-10-21T01:00Z (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-17T00:00Z; https://github.com/sakanarm/IcebreakerArena

[Back to the awesome list](../../README.md)
