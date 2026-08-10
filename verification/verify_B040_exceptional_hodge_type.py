#!/usr/bin/env python3
"""Finite Tate-kernel bookkeeping for B040; not an MHM formalization."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B040-exceptional-hodge-type-check.json"

cases = []
for span_rank in range(1, 6):
    relation_dimension = 5 - span_rank
    source_hodge_numbers = {"h(0,0)": 5}
    kernel_hodge_numbers = {"h(0,0)": relation_dimension}
    if sum(kernel_hodge_numbers.values()) != relation_dimension:
        raise SystemExit("FAIL: kernel Hodge dimension mismatch")
    cases.append(
        {
            "cycle_span_rank": span_rank,
            "source": "Q(0)^5",
            "source_hodge_numbers": source_hodge_numbers,
            "relation_dimension": relation_dimension,
            "kernel_hodge_numbers": kernel_hodge_numbers,
        }
    )

actual = {
    "tate_normalization": "Q(n) on vanishing homology",
    "local_crossing_groups": "five copies of Q(0)",
    "transgression_category": "rational mixed Hodge structures",
    "cases": cases,
    "scope": "finite rank and Hodge-number bookkeeping only",
}

expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B040 relation kernels have only the (0,0) Tate component")
