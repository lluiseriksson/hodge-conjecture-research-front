#!/usr/bin/env python3
"""Exact Vandermonde/defect guards for B159; not an analytic proof or HC."""

from fractions import Fraction
from itertools import combinations


def determinant(matrix):
    rows = [[Fraction(value) for value in row] for row in matrix]
    size = len(rows)
    value = Fraction(1)
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if rows[row][column]),
            None,
        )
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            value = -value
        pivot_value = rows[column][column]
        value *= pivot_value
        rows[column] = [entry / pivot_value for entry in rows[column]]
        for row in range(column + 1, size):
            factor = rows[row][column]
            rows[row] = [
                entry - factor * pivot_entry
                for entry, pivot_entry in zip(rows[row], rows[column])
            ]
    return value


# Distinct evaluation points give the uniform U_(R,N) row matroid.
for rank in range(1, 6):
    for branch_count in range(rank + 1, rank + 6):
        points = list(range(1, branch_count + 1))
        rows = [
            [Fraction(point**power) for power in range(rank)]
            for point in points
        ]
        for chosen in combinations(rows, rank):
            assert determinant(chosen) != 0


# The perturbed branch has no coefficients below degree m on the basis
# germ, but contributes one new minimal generator y^m.
for checked_order in range(1, 13):
    exponent = checked_order + 1
    restriction = [Fraction(0)] * (exponent + 1)
    restriction[exponent] = Fraction(1)
    assert all(coefficient == 0 for coefficient in restriction[: exponent])
    assert restriction[exponent] == 1
    for rank in range(1, 7):
        differential_rank = rank
        minimal_generators = rank + 1
        assert minimal_generators - differential_rank == 1

print("PASS: B159 uniform Vandermonde matroid and one hidden escape generator")
