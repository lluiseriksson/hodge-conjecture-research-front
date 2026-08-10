#!/usr/bin/env python3
"""Finite linear model for B104's lift-independent obstruction coset."""

from fractions import Fraction

# H_(2n)(W,N)=Q^2 and j_*A is the second coordinate axis.
t_w = (Fraction(5), Fraction(7))
gamma_zero = (Fraction(5), Fraction(2))
absolute_ambiguity = (Fraction(0), Fraction(5))


def add(left, right):
    return tuple(x + y for x, y in zip(left, right))


def subtract(left, right):
    return tuple(x - y for x, y in zip(left, right))


def obstruction_coset(representative):
    # Quotient by the second coordinate axis.
    return subtract(t_w, representative)[0]


assert obstruction_coset(gamma_zero) == 0
gamma_bordant = add(gamma_zero, absolute_ambiguity)
assert gamma_bordant == t_w
assert obstruction_coset(gamma_bordant) == 0

# A nonzero first coordinate cannot be changed by absolute lift ambiguity.
wrong_gamma = (Fraction(4), Fraction(2))
assert obstruction_coset(wrong_gamma) == 1
assert obstruction_coset(add(wrong_gamma, absolute_ambiguity)) == 1

# Primitive ambient value is the first coordinate and is preserved.
assert t_w[0] == gamma_bordant[0] == Fraction(5)

print("PASS: B104 lift-independent bordism obstruction coset")
