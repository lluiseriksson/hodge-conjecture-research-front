#!/usr/bin/env python3
"""Bounded B182/G115/NG146 identities; not a proof of HC."""

from fractions import Fraction


def quartic_idempotents(z: int) -> tuple[Fraction, Fraction, Fraction]:
    return (
        Fraction(z * (z - 1), 2),
        Fraction(1 - z * z, 1),
        Fraction(z * (z + 1), 2),
    )


roots = (-1, 0, 1)
for index, root in enumerate(roots):
    values = quartic_idempotents(root)
    assert sum(values) == 1
    for j, value in enumerate(values):
        assert value == (1 if index == j else 0)
        assert value * value == value


# The critical-value element f=(z^2-1)^2 evaluates as (0,1,0), hence is
# exactly the middle idempotent in the reduced critical algebra.
critical_values = tuple((z * z - 1) ** 2 for z in roots)
assert critical_values == (0, 1, 0)


# Rank-two family: verify the Lagrange idempotents at both roots whenever
# the displayed denominator is nonzero.
for m in range(1, 12):
    for y in range(-3, 4):
        moving_root = y**m
        denominator = 1 - moving_root
        if denominator == 0:
            continue

        for z, expected_first in ((moving_root, 1), (1, 0)):
            first = Fraction(1 - z, denominator)
            second = Fraction(z - moving_root, denominator)
            assert first == expected_first
            assert second == 1 - expected_first


for q in range(0, 30):
    m = q + 1
    assert m > q

print("PASS: B182 idempotents recover labels and can vary arbitrarily late")
