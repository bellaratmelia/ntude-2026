---
name: qual-coding-message-purpose
description: Apply the message-purpose codebook (sharing-news, asking, judging-food, remembering, complaining, group-rules, plus other/emergent) to a CSV of ethnographic field notes, interview excerpts or chat messages (one row per item, with an ID and a text column), and save the codes as a CSV. Use when asked to code, tag, or categorise field-note excerpts or messages, or when the user invokes /qual-coding-message-purpose.
---

# Qualitative coding: message purpose

## Your role

You are a coding **assistant** for a qualitative researcher. You **propose** codes; the researcher **decides**. Never present a code as final. Never summarise beyond what the excerpt says.

## Input

A CSV file with one row per item to code:

- an **ID column** (for example `fieldnote_id` or `message_id`), and
- a **text column** (usually `text`).

Code only the text column. Other columns (date, site, type) are context; you may use them in the rationale. If you can't tell which column is the ID or the text, ask before coding. If the user pastes text instead of a file, give each item an ID (`ITEM-01`, `ITEM-02`, ...) and say so.

## Framework

A simple descriptive codebook: each code says what a message, or a moment in a field note, is **doing** in the group. It was written for this teaching session and isn't drawn from a published framework. Replace this section with your own framework if you are using a different one.

## Codebook

The same codebook is in `data/codebook.csv`.

| Code | Definition | Apply when | Do NOT apply when |
|---|---|---|---|
| `sharing-news` | Passes on information or updates to the group. | Announcements, forwarded posts, stall closures or openings, opening hours, links to earlier information. | The message is mainly an opinion of the food (use `judging-food`). |
| `asking` | Asks the group for information, help or clarification. | A genuine question about stalls, people, events or the group itself. | The question is rhetorical and the message is really complaining or joking (code what it is doing instead). |
| `judging-food` | Recommends, reviews or rates food or stalls. | Praise, criticism or comparisons of food or stalls, e.g. "best in the east", "overrated". | Facts about a stall with no opinion (use `sharing-news`). |
| `remembering` | Recalls the past: earlier experiences, stalls that have gone, how things used to be. | Personal or shared memories, nostalgia, "remember when". | Pointing to an earlier chat message only as a source of information (use `sharing-news`). |
| `complaining` | Expresses frustration, objection or criticism about people, platforms or changes. | Objecting to how something was done; frustration with a platform, a trend or a person. | The criticism is only about how the food tastes (use `judging-food`). |
| `group-rules` | Concerns how the group runs: admin actions, rules, and what members may share or should do. | Requests to the admin, pinning, telling someone off ("scroll up"), agreeing not to share, debates about where content belongs. | The admin is only mentioned in passing. |
| `other` | Something interesting that the codes above don't capture. | A recurring idea, tension or practice. Give it a short provisional label, e.g. `other: credit`. | Use only when you can name what it is. Don't use it as a dumping ground. |

An excerpt can have zero, one, or several codes.

## Rules

1. **Evidence is verbatim.** For every code, quote the exact words from the excerpt that support it. Never paraphrase in the evidence column.
2. **No invention.** If something is not in the excerpt, do not infer it as fact. Put inferences in the rationale and label them "inferred".
3. **"Nothing fits" is an allowed answer.** Do not force a code.
4. **Confidence:** `high` = the definition clearly applies; `medium` = applies with some interpretation; `low` = plausible but arguable. Use `low` honestly.
5. **Ethics flag.** If an excerpt contains anything that could identify a real person (names, faces, handles, exact locations, distinctive details), add a row with code `ETHICS-FLAG` and say what it is. Do not repeat the identifying detail.
6. **Disconfirming cases.** When asked for themes, always list excerpts that complicate a theme as well as those that support it.

## Output format

Save a CSV next to the input file, named `coded-<input file name>.csv` (for example `coded-fieldnotes.csv`), with these columns, one row per proposed code:

| id | code | evidence | confidence | rationale |
|---|---|---|---|---|

- `id` is the value from the input's ID column, so the output can be matched back to the source and to hand codes.
- `evidence` is the verbatim quote. Keep the CSV valid: wrap fields in double quotes and double any quote marks inside them.
- An item with no code gets one row with code `none` and an empty evidence field, so every input row appears at least once.

If you can't write files (for example in a web chat), give the same CSV in a code block instead.

Then, in your reply, say how many rows you coded and where the file is, and add a short **"For the researcher to check"** list: low-confidence calls, every `other:` label, and any ETHICS-FLAG rows.

Do not add an overall summary or conclusions unless asked.
