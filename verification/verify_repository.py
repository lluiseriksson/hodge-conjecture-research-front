#!/usr/bin/env python3
"""Read-only consistency checks. A green run is not mathematical proof."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {
    "EXPLORATORY",
    "NUMERICAL",
    "CONDITIONAL",
    "PROVED",
    "FORMALLY VERIFIED",
    "NO-GO",
}
REQUIRED_PATHS = [
    "README.md",
    "docs/problem-statement.md",
    "docs/vertical-map.md",
    "docs/verification-ledger.md",
    "docs/no-go-ledger.md",
    "docs/source-citations",
    "experiments",
    "proofs",
    "formal",
    "verification",
    "artifacts",
]
BRICK_KEYS = {
    "brick_id",
    "status",
    "base_field",
    "variety",
    "smoothness",
    "projectivity",
    "dimension",
    "codimension",
    "coefficient_field",
    "cohomology_theory",
    "hodge_type",
    "cycle_class_map",
    "cycle_equivalence",
    "scope",
    "dependencies",
    "claim",
    "falsifier",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


for rel in REQUIRED_PATHS:
    if not (ROOT / rel).exists():
        fail(f"missing required path: {rel}")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
if "does not prove or disprove" not in readme:
    fail("README lacks explicit non-claim")

for markdown in ROOT.rglob("*.md"):
    relative_parts = markdown.relative_to(ROOT).parts
    if relative_parts and relative_parts[0] == "work":
        continue
    text = markdown.read_text(encoding="utf-8")
    control_codes = sorted({
        ord(character)
        for character in text
        if ord(character) < 32 and character not in "\n\r\t"
    })
    if control_codes:
        fail(
            f"{markdown.relative_to(ROOT)}: forbidden control characters "
            f"{control_codes}"
        )
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        clean = target.split("#", 1)[0]
        if clean and not (markdown.parent / clean).resolve().exists():
            fail(f"{markdown.relative_to(ROOT)}: broken local link {target!r}")

brick_ids: set[str] = set()
for path in sorted((ROOT / "proofs").glob("*.md")):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail(f"{path.name}: missing YAML-like front matter")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    missing = BRICK_KEYS - fields.keys()
    if missing:
        fail(f"{path.name}: missing metadata {sorted(missing)}")
    if fields["status"] not in ALLOWED:
        fail(f"{path.name}: invalid status {fields['status']!r}")
    if fields["scope"] not in {"absolute", "relative", "generic", "fiberwise", "relative and fiberwise"}:
        fail(f"{path.name}: invalid scope {fields['scope']!r}")
    brick_id = fields["brick_id"]
    if brick_id in brick_ids:
        fail(f"duplicate brick id: {brick_id}")
    brick_ids.add(brick_id)

ledger = (ROOT / "docs" / "verification-ledger.md").read_text(encoding="utf-8")
for brick_id in brick_ids:
    if brick_id not in ledger:
        fail(f"brick {brick_id} absent from verification ledger")

state = json.loads((ROOT / "artifacts" / "research-state.json").read_text(encoding="utf-8"))
if state["terminal_status"] != "OPEN":
    fail("terminal status must remain OPEN unless a separately audited resolution exists")
if set(state["allowed_labels"]) != ALLOWED:
    fail("machine-readable allowed labels disagree with verifier")
if state["estimates_percent"]["actual_general_hodge_progress"] != 0:
    fail("initial actual-progress estimate changed without an audited promotion")

print(f"PASS: repository topology, {len(brick_ids)} bricks, labels, ledger, and open-status guard")


if __name__ == "__main__":
    sys.exit(0)
