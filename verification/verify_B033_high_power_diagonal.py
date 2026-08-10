#!/usr/bin/env python3
"""Exact formula checks for B033; not a geometry, monodromy, or Hodge proof."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B033-high-power-diagonal-check.json"


def row(k: int) -> dict[str, int | bool]:
    node_count = k * k - 3 * k + 3
    smoothing_corank = comb(k - 4, 2)
    smoothing_rank = node_count - smoothing_corank
    return {
        "k": k,
        "m": k // 2,
        "node_count": node_count,
        "smoothing_corank": smoothing_corank,
        "smoothing_rank": smoothing_rank,
        "two_rank_margin": 2 * smoothing_rank - node_count,
        "adjoint_defect": 1,
        "partition_cardinality_possible": node_count <= 2 * smoothing_rank,
    }


actual = {
    "formulas": {
        "node_count": "k^2-3k+3",
        "smoothing_corank": "binomial(k-4,2)",
        "smoothing_rank": "(k^2+3k-14)/2",
        "two_rank_margin": "6k-17",
        "adjoint_defect": "1",
    },
    "samples": [row(k) for k in (6, 8, 10, 20)],
    "primitive_diagonal": {
        "gamma_square": 3,
        "primitive_coefficient_numerator": 1,
        "primitive_coefficient_denominator": 3,
        "ambient_rank": 1,
    },
}

expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
assert actual == expected
assert all(sample["partition_cardinality_possible"] for sample in actual["samples"])
print("PASS: B033 exact Chern, evaluation-rank, defect, and primitive arithmetic")
