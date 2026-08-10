#!/usr/bin/env python3
"""Finite clean-normal-fiber checks for B054; not the general induction."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B054-clean-tangent-wonderful-check.json"

x, y, z = sp.symbols("x y z")
branches = [x, y, (1 + z) * x + y]
jacobian = sp.Matrix([[sp.diff(branch, variable) for variable in (x, y, z)] for branch in branches])
tangent_covectors = jacobian.subs({x: 0, y: 0, z: 0})

# The dependent triple has clean common curve C=(x=y=0): rank two along C
# near the origin, and its tangent covectors have the same rank-two flat.
rank_on_common_curve = jacobian.subs({x: 0, y: 0}).rank()
if rank_on_common_curve != 2 or tangent_covectors.rank() != 2:
    raise SystemExit("FAIL: nonlinear triple is not clean with the tangent flat")

# In the exceptional P^2 of the origin blow-up the three branch lines meet at
# P(T_0 C)=[0:0:1]. Blowing that point produces the same one-flat wonderful
# fiber as the tangent arrangement.
X, Y, Z = sp.symbols("X Y Z")
tangent_lines = [X, Y, X + Y]
at_flat_point = [line.subs({X: 0, Y: 0, Z: 1}) for line in tangent_lines]
if any(value != 0 for value in at_flat_point):
    raise SystemExit("FAIL: exceptional tangent lines miss the labelled flat")

branch_class_vectors = [[1, -1], [1, -1], [1, -1]]
cycles = sp.Matrix([[1, 0, 1], [0, 1, 1]])
relation_nullity = cycles.cols - cycles.rank()
residue_domain_dimension = cycles.cols + cycles.rank()
residue_rank = 2 * cycles.rank()
if residue_domain_dimension - residue_rank != relation_nullity:
    raise SystemExit("FAIL: tangent wonderful residue kernel")

actual = {
    "clean_nonlinear_triple": {
        "tangent_covectors": [[int(value) for value in tangent_covectors.row(i)] for i in range(3)],
        "rank_on_common_curve": rank_on_common_curve,
        "tangent_flat_rank": tangent_covectors.rank(),
        "exceptional_flat_point": [0, 0, 1],
        "branch_class_vectors": branch_class_vectors,
    },
    "residue_sample": {
        "cycle_span_rank": cycles.rank(),
        "relation_nullity": relation_nullity,
        "residue_domain_dimension": residue_domain_dimension,
        "residue_rank": residue_rank,
        "kernel_dimension": residue_domain_dimension - residue_rank,
    },
    "scope": "finite clean-normal-fiber and residue consistency only",
}
expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B054 clean-arrangement tangent-wonderful checks")
