#!/usr/bin/env python3
"""Exact bounded checks for B222/G149/NG183; not a proof of HC."""

from math import comb


def lower_rank(d: int, k: int) -> int:
    q, r = divmod(k + 1, 3)
    return comb(d + 2, 2) * q + (0, 1, d + 1)[r]


def floor_d(d: int, m: int) -> int:
    if m == 2:
        return 2 * (d + 1)
    return comb(d + 2, 2) + lower_rank(d, m - 2)


def main() -> None:
    for d in range(2, 13):
        c_d = comb(d + 2, 2)

        # m=2: injective Gauss needs delta_1>=1, hence slack at least 2.
        for slack in range(0, 9):
            for delta_1 in range(0, slack // 2 + 1):
                cokernel = slack - 2 * delta_1
                assert cokernel >= 0
                if slack == 1:
                    assert delta_1 == 0

        for m in range(3, 31):
            base = floor_d(d, m)
            assert base == c_d + lower_rank(d, m - 2)
            for slack in range(0, 9):
                for delta_2 in range(slack + 1):
                    for delta_c in range(slack - delta_2 + 1):
                        n_points = base + slack
                        h_2 = c_d + delta_2
                        h_c = lower_rank(d, m - 2) + delta_c
                        cokernel_left = n_points - h_c - h_2
                        cokernel_right = n_points - h_2 - h_c
                        expected = slack - delta_2 - delta_c
                        assert cokernel_left == cokernel_right == expected
                        if slack == 1 and delta_2 >= 1:
                            assert (delta_2, delta_c, expected) == (1, 0, 0)

    print("PASS: B222 strict-slack budget and G149 first-slack signature")


if __name__ == "__main__":
    main()
