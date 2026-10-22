# AI-Augmented Qualitative Research

Slides and materials for a guest seminar for the MA in Digital Ethnography, NTU.

**Slides:** https://bellaratmelia.github.io/ntude-2026/

## What's here

| Path | What it is |
|---|---|
| `index.qmd` | The slides (Quarto revealjs) |
| `materials/prompts/` | Every prompt used in the session, ready to copy |
| `materials/sample-ai-output.md` | Example AI coding output, for anyone without AI access |
| `materials/skills/qual-coding/SKILL.md` | A ready-made qualitative coding Skill (message purpose: what each message is doing) |
| `materials/skills/qual-coding-boyd/SKILL.md` | Alternative version of the Skill using boyd's networked-publics affordances |
| `materials/data/codebook.csv` | The message-purpose codebook used in the session |
| `materials/data/codebook_boyd.csv` | The alternative boyd codebook |
| `materials/data/fieldnotes.csv` | Six **fictional** field-note excerpts from a made-up hawker-food Telegram group ("Makan Kakis SG"), one row each |
| `materials/data/fieldwork-log.csv` | A 40-entry **fictional** fieldwork log for the same group, for the first task |
| `materials/data/messages.csv` | 210 **fictional** chat messages from the same group, for the at-scale demo |
| `materials/data/hand-codes.csv` | 30 of those messages (seed 42), hand-coded by the presenter for the comparison demo |
| `materials/reading-list.md` | Studies on using AI for content analysis and qualitative coding |

## Using the coding Skill

- **Claude.ai:** Settings → Capabilities → Skills → upload the `qual-coding` folder (zipped).
- **Claude Code:** copy the `qual-coding` folder into `~/.claude/skills/` (personal) or `.claude/skills/` inside a project.

Then ask Claude to code a CSV (one row per item, with an ID column and a `text` column), or type `/qual-coding-message-purpose`. It saves the codes as `coded-<file name>.csv`.

Swap in your own framework by editing the **Framework** and **Codebook** sections.

## Building the slides

```bash
quarto render
```

Output goes to `_site/`. To publish on GitHub Pages:

```bash
quarto publish gh-pages
```

## A note on data

Don't put real participant data into AI tools without checking your ethics approval and your institution's data-handling rules. The sample field notes here are made up.
