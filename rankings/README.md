# Game Rankings

> Generate these reports with `node scripts/generate-rankings.mjs --as-of=YYYY-MM-DD`.

## Current reports

- [Top games this week](this-week.md) — **10** ranked rows.
- [Top games this month](this-month.md) — **0** ranked rows.
- [Date audit data](date-audit.json) — normalized date fields for every curated game unit.

## Daily rankings

| Date | Ranked rows | Counted units | Report |
| --- | ---: | ---: | --- |
| 2026-10-11 | 0 | 0 | [Open report](daily/2026-10-11.md) |
| 2026-10-12 | 0 | 0 | [Open report](daily/2026-10-12.md) |
| 2026-10-13 | 0 | 0 | [Open report](daily/2026-10-13.md) |
| 2026-10-14 | 0 | 0 | [Open report](daily/2026-10-14.md) |
| 2026-10-15 | 0 | 0 | [Open report](daily/2026-10-15.md) |
| 2026-10-16 | 0 | 0 | [Open report](daily/2026-10-16.md) |
| 2026-10-17 | 0 | 0 | [Open report](daily/2026-10-17.md) |

## Date coverage

| Date signal | Records | Game units | Meaning |
| --- | ---: | ---: | --- |
| Explicit publication date | 152 | 287 | `published_on` |
| Publication or qualifying evidence date | 165 | 325 | `published_on`, `recent_game_evidence_on`, or `fresh_activity_date` |
| Date unknown for ranking | 1006 | 1153 | Exclude from date rankings |
| Repository creation metadata | 1171 | 1478 | Audit context only; not publication |

## Date policy

- Treat `published_on` as the preferred publication date.
- Use recent gameplay evidence or fresh repository activity only when no publication date exists, and label the basis in the report.
- Use game-creation evidence or a labeled repository-creation proxy for the seven-day weekly ranking only.
- Keep repository creation and `verified_on` dates separate from publication.
- Exclude low-quality records below the 7.0 curated-list threshold; keep them in [bad-games.md](../bad-games.md).
- Show unknown dates instead of guessing.
- Regenerate all reports after changing `games.json`.

As of: **2026-10-17**
