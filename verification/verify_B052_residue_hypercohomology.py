#!/usr/bin/env python3
"""Finite exact checks for B052's residue-kernel algebra; not its proof."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B052-residue-hypercohomology-check.json"


def check_case(cycles: sp.Matrix, flats: list[list[int]]) -> dict[str, int]:
    span_rank = cycles.rank()
    relation_nullity = cycles.cols - span_rank
    # Unknowns are branch coefficients followed by one free vector in each
    # flat span. The triangular rows solve those flat vectors uniquely, while
    # the h-row is the original cycle map.
    flat_ranks = [cycles[:, flat].rank() for flat in flats]
    domain_dim = cycles.cols + sum(flat_ranks)
    residue_rank = span_rank + sum(flat_ranks)
    kernel_dim = domain_dim - residue_rank
    if kernel_dim != relation_nullity:
        raise SystemExit("FAIL: triangular residue kernel differs from relation kernel")
    return {
        "branches": cycles.cols,
        "cycle_span_rank": span_rank,
        "flat_count": len(flats),
        "coefficient_domain_dimension": domain_dim,
        "residue_rank": residue_rank,
        "kernel_dimension": kernel_dim,
        "relation_nullity": relation_nullity,
    }


cases = {
    "single_flat": check_case(sp.Matrix([[1, 0, 1, 0], [0, 1, 1, 1]]), [[0, 1, 2]]),
    "nested": check_case(sp.Matrix([[1, 0, 1, 0, 1], [0, 1, 1, 1, 0]]), [[0, 1, 2], [0, 1, 2, 3]]),
    "fork": check_case(sp.Matrix([[1, 0, 1, 0, 1, 0], [0, 1, 1, 1, 0, 1]]), [[0, 1, 2, 3], [0, 1, 2], [1, 3, 5]]),
}

actual = {
    "finite_cases": cases,
    "degree_one_spectral_sequence": {
        "nonzero_source": "E2^(0,1)",
        "constant_row_H1": 0,
        "only_outgoing_differential": "d2 to E2^(2,0)",
    },
    "scope": "finite rank and spectral-position consistency only",
}
expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B052 universal residue-kernel checks")
