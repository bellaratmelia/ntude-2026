# Hands-on activities

Each activity has two paths:

- **Path A**: Claude with connectors and/or Skills switched on
- **Path B**: any AI chat tool (Claude, ChatGPT, Gemini, Copilot). Free tiers are fine.

If you have no AI access at all, pair with someone who does, or use `sample-ai-output.md`.

---

## Try 1: same prompt, different answers (10 min, pairs)

**Round 1 (ad hoc).** Each partner, separately, pastes this into their AI tool:

```text
Here is a field note from an online community. Give me three
analytic observations about it.

[FN-04] 19 Mar, 7.05pm. The Instagram account reposted a member's
review without crediting them. The member complained in the Telegram
group: "I wrote it for the group, not for IG." Admin apologised and
said they would "ask first next time". Several members reacted with
the thumbs-up emoji; one wrote "but the IG is public what, anyone
can see anyway".
```

Compare your answers.

**Round 2 (structured).** Start a **new chat**.

- Path A: use the uploaded `qual-coding-networked-publics` Skill.
- Path B: paste the **whole** of `skills/qual-coding/SKILL.md` as your first message.

Then send `Code FN-04` plus the same excerpt. Compare again.

**Talk:** What changed between rounds? What still varied? Which output could you defend in a methods section?

---

## Try 2: search your own topic, then check it (13 min, pairs)

1. Copy the **discovery prompt** from `prompts/literature-discovery.md`. Replace the topic with **your own research topic**.
   - Path A: connectors on (Settings → Connectors → Consensus and/or alphaXiv)
   - Path B: any AI tool, no connector
2. **Check three references.** Open each DOI or link.

   | Ref | Exists? | Right authors and year? | Does the paper say what the table says? |
   |---|---|---|---|
   | 1 | | | |
   | 2 | | | |
   | 3 | | | |

3. Compare with your partner, ideally one Path A and one Path B.
4. If time: run the **chaining prompt** (same file) on your results.

**Talk:** How many references checked out? What do you know exists that didn't show up? Did the "gaps" feel real?

---

## Try 3a: code it yourself first (8 min, alone, no AI)

Open `skills/qual-coding/SKILL.md` and read the **Codebook**.

Code **FN-02** and **FN-04** from `data/fieldnotes.md` **by hand**. For each code, write:

| Excerpt | Code | Exact words that support it | Confidence (high / medium / low) |
|---|---|---|---|
| FN-02 | | | |
| FN-04 | | | |

Don't use AI for this step. Your own reading is the baseline.

## Try 3b: run the Skill (10 min)

- **Path A (Claude with Skills):** upload the `qual-coding` folder (Settings → Capabilities → Skills), then send:

  ```text
  /qual-coding-networked-publics
  Code all six excerpts below.
  ```

  and paste the contents of `data/fieldnotes.md`.

- **Path B (any AI tool):** new chat → paste the whole `SKILL.md` → then send *"Code all six excerpts below"* and paste `data/fieldnotes.md`.

Check as you read: does every code have a **verbatim** quote? Where is confidence **low**? What went into **other**?

No access, or stuck? Use `sample-ai-output.md`.

## Try 3c: compare and log (7 min, pairs)

1. Put your hand codes for FN-02 and FN-04 next to the AI's.
2. Fill in **at least four rows** of `audit-log-template.md`: Accept / Reject / Modify / Promote, and **why**.
3. Compare logs with your partner.

If time, ask the AI for themes:

```text
Looking across all the codes you proposed: suggest 2–3 candidate
themes. For each, list the excerpt IDs that support it AND any that
complicate it. Do not finalise anything.
```

**Talk:** Where did you and the AI disagree, and who was right? Did it over-code? Would you trust it on excerpt 200 without checking?
