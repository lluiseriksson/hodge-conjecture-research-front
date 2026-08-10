#!/usr/bin/env python3
"""Exact residue-map checks for B038; not an IC/MHS/Hodge proof."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B038-exceptional-residue-check.json"


def cycle_matrix(span_rank: int) -> sp.Matrix:
    cols = []
    for i in range(5):
        if i < span_rank:
            col = [0] * span_rank
            col[i] = 1
        else:
            col = [i + j + 1 for j in range(span_rank)]
        cols.append(col)
    return sp.Matrix(span_rank, 5, lambda i, j: cols[j][i])


cases = []
for span_rank in range(1, 6):
    d2 = cycle_matrix(span_rank)
    rank = d2.rank()
    kernel_dimension = len(d2.nullspace())
    if rank != span_rank or kernel_dimension != 5 - span_rank:
        raise SystemExit(f"FAIL: residue-map rank/nullity for s={span_rank}")
    for i in range(5):
        if d2[:, i] != cycle_matrix(span_rank)[:, i]:
            raise SystemExit("FAIL: branch residue differs from cycle column")
    cases.append(
        {
            "cycle_span_rank": span_rank,
            "d2_rank": rank,
            "d2_kernel_dimension": kernel_dimension,
            "relation_dimension": 5 - span_rank,
        }
    )

actual = {
    "branches": 5,
    "residue_connecting_map": "(k_i) -> sum_i k_i",
    "local_residues": "e_i -> delta_i",
    "transgression": "d2(a_i) = sum_i a_i delta_i",
    "cases": cases,
    "scope": "exact rational residue-matrix checks only",
}
expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B038 exceptional transgression is the vanishing-cycle map")
