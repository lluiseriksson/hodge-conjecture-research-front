#!/usr/bin/env python3
"""Verify B059's strict rational linear-algebra countermodel."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B059-pairing-versus-exact-class-check.json"

zeta = sp.Matrix([[1, 0]])
c = sp.Matrix([1, 0])
d = sp.Matrix([1, 1])
detector = sp.Matrix.hstack(d)
augmented = sp.Matrix.hstack(d, c)

actual = {
    "specified_functional": [int(value) for value in zeta],
    "preselected_class": [int(value) for value in c],
    "detector_generator": [int(value) for value in d],
    "preselected_pairing": int((zeta * c)[0]),
    "detector_pairing": int((zeta * d)[0]),
    "detector_rank": detector.rank(),
    "augmented_rank": augmented.rank(),
    "preselected_class_in_detector_span": detector.rank() == augmented.rank(),
    "scope": "finite rational type-(0,0) linear-algebra countermodel only",
}

if actual["detector_pairing"] == 0:
    raise SystemExit("FAIL: detector does not pair nontrivially")
if actual["preselected_class_in_detector_span"]:
    raise SystemExit("FAIL: preselected class unexpectedly lies in detector span")

expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B059 pairing versus exact-class strictness countermodel")
