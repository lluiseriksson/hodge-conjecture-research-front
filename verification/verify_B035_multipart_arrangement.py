#!/usr/bin/env python3
"""Finite checks for B035's U(2,5) combinatorics; not an IC/Hodge proof."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B035-multipart-arrangement-check.json"


def independent(subset: tuple[int, ...] | list[int]) -> bool:
    """Independence in the simple rank-two uniform matroid."""
    return len(subset) <= 2


def partitions_into_q_independent(r: int, q: int) -> bool:
    for coloring in itertools.product(range(q), repeat=r):
        blocks = [[i for i, color in enumerate(coloring) if color == c] for c in range(q)]
        if all(independent(block) for block in blocks):
            return True
    return False


results = []
for r in range(1, 9):
    minimum = next(q for q in range(1, r + 1) if partitions_into_q_independent(r, q))
    asserted = (r + 1) // 2
    if minimum != asserted:
        raise SystemExit(f"FAIL: U(2,{r}) block number {minimum} != {asserted}")
    results.append({"branches": r, "minimum_independent_blocks": minimum})

if not partitions_into_q_independent(4, 2):
    raise SystemExit("FAIL: four branches should admit two blocks")
if partitions_into_q_independent(5, 2):
    raise SystemExit("FAIL: five branches should not admit two blocks")
if not partitions_into_q_independent(5, 3):
    raise SystemExit("FAIL: five branches should admit three blocks")

vertices = ["E"] + [f"H{i}" for i in range(1, 6)]
edges = [["E", f"H{i}"] for i in range(1, 6)]
if len(vertices) != 6 or len(edges) != 5:
    raise SystemExit("FAIL: exceptional star has wrong size")
if any(edge[0] != "E" for edge in edges):
    raise SystemExit("FAIL: non-exceptional edge in star")

actual = {
    "matroid": "U(2,r)",
    "block_numbers": results,
    "minimal_not_two_colorable": 5,
    "witness_partition_sizes": [2, 2, 1],
    "resolved_incidence": {"vertices": vertices, "edges": edges},
    "monodromy_identities_checked_in_proof": [
        "N_i^2=0",
        "N_i N_j=0 for i != j",
        "N_E=sum_i N_i",
        "N_E N_i=0",
    ],
    "scope": "finite combinatorial and incidence check only",
}

expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B035 minimal three-block matroid and exceptional-star checks")
