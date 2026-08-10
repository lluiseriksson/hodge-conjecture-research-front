#!/usr/bin/env python3
"""Strict one-dimensional countermodel for B092."""

from fractions import Fraction

t_nearby = Fraction(1)
beta_special = t_nearby  # S -> P is the identity.
can_obstruction = Fraction(0)

rho_zero = Fraction(0) * beta_special
rho_identity = Fraction(1) * beta_special

assert can_obstruction == 0
assert rho_zero == 0
assert rho_identity != 0
print("PASS: B092 identical lift data allow zero or nonzero local component")
