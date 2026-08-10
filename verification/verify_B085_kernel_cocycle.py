#!/usr/bin/env python3
"""Exact linear model for B085's kernel-valued monodromy obstruction."""

from fractions import Fraction


def monodromy(vector):
    x, y = vector
    return x, x + y


def quotient(vector):
    x, _y = vector
    return x


t = (Fraction(1), Fraction(0))
d = tuple(a - b for a, b in zip(monodromy(t), t))
assert quotient(monodromy(t)) == quotient(t)
assert d == (0, 1)

# M is the identity on J=Q(0,1), so im(M_J-I)=0 and the defect survives.
kernel_generator = (Fraction(0), Fraction(1))
assert monodromy(kernel_generator) == kernel_generator
for k in range(-5, 6):
    adjusted = (t[0], t[1] + Fraction(k))
    assert monodromy(adjusted) != adjusted

print("PASS: B085 fixed quotient can carry a nonzero kernel cocycle with no invariant lift")
