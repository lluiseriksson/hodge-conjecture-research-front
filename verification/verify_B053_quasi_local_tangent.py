#!/usr/bin/env python3
"""Finite blow-up/tangent checks for B053; not the general proof."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B053-quasi-local-tangent-check.json"
SLOPES = [0, 1, 2, 4, 8]

x, u = sp.symbols("x u")
strict_transforms = [u - slope - slope**4 * x for slope in SLOPES]
exceptional_intersections = [sp.solve(expr.subs(x, 0), u)[0] for expr in strict_transforms]
transverse_determinants = []
for expr in strict_transforms:
    jacobian = sp.Matrix([[1, 0], [sp.diff(expr, x), sp.diff(expr, u)]])
    transverse_determinants.append(int(jacobian.det()))
if len(set(exceptional_intersections)) != len(SLOPES):
    raise SystemExit("FAIL: curved branches do not separate on the exceptional line")
if any(value != 1 for value in transverse_determinants):
    raise SystemExit("FAIL: strict branch is not transverse to the exceptional divisor")

# A rank-three Vandermonde sample checks the uniform exceptional incidence:
# every triple of normal covectors is independent, hence no three
# projectivized tangent hyperplanes meet.
covectors = [sp.Matrix([1, slope, slope**2]) for slope in SLOPES]
triple_determinants = [
    int(sp.Matrix.hstack(*(covectors[index] for index in triple)).det())
    for triple in itertools.combinations(range(len(SLOPES)), 3)
]
if any(value == 0 for value in triple_determinants):
    raise SystemExit("FAIL: tangent normal arrangement is not uniform")

cycles = sp.Matrix([[1, 0, 1, 1, 2], [0, 1, 1, -1, 1]])
relation_nullity = cycles.cols - cycles.rank()

actual = {
    "plane_curved_example": {
        "slopes": SLOPES,
        "exceptional_intersections": [int(value) for value in exceptional_intersections],
        "exceptional_multiplicity": 1,
        "transverse_determinants": transverse_determinants,
    },
    "rank_three_tangent_sample": {
        "triple_determinants": triple_determinants,
        "uniform": True,
    },
    "relation_sample": {
        "branches": cycles.cols,
        "cycle_span_rank": cycles.rank(),
        "degree_one_nullity": relation_nullity,
    },
    "scope": "finite blow-up and tangent-incidence consistency only",
}
expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B053 quasi-local tangent-invariance checks")
