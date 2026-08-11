#!/usr/bin/env python3
"""Exact lightweight checks for B246, G169-G170, and NG204; not a proof of HC."""


def main() -> None:
    for d in range(8, 42, 2):
        standard_floor = 5 * d - 3
        nonstandard_floor = 4 * d + 4

        # Residual-U branch: pair plus third tangent on Q(U).
        assert 2 * (d + 1) + 2 * (d - 1) + (d - 3) == standard_floor

        # Other branch: both escape patterns are at least as large.
        assert (3 * d + 2) + (d - 1) + (d - 3) == 5 * d - 2
        assert (3 * d + 2) + (d - 2) + (d - 3) == standard_floor
        assert (3 * d + 2) + (d - 2) + 1 + (d - 3) == 5 * d - 2
        assert 10 < 4 * d

        # Standard is strictly above the common nonstandard boundary.
        assert standard_floor > nonstandard_floor

        # The common point-rank floor gives slack 6d+6.
        delta_floor = nonstandard_floor - (d + 1)
        assert delta_floor == 3 * d + 3
        assert 2 * delta_floor == 6 * d + 6

        # G169 and all four layers through 6d+5 lie below the floor.
        for slack in range(6 * d + 2, 6 * d + 6):
            assert d + 1 + slack // 2 < nonstandard_floor

        # Next balanced G170 signature.
        slack = 6 * d + 6
        delta_1 = 3 * d + 3
        length = 2 * (d + 1) + slack
        h_1 = d + 1 + delta_1
        assert length == 8 * d + 8
        assert h_1 == nonstandard_floor == length // 2
        assert slack - 2 * delta_1 == 0

    print("PASS: B246 standard five-block floor, G169-G170, and NG204")


if __name__ == "__main__":
    main()
