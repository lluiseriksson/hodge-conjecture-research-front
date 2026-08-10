#!/usr/bin/env python3
"""Finite exact checks for B050's anchored quotient lemma; not its proof."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B050-coefficient-sheaf-check.json"


def check_case(cycles: sp.Matrix, subsets: list[list[int]]) -> dict[str, object]:
    # Columns give vanishing cycles in a Lagrangian subspace of a symplectic
    # space. This allows dependencies while making every residue product zero.
    rank = cycles.rows
    zero = sp.zeros(rank)
    identity = sp.eye(rank)
    symplectic = sp.Matrix.vstack(
        sp.Matrix.hstack(zero, identity), sp.Matrix.hstack(-identity, zero)
    )
    deltas = [sp.Matrix.vstack(cycles[:, i], sp.zeros(rank, 1)) for i in range(cycles.cols)]
    residues = [delta * delta.T * symplectic for delta in deltas]
    anchor = sum(residues, sp.zeros(2 * rank))
    common_map = sp.Matrix.vstack(*residues)
    if anchor.rank() != common_map.rank():
        raise SystemExit("FAIL: anchor kernel differs from common kernel")

    others = [sum((residues[i] for i in subset), sp.zeros(2 * rank)) for subset in subsets]
    target_dims = [matrix.rank() for matrix in others]
    stacked = sp.Matrix.vstack(anchor, *others)
    cokernel_dim = anchor.rank() + sum(target_dims) - stacked.rank()
    if cokernel_dim != sum(target_dims):
        raise SystemExit("FAIL: anchored quotient dimension")
    all_residues = [anchor, *others]
    if any(left * right != sp.zeros(2 * rank) for left in all_residues for right in all_residues):
        raise SystemExit("FAIL: nonzero residue product")
    return {
        "vanishing_cycle_rank": cycles.rank(),
        "anchor_rank": anchor.rank(),
        "coefficient_dimensions": target_dims,
        "degree_one_dimension": cokernel_dim,
        "higher_terms_zero": True,
    }


cases = {
    "independent": check_case(sp.eye(4), [[0], [1, 2], [0, 1, 2]]),
    "repeated_cycle": check_case(sp.Matrix([[1, 1, 0], [0, 0, 1]]), [[0, 1], [2]]),
    "dependent_triple": check_case(sp.Matrix([[1, 0, 1], [0, 1, 1]]), [[0, 1, 2], [0, 2]]),
}

actual = {"finite_cases": cases, "scope": "finite anchored-quotient consistency only"}
expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B050 anchored SNC coefficient-sheaf checks")
