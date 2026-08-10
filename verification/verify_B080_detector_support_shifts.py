#!/usr/bin/env python3
"""Dimension/shift identities for B080; not a multiplicity calculation."""

for n in range(1, 51):
    total_dimension = 2 * n + 1
    detector_raw_degree = total_dimension - 1
    assert detector_raw_degree == 2 * n
    for codimension in (0, 1, 2):
        support_dimension = 2 - codimension
        shift_b = support_dimension - 1
        normalized_degree = shift_b - support_dimension
        parity_expression = shift_b + total_dimension - support_dimension
        assert shift_b == 1 - codimension
        assert normalized_degree == -1
        assert parity_expression == 2 * n
        assert parity_expression % 2 == 0

print("PASS: B080 full, divisor, and point total-degree shifts are toric-parity allowed")
