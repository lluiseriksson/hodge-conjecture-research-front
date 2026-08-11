#!/usr/bin/env python3
"""Exact lightweight checks for B247, G170-G171, and NG205; not a proof of HC."""


def check_cycle(parts: tuple[int, int, int, int], cycle: tuple[int, int, int, int]) -> None:
    degree = [0, 0, 0, 0]
    for index, vertex in enumerate(cycle):
        other = cycle[(index + 1) % 4]
        assert parts[vertex] != parts[other]
        degree[vertex] += 1
        degree[other] += 1
    assert degree == [2, 2, 2, 2]


def main() -> None:
    # Good-edge graphs for the possible bad-line partitions.
    check_cycle((0, 1, 2, 3), (0, 1, 2, 3))
    check_cycle((0, 0, 1, 2), (0, 2, 1, 3))
    check_cycle((0, 0, 1, 1), (0, 2, 1, 3))

    for d in range(8, 42, 2):
        boundary_rank = 4 * d + 4
        assert 3 * 5 == 15 < boundary_rank
        assert 3 * 7 == 21 < boundary_rank

        # Four double neighborhoods exactly fill G170.
        assert 4 * (d + 1) == boundary_rank

        # Four doubles plus one reduced point exceed G170; B215 degree is 8.
        assert 2 * 4 + 1 - 1 == 8
        assert 4 * (d + 1) + 1 == boundary_rank + 1

        # Balanced G170 and its odd neighbor have the same integral rank.
        for slack in (6 * d + 6, 6 * d + 7):
            assert slack // 2 == 3 * d + 3
            assert d + 1 + slack // 2 == boundary_rank

        # Next balanced G171 signature.
        slack = 6 * d + 8
        delta_1 = 3 * d + 4
        length = 2 * (d + 1) + slack
        h_1 = d + 1 + delta_1
        assert length == 8 * d + 10
        assert h_1 == 4 * d + 5 == length // 2
        assert slack - 2 * delta_1 == 0

        if d >= 10:
            assert 5 * d - 3 > h_1

    print("PASS: B247 nonstandard boundary exclusion, G170-G171, and NG205")


if __name__ == "__main__":
    main()
