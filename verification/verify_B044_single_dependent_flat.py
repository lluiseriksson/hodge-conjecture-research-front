#!/usr/bin/env python3
"""Exact two-class residue checks for B044; not an IC/MHM proof."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B044-single-dependent-flat-check.json"


def cycle_matrix(total_rank: int, flat_rank: int) -> sp.Matrix:
    columns: list[list[int]] = []
    for i in range(3):
        col = [0] * total_rank
        col[i % flat_rank] = 1
        columns.append(col)
    for j in range(4):
        col = [0] * total_rank
        pivot = flat_rank + j
        if pivot < total_rank:
            col[pivot] = 1
        else:
            col[(j + 1) % total_rank] += j + 2
        columns.append(col)
    return sp.Matrix(total_rank, 7, lambda i, j: columns[j][i])


cases = []
for flat_rank in range(1, 4):
    for total_rank in range(flat_rank, flat_rank + 5):
        D = cycle_matrix(total_rank, flat_rank)
        if D.rank() != total_rank:
            raise SystemExit("FAIL: cycle matrix rank")
        Df = D[:, :3]
        B = sp.Matrix.hstack(*Df.columnspace())
        if B.rank() != flat_rank:
            raise SystemExit("FAIL: dependent-flat span rank")

        zero = sp.zeros(total_rank, flat_rank)
        lower_a = sp.Matrix.hstack(-Df, sp.zeros(total_rank, 4))
        residue = sp.Matrix.vstack(
            sp.Matrix.hstack(zero, D),
            sp.Matrix.hstack(B, lower_a),
        )
        kernel_dimension = len(residue.nullspace())
        relation_dimension = 7 - total_rank
        if kernel_dimension != relation_dimension:
            raise SystemExit("FAIL: resolved kernel differs from relation kernel")

        for vector in residue.nullspace():
            w = vector[:flat_rank, :]
            a = vector[flat_rank:, :]
            if D * a != sp.zeros(total_rank, 1):
                raise SystemExit("FAIL: projection is not a cycle relation")
            if B * w != Df * a[:3, :]:
                raise SystemExit("FAIL: exceptional-flat residue equation")

        cases.append(
            {
                "flat_span_rank": flat_rank,
                "total_span_rank": total_rank,
                "resolved_kernel_dimension": kernel_dimension,
                "relation_dimension": relation_dimension,
            }
        )

actual = {
    "exceptional_fiber": "Bl_p(P^2)",
    "divisor_classes": {"C": "e", "M_1_to_3": "h-e", "M_4_to_7": "h"},
    "residue_equations": [
        "sum_1^7 a_i delta_i = 0",
        "w - sum_1^3 a_i delta_i = 0",
    ],
    "tested_cases": cases,
    "non_full_support_H1_contribution": 0,
    "kernel_hodge_type": "(0,0)",
    "scope": "exact residue-matrix and shift bookkeeping only",
}

expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B044 dependent-flat residue kernel equals the full relation kernel")
