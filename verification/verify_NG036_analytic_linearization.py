#!/usr/bin/env python3
"""Exact jet obstruction for NG036; not an IC computation."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "NG036-analytic-linearization-check.json"
SLOPES = [sp.Rational(v) for v in (0, 1, 2, 4, 8)]


def mobius_from(src: tuple[sp.Rational, ...], dst: tuple[sp.Rational, ...]):
    rows = [[x, 1, -y * x, -y] for x, y in zip(src, dst)]
    kernel = sp.Matrix(rows).nullspace()
    return tuple(kernel[0]) if len(kernel) == 1 else None


def normalize(matrix: tuple[sp.Expr, ...]) -> tuple[sp.Expr, ...]:
    first = next(entry for entry in matrix if entry != 0)
    return tuple(sp.factor(entry / first) for entry in matrix)


automorphisms: set[tuple[sp.Expr, ...]] = set()
for src in itertools.permutations(SLOPES, 3):
    for dst in itertools.permutations(SLOPES, 3):
        matrix = mobius_from(src, dst)
        if matrix is None:
            continue
        a, b, c, d = matrix
        images = []
        valid = True
        for slope in SLOPES:
            denominator = c * slope + d
            if denominator == 0:
                valid = False
                break
            images.append(sp.factor((a * slope + b) / denominator))
        if valid and set(images) == set(SLOPES):
            automorphisms.add(normalize(matrix))

gradients = [sp.Matrix([-slope, 1]) for slope in SLOPES]
pair_determinants = [
    int(sp.Matrix.hstack(gradients[i], gradients[j]).det())
    for i in range(len(SLOPES))
    for j in range(i + 1, len(SLOPES))
]
if any(value == 0 for value in pair_determinants):
    raise SystemExit("FAIL: quasi-local pair transversality")

vandermonde = sp.Matrix([[slope**power for power in range(4)] for slope in SLOPES])
curvature = sp.Matrix([slope**4 for slope in SLOPES])
augmented = vandermonde.row_join(curvature)
if vandermonde.rank() != 4 or augmented.rank() != 5:
    raise SystemExit("FAIL: quartic curvature does not obstruct cubic jet action")
if automorphisms != {(sp.Integer(1), sp.Integer(0), sp.Integer(0), sp.Integer(1))}:
    raise SystemExit("FAIL: slope set has a nontrivial projective stabilizer")

actual = {
    "slopes": [int(value) for value in SLOPES],
    "pair_determinants": pair_determinants,
    "projective_stabilizer_size": len(automorphisms),
    "cubic_evaluation_rank": vandermonde.rank(),
    "augmented_curvature_rank": augmented.rank(),
    "simultaneously_linearizable": False,
    "scope": "quadratic-jet analytic obstruction only",
}
expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: NG036 quasi-local analytic-linearization obstruction")
