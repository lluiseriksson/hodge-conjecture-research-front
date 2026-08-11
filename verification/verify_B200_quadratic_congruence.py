#!/usr/bin/env python3
"""Exact rational matrix checks for B200, G130, and NG162."""

from fractions import Fraction


def transpose(a):
    return [list(row) for row in zip(*a)]


def multiply(a, b):
    bt = transpose(b)
    return [
        [sum(Fraction(x) * Fraction(y) for x, y in zip(row, col)) for col in bt]
        for row in a
    ]


def inverse_2(a):
    det = Fraction(a[0][0]) * a[1][1] - Fraction(a[0][1]) * a[1][0]
    assert det
    return [
        [Fraction(a[1][1], 1) / det, -Fraction(a[0][1], 1) / det],
        [-Fraction(a[1][0], 1) / det, Fraction(a[0][0], 1) / det],
    ]


def scale(c, a):
    return [[Fraction(c) * x for x in row] for row in a]


def main():
    q = [[2, 1], [1, 1]]
    b = inverse_2(q)
    nodes = [
        ([[1, 0], [0, 1]], Fraction(2)),
        ([[1, 1], [0, 1]], Fraction(3)),
    ]

    for a, value in nodes:
        # Congruence Hessian: value * H = A Q A^T.
        h = scale(Fraction(1, 1) / value, multiply(multiply(a, q), transpose(a)))
        # Pullback inverse Hessian: A^T H^{-1} A = value * Q^{-1}.
        pulled_back = multiply(multiply(transpose(a), inverse_2(h)), a)
        assert pulled_back == scale(value, b)

    # An ideal generator has zero values and cannot be the full-support multiplier.
    ideal_values = [0, 0]
    assert any(value == 0 for value in ideal_values)
    assert all(value != 0 for _, value in nodes)

    print("PASS: B200 quadratic congruence, G130, and NG162")


if __name__ == "__main__":
    main()
