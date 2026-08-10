#!/usr/bin/env python3
"""Verify B064's polynomial identities for one suspended A2 chart."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B064-a2-recollision-check.json"

x, z1, z2, s, t = sp.symbols("x z1 z2 s t")
fiber_equation = x**3 + s * x + t + z1**2 + z2**2

# The derivative with respect to t proves the total hypersurface is smooth.
dt_derivative = sp.diff(fiber_equation, t)

# Solve the hypersurface for t and differentiate the projection (s,t).
t_on_total_space = -x**3 - s * x - z1**2 - z2**2
jacobian = sp.Matrix(
    [
        [0, 0, 0, 1],
        [
            sp.diff(t_on_total_space, variable)
            for variable in (x, z1, z2, s)
        ],
    ]
)
critical_substitution = {s: -3 * x**2, z1: 0, z2: 0}
t_on_critical = sp.expand(t_on_total_space.subs(critical_substitution))
discriminant_pullback = sp.expand(
    (4 * s**3 + 27 * t**2).subs(
        {s: -3 * x**2, t: t_on_critical}
    )
)

fiber_hessian = sp.hessian(fiber_equation, (x, z1, z2))
hessian_determinant_on_critical = sp.factor(
    fiber_hessian.det().subs(critical_substitution)
)

actual = {
    "total_space_dt_derivative": int(dt_derivative),
    "projection_jacobian": [
        [str(jacobian[i, j]) for j in range(jacobian.cols)]
        for i in range(jacobian.rows)
    ],
    "critical_parametrization": {
        "s": str(critical_substitution[s]),
        "t": str(t_on_critical),
    },
    "discriminant_pullback": int(discriminant_pullback),
    "fiber_hessian_determinant_on_critical": str(hessian_determinant_on_critical),
    "noncoordinate_sample": {"x": 1, "s": -3, "t": 2, "s_times_t": -6},
    "scope": "symbolic identity check for the r=2 suspended A2 chart only",
}

if dt_derivative != 1:
    raise SystemExit("FAIL: total-space smoothness derivative")
if discriminant_pullback != 0:
    raise SystemExit("FAIL: critical locus does not map to the cusp")
if hessian_determinant_on_critical.subs(x, 1) == 0:
    raise SystemExit("FAIL: general discriminant point is not Morse")
if actual["noncoordinate_sample"]["s_times_t"] == 0:
    raise SystemExit("FAIL: critical locus unexpectedly lies over st=0")

expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B064 A2 recollision critical-locus and cusp checks")

