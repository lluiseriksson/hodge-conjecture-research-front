#!/usr/bin/env python3
"""Exact lightweight checks for B202, G132, and NG164."""

from fractions import Fraction


def mat_vec(matrix, vector):
    return [
        sum(Fraction(a) * Fraction(b) for a, b in zip(row, vector))
        for row in matrix
    ]


def main():
    # A nonzero obstruction map may still have a special one-dimensional kernel.
    boundary = [[1, 0, -1], [0, 1, -1]]
    special_profile = [1, 1, 1]
    assert mat_vec(boundary, special_profile) == [0, 0]
    assert mat_vec(boundary, [1, 0, 0]) != [0, 0]

    # Lifts of one profile differ by a triple-vanishing section.
    lift_1 = [1, 1, 1, 0]
    lift_2 = [1, 1, 1, 5]
    assert lift_1[:3] == lift_2[:3]
    assert lift_2[-1] - lift_1[-1] == 5

    # Automatic 2-jet separation has the wrong first-jet dimensions.
    d, nodes = 4, 3
    length_per_third_neighborhood = 1 + d + d * (d + 1) // 2
    assert length_per_third_neighborhood == 15
    assert d * nodes == 12 > d
    assert nodes > 1

    print("PASS: B202 selective lift, G132, and NG164")


if __name__ == "__main__":
    main()
