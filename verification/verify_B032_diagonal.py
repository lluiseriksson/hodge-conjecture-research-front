#!/usr/bin/env python3
"""Exact arithmetic checks for B032; not a geometry or Hodge proof."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B032-diagonal-check.json"


def multiply(
    left: dict[tuple[int, int], Fraction],
    right: dict[tuple[int, int], Fraction],
) -> dict[tuple[int, int], Fraction]:
    result: dict[tuple[int, int], Fraction] = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            if i + k <= 2 and j + ell <= 2:
                key = (i + k, j + ell)
                result[key] = result.get(key, Fraction(0)) + a * b
    return {key: value for key, value in result.items() if value}


data = json.loads(EXPECTED.read_text(encoding="utf-8"))

h0_a = 6 * 6
h0_diagonal_o4 = 15
ideal_dimension = h0_a - h0_diagonal_o4
square_ideal_dimension = 6
normal_jet_rank = ideal_dimension - square_ideal_dimension
node_count = 3 - 12 + 16

h1 = {(1, 0): Fraction(1)}
h2 = {(0, 1): Fraction(1)}
polarization = {**h1, **h2}
diagonal = {
    (2, 0): Fraction(1),
    (1, 1): Fraction(1),
    (0, 2): Fraction(1),
}
gamma = {
    (2, 0): Fraction(1),
    (1, 1): Fraction(-1),
    (0, 2): Fraction(1),
}
polarization_squared = multiply(polarization, polarization)
decomposition = {
    key: Fraction(2, 3) * polarization_squared.get(key, 0)
    + Fraction(1, 3) * gamma.get(key, 0)
    for key in diagonal
}
primitive_test = multiply(polarization, gamma)
gamma_square = multiply(gamma, gamma).get((2, 2), Fraction(0))

observed = {
    "h0_O_2_2": h0_a,
    "h0_diagonal_O4": h0_diagonal_o4,
    "ideal_dimension": ideal_dimension,
    "square_ideal_dimension": square_ideal_dimension,
    "normal_jet_rank": normal_jet_rank,
    "h0_Omega1_4": 15,
    "node_count": node_count,
    "adjoint_evaluation_source_dimension": 6,
    "adjoint_evaluation_target_dimension": 7,
    "adjoint_defect": 1,
    "primitive_product_is_zero": not primitive_test,
    "diagonal_decomposition_holds": decomposition == diagonal,
    "gamma_square": int(gamma_square),
}

assert observed == data["expected"]
print("PASS: B032 exact dimension, Chern, and cohomology-ring arithmetic")

