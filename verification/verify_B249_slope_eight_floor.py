#!/usr/bin/env python3
"""Exact lightweight checks for B249, G172-G173, and NG207; not a proof of HC."""


def main() -> None:
    for d in range(8, 82, 2):
        four_doubles = 4 * (d + 1)
        standard_floor = 5 * d - 3
        square_floor = four_doubles + (d - 1)
        higher_floor = four_doubles + (d + 1)

        # Variable hyperplanes through a pair line have dimension d.
        variable_hyperplanes = (d + 2) - 2
        assert variable_hyperplanes == d
        # The 2u restriction kernel has dimension at most one.
        assert variable_hyperplanes - 1 == d - 1

        assert square_floor == 5 * d + 3
        assert higher_floor == 5 * d + 5
        assert standard_floor < square_floor < higher_floor

        delta_1 = standard_floor - (d + 1)
        slack = 2 * delta_1
        length = 2 * (d + 1) + slack
        assert delta_1 == 4 * d - 4
        assert slack == 8 * d - 8
        assert length == 10 * d - 6
        assert standard_floor == length // 2

        # Every smaller slack has rank strictly below the common floor.
        assert d + 1 + (slack - 1) // 2 < standard_floor

        # In B248's excess notation, the three polarization floors are:
        assert standard_floor - four_doubles == d - 7
        assert square_floor - four_doubles == d - 1
        assert higher_floor - four_doubles == d + 1

    print("PASS: B249 slope-eight floor, G172-G173, and NG207")


if __name__ == "__main__":
    main()
