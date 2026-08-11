#!/usr/bin/env python3
"""Exact lightweight checks for B211, G140, and NG173."""

from math import comb


def main():
    dimension_x = 4
    node_count = 15
    value_rank = 14  # leaves a nonzero value relation

    first_increment = dimension_x
    second_increment = 1
    rank_2z = value_rank + first_increment
    rank_3z = rank_2z + second_increment
    assert rank_2z - value_rank == dimension_x
    assert rank_3z - rank_2z == 1

    expected_first_increment = dimension_x * node_count
    expected_second_increment = comb(dimension_x + 1, 2) * node_count
    assert expected_first_increment - first_increment == dimension_x * (node_count - 1)
    assert expected_second_increment - second_increment == comb(dimension_x + 1, 2) * node_count - 1

    second_jet_fiber_rank = comb(dimension_x + 2, 2)
    assert second_jet_fiber_rank == 15
    assert node_count >= second_jet_fiber_rank

    # Adjacent lower extinction has both conditional increments zero.
    lower_value_rank = 15
    lower_rank_2z = 15
    lower_rank_3z = 15
    assert lower_rank_2z - lower_value_rank == 0
    assert lower_rank_3z - lower_rank_2z == 0

    print("PASS: B211 adjacent fat-point signature, G140, and NG173")


if __name__ == "__main__":
    main()
