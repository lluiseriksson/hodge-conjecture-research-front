#!/usr/bin/env python3
"""Verify the elementary product identity behind B088's Hurwitz move."""

from fractions import Fraction


def matmul(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def inv2(a):
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    return (
        (a[1][1] / det, -a[0][1] / det),
        (-a[1][0] / det, a[0][0] / det),
    )


m1 = ((Fraction(1), Fraction(1)), (Fraction(0), Fraction(1)))
m2 = ((Fraction(1), Fraction(0)), (Fraction(-1), Fraction(1)))
old_product = matmul(m2, m1)
new_first = m2
new_second = matmul(matmul(m2, m1), inv2(m2))
new_product = matmul(new_second, new_first)

assert new_product == old_product
print("PASS: B088 Hurwitz move preserves the ordered composite monodromy")
