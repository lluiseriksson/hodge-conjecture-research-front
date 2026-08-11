#!/usr/bin/env python3
"""Bounded B181/G114/NG145 identities; not a proof of HC."""


def f(z: int) -> int:
    return (z * z - 1) ** 2


critical_points = (-1, 0, 1)
critical_values = tuple(f(z) for z in critical_points)
assert critical_values == (0, 1, 0)


# Normalized resultant product is w^2(w-1), with leading factor 4^4.
for w in range(-20, 21):
    product = 1
    for value in critical_values:
        product *= w - value
    resultant = (4**4) * product
    assert product == w * w * (w - 1)
    assert resultant == 256 * w * w * (w - 1)


def resultant_derivative(w: int) -> int:
    return 256 * (3 * w * w - 2 * w)


assert resultant_derivative(0) == 0
assert critical_points[0] != critical_points[2]
assert critical_values[0] == critical_values[2]

print("PASS: B181 value resultant collides two distinct tracked labels")
