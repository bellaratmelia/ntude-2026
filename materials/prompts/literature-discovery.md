# Literature discovery prompts

Use these with connectors switched on (in Claude: **Settings → Connectors**). Change the topic in brackets to your own.

## 1. Discover across sources

```text
I'm a master's student in digital ethnography. Find recent (2020+)
peer-reviewed work on [how young people perform identity in
semi-private online spaces (e.g. close friends lists, group chats,
finstas, Discord servers)].

For each source you search, tell me which one it came from.
Return a table: citation, year, method (ethnography / interviews /
survey / computational / mixed), field site/platform, and a
one-sentence finding. Only include items you actually retrieved;
do not fill gaps from memory. Give me the DOI or link for each.
```

## 2. Search your own Zotero library

Needs a Zotero MCP server set up locally.

```text
Search my Zotero library for everything I've saved on [digital
identity formation or self-presentation online]. Group the results
by theoretical framing (e.g. Goffman/dramaturgy, affordances,
networked publics, other). Flag anything I've saved but never
tagged.
```

## 3. Chain: summary, then gaps

```text
Using the papers in the table above:

1. For each, write a 3-line structured note: research question,
   field site + method, key contribution.
2. Then compare them: which platforms, populations, and methods are
   well covered, and which are thin or missing?
3. Present the gaps as questions, not conclusions, e.g.
   "Few studies appear to look at X. Is that a real gap, or a
   limitation of this search?"

Cite the paper for every claim. If you are inferring rather than
reading it from the paper, say so.
```

## Checks before you trust the results

- Open at least a few DOIs. Do the papers exist, and do they say what the table says?
- Ask: which databases did this **not** search? Books, regional journals, and non-English work are often missing.
- Treat "gaps" as hypotheses about the literature, not findings.
