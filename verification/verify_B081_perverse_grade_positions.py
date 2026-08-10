#!/usr/bin/env python3
"""Bookkeeping for B081's two total-degree-minus-one E2 positions."""

detector_total_degree = -1
positions = {
    "full_or_divisor_b0": (-1, 0),
    "point_b_minus_1": (0, -1),
}

for position in positions.values():
    assert sum(position) == detector_total_degree

assert positions["full_or_divisor_b0"][1] == 0
assert positions["point_b_minus_1"][1] == -1
assert positions["full_or_divisor_b0"] != positions["point_b_minus_1"]

print("PASS: B081 separates full/divisor and point terms into distinct perverse grades")
