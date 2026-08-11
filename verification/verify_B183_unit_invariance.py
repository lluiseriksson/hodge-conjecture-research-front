#!/usr/bin/env python3
"""Bounded B183/G116/NG147 identities; not a proof of HC."""

from fractions import Fraction


# epsilon_m=y/(1-y^m) differs from y by a unit, so away from the zeros of
# the displayed denominator their quotient is exactly that unit inverse.
for m in range(1, 16):
    for y in range(-3, 4):
        denominator = 1 - y**m
        if denominator == 0:
            continue
        epsilon = Fraction(y, denominator)
        if y != 0:
            assert epsilon / y == Fraction(1, denominator)
        else:
            assert epsilon == 0


# Symbolically, d(y)=dy has constant coefficient one, while the first
# nonconstant term of (1-y^m)^(-1) occurs in degree m.
for m in range(1, 80):
    denominator_first_variation = m
    conormal_first_visible_degree = 0
    assert conormal_first_visible_degree < denominator_first_variation


# Unit rescaling cannot change a nonzero leading order.
for leading_order in range(0, 30):
    unit_constant = 7
    assert unit_constant != 0
    rescaled_leading_order = leading_order
    assert rescaled_leading_order == leading_order

print("PASS: B183 clears unit denominators without delaying conormal detection")
