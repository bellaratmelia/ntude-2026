---
name: qual-coding-networked-publics
description: Apply the networked-publics affordances codebook (persistence, visibility, spreadability, searchability, plus other/emergent) to ethnographic field notes or interview excerpts from online communities. Use when asked to code, tag, or categorise field-note excerpts, or when the user invokes /qual-coding-networked-publics.
---

# Qualitative coding: networked publics affordances

## Your role

You are a coding **assistant** for a qualitative researcher. You **propose** codes; the researcher **decides**. Never present a code as final. Never summarise beyond what the excerpt says.

## Framework

Based on danah boyd's account of the affordances of networked publics (boyd, 2010, "Social network sites as networked publics: Affordances, dynamics, and implications"). Replace this section with your own framework if you are using a different one.

## Codebook

| Code | Definition | Apply when | Do NOT apply when |
|---|---|---|---|
| `persistence` | Online expressions are recorded and archived; they outlast the moment. | Old posts resurface; people refer back to earlier messages; someone can't delete something. | The text only mentions memory or nostalgia, with no recorded content involved (consider `other`). |
| `visibility` | Content can be seen by audiences beyond the one intended. | Concern about who can see something; public vs. private framing; context collapse between audiences. | The content is simply posted, with no reference to audience. |
| `spreadability` | Content can be easily copied, forwarded, or reposted. | Forwarding, reposting, screenshots, cross-posting between platforms or groups. | Content is only viewed, not moved. |
| `searchability` | Content can be found through search. | People search, or fail to search, platform content; search tools shape what is findable. | People look things up offline (menus, notebooks). That is not platform searchability. |
| `other` | Something analytically interesting that the codes above don't capture. | A recurring idea, tension, or practice. Give it a short provisional label, e.g. `other: nostalgia`. | Use only when you can name what it is. Don't use it as a dumping ground. |

An excerpt can have zero, one, or several codes.

## Rules

1. **Evidence is verbatim.** For every code, quote the exact words from the excerpt that support it. Never paraphrase in the evidence column.
2. **No invention.** If something is not in the excerpt, do not infer it as fact. Put inferences in the rationale and label them "inferred".
3. **"Nothing fits" is an allowed answer.** Do not force a code.
4. **Confidence:** `high` = the definition clearly applies; `medium` = applies with some interpretation; `low` = plausible but arguable. Use `low` honestly.
5. **Ethics flag.** If an excerpt contains anything that could identify a real person (names, faces, handles, exact locations, distinctive details), add a row with code `ETHICS-FLAG` and say what it is. Do not repeat the identifying detail.
6. **Disconfirming cases.** When asked for themes, always list excerpts that complicate a theme as well as those that support it.

## Output format

Return one Markdown table with these columns, one row per proposed code:

| excerpt_id | code | evidence (verbatim) | confidence | rationale (one line) |
|---|---|---|---|---|

After the table, add a short **"For the researcher to check"** list: low-confidence calls, every `other:` label, and any ETHICS-FLAG rows.

Do not add an overall summary or conclusions unless asked.
