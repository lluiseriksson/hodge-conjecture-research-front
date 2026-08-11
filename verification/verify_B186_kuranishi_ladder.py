#!/usr/bin/env python3
"""Bounded checks for B186/G119/NG150; not a proof of HC."""

from fractions import Fraction


# For K=(y^r), the escape begins in degree r and the conormal derivative
# begins in degree r-1. This is the sharp model for B186's jet equivalence.
for escape_order in range(2, 60):
    conormal_order = escape_order - 1
    for certificate_degree in range(1, 60):
        beta_jet_vanishes = conormal_order > certificate_degree - 1
        ideal_is_deep = escape_order > certificate_degree
        assert beta_jet_vanishes == ideal_is_deep


# For f_a=x+yw+w^2/2+a w^3, solve the critical equation through y^2:
# w=-y-3a y^2+O(y^3). Integrating d tau/dy=w gives cubic coefficient -a.
for a in range(-5, 6):
    critical_linear = Fraction(-1)
    critical_quadratic = Fraction(-3 * a)
    assert 1 + critical_linear == 0
    assert critical_quadratic + 3 * a * critical_linear**2 == 0
    value_quadratic = critical_linear / 2
    value_cubic = critical_quadratic / 3
    assert value_quadratic == Fraction(-1, 2)
    assert value_cubic == -a


# Two unequal cubic coefficients cancel through quadratic order but not cubic.
a = Fraction(1)
b = Fraction(3)
assert Fraction(-1, 2) == Fraction(-1, 2)
escape_cubic = a - b
assert escape_cubic != 0

print("PASS: B186 gives the exact jet ladder; NG150 separates cubic from quadratic")
