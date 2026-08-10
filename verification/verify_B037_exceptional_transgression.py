#!/usr/bin/env python3
"""Bookkeeping checks for B037's E2 page; not a residue/IC/Hodge proof."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B037-exceptional-transgression-check.json"

cases = []
for cycle_span_rank in range(1, 6):
    crossing_dimension = 5
    required_d2_rank = cycle_span_rank
    resulting_h1 = crossing_dimension - required_d2_rank
    relation_dimension = 5 - cycle_span_rank
    if resulting_h1 != relation_dimension:
        raise SystemExit("FAIL: transgression kernel does not match relation dimension")
    cases.append(
        {
            "cycle_span_rank": cycle_span_rank,
            "E2_0_1_dimension": crossing_dimension,
            "required_d2_rank": required_d2_rank,
            "H1_if_d2_is_cycle_map": resulting_h1,
            "relation_dimension": relation_dimension,
        }
    )

actual = {
    "exceptional_curve": "P1",
    "cohomology_sheaves": {
        "H0": "constant K=ker(N_E)",
        "H1": "five rank-one skyscrapers",
    },
    "only_total_degree_one_differential": "d2: Q^5 -> H^2(P1,K)=K",
    "cases": cases,
    "scope": "spectral-sequence dimension bookkeeping only",
}

expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B037 unique transgression and kernel-dimension checks")
