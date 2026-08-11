#!/usr/bin/env python3
"""Finite linear-algebra guards for B156; not an analytic proof or HC."""

from fractions import Fraction


def rank(matrix):
    rows = [[Fraction(value) for value in row] for row in matrix]
    if not rows:
        return 0
    row_count = len(rows)
    column_count = len(rows[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if rows[row][column]),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [value / scale for value in rows[pivot_row]]
        for row in range(row_count):
            if row != pivot_row and rows[row][column]:
                factor = rows[row][column]
                rows[row] = [
                    value - factor * pivot_value
                    for value, pivot_value in zip(rows[row], rows[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def multiply(left, right):
    return [
        [sum(a * b for a, b in zip(row, column)) for column in zip(*right)]
        for row in left
    ]


# I/mI has R visible generators and H hidden generators. Extra columns are
# redundant analytic generators. The defect identities must hold for a
# range of exact rational matrices.
for visible in range(1, 6):
    for hidden in range(0, 5):
        minimal = visible + hidden
        for redundant in range(0, 5):
            generator_map = [
                [
                    Fraction(int(row == column))
                    if column < minimal
                    else Fraction((row + 2) * (column + 1))
                    for column in range(minimal + redundant)
                ]
                for row in range(minimal)
            ]
            cotangent_map = [
                [Fraction(int(row == column)) for column in range(minimal)]
                for row in range(visible)
            ]
            differential_map = multiply(cotangent_map, generator_map)

            mu = rank(generator_map)
            differential_rank = rank(differential_map)
            syzygy_value_dimension = len(generator_map[0]) - mu
            linear_relation_dimension = len(generator_map[0]) - differential_rank
            defect_dimension = mu - differential_rank

            assert mu == minimal
            assert differential_rank == visible
            assert defect_dimension == hidden
            assert linear_relation_dimension - syzygy_value_dimension == hidden


# For tau_m=(x,x+y^m), the minimal-generator matrix is invertible, but its
# cotangent image has rank one: one linear relation survives as one hidden
# nonlinear generator and no nonzero constant syzygy exists.
generator_map = [[1, 1], [0, 1]]
cotangent_map = [[1, 0]]
differential_map = multiply(cotangent_map, generator_map)
assert rank(generator_map) == 2
assert rank(differential_map) == 1
assert 2 - rank(generator_map) == 0
assert (2 - rank(differential_map)) - (2 - rank(generator_map)) == 1

print("PASS: B156 syzygy-evaluation exact sequence and hidden-generator defect")
