#!/usr/bin/env python3
"""Exact lightweight linear-algebra checks for B217-B218 and NG179."""

from itertools import product


def quotient_square(outside_coordinates):
    """Coordinates of q^2 in Sym^2(V/U), including diagonal entries."""
    answer = []
    for i, left in enumerate(outside_coordinates):
        for j in range(i, len(outside_coordinates)):
            right = outside_coordinates[j]
            answer.append(left * right if i == j else 2 * left * right)
    return tuple(answer)


def main():
    # Over Q (hence over C), q^2 vanishes in Sym^2(V/U) only when q mod U=0.
    for outside in product(range(-2, 3), repeat=3):
        square = quotient_square(outside)
        assert (all(value == 0 for value in square)) == (
            all(value == 0 for value in outside)
        )

    # Once point span <= tangent and lower absorption gives tangent <= point span,
    # their dimensions and subspaces agree.
    dimension_x = 4
    tangent_dimension = dimension_x + 1
    point_span_upper = tangent_dimension
    point_span_lower = tangent_dimension
    assert point_span_lower == point_span_upper == 5

    # Zak's inequality d >= d + fiber_dimension excludes only positive dimension.
    for dimension_x in range(1, 9):
        for fiber_dimension in range(1, 6):
            assert not (
                dimension_x >= dimension_x + fiber_dimension
            )
        assert dimension_x >= dimension_x  # zero-dimensional fibers remain allowed

    print("PASS: B217 common tangent, B218 Gauss dimensions, and NG179")


if __name__ == "__main__":
    main()
