#!/usr/bin/env python3
"""Bookkeeping for B081/B121's three total-degree-minus-one positions."""

detector_total_degree = -1
positions = {
    "ambient_full_b1": (-2, 1),
    "full_or_divisor_b0": (-1, 0),
    "point_b_minus_1": (0, -1),
}

for position in positions.values():
    assert sum(position) == detector_total_degree

assert positions["ambient_full_b1"][1] == 1
assert positions["full_or_divisor_b0"][1] == 0
assert positions["point_b_minus_1"][1] == -1
assert len(set(positions.values())) == 3

print("PASS: B081/B121 separate ambient, relation/divisor, and point grades")
