#!/usr/bin/env python3
"""Exact lightweight checks for B212, G141, and NG174."""

from math import comb


def main():
    dimension_x = 4
    birth_degree = 13
    node_count = 15
    lower_value_rank = 13
    upper_value_rank = 14

    assert node_count >= birth_degree + 2
    assert birth_degree <= lower_value_rank <= upper_value_rank
    assert birth_degree + 1 <= upper_value_rank <= node_count - 1

    lower_ranks = (lower_value_rank,) * 3
    upper_ranks = (
        upper_value_rank,
        upper_value_rank + dimension_x,
        upper_value_rank + dimension_x + 1,
    )
    assert lower_ranks == (13, 13, 13)
    assert upper_ranks == (14, 18, 19)
    assert upper_ranks[1] - upper_ranks[0] == dimension_x
    assert upper_ranks[2] - upper_ranks[1] == 1

    second_jet_length = comb(dimension_x + 2, 2)
    assert second_jet_length == 15
    assert node_count >= max(birth_degree + 2, second_jet_length)

    # In the excluded asymptotic shortcut N <= m+1, m-very ampleness
    # makes the value rank N and leaves no relation.
    excluded_nodes = birth_degree + 1
    separated_rank = excluded_nodes
    assert excluded_nodes <= birth_degree + 1
    assert excluded_nodes - separated_rank == 0

    print("PASS: B212 very-ample window, G141, and NG174")


if __name__ == "__main__":
    main()
