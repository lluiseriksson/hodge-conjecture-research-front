#!/usr/bin/env python3
"""Exact lightweight checks for B214, G143, and NG176."""

from math import comb


def node_floor(dimension_x, birth_degree):
    second_jet_length = comb(dimension_x + 2, 2)
    if birth_degree == 2:
        return 2 * (dimension_x + 1)
    if birth_degree == 3:
        return second_jet_length + dimension_x + 1
    return second_jet_length + max(second_jet_length, birth_degree - 1)


def main():
    dimension_x = 4
    second_jet_length = comb(dimension_x + 2, 2)
    assert second_jet_length == 15

    assert node_floor(dimension_x, 2) == 10
    assert node_floor(dimension_x, 3) == 20
    assert node_floor(dimension_x, 4) == 30
    assert node_floor(dimension_x, 13) == 30
    assert node_floor(dimension_x, 17) == 31

    birth_degree = 13
    node_count = node_floor(dimension_x, birth_degree)

    def lower_rank(k):
        if k == 1:
            return dimension_x + 1
        return max(second_jet_length, k + 1)

    complementary = [
        lower_rank(a) + lower_rank(birth_degree - a)
        for a in range(1, birth_degree)
    ]
    assert max(complementary) == node_count
    assert complementary[1] == second_jet_length * 2

    previous_floor = dimension_x + 1 + max(
        birth_degree, dimension_x + 1
    )
    assert previous_floor == 18 < node_count

    print("PASS: B214 universal second jets, G143, and NG176")


if __name__ == "__main__":
    main()
