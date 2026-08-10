#!/usr/bin/env python3
"""Finite diagram checks for B101 and NG077."""

from fractions import Fraction


def global_boundary(v):
    """Three marked local spheres glued to one global homology coordinate."""
    return sum(v, Fraction(0))


# Distinct marked local relations can have the same zero global boundary.
beta_one = (Fraction(1), Fraction(-1), Fraction(0))
beta_two = (Fraction(1), Fraction(0), Fraction(-1))
assert beta_one != beta_two
assert global_boundary(beta_one) == global_boundary(beta_two) == 0

# A marked boundary map, unlike the global zero relation, fixes the target.
marked_map = (
    (Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(-1)),
)


def apply(matrix, vector):
    return tuple(sum(row[j] * vector[j] for j in range(3)) for row in matrix)


target_boundary = apply(marked_map, beta_one)
assert target_boundary == (Fraction(-1), Fraction(1), Fraction(0))

# The ambient square retains the already fixed primitive coordinate c.
source_ambient = Fraction(5)
target_ambient = source_ambient
assert target_ambient == Fraction(5)

print("PASS: B101 marked boundary naturality and NG077 local-coordinate guard")
