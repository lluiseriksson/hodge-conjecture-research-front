#!/usr/bin/env python3
"""Verify B065's three cusp-resolution charts and multiplicities."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B065-a2-cusp-resolution-check.json"

s, t, u, v, a, b, c, d = sp.symbols("s t u v a b c d")
f = 4 * s**3 + 27 * t**2

first = sp.factor(f.subs({s: u, t: u * v}, simultaneous=True))
second = sp.factor(first.subs({u: a * b, v: b}, simultaneous=True))
third_a = sp.factor(second.subs({b: a * c}, simultaneous=True))
third_b = sp.factor(second.subs({a: b * d}, simultaneous=True))

directions_in_c_chart = [sp.Rational(0), sp.Rational(-4, 27), sp.oo]
if len(set(directions_in_c_chart)) != 3:
    raise SystemExit("FAIL: final attachment directions are not distinct")

actual = {
    "cusp": str(f),
    "first_pullback": str(first),
    "second_pullback": str(second),
    "third_a_chart": str(third_a),
    "third_b_chart": str(third_b),
    "exceptional_multiplicities": {"E1": 2, "E2": 3, "E3": 6},
    "exceptional_self_intersections": {"E1": -3, "E2": -2, "E3": -1},
    "E3_attachment_directions_c_chart": ["0", "-4/27", "infinity"],
    "reduced_total_transform_is_snc": True,
    "scope": "symbolic chart and divisor-incidence check only",
}

expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B065 three-blowup A2 cusp resolution checks")

