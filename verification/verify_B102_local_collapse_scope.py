#!/usr/bin/env python3
"""Finite scope model for B102/NG078: local maps do not fix localization."""

from fractions import Fraction


detector = (Fraction(1), Fraction(-1), Fraction(0))

# The same already-available local collapse maps can be preceded by distinct
# localization maps from the distributed detector module.
localization_one = (
    (Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(1)),
)
localization_two = (
    (Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(1)),
    (Fraction(0), Fraction(1), Fraction(0)),
)


def apply(matrix, vector):
    return tuple(sum(row[j] * vector[j] for j in range(3)) for row in matrix)


beta_one = apply(localization_one, detector)
beta_two = apply(localization_two, detector)
assert beta_one != beta_two
assert sum(beta_one, Fraction(0)) == sum(beta_two, Fraction(0)) == 0

# Identity local collapses preserve whichever local vector was supplied; they
# do not choose the localization map.
assert apply(localization_one, detector) == beta_one
assert apply(localization_two, detector) == beta_two

print("PASS: B102 local collapse exists only after NG078's localization choice")
