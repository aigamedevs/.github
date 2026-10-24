# Accomplice

> Verified game note.

![Accomplice screenshot](https://raw.githubusercontent.com/kinnuworks/accomplice/master/apps/echo-sim/screenshots/out/01-home.png)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 3.8/10 ([manually reviewed image](https://github.com/kinnuworks/accomplice/blob/master/apps/echo-sim/screenshots/out/01-home.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-24
- **Repository:** [https://github.com/kinnuworks/accomplice](https://github.com/kinnuworks/accomplice)
- **Evidence:** [direct model evidence](https://github.com/kinnuworks/accomplice/commit/f47befd60b3ab000537cd00ea35f09467082cf75)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/kinnuworks/accomplice/blob/master/apps/echo-sim/screenshots/out/01-home.png) — 📸 3.8/10 · manual visual review · Use this frame for the game-level score. TV app home screen with text cards; mostly interface.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A murder-mystery party game for Fire TV where one of your friends is secretly helping the killer. Phones as controllers, AI suspects you question out loud, an Alexa+ add-on, deployed on AWS. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/kinnuworks/accomplice/blob/master/apps/server/src/room.ts](https://github.com/kinnuworks/accomplice/blob/master/apps/server/src/room.ts)
- [https://github.com/kinnuworks/accomplice/commit/f47befd60b3ab000537cd00ea35f09467082cf75](https://github.com/kinnuworks/accomplice/commit/f47befd60b3ab000537cd00ea35f09467082cf75)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; https://github.com/kinnuworks/accomplice

[Back to the awesome list](../../README.md)
