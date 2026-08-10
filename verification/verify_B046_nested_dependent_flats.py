#!/usr/bin/env python3
"""Nested three-class residue checks for B046; not an IC/MHM proof."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B046-nested-dependent-flats-check.json"

forms = sp.Matrix(
    [
        [1, 0, 1, 0, 1],
        [0, 1, 1, 0, 2],
        [0, 0, 0, 1, 3],
        [0, 0, 0, 0, 0],
    ]
)
if forms.rank() != 3 or forms[:, [0, 1, 2]].rank() != 2:
    raise SystemExit("FAIL: stated nested flats have the wrong ranks")
for triple in combinations(range(5), 3):
    expected_rank = 2 if triple == (0, 1, 2) else 3
    if forms[:, triple].rank() != expected_rank:
        raise SystemExit("FAIL: unintended dependent triple in the explicit model")


def cycle_matrix(rank: int) -> sp.Matrix:
    columns = []
    for j in range(9):
        col = [0] * rank
        if j < rank:
            col[j] = 1
        else:
            col[(j + 1) % rank] = j + 2
            col[(2 * j + 1) % rank] += 1
        columns.append(col)
    return sp.Matrix(rank, 9, lambda i, j: columns[j][i])


cases = []
S_indices = [0, 1, 2]
T_indices = [0, 1, 2, 3, 4]
for total_rank in range(1, 10):
    D = cycle_matrix(total_rank)
    if D.rank() != total_rank:
        raise SystemExit("FAIL: total cycle rank")
    DS = D[:, S_indices]
    DT = D[:, T_indices]
    BS = sp.Matrix.hstack(*DS.columnspace())
    BT = sp.Matrix.hstack(*DT.columnspace())
    tS, tT = BS.cols, BT.cols

    top = sp.Matrix.hstack(sp.zeros(total_rank, tT + tS), D)
    coeff_T = sp.zeros(total_rank, 9)
    coeff_S = sp.zeros(total_rank, 9)
    for local, index in enumerate(T_indices):
        coeff_T[:, index] = -DT[:, local]
    for local, index in enumerate(S_indices):
        coeff_S[:, index] = -DS[:, local]
    middle = sp.Matrix.hstack(BT, sp.zeros(total_rank, tS), coeff_T)
    bottom = sp.Matrix.hstack(sp.zeros(total_rank, tT), BS, coeff_S)
    residue = sp.Matrix.vstack(top, middle, bottom)

    kernel = residue.nullspace()
    relation_dimension = 9 - total_rank
    if len(kernel) != relation_dimension:
        raise SystemExit("FAIL: nested residue kernel dimension")
    for vector in kernel:
        a = vector[tT + tS :, :]
        if D * a != sp.zeros(total_rank, 1):
            raise SystemExit("FAIL: nested projection is not a global relation")
    if kernel:
        projected = sp.Matrix.hstack(
            *(vector[tT + tS :, :] for vector in kernel)
        )
        if projected.rank() != relation_dimension:
            raise SystemExit("FAIL: projection is not an isomorphism")

    cases.append(
        {
            "total_span_rank": total_rank,
            "codim2_flat_span_rank": tS,
            "codim3_flat_span_rank": tT,
            "resolved_kernel_dimension": len(kernel),
            "relation_dimension": relation_dimension,
        }
    )

actual = {
    "first_five_form_rank": forms.rank(),
    "unique_dependent_triple": [1, 2, 3],
    "exceptional_fiber": "Bl_strict_line(Bl_point(P^3))",
    "branch_classes": {
        "i_in_S": "h-e_T-e_S",
        "i_in_T_minus_S": "h-e_T",
        "i_outside_T": "h",
    },
    "residue_components": ["global", "T_partial_sum", "S_partial_sum"],
    "tested_cases": cases,
    "minimum_non_full_support_degree": 2,
    "kernel_hodge_type": "(0,0)",
    "scope": "exact residue-matrix and support-shift bookkeeping only",
}
expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B046 nested residue kernel equals the full relation kernel")
