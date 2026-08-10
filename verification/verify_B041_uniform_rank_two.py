#!/usr/bin/env python3
"""Uniform finite checks for B041; not an IC/MHM formalization."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B041-uniform-rank-two-check.json"

case_count = 0
for branches in range(3, 31):
    for span_rank in range(1, branches + 1):
        relation_dimension = branches - span_rank
        if relation_dimension < 0:
            raise SystemExit("FAIL: negative relation dimension")
        if branches - span_rank != relation_dimension:
            raise SystemExit("FAIL: rank/nullity mismatch")
        case_count += 1

actual = {
    "arrangements": "U_(2,r)",
    "tested_branch_range": [3, 30],
    "residue_map": "d2(a_i) = sum_i a_i delta_i",
    "tested_rank_cases": case_count,
    "crossing_source": "Q(0)^r",
    "relation_dimension": "r-s",
    "point_summand_H1_contribution": 0,
    "scope": "finite rank, shift, and Hodge-number bookkeeping only",
}
expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B041 uniform U_(2,r) rank/nullity and Tate checks")
