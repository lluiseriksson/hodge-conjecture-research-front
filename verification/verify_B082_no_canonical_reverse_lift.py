#!/usr/bin/env python3
"""Finite-dimensional model for B082's forward-quotient directionality."""

from fractions import Fraction


def shear(t, vector):
    """Automorphism (x,y) -> (x,y+t*x), preserving q(x,y)=x."""
    x, y = vector
    return x, y + t * x


target = Fraction(1)
lifts = [(target, Fraction(y)) for y in range(-3, 4)]

assert all(x == target for x, _ in lifts)
assert len(set(lifts)) > 1

# No lift of 1 is fixed by every automorphism preserving the quotient map.
for lift in lifts:
    assert shear(Fraction(1), lift) != lift

# A prospective local subspace can have zero image despite a nonzero target.
local_subspace = [(Fraction(0), Fraction(y)) for y in range(-3, 4)]
assert all(x == 0 for x, _ in local_subspace)
assert target not in {x for x, _ in local_subspace}

print("PASS: B082 forward quotients give neither a canonical reverse lift nor a fixed-local lift")
