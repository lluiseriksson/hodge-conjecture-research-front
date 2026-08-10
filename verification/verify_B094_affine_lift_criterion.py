#!/usr/bin/env python3
"""Finite rational checks for B094's affine lift criterion."""

from fractions import Fraction


def has_detecting_lift(base_value, ambiguity_values):
    candidates = [base_value]
    candidates.extend(base_value + value for value in ambiguity_values)
    return any(value != 0 for value in candidates)


cases = [
    (Fraction(0), [Fraction(0)], False),
    (Fraction(2), [Fraction(0)], True),
    (Fraction(0), [Fraction(3)], True),
    (Fraction(2), [Fraction(-2), Fraction(0)], True),
]

for base, ambiguity, expected in cases:
    criterion = base != 0 or any(value != 0 for value in ambiguity)
    assert criterion == expected
    assert has_detecting_lift(base, ambiguity) == expected

print("PASS: B094 affine lift-pairing disjunction")
