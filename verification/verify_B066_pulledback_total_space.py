#!/usr/bin/env python3
"""Verify B066's pullback equations and boundary singular loci."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B066-pulledback-total-space-check.json"

x, z, a, c, b, d = sp.symbols("x z a c b d")

Fa = x**3 + a**2 * c * x + a**3 * c**2 + z**2
Fb = x**3 + b**2 * d * x + b**3 * d + z**2

grad_a = [sp.factor(sp.diff(Fa, q)) for q in (x, z, a, c)]
grad_b = [sp.factor(sp.diff(Fb, q)) for q in (x, z, b, d)]

def all_zero(expressions: list[sp.Expr], substitution: dict[sp.Symbol, sp.Expr]) -> bool:
    return all(sp.expand(expr.subs(substitution)) == 0 for expr in expressions)

if not all_zero([Fa, *grad_a], {x: 0, z: 0, a: 0}):
    raise SystemExit("FAIL: a=0 boundary section is not singular")
if not all_zero([Fa, *grad_a], {x: 0, z: 0, c: 0}):
    raise SystemExit("FAIL: c=0 boundary section is not singular")
if not all_zero([Fb, *grad_b], {x: 0, z: 0, b: 0}):
    raise SystemExit("FAIL: b=0 boundary section is not singular")
if all_zero([Fb, *grad_b], {x: 0, z: 0, d: 0}):
    raise SystemExit("FAIL: generic E1 section should be smooth in total space")

# Off both axes, the last two derivatives give incompatible values of x.
off_axis_a_resultant = sp.factor(
    sp.resultant(2 * x + 3 * a * c, x + 2 * a * c, x)
)
off_axis_b_resultant = sp.factor(
    sp.resultant(2 * x + 3 * b, x + b, x)
)

actual = {
    "a_chart_base_map": {"s": "a**2*c", "t": "a**3*c**2"},
    "a_chart_equation": str(Fa),
    "a_chart_gradient": [str(value) for value in grad_a],
    "a_chart_off_axis_resultant": str(off_axis_a_resultant),
    "b_chart_base_map": {"s": "b**2*d", "t": "b**3*d"},
    "b_chart_equation": str(Fb),
    "b_chart_gradient": [str(value) for value in grad_b],
    "b_chart_off_axis_resultant": str(off_axis_b_resultant),
    "singular_loci": {
        "a_chart": ["x=z=a=0", "x=z=c=0"],
        "b_chart": ["x=z=b=0"],
    },
    "scope": "r=1 symbolic Jacobian model; additional quadratic variables behave identically",
}

expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B066 resolved-base pullback total-space singularity checks")
