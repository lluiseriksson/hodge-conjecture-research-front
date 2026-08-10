#!/usr/bin/env python3
"""Exact S3-invariant calculation for the rational A2 root lattice."""

from fractions import Fraction

import sympy as sp


s1 = sp.Matrix([[-1, 1], [0, 1]])
s2 = sp.Matrix([[1, 0], [1, -1]])
identity = sp.eye(2)

assert s1 * s1 == identity
assert s2 * s2 == identity
assert (s1 * s2) ** 3 == identity

group = set()
frontier = {tuple(identity)}
while frontier:
    raw = frontier.pop()
    matrix = sp.Matrix(2, 2, raw)
    if raw in group:
        continue
    group.add(raw)
    for generator in (s1, s2):
        product = matrix * generator
        key = tuple(product)
        if key not in group:
            frontier.add(key)

assert len(group) == 6

average = sp.zeros(2)
for raw in group:
    average += sp.Matrix(2, 2, raw)
average *= Fraction(1, 6)

fixed_equations = (s1 - identity).col_join(s2 - identity)
assert fixed_equations.rank() == 2
assert average == sp.zeros(2)

print("PASS: B073 A2 standard S3 representation has zero invariants and zero average")
