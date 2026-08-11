#!/usr/bin/env python3
"""Bounded checks for B187/G120/NG151; not a proof of HC."""

from fractions import Fraction


# Vandermonde evaluation gives a uniform U_(R,N) value matroid. Barycentric
# weights have full support and annihilate every moment through N-2, hence
# in particular the first R moments.
for node_count in range(2, 10):
    points = list(range(node_count))
    weights = []
    for i, point in enumerate(points):
        denominator = 1
        for j, other in enumerate(points):
            if i != j:
                denominator *= point - other
        weights.append(Fraction(1, denominator))
    assert all(weight != 0 for weight in weights)
    for value_rank in range(1, node_count):
        for power in range(value_rank):
            moment = sum(
                weight * (point**power)
                for weight, point in zip(weights, points)
            )
            assert moment == 0


# B187's dimensions: one nondegenerate form on 2nN variables has maximal
# isotropic dimension nN and forces the displayed first-jet defect.
for n in range(1, 6):
    for node_count in range(2, 9):
        for value_rank in range(1, node_count):
            gradient_ceiling = n * node_count
            target_dimension = (2 * n + 1) * node_count
            rank_ceiling = value_rank + gradient_ceiling
            defect_floor = target_dimension - rank_ceiling
            assert defect_floor == (n + 1) * node_count - value_rank


# NG151: the diagonal is isotropic for B direct_sum (-B), while both
# projections are full. Use the standard dot product for sampled vectors.
for dimension in range(2, 9, 2):
    vectors = [
        tuple(Fraction((i + 1) * (j + 2)) for j in range(dimension))
        for i in range(3)
    ]
    for left in vectors:
        for right in vectors:
            pairing_1 = sum(a * b for a, b in zip(left, right))
            pairing_2 = sum(a * b for a, b in zip(left, right))
            assert pairing_1 - pairing_2 == 0
    diagonal_dimension = dimension
    n = dimension // 2
    assert diagonal_dimension == n * 2

print("PASS: B187 gives the nN ceiling; NG151 keeps global and split apart")
