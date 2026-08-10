#!/usr/bin/env python3
"""Finite tangent-form model for B089's marked plane-slice avoidance."""

from fractions import Fraction

forms = [
    (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(1), Fraction(0)),
]
v0 = (Fraction(1), Fraction(1), Fraction(1), Fraction(0))
w = (Fraction(0), Fraction(1), Fraction(2), Fraction(1))


def evaluate(form, vector):
    return sum(a * b for a, b in zip(form, vector))


restricted = [(evaluate(form, v0), evaluate(form, w)) for form in forms]
for i in range(len(restricted)):
    for j in range(i + 1, len(restricted)):
        ai, bi = restricted[i]
        aj, bj = restricted[j]
        assert ai * bj - aj * bi != 0

print("PASS: B089 marked two-plane has distinct restricted branch tangents")
