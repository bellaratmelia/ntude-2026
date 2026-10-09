# AI-Augmented Qualitative Research

Slides and materials for a guest seminar for the MA in Digital Ethnography, NTU.

**Slides:** TODO: GitHub Pages URL

## What's here

| Path | What it is |
|---|---|
| `index.qmd` | The slides (Quarto revealjs) |
| `materials/hands-on.md` | Step-by-step instructions for every hands-on activity (Path A and Path B) |
| `materials/prompts/` | Every prompt used in the session, ready to copy |
| `materials/sample-ai-output.md` | Example AI coding output, for anyone without AI access |
| `materials/before-the-session.md` | Pre-session note for students (laptop, AI account) |
| `materials/skills/qual-coding/SKILL.md` | A ready-made qualitative coding Skill (networked publics affordances) |
| `materials/data/fieldnotes.md` | Six **fictional** field-note excerpts for practice |
| `materials/audit-log-template.md` | A decision log for AI-assisted coding |
| `materials/api/code_excerpts.py` | Optional: run the coding Skill over a dataset via the Claude API |

## Using the coding Skill

- **Claude.ai:** Settings → Capabilities → Skills → upload the `qual-coding` folder (zipped).
- **Claude Code:** copy the `qual-coding` folder into `~/.claude/skills/` (personal) or `.claude/skills/` inside a project.

Then ask Claude to code some field notes, or type `/qual-coding-networked-publics`.

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
