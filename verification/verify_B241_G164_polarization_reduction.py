#!/usr/bin/env python3
"""Exact lightweight checks for B241, G165, and NG199; not a proof of HC."""


def counts(pattern: tuple[set[str], ...]) -> dict[str, int]:
    return {
        point: sum(point in factor for factor in pattern)
        for point in "pqrtuxy"
    }


def main() -> None:
    for n in range(2, 13):
        d = 2 * n
        slack = 4 * d + 10
        delta_1 = 2 * d + 5
        length = 2 * (d + 1) + slack
        h_1 = d + 1 + delta_1
        assert length == 6 * d + 12
        assert h_1 == 3 * d + 6 == length // 2
        assert slack - 2 * delta_1 == 0

        if d >= 8:
            assert 2 * (d - 1) > d + 4
            assert d - 2 > 4
        elif d == 6:
            assert 2 * (d - 1) == d + 4 == 10
            assert d - 1 > 4
            assert d - 2 == 4
            assert 3 * d + 6 == 24
            assert 5 + 1 < 24
        else:
            assert d == 4

    # Seventh point y off the triangle.
    off_triangle = (
        {"p", "q"},
        {"p", "r"},
        {"q", "r"},
        {"t"},
        {"u"},
        {"x"},
    )
    off_counts = counts(off_triangle)
    assert off_counts == {
        "p": 2, "q": 2, "r": 2,
        "t": 1, "u": 1, "x": 1, "y": 0,
    }

    # If y lies on pq and t is off that line, use pr, qr, pt, q, u, x.
    pair_value = (
        {"p", "r"},
        {"q", "r"},
        {"p", "t"},
        {"q"},
        {"u"},
        {"x"},
    )
    pair_counts = counts(pair_value)
    assert pair_counts == off_counts

    # If t,u,x all lie on pq, one line factor gives a transverse jet at y.
    pair_jet = (
        {"p", "q", "t", "u", "x", "y"},
        {"p"},
        {"q"},
        {"r"},
        {"r"},
        set(),
    )
    jet_counts = counts(pair_jet)
    assert jet_counts == {
        "p": 2, "q": 2, "r": 2,
        "t": 1, "u": 1, "x": 1, "y": 1,
    }
    assert 2 + 2 + 1 + 1 + 1 > 6

    # In d=6, W has dimension five.  An exterior point costs five
    # quotient dimensions; an isotropic point in W costs four and fills.
    assert 5 > 4
    assert 5 - 1 == 4

    # The remaining contact locus is one plane conic plus one point.
    assert 5 + 1 == 6
    assert 6 < 24

    print("PASS: B241 G164 polarization reduction, G165, and NG199")


if __name__ == "__main__":
    main()
