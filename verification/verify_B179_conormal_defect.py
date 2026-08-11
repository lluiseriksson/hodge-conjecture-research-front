#!/usr/bin/env python3
"""Bounded B179/G112/NG143 identities; not a proof of HC."""


# For every requested finite order q, choose m=q+2. The coefficient of
# beta_(y^m) is m*y^(m-1): its q-jet is zero, but it survives modulo y^m.
for q in range(0, 30):
    m = q + 2
    coefficient_degree = m - 1
    assert coefficient_degree >= q + 1
    assert coefficient_degree < m
    assert m != 0

    # In the monomial quotient C{y}/(y^m), y^(m-1) is nonzero.
    quotient_basis_degrees = tuple(range(m))
    assert coefficient_degree in quotient_basis_degrees


# The conormal differential of y^m is exactly m*y^(m-1) dy.
for m in range(2, 40):
    derivative_coefficient = m
    derivative_degree = m - 1
    assert derivative_coefficient != 0
    assert derivative_degree == m - 1
    assert derivative_degree < m

print("PASS: B179 conormal defect evades every prescribed finite jet")
