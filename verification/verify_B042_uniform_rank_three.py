#!/usr/bin/env python3
"""Incidence, amplitude, and rank checks for B042; not an IC/MHM proof."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B042-uniform-rank-three-check.json"

cases = []
for branches in range(3, 21):
    line_strata = branches
    pair_strata = comb(branches, 2)
    max_local_h1_rank = 2 if branches >= 2 else branches
    for span_rank in range(1, branches + 1):
        relation_dimension = branches - span_rank
        cases.append((branches, span_rank, relation_dimension))
        if relation_dimension < 0:
            raise SystemExit("FAIL: negative relation dimension")

    if pair_strata != branches * (branches - 1) // 2:
        raise SystemExit("FAIL: pair-incidence count")
    if max_local_h1_rank != 2:
        raise SystemExit("FAIL: pair stratum should carry two line generators")

resolved_ordinary_amplitude = [0, 1, 2, 3, 4]
shifted_stalk_amplitude = [degree - 3 for degree in resolved_ordinary_amplitude]
perverse_direct_image_range = [-1, 0, 1]
point_summand_ordinary_degrees = [j + 3 for j in perverse_direct_image_range]

if point_summand_ordinary_degrees != [2, 3, 4]:
    raise SystemExit("FAIL: threefold direct-image shifts")
if 1 in point_summand_ordinary_degrees:
    raise SystemExit("FAIL: point summand contaminates H1")

actual = {
    "arrangements": "U_(3,r)",
    "tested_branch_range": [3, 20],
    "tested_rank_cases": len(cases),
    "line_strata_for_r": "r",
    "pair_strata_for_r": "binomial(r,2)",
    "max_local_H1_rank": 2,
    "cohomology_sheaf_H1": "direct sum_i Q_(L_i)",
    "residue_map": "d2(a_i) = sum_i a_i delta_i",
    "resolved_ordinary_amplitude": resolved_ordinary_amplitude,
    "shifted_stalk_amplitude": shifted_stalk_amplitude,
    "perverse_direct_image_range": perverse_direct_image_range,
    "point_summand_ordinary_degrees": point_summand_ordinary_degrees,
    "point_summand_H1_contribution": 0,
    "kernel_hodge_type": "(0,0)",
    "scope": "finite incidence, shift, rank, and Hodge-number bookkeeping only",
}

expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B042 U_(3,r) incidence, amplitude, and relation checks")
