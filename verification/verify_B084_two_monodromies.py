#!/usr/bin/env python3
"""Exact guard: invariance for one action does not imply invariance for another."""

from fractions import Fraction

alpha = (Fraction(1), Fraction(0))


def detector_monodromy(v):
    return v


def collision_monodromy(v):
    x, y = v
    return (x, x + y)


assert detector_monodromy(alpha) == alpha
assert collision_monodromy(alpha) != alpha

print("PASS: B084/NG061 separate detector-loop invariance from collision invariance")
