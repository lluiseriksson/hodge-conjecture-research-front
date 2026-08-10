#!/usr/bin/env python3
"""Exact integer check of the complete-intersection calculation in B031.

This checks only the Hilbert-function arithmetic. It does not prove the
geometric nodality, specialization sequence, or any Hodge statement.
"""

from __future__ import annotations

import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B031-plane-family-check.json"


def forms_in_three_variables(degree: int) -> int:
    return comb(degree + 2, 2) if degree >= 0 else 0


def ci_hilbert_value(d: int) -> int:
    """Hilbert value at 2d-5 for a (d-1,d-1) CI in P^2."""
    t = 2 * d - 5
    a = d - 1
    return (
        forms_in_three_variables(t)
        - 2 * forms_in_three_variables(t - a)
        + forms_in_three_variables(t - 2 * a)
    )


data = json.loads(EXPECTED.read_text(encoding="utf-8"))
first = data["degree_min"]
last = data["degree_max"]
assert first >= 3

samples: list[dict[str, int]] = []
for d in range(first, last + 1):
    length = (d - 1) ** 2
    value = ci_hilbert_value(d)
    defect = length - value
    assert defect == 1, (d, length, value, defect)
    if d in data["sample_degrees"]:
        samples.append(
            {
                "degree": d,
                "nodes": length,
                "hilbert_value_at_2d_minus_5": value,
                "evaluation_defect": defect,
            }
        )

assert samples == data["samples"]
print(
    "PASS: B031 exact Hilbert-function defect is 1 for "
    f"every tested degree {first}..{last}"
)

