#!/usr/bin/env python3
"""Exact lightweight checks for B244, G167-G168, and NG202; not a proof of HC."""


def main() -> None:
    for d in range(8, 42, 2):
        # Polarization-wise point-span floors.
        standard_h = 4 * d
        nonstandard_h = 4 * d + 4
        assert nonstandard_h > standard_h

        # Standard tangent quotient arithmetic.
        assert 2 * (d + 1) + 2 * (d - 1) == standard_h
        assert (3 * d + 2) + (d - 2) == standard_h
        assert d - 1 > d - 2

        # Sextic and quartic support bounds.
        assert 3 * 7 < 3 * d + 3
        assert 3 * 5 < 3 * d + 3
        assert 2 * 5 + 3 < 3 * d + 5
        assert (3 * d + 6) + (d - 2) == nonstandard_h

        # Slack consequences of h=d+1+delta and 2 delta<=s.
        standard_delta = standard_h - (d + 1)
        nonstandard_delta = nonstandard_h - (d + 1)
        assert standard_delta == 3 * d - 1
        assert 2 * standard_delta == 6 * d - 2
        assert nonstandard_delta == 3 * d + 3
        assert 2 * nonstandard_delta == 6 * d + 6

        # Both boundary layers have maximal point rank 4d.
        for slack in (6 * d - 2, 6 * d - 1):
            assert d + 1 + slack // 2 == 4 * d

        # G167 lies strictly below the new floor from d=8 onward.
        assert 4 * d + 14 <= 6 * d - 1

        # The slope-six balanced signature.
        slack = 6 * d
        delta_1 = 3 * d
        length = 2 * (d + 1) + slack
        h_1 = d + 1 + delta_1
        assert length == 8 * d + 2
        assert h_1 == 4 * d + 1 == length // 2
        assert slack - 2 * delta_1 == 0

    print("PASS: B244 slope-six floor, G167-G168, and NG202")


if __name__ == "__main__":
    main()
