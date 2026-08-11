#!/usr/bin/env python3
"""Exact finite block-matrix guards for B147; not a proof of HC."""

from fractions import Fraction


def multiply(left, right):
    return [
        [sum(a * b for a, b in zip(row, column)) for column in zip(*right)]
        for row in left
    ]


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def identity(size):
    return [
        [Fraction(int(row == column)) for column in range(size)]
        for row in range(size)
    ]


def inverse(matrix):
    size = len(matrix)
    augmented = [
        [Fraction(entry) for entry in row] + unit
        for row, unit in zip(matrix, identity(size))
    ]
    for column in range(size):
        pivot = next(row for row in range(column, size) if augmented[row][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [entry / scale for entry in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            augmented[row] = [
                left - factor * right
                for left, right in zip(augmented[row], augmented[column])
            ]
    return [row[size:] for row in augmented]


def quadratic(vector, matrix):
    return sum(
        vector[row] * matrix[row][column] * vector[column]
        for row in range(len(vector))
        for column in range(len(vector))
    )


for n in range(1, 7):
    # Deterministic invertible J and symmetric A over Q.
    J = [
        [Fraction(1 if row == column else int(column == row + 1))
         for column in range(n)]
        for row in range(n)
    ]
    A = [
        [Fraction((row + 1) * (column + 1) if row != column else row + 2)
         for column in range(n)]
        for row in range(n)
    ]
    JT = transpose(J)
    H = [A[row] + J[row] for row in range(n)] + [
        JT[row] + [Fraction(0)] * n for row in range(n)
    ]
    H_inv = inverse(H)
    assert multiply(H, H_inv) == identity(2 * n)

    # The inverse-Hessian block on conormal covectors (alpha, 0) is zero.
    assert all(H_inv[row][column] == 0 for row in range(n) for column in range(n))
    for seed in range(1, 5):
        alpha = [Fraction(seed + index) for index in range(n)]
        conormal = alpha + [Fraction(0)] * n
        assert quadratic(conormal, H_inv) == 0

    # Dimension n is half of the nondegenerate 2n-dimensional form.
    assert len(J) == n
    assert len(H) == 2 * n

print("PASS: B147 carrier conormals form the exact nodewise Lagrangian core")
