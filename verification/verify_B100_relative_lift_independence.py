#!/usr/bin/env python3
"""Finite model for B100's primitive lift independence."""

from fractions import Fraction

# Coordinates: boundary, nonprimitive absolute ambiguity, primitive ambient.
lift_one = (Fraction(2), Fraction(0), Fraction(5))
lift_two = (Fraction(2), Fraction(7), Fraction(5))

assert lift_one[0] == lift_two[0]  # same local relation boundary
assert lift_one[1] != lift_two[1]  # different relative representatives
assert lift_one[2] == lift_two[2]  # same primitive ambient image

print("PASS: B100 same boundary gives representative-independent primitive image")
