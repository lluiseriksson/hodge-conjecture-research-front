#!/usr/bin/env python3
"""Exact 2x2 guards for B170/NG134; not a proof of HC."""


def determinant_2x2(a, b, c, d):
    return a * d - b * c


# NG134: d(x, x-y^2) has determinant -2y.
for y in range(-8, 9):
    det = determinant_2x2(1, 0, 1, -2 * y)
    assert det == -2 * y
    assert (det == 0) == (y == 0)

# B170 strength guard: tau=(x,(1+y)x) has ideal (x), but its Jacobian
# determinant is x, so constant Jacobian rank is sufficient, not necessary.
for x in range(-8, 9):
    det = determinant_2x2(1, 0, 1, x)
    assert det == x
    assert (det == 0) == (x == 0)

# Minimal-generator arithmetic in the escaping model.
central_rank = 1
minimal_generators = 2  # (x, y^2)
hidden_generator_dimension = minimal_generators - central_rank
assert hidden_generator_dimension == 1

print("PASS: B170 constant-rank certificate and NG134 linear quadratic escape")
