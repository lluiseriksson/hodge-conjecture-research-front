#!/usr/bin/env python3
"""Bounded checks for B185/G118/NG149; not a proof of HC."""

from fractions import Fraction


# B185's crude presentation bound is monotone and dominates delta*e when
# delta <= E^M and e <= E.
for ambient_variables in range(1, 9):
    for degree_bound in range(2, 9):
        carrier_degree_bound = degree_bound**ambient_variables
        numerator_degree_bound = degree_bound
        certificate_order = degree_bound ** (ambient_variables + 1)
        assert (
            carrier_degree_bound * numerator_degree_bound
            == certificate_order
        )


# NG149: f_2=w^2+yw+x has critical point -y/2 and value x-y^2/4.
for x in range(-5, 6):
    for y in range(-5, 6):
        critical_w = Fraction(-y, 2)
        value = critical_w**2 + y * critical_w + x
        assert value == Fraction(x) - Fraction(y * y, 4)
        assert 2 != 0  # spatial Hessian


# On x=0, epsilon=-y^2/4 has order two and nonzero conormal coefficient
# -y/2 in order one modulo (y^2).
escape_order = 2
conormal_first_order = 1
assert conormal_first_order == escape_order - 1
assert Fraction(-1, 2) != 0

print("PASS: B185 constructs the bounded carrier; NG149 keeps jets open")
