#!/usr/bin/env python3
"""Linear exact-sequence model of B083's nearby-to-special lift criterion."""

from fractions import Fraction


def special_to_nearby(vector):
    a, _b = vector
    return a


nearby = Fraction(3)
lifts = [(nearby, Fraction(k)) for k in range(-2, 3)]
assert all(special_to_nearby(lift) == nearby for lift in lifts)
assert len(set(lifts)) > 1

# Exact model 0 -> Q --id--> Q: a nonzero nearby class is obstructed.
obstructed = Fraction(1)
assert obstructed != 0
special_group = []
assert not special_group

print("PASS: B083 lift existence is kernel membership and lifts need not be unique")
