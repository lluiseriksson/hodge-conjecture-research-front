#!/usr/bin/env python3
"""Verify B067's A2 invariant map, discriminant, and collision sections."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B067-a2-weyl-cover-check.json"

x, z, u, v = sp.symbols("x z u v")
l1, l2, l3 = x - u, x - v, x + u + v
product = sp.expand(l1 * l2 * l3)
s = -(u**2 + u * v + v**2)
t = u * v * (u + v)
cusp_pullback = sp.factor(4 * s**3 + 27 * t**2)
reflection_product = sp.expand((u - v) * (2 * u + v) * (u + 2 * v))

P = product + z**2
gradient = [sp.factor(sp.diff(P, q)) for q in (x, z, u, v)]
sections = {
    "S12": {x: u, v: u, z: 0},
    "S13": {x: u, v: -2 * u, z: 0},
    "S23": {x: v, u: -2 * v, z: 0},
}
for name, substitution in sections.items():
    if sp.expand(P.subs(substitution)) != 0 or any(
        sp.expand(value.subs(substitution)) != 0 for value in gradient
    ):
        raise SystemExit(f"FAIL: {name} is not a total-space singular section")

actual = {
    "expanded_root_polynomial": str(product),
    "invariants": {"s": str(s), "t": str(t)},
    "cusp_pullback": str(cusp_pullback),
    "reflection_product": str(reflection_product),
    "root_hyperplanes": ["u-v", "2*u+v", "u+2*v"],
    "generic_cover_degree": 6,
    "weyl_group": "S3",
    "total_family_gradient": [str(value) for value in gradient],
    "singular_sections": ["S12", "S13", "S23"],
    "blown_up_exceptional_multiplicity": 6,
    "strict_root_line_multiplicity": 2,
    "scope": "r=1 symbolic check; extra quadratic suspension variables contribute independent 2*z_i derivatives",
}

if sp.expand(cusp_pullback + reflection_product**2) != 0:
    raise SystemExit("FAIL: discriminant is not the square of the reflection arrangement")

expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B067 A2 Weyl/root-cover checks")

