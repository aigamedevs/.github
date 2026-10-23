# PlayTogether

> Verified game note.

![PlayTogether screenshot](https://raw.githubusercontent.com/nguyensiclc/PlayTogether/main/docs/design/co-tuong/mockup-1.jpg)

## At a glance

- **Score:** 7.5/10
- **Screenshot rating:** 6.0/10 ([manually reviewed image](https://github.com/nguyensiclc/PlayTogether/blob/main/docs/design/co-tuong/mockup-1.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-23
- **Repository:** [https://github.com/nguyensiclc/PlayTogether](https://github.com/nguyensiclc/PlayTogether)
- **Evidence:** [direct model evidence](https://github.com/nguyensiclc/PlayTogether/commit/cd4380f44107fb96064c491f2f374ac7250d9502)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/nguyensiclc/PlayTogether/blob/main/docs/design/co-tuong/mockup-1.jpg) — 📸 6.0/10 · manual visual review · Use this frame for the game-level score. Xiangqi board with player cards and buttons on a warm parchment UI; tidy and readable.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Website chơi game chung nhiều người: tạo phòng → chọn game → gửi link mời bạn → chơi. Không cần đăng ký. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/nguyensiclc/PlayTogether/blob/main/packages/engine/co-vua/rules.ts](https://github.com/nguyensiclc/PlayTogether/blob/main/packages/engine/co-vua/rules.ts)
- [https://github.com/nguyensiclc/PlayTogether/commit/cd4380f44107fb96064c491f2f374ac7250d9502](https://github.com/nguyensiclc/PlayTogether/commit/cd4380f44107fb96064c491f2f374ac7250d9502)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-21T01:00Z..2026-10-23T01:00Z (20-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-20T01:00Z; https://github.com/nguyensiclc/PlayTogether

[Back to the awesome list](../../README.md)
