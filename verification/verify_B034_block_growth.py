#!/usr/bin/env python3
"""Exact diagonal-family checks for B034; not an asymptotic-RR or Hodge proof."""

from __future__ import annotations

import json
from math import ceil, comb, factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B034-block-growth-check.json"


def top_chern_omega_twist(n: int, k: int) -> int:
    """Coefficient of H^n in (1+(k-1)H)^(n+1)/(1+kH)."""
    return sum(
        comb(n + 1, n - j) * (k - 1) ** (n - j) * (-k) ** j
        for j in range(n + 1)
    )


def sample(n: int, m: int) -> dict[str, int | bool]:
    k = 2 * m
    nodes = top_chern_omega_twist(n, k)
    block_capacity = comb(k + n, n)
    return {
        "n": n,
        "m": m,
        "k": k,
        "nodes": nodes,
        "block_capacity_upper_bound": block_capacity,
        "minimum_blocks_lower_bound": ceil(nodes / block_capacity),
        "two_blocks_cardinality_impossible": nodes > 2 * block_capacity,
        "asymptotic_ratio_target": factorial(n),
    }


actual = {
    "exact_formula": "[H^n](1+(k-1)H)^(n+1)/(1+kH)",
    "asymptotic_node_to_capacity_ratio": "n!",
    "samples": [
        sample(2, 50),
        sample(3, 5),
        sample(3, 50),
        sample(4, 3),
        sample(4, 50),
    ],
}

expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
assert actual == expected
assert not actual["samples"][0]["two_blocks_cardinality_impossible"]
assert all(
    row["two_blocks_cardinality_impossible"]
    for row in (actual["samples"][1], actual["samples"][3])
)
print("PASS: B034 exact diagonal Chern counts and block-capacity bounds")
