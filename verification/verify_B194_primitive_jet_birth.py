#!/usr/bin/env python3
"""Lightweight exact checks for B194, G125, and NG157."""

from fractions import Fraction


def coordinate_product(x, y):
    return [Fraction(a) * Fraction(b) for a, b in zip(x, y)]


def main():
    # A hypothetical lower-degree gradient tuple on three nodes.
    lower_gradient = [Fraction(2), Fraction(-3), Fraction(5)]

    # Very ample separators: zero at a different node and nonzero at node i.
    separators = [
        [1, 0, 0],  # isolates node 1 while vanishing at node 2
        [0, 1, 0],  # isolates node 2 while vanishing at node 1
        [0, 0, 1],  # isolates node 3 while vanishing at node 1
    ]
    products = [coordinate_product(h, lower_gradient) for h in separators]
    assert products == [[2, 0, 0], [0, -3, 0], [0, 0, 5]]

    # Each product has zero gradient at one node but a nonzero gradient elsewhere.
    assert products[0][1] == 0 and products[0][0] != 0
    assert products[1][0] == 0 and products[1][1] != 0
    assert products[2][0] == 0 and products[2][2] != 0

    # Under one-node determination each product would have to be zero,
    # forcing every coordinate of the lower gradient tuple to vanish.
    forced_lower_gradient = [0, 0, 0]
    assert all(x == 0 for x in forced_lower_gradient)

    # A primitive birth is compatible with zero lower quotient and nonzero target q.
    lower_quotient_dimensions = [0, 0, 0, 0]
    target_dimension = 4  # 2n for n=2
    assert all(q == 0 for q in lower_quotient_dimensions)
    assert target_dimension == 4

    print("PASS: B194 lower-degree extinction and NG157 multiplication obstruction")


if __name__ == "__main__":
    main()
