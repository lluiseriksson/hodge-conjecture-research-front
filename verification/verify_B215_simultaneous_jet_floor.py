#!/usr/bin/env python3
"""Exact lightweight checks for B215, G144, and NG177."""

from math import comb


def lower_rank(dimension_x, degree):
    if degree == 1:
        return dimension_x + 1
    second_jet_length = comb(dimension_x + 2, 2)
    quotient, remainder = divmod(degree + 1, 3)
    return second_jet_length * quotient + remainder


def node_floor(dimension_x, birth_degree):
    if birth_degree == 2:
        return 2 * (dimension_x + 1)
    second_jet_length = comb(dimension_x + 2, 2)
    if birth_degree % 3 == 0:
        return second_jet_length * (birth_degree // 3) + dimension_x + 1
    quotient, remainder = divmod(birth_degree + 2, 3)
    return second_jet_length * quotient + remainder


def main():
    dimension_x = 4
    second_jet_length = comb(dimension_x + 2, 2)
    assert second_jet_length == 15

    expected = {
        2: 10,
        3: 20,
        4: 30,
        5: 31,
        6: 35,
        7: 45,
        8: 46,
        9: 50,
        13: 75,
    }
    for birth_degree, floor in expected.items():
        assert node_floor(dimension_x, birth_degree) == floor

    birth_degree = 13
    complementary = [
        lower_rank(dimension_x, a)
        + lower_rank(dimension_x, birth_degree - a)
        for a in range(1, birth_degree)
    ]
    assert max(complementary) == node_floor(dimension_x, birth_degree)
    assert complementary[1] == 75  # degrees 2 and 11

    # Mixed interpolation: degree k=11 has q=4 triples and no residual point.
    quotient, remainder = divmod(11 + 1, 3)
    assert (quotient, remainder) == (4, 0)
    assert lower_rank(dimension_x, 11) == 4 * second_jet_length

    previous_floor = second_jet_length + max(second_jet_length, 13 - 1)
    assert previous_floor == 30 < node_floor(dimension_x, 13)

    # Exhaustively compare the closed formula with every complementary
    # split over a broad lightweight range.
    for dimension in range(1, 9):
        for degree in range(2, 61):
            direct_maximum = max(
                lower_rank(dimension, a)
                + lower_rank(dimension, degree - a)
                for a in range(1, degree)
            )
            assert node_floor(dimension, degree) == direct_maximum

    print("PASS: B215 simultaneous second jets, G144, and NG177")


if __name__ == "__main__":
    main()
