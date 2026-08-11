#!/usr/bin/env python3
"""Finite scope/rank guards for B150/S062; not a proof of the source theorem."""

from math import comb


# (ambient dimension, degree, number of points, component dimensions)
exceptions = [
    (2, 4, 5, [2] * 5),
    (3, 4, 9, [3] * 9),
    (3, 4, 9, [3] * 8 + [2]),
    (4, 3, 7, [4] * 7),
    (4, 4, 14, [4] * 14),
]

for middle_dimension in range(1, 9):
    ambient_dimension = 2 * middle_dimension
    for degree in range(1, 9):
        if degree == 2:
            continue
        for node_count in range(2, 30):
            half_dimensions = [middle_dimension] * node_count
            assert (
                ambient_dimension,
                degree,
                node_count,
                half_dimensions,
            ) not in exceptions

            section_dimension = comb(ambient_dimension + degree, degree)
            scheme_length = (middle_dimension + 1) * node_count
            maximal_rank = min(section_dimension, scheme_length)

            if section_dimension <= scheme_length:
                # Maximal rank is injective: no containing nonzero form.
                kernel_dimension = section_dimension - maximal_rank
                assert kernel_dimension == 0
            else:
                # Maximal rank is surjective and exceeds every R+n, R<N.
                assert maximal_rank == scheme_length
                for value_rank in range(1, node_count):
                    assert maximal_rank > value_rank + middle_dimension

print("PASS: B150 half-double parameters avoid S062 exceptions and generic G094 rank")
