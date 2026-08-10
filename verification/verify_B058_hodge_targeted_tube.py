#!/usr/bin/env python3
"""Finite B058 pairing/surjectivity illustration; not the Hodge theorem."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B058-hodge-targeted-tube-check.json"

pairing = sp.diag(2, 3)
zeta = sp.Matrix([1, 0])
target = sp.Matrix([1, 0])
tube = sp.Matrix([[1, 0, 1], [0, 1, 1]])
preimage = sp.Matrix([1, 0, 0])

pairing_value = int((zeta.T * pairing * target)[0])
recovered = tube * preimage

if pairing.det() == 0 or tube.rank() != 2:
    raise SystemExit("FAIL: sample pairing or tube map is not full rank")
if pairing_value == 0 or recovered != target:
    raise SystemExit("FAIL: selected Hodge target is not detected or recovered")

actual = {
    "hodge_pairing_matrix": [
        [int(pairing[i, j]) for j in range(pairing.cols)]
        for i in range(pairing.rows)
    ],
    "specified_class": [int(value) for value in zeta],
    "selected_hodge_homology_class": [int(value) for value in target],
    "nonzero_pairing": pairing_value,
    "tube_matrix": [
        [int(tube[i, j]) for j in range(tube.cols)]
        for i in range(tube.rows)
    ],
    "tube_rank": tube.rank(),
    "tube_preimage": [int(value) for value in preimage],
    "exact_target_recovery": bool(recovered == target),
    "scope": "finite rational linear-algebra illustration only",
}

expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B058 Hodge-targeted tube selection illustration")
