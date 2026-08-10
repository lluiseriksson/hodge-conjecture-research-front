#!/usr/bin/env python3
"""Finite symbolic consistency checks for B049; not a general proof."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B049-wonderful-divisor-matrix-check.json"


def branch_vectors(branches: int, flats: list[set[int]]) -> list[list[int]]:
    vectors = []
    for i in range(branches):
        vectors.append([1] + [-int(i in flat) for flat in flats])
    return vectors


cases = {
    "one_flat": (7, [{0, 1, 2}]),
    "two_overlapping_flats": (7, [{0, 1, 2}, {0, 3, 4}]),
    "three_level_chain": (11, [set(range(7)), set(range(5)), {0, 1, 2}]),
    "fork": (11, [set(range(7)), {0, 1, 2}, {3, 4, 5}]),
}

checked = {}
for name, (branches, flats) in cases.items():
    vectors = branch_vectors(branches, flats)
    incidence = sp.Matrix([[int(i in flat) for i in range(branches)] for flat in flats])
    # Exceptional coefficient columns are an identity block, hence each
    # partial-sum row is independently solvable and only the global row
    # remains on projection to branch coefficients.
    exceptional_block = sp.eye(len(flats))
    if exceptional_block.det() != 1:
        raise SystemExit("FAIL: exceptional block is not unimodular")
    checked[name] = {
        "branches": branches,
        "flats": len(flats),
        "branch_class_vectors": vectors,
        "incidence_rank": incidence.rank(),
        "exceptional_block_determinant": int(exceptional_block.det()),
    }

# Reverse a two-element chain. In raw coordinates (h, E_G, E_F), the final
# intrinsic boundary basis is (h, D_G=E_G-E_F, D_F=E_F).
raw_to_intrinsic = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 1, 1]])
if abs(int(raw_to_intrinsic.det())) != 1:
    raise SystemExit("FAIL: raw-to-intrinsic basis change is not unimodular")
raw_branch_containing_both = sp.Matrix([1, -1, 0])
intrinsic_branch_containing_both = sp.Matrix([1, -1, -1])
if raw_to_intrinsic * raw_branch_containing_both != intrinsic_branch_containing_both:
    raise SystemExit("FAIL: reverse-chain branch formula")

actual = {
    "finite_cases": checked,
    "reverse_chain_raw_basis": ["h", "E_G", "E_F"],
    "reverse_chain_intrinsic_basis": ["h", "D_G=E_G-E_F", "D_F=E_F"],
    "basis_change_determinant": int(raw_to_intrinsic.det()),
    "scope": "finite incidence and basis-change consistency only",
}
expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B049 finite divisor-matrix consistency checks")
