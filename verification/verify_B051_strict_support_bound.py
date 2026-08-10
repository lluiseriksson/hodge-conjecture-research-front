#!/usr/bin/env python3
"""Exact shift checks for B051; not a decomposition-theorem proof."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B051-strict-support-bound-check.json"

checked = []
for codimension in range(2, 21):
    fiber_dimension = codimension - 1
    constant_row_top = 2 * fiber_dimension
    coefficient_row_top = 1 + 2 * (fiber_dimension - 1)
    perverse_radius = constant_row_top - codimension
    first_lower_support_degree = codimension - perverse_radius
    if coefficient_row_top > constant_row_top:
        raise SystemExit("FAIL: coefficient row exceeds constant-row amplitude")
    if perverse_radius != codimension - 2:
        raise SystemExit("FAIL: perverse-radius arithmetic")
    if first_lower_support_degree != 2:
        raise SystemExit("FAIL: lower support can enter degree one")
    checked.append(
        {
            "codimension": codimension,
            "fiber_dimension": fiber_dimension,
            "constant_row_top": constant_row_top,
            "coefficient_row_top": coefficient_row_top,
            "perverse_interval": [-perverse_radius, perverse_radius],
            "first_lower_support_degree": first_lower_support_degree,
        }
    )

actual = {"codimensions": checked, "scope": "shift arithmetic only"}
expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B051 strict-support shift bounds")
