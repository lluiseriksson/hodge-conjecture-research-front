#!/usr/bin/env python3
"""Exact shift convolution for B079; this is not a proof of G044."""

normal_exceptional_degrees = [2]
curve_coefficient_degrees = [0, 1, 2]
proper_support_degrees = sorted(
    a + b for a in normal_exceptional_degrees for b in curve_coefficient_degrees
)

assert proper_support_degrees == [2, 3, 4]
assert 3 in proper_support_degrees
assert 3 % 2 == 1

print("PASS: B079 coefficient convolution produces proper-support degrees 2, 3, 4")
