#!/usr/bin/env python3
"""Finite matrix illustration for B055; not the abstract proof."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B055-local-system-rigidity-check.json"

rho = sp.Matrix([[1, 1, 0], [0, 1, 0], [0, 0, 1]])
phi = sp.Matrix([[0, 0, 1]])

commutes = phi * rho == phi
if not commutes:
    raise SystemExit("FAIL: sample is not a morphism to a constant local system")

orbit_rows = [phi * (rho**power) for power in range(6)]
stacked = sp.Matrix.vstack(*orbit_rows)

actual = {
    "monodromy_matrix": [[int(rho[i, j]) for j in range(rho.cols)] for i in range(rho.rows)],
    "ambient_map": [[int(phi[i, j]) for j in range(phi.cols)] for i in range(phi.rows)],
    "commutes_to_constant_target": commutes,
    "ambient_rank": phi.rank(),
    "kernel_rank": len(phi.nullspace()),
    "orbit_image_rank": stacked.rank(),
    "scope": "finite matrix illustration only; B055 is proved abstractly",
}

expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B055 local-system ambient-image rigidity illustration")
