#!/usr/bin/env python3
"""Exact lightweight checks for B213, G142, and NG175."""


def main():
    dimension_x = 4
    birth_degree = 13
    node_count = 18

    def lower_value_rank(k):
        return max(k + 1, dimension_x + 1)

    # Every complementary pair obeys the transported-relation ceiling.
    for a in range(1, birth_degree):
        left = lower_value_rank(a)
        right = lower_value_rank(birth_degree - a)
        assert left + right <= node_count

    rank_h = lower_value_rank(1)
    rank_previous = lower_value_rank(birth_degree - 1)
    assert rank_h == dimension_x + 1 == 5
    assert rank_previous == birth_degree == 13
    assert node_count - rank_previous == rank_h

    universal_floor = dimension_x + 1 + max(
        birth_degree, dimension_x + 1
    )
    assert universal_floor == 18
    assert node_count >= universal_floor

    # B212 alone would allow 15 nodes here; B213 excludes that range.
    old_window_nodes = birth_degree + 2
    assert old_window_nodes == 15
    assert old_window_nodes < universal_floor

    print("PASS: B213 relation transport, G142, and NG175")


if __name__ == "__main__":
    main()
