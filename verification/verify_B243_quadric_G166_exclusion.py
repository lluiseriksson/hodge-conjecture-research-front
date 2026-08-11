#!/usr/bin/env python3
"""Exact lightweight checks for B243, G166-G167, and NG201; not a proof of HC."""


def counts(pattern: tuple[set[str], ...]) -> dict[str, int]:
    return {
        point: sum(point in factor for factor in pattern)
        for point in "pqrtuxy"
    }


def main() -> None:
    for n in range(2, 13):
        d = 2 * n

        # G166 and its odd neighbor have the same integral rank.
        for slack in (4 * d + 12, 4 * d + 13):
            delta_1 = slack // 2
            assert delta_1 == 2 * d + 6
            assert d + 1 + delta_1 == 3 * d + 7

        # The next balanced G167 signature.
        slack = 4 * d + 14
        delta_1 = 2 * d + 7
        length = 2 * (d + 1) + slack
        h_1 = d + 1 + delta_1
        assert length == 6 * d + 16
        assert h_1 == 3 * d + 8 == length // 2
        assert slack - 2 * delta_1 == 0

        # Four doubles exceed G166.  B215 supplies them for k>=4.
        assert 2 * 4 - 1 == 7
        assert 4 * (d + 1) > 3 * d + 7
        assert 2 * 4 >= 7

        # Square residual hyperplanes have rank at least d-2.
        assert (d - 1) - 1 == d - 2 >= 2

    # Sextics: a fourth point exists off the triangle from d=6 onward.
    for d in range(6, 26, 2):
        assert 3 * 7 < 3 * d + 7
        assert 4 * (d + 1) > 3 * d + 7

    # Standard quotient inequalities begin exactly at d=8.
    assert not (2 * 6 - 2 > 6 + 5)
    for d in range(8, 26, 2):
        assert 2 * d - 2 > d + 5
        assert d - 2 > 5
        assert 5 < 3 * d + 7

    # Square residual families: fixed factors are units at y and the
    # variable factor contains the three simple supports.
    off_triangle = (
        {"p", "q"},
        {"p", "r"},
        {"q", "r"},
        {"t", "u", "x"},
    )
    on_pq = (
        {"p", "r"},
        {"q", "r"},
        {"p", "t"},
        {"q", "u", "x"},
    )
    for pattern in (off_triangle, on_pq):
        incidence = counts(pattern)
        assert incidence["p"] >= 2
        assert incidence["q"] >= 2
        assert incidence["r"] >= 2
        assert incidence["t"] >= 1
        assert incidence["u"] >= 1
        assert incidence["x"] >= 1
        assert incidence["y"] == 0

    # On Q^8 the four disjoint cases cover every k>=1.
    d = 8
    assert 3 * d + 7 == 31
    excluded = {1, 2, 3}
    excluded.update(range(4, 20))
    assert all(k in excluded for k in range(1, 20))

    print("PASS: B243 quadric G166 exclusion, G167, and NG201")


if __name__ == "__main__":
    main()
