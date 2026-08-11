#!/usr/bin/env python3
"""Exact lightweight checks for B216's equality saturation."""

from math import comb


def lower_rank(dimension_x, degree):
    second_jet_length = comb(dimension_x + 2, 2)
    quotient, remainder = divmod(degree + 1, 3)
    residual_rank = (0, 1, dimension_x + 1)[remainder]
    return second_jet_length * quotient + residual_rank


def node_floor(dimension_x, birth_degree):
    if birth_degree == 2:
        return 2 * (dimension_x + 1)
    quotient, remainder = divmod(birth_degree + 2, 3)
    residual_rank = (0, 1, dimension_x + 1)[remainder]
    return comb(dimension_x + 2, 2) * quotient + residual_rank


def main():
    # The canonical complementary split realizes the closed floor.
    for dimension_x in range(1, 9):
        second_jet_length = comb(dimension_x + 2, 2)
        for birth_degree in range(3, 61):
            assert node_floor(dimension_x, birth_degree) == (
                second_jet_length + lower_rank(dimension_x, birth_degree - 2)
            )

    # Fourfold example: equality fixes both ranks and both relation dimensions.
    dimension_x = 4
    birth_degree = 13
    nodes = node_floor(dimension_x, birth_degree)
    rank_two = comb(dimension_x + 2, 2)
    rank_complement = lower_rank(dimension_x, birth_degree - 2)
    assert (nodes, rank_two, rank_complement) == (75, 15, 60)
    assert nodes - rank_complement == rank_two
    assert nodes - rank_two == rank_complement

    # In birth degree two the same dimension argument saturates tangent rank.
    nodes = node_floor(dimension_x, 2)
    tangent_rank = dimension_x + 1
    assert nodes == 10 == 2 * tangent_rank
    assert nodes - tangent_rank == tangent_rank

    # One slack node destroys the dimension-forced surjectivity conclusion.
    assert (75 + 1) - rank_complement > rank_two

    print("PASS: B216 equality saturation and transport dimensions")


if __name__ == "__main__":
    main()
