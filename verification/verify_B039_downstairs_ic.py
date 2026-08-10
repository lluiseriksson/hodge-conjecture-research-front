#!/usr/bin/env python3
"""Shift/support bookkeeping for B039; not an MHS or Hodge-type proof."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B039-downstairs-ic-check.json"


ordinary_resolved_degrees = [0, 1, 2]
surface_shift = 2
perverse_stalk_degrees = [d - surface_shift for d in ordinary_resolved_degrees]

if max(perverse_stalk_degrees) > 0:
    raise SystemExit("FAIL: the origin stalk violates the perverse upper bound")

point_perverse_degree = 0
point_ordinary_degree = point_perverse_degree + surface_shift
if point_ordinary_degree == 1:
    raise SystemExit("FAIL: point-supported summand contaminates ordinary H^1")

actual = {
    "surface_dimension": surface_shift,
    "resolved_ordinary_amplitude": ordinary_resolved_degrees,
    "shifted_perverse_stalk_amplitude": perverse_stalk_degrees,
    "extra_support": "origin only",
    "point_summand_perverse_degree": point_perverse_degree,
    "point_summand_ordinary_degree": point_ordinary_degree,
    "ordinary_degree_one_contribution_from_point_summand": 0,
    "conclusion": "resolved H1 equals downstairs IC-stalk H1",
    "scope": "exact shift and support bookkeeping only",
}

expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B039 point-supported summands cannot alter ordinary degree one")
