# VOID RUNNER

> Verified game note.

![VOID RUNNER screenshot](https://raw.githubusercontent.com/Arash1Kazemi/void-runner/main/circuit_preview.png)

## At a glance

- **Score:** 7.2/10
- **Screenshot rating:** 3.8/10 ([manually reviewed image](https://github.com/Arash1Kazemi/void-runner/blob/main/circuit_preview.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** C
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-24
- **Repository:** [https://github.com/Arash1Kazemi/void-runner](https://github.com/Arash1Kazemi/void-runner)
- **Evidence:** [direct model evidence](https://github.com/Arash1Kazemi/void-runner/commit/9b8546826247cd8ba4b677e5b9f52583fb246a81)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Arash1Kazemi/void-runner/blob/main/circuit_preview.png) — 📸 3.8/10 · manual visual review · Use this frame for the game-level score. Simulated LED matrix and keypad wiring view; technical diagram more than a game scene.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A vertical space shooter for the Arduino Mega: a 16 × 24 screen of single LEDs plus three. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Arash1Kazemi/void-runner/blob/main/tools/gen_circuit.py](https://github.com/Arash1Kazemi/void-runner/blob/main/tools/gen_circuit.py)
- [https://github.com/Arash1Kazemi/void-runner/commit/9b8546826247cd8ba4b677e5b9f52583fb246a81](https://github.com/Arash1Kazemi/void-runner/commit/9b8546826247cd8ba4b677e5b9f52583fb246a81)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; https://github.com/Arash1Kazemi/void-runner

[Back to the awesome list](../../README.md)
