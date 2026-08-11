#!/usr/bin/env python3
"""Finite matrix/jet guards for B155/NG125; not an analytic proof or HC."""

from fractions import Fraction


def multiply(left, right):
    return [
        [sum(a * b for a, b in zip(row, column)) for column in zip(*right)]
        for row in left
    ]


# Constant rank-R factorizations A=[I;C] have the explicit left inverse
# B=[I,0], so (tau)=(f) in this finite model.
for rank in range(1, 7):
    for extra_rows in range(1, 6):
        identity = [
            [Fraction(int(row == column)) for column in range(rank)]
            for row in range(rank)
        ]
        lower = [
            [Fraction((row + 1) * (column + 2)) for column in range(rank)]
            for row in range(extra_rows)
        ]
        matrix_a = identity + lower
        matrix_b = [
            [Fraction(int(column == row)) for column in range(rank + extra_rows)]
            for row in range(rank)
        ]
        assert multiply(matrix_b, matrix_a) == identity


# No fixed finite jet order distinguishes the integrable germ (x,x) from
# tau_m=(x,x+y^m): all coefficients below m agree.
for checked_order in range(2, 15):
    exponent = checked_order + 1
    smooth_series = [Fraction(0)] * (exponent + 1)
    obstructed_series = [Fraction(0)] * (exponent + 1)
    obstructed_series[exponent] = Fraction(1)
    assert smooth_series[: checked_order + 1] == obstructed_series[: checked_order + 1]
    assert obstructed_series[exponent] == 1

print("PASS: B155 left-inverse factorization and NG125 all-order family")
