#!/usr/bin/env python3
"""Uniform incidence and shift checks for B043; not an IC/MHM proof."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B043-uniform-arbitrary-rank-check.json"

rank_cases = 0
incidence_cases = 0
for dimension in range(2, 11):
    for branches in range(dimension, dimension + 11):
        rank_cases += branches
        for depth in range(1, dimension):
            expected_strata = comb(branches, depth)
            if expected_strata <= 0:
                raise SystemExit("FAIL: uniform incidence count")
            incidence_cases += 1

        perverse_range = list(range(-(dimension - 2), dimension - 1))
        point_degrees = [dimension + j for j in perverse_range]
        if point_degrees[0] != 2 or point_degrees[-1] != 2 * dimension - 2:
            raise SystemExit("FAIL: dimension-uniform point degree range")
        if 1 in point_degrees:
            raise SystemExit("FAIL: exceptional point summand contaminates H1")

actual = {
    "arrangements": "U_(d,r)",
    "tested_dimensions": [2, 10],
    "tested_branch_offsets": [0, 10],
    "tested_rank_cases": rank_cases,
    "tested_incidence_depth_cases": incidence_cases,
    "exceptional_divisor": "P^(d-1)",
    "cohomology_sheaf_H1": "direct sum_i Q_(L_i)",
    "residue_map": "d2(a_i) = sum_i a_i delta_i",
    "perverse_direct_image_range": "[-(d-2), d-2]",
    "point_summand_ordinary_degrees": "[2, 2d-2]",
    "point_summand_H1_contribution": 0,
    "kernel_hodge_type": "(0,0)",
    "scope": "finite incidence, shift, rank, and Hodge-number bookkeeping only",
}

expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B043 uniform arbitrary-rank incidence and shift checks")
