#!/usr/bin/env python3
"""Finite B057/NG038 matrix illustration; not the geometric theorem."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B057-thimble-extension-check.json"

identity = sp.eye(2)
a = sp.Matrix([[1, 1], [0, 1]])
b = sp.Matrix([[1, 0], [-1, 1]])
factors = [a, b] * 6

d_a, m_a = sp.Matrix([1, 0]), sp.Matrix([[0, 1]])
d_b, m_b = sp.Matrix([0, 1]), sp.Matrix([[-1, 0]])

alpha = sp.Matrix([1, 0])
current = alpha
coefficients: list[int] = []
boundary_columns: list[sp.Matrix] = []
extension_rows: list[sp.Matrix] = []
prefix = identity

for monodromy in factors:
    if monodromy == a:
        direction, covector = d_a, m_a
    else:
        direction, covector = d_b, m_b
    if monodromy - identity != direction * covector:
        raise SystemExit("FAIL: rank-one Picard-Lefschetz factorization")
    coefficients.append(int((covector * current)[0]))
    boundary_columns.append(direction)
    extension_rows.append(covector * prefix)
    current = monodromy * current
    prefix = monodromy * prefix

boundary_matrix = sp.Matrix.hstack(*boundary_columns)
extension_matrix = sp.Matrix.vstack(*extension_rows)
coefficient_vector = sp.Matrix(coefficients)
total_monodromy = prefix

if boundary_matrix * extension_matrix != total_monodromy - identity:
    raise SystemExit("FAIL: boundary-extension telescoping identity")
if current != alpha or boundary_matrix * coefficient_vector != sp.zeros(2, 1):
    raise SystemExit("FAIL: invariant class does not give a relation")
if coefficient_vector != extension_matrix * alpha:
    raise SystemExit("FAIL: B013 coefficients differ from extension coordinates")

actual = {
    "factor_count": len(factors),
    "total_monodromy": [
        [int(total_monodromy[i, j]) for j in range(total_monodromy.cols)]
        for i in range(total_monodromy.rows)
    ],
    "input_class": [int(value) for value in alpha],
    "extension_coefficients": coefficients,
    "extension_nonzero": any(coefficients),
    "boundary": [int(value) for value in boundary_matrix * coefficient_vector],
    "boundary_kernel_dimension": boundary_matrix.cols - boundary_matrix.rank(),
    "equator_image_rank": extension_matrix.rank(),
    "equator_quotient_dimension": (
        boundary_matrix.cols - boundary_matrix.rank() - extension_matrix.rank()
    ),
    "chosen_extension_quotient_class_zero": bool(
        extension_matrix.row_join(coefficient_vector).rank() == extension_matrix.rank()
    ),
    "scope": "finite Picard-Lefschetz composition and equator-quotient illustration only",
}

expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B057 thimble-extension and NG038 equator checks")
