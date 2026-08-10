#!/usr/bin/env python3
"""Finite quotient model for B098's equator/base-locus independence."""

from fractions import Fraction

# Coordinates: equator, base-locus, primitive ambient.
def ambient_map(vector):
    return vector[2]


t = (Fraction(7), Fraction(-4), Fraction(3))
equator_change = (Fraction(5), Fraction(0), Fraction(0))
base_change = (Fraction(0), Fraction(11), Fraction(0))

changed = tuple(t[i] + equator_change[i] + base_change[i] for i in range(3))
assert ambient_map(t) == ambient_map(changed) == Fraction(3)
print("PASS: B098 nearby ambient value survives both quotient kernels")
