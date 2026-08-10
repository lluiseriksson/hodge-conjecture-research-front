#!/usr/bin/env python3
"""Three-class residue checks for B045; not an IC/MHM proof."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B045-two-dependent-flats-check.json"


def cycle_matrix(rank: int) -> sp.Matrix:
    columns = []
    for j in range(7):
        col = [0] * rank
        if j < rank:
            col[j] = 1
        else:
            col[(2 * j + 1) % rank] = j + 1
            col[(3 * j + 2) % rank] += 1
        columns.append(col)
    return sp.Matrix(rank, 7, lambda i, j: columns[j][i])


cases = []
for total_rank in range(1, 8):
    D = cycle_matrix(total_rank)
    if D.rank() != total_rank:
        raise SystemExit("FAIL: cycle span rank")

    A_indices = [0, 1, 2]
    B_indices = [0, 3, 4]
    DA = D[:, A_indices]
    DB = D[:, B_indices]
    BA = sp.Matrix.hstack(*DA.columnspace())
    BB = sp.Matrix.hstack(*DB.columnspace())
    tA, tB = BA.cols, BB.cols

    top = sp.Matrix.hstack(sp.zeros(total_rank, tA + tB), D)
    lower_A_coeff = sp.zeros(total_rank, 7)
    lower_B_coeff = sp.zeros(total_rank, 7)
    for local, index in enumerate(A_indices):
        lower_A_coeff[:, index] = -DA[:, local]
    for local, index in enumerate(B_indices):
        lower_B_coeff[:, index] = -DB[:, local]

    middle = sp.Matrix.hstack(BA, sp.zeros(total_rank, tB), lower_A_coeff)
    bottom = sp.Matrix.hstack(sp.zeros(total_rank, tA), BB, lower_B_coeff)
    residue = sp.Matrix.vstack(top, middle, bottom)

    kernel = residue.nullspace()
    expected_dimension = 7 - total_rank
    if len(kernel) != expected_dimension:
        raise SystemExit("FAIL: resolved kernel dimension")
    for vector in kernel:
        a = vector[tA + tB :, :]
        if D * a != sp.zeros(total_rank, 1):
            raise SystemExit("FAIL: projection is not a global relation")

    cases.append(
        {
            "total_span_rank": total_rank,
            "flat_A_span_rank": tA,
            "flat_B_span_rank": tB,
            "resolved_kernel_dimension": len(kernel),
            "relation_dimension": expected_dimension,
        }
    )

actual = {
    "exceptional_fiber": "Bl_(p_A,p_B)(P^2)",
    "divisor_classes": {
        "C_A": "e_A",
        "C_B": "e_B",
        "M_1": "h-e_A-e_B",
        "M_2_M_3": "h-e_A",
        "M_4_M_5": "h-e_B",
        "M_6_M_7": "h",
    },
    "residue_components": ["global", "flat_A_partial_sum", "flat_B_partial_sum"],
    "tested_cases": cases,
    "non_full_support_H1_contribution": 0,
    "kernel_hodge_type": "(0,0)",
    "scope": "exact residue-matrix and shift bookkeeping only",
}
expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B045 two-flat residue kernel equals the full relation kernel")
