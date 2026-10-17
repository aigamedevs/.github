# 楓嶺 · 回音鐘 Maple Ridge

> Verified game note.

![楓嶺 · 回音鐘 Maple Ridge screenshot placeholder](maple-ridge-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-17
- **Repository:** [https://github.com/austin410203/3d_wordpuzzle](https://github.com/austin410203/3d_wordpuzzle)
- **Evidence:** [direct model evidence](https://github.com/austin410203/3d_wordpuzzle/commit/6ad6fc8a3a161b86b0f91ba7d680e11a3f53a8aa)
- **Live demo:** [open demo](https://3dwordpuzzle.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

像素風(three.js 低解析度渲染 + 描邊)的解謎探險遊戲。回到過世爺爺的楓嶺,推石頭、釣魚、修水車、點古燈、闖山洞,登頂敲響回音鐘。. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/austin410203/3d_wordpuzzle/blob/main/src/game.js](https://github.com/austin410203/3d_wordpuzzle/blob/main/src/game.js)
- [https://github.com/austin410203/3d_wordpuzzle/commit/6ad6fc8a3a161b86b0f91ba7d680e11a3f53a8aa](https://github.com/austin410203/3d_wordpuzzle/commit/6ad6fc8a3a161b86b0f91ba7d680e11a3f53a8aa)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-16..2026-10-17 (1-hour Opus, 3-hour Sonnet, 6-hour other UTC partitions) joined to repositories created after 2026-10-16T00:00Z; https://github.com/austin410203/3d_wordpuzzle

[Back to the awesome list](../../README.md)
