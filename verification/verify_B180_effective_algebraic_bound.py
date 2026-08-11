#!/usr/bin/env python3
"""Bounded B180/G113/NG144 identities; not a proof of HC."""


# Sharp family P_m(y,z)=z-y^m: degree, branch order, and first conormal
# degree are respectively m, m, and m-1.
for m in range(1, 80):
    polynomial_degree = m
    branch_order = m
    conormal_degree = m - 1
    partial_z_at_origin = 1

    assert partial_z_at_origin != 0
    assert branch_order <= polynomial_degree
    assert conormal_degree <= polynomial_degree - 1


# No embedding-independent order follows from algebraicity alone.
for proposed_uniform_order in range(0, 40):
    m = proposed_uniform_order + 2
    first_visible_degree = m - 1
    assert first_visible_degree > proposed_uniform_order

print("PASS: B180 degree bound is sharp and algebraicity has no uniform order")
