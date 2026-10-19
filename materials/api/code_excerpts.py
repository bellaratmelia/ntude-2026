"""Run the qualitative coding Skill over field notes or a chat export via the Claude API.

Setup (once):
    pip install anthropic pydantic
    set ANTHROPIC_API_KEY=...        (Windows)   /   export ANTHROPIC_API_KEY=...   (macOS/Linux)

Run from the repo root:
    python materials/api/code_excerpts.py                                    (the six field notes)
    python materials/api/code_excerpts.py materials/data/messages.csv --limit 20   (first 20 chat messages)

Writes one JSON line per excerpt to coded_output.jsonl, plus the model name and
date, so the run itself becomes part of your audit trail.
"""

import argparse
import csv
import datetime
import json
import re
from pathlib import Path

import anthropic
from pydantic import BaseModel

MODEL = "claude-opus-5-5"
SKILL = Path("materials/skills/qual-coding/SKILL.md")
DATA = Path("materials/data/fieldnotes.md")
OUT = Path("coded_output.jsonl")


class Code(BaseModel):
    code: str
    evidence: str      # verbatim quote from the excerpt
    confidence: str    # high / medium / low
    rationale: str


class CodedExcerpt(BaseModel):
    excerpt_id: str
    codes: list[Code]
    to_check: list[str]  # low-confidence calls, "other:" labels, ethics flags


def load_excerpts(path: Path) -> dict[str, str]:
    """Split the field notes into {"FN-01": "...", ...} using the [FN-xx] markers."""
    text = path.read_text(encoding="utf-8")
    parts = re.findall(r"\[(FN-\d+)\](.*?)(?=\n\[FN-\d+\]|\Z)", text, flags=re.S)
    return {eid: body.strip() for eid, body in parts}


def load_messages(path: Path) -> dict[str, str]:
    """Read a chat export CSV into {"MSG-001": "...", ...} using message_id and text."""
    with path.open(encoding="utf-8", newline="") as f:
        return {row["message_id"]: row["text"] for row in csv.DictReader(f)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("data", nargs="?", type=Path, default=DATA)
    parser.add_argument("--limit", type=int, help="code only the first N items (try a few before running them all)")
    args = parser.parse_args()

    items = load_messages(args.data) if args.data.suffix == ".csv" else load_excerpts(args.data)
    if args.limit:
        items = dict(list(items.items())[: args.limit])

    client = anthropic.Anthropic()
    skill = SKILL.read_text(encoding="utf-8")
    run_info = {"model": MODEL, "skill": str(SKILL), "data": str(args.data), "date": datetime.date.today().isoformat()}

    with OUT.open("w", encoding="utf-8") as f:
        for eid, body in items.items():
            result = client.messages.parse(
                model=MODEL,
                max_tokens=4000,
                system=skill,
                messages=[{"role": "user", "content": f"[{eid}] {body}"}],
                output_format=CodedExcerpt,
            )
            if result.stop_reason == "refusal" or result.parsed_output is None:
                print(f"{eid}: no structured output (stop_reason={result.stop_reason}); check manually")
                continue
            row = {**run_info, **result.parsed_output.model_dump()}
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
            print(f"{eid}: {[c.code for c in result.parsed_output.codes]}")

    print(f"Saved to {OUT}")


if __name__ == "__main__":
    main()
