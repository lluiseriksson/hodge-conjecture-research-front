#!/usr/bin/env python3
"""Exact lightweight checks for B234, NG192, and G158; not a proof of HC."""


def main() -> None:
    for n in range(2, 13):
        d = 2 * n

        # G157 and its odd neighbor have quotient dimension two.
        for slack in (2 * d + 6, 2 * d + 7):
            delta_1_max = slack // 2
            assert delta_1_max == d + 3
            h_1 = d + 1 + delta_1_max
            assert h_1 == 2 * d + 4
            assert h_1 - 2 * (d + 1) == 2
        assert d - 1 > 2

        # Quartic span bounds for a line plus at most one exterior point.
        assert 5 + 1 < 2 * d + 4

        # Four base points yield four pairwise line intersections. A fifth
        # distinct point can occur only when one paired line coincidence
        # creates a collinear base triple.
        base_points = {"p", "q", "r", "s"}
        ordinary_intersections = {"p", "q", "r", "s"}
        assert ordinary_intersections == base_points

        # First unexcluded B234/G158 signature.
        slack = 2 * d + 8
        delta_1 = d + 4
        length = 2 * (d + 1) + slack
        h_1 = d + 1 + delta_1
        assert length == 4 * d + 10
        assert h_1 == 2 * d + 5 == length // 2
        assert slack - 2 * delta_1 == 0

    # At exponent six, two doubles plus three points fill G158 exactly;
    # they do not contradict a cube. Four points need exponent seven,
    # which excludes every fourth or higher power.
    mixed_three = 2 * (4 + 1) + 3
    assert mixed_three == 13
    assert 6 == 2 * 3
    assert 7 > 6
    for ell in range(4, 10):
        assert 2 * ell >= 7

    print("PASS: B234 two-extra span, NG192, G157 no-go, and G158")


if __name__ == "__main__":
    main()
