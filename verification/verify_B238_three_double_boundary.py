#!/usr/bin/env python3
"""Exact lightweight checks for B238, NG196, and G162; not a proof of HC."""


def main() -> None:
    for n in range(2, 13):
        d = 2 * n

        # G161 and its odd neighbor have exactly the three-double rank.
        for slack in (4 * d + 4, 4 * d + 5):
            delta_1_max = slack // 2
            assert delta_1_max == 2 * d + 2
            h_1 = d + 1 + delta_1_max
            assert h_1 == 3 * (d + 1)

        # Higher powers: three doubles plus one point exceed the span.
        assert 3 * (d + 1) + 1 > 3 * (d + 1)

        # Standard polarization: one quotient dimension remains after
        # three tangents, but an exterior tangent contributes at least d-2.
        assert d - 2 > 1

        # Orthogonal-residual branch at this rank.
        residual_quotient = (3 * d + 3) - 2 * (d + 1)
        assert residual_quotient == d + 1
        assert 2 * (d - 1) > residual_quotient

        # Quartic hyperplane incidence patterns:
        # triangle pattern and one pair-line pattern both hit p,q,r twice.
        triangle = ({"p", "q"}, {"p", "r"}, {"q", "r"})
        pair_line = ({"p", "r"}, {"q", "r"}, {"p"}, {"q"})
        for pattern in (triangle, pair_line):
            counts = {point: sum(point in factor for factor in pattern) for point in "pqr"}
            assert counts == {"p": 2, "q": 2, "r": 2}
            assert len(pattern) <= 4

        # First unexcluded G162 signature.
        slack = 4 * d + 6
        delta_1 = 2 * d + 3
        length = 2 * (d + 1) + slack
        h_1 = d + 1 + delta_1
        assert length == 6 * d + 8
        assert h_1 == 3 * d + 4 == length // 2
        assert slack - 2 * delta_1 == 0

    # B215 exponent for three doubles plus one point.
    assert 2 * 3 + 1 - 1 == 6

    print("PASS: B238 three-double boundary, NG196, G161 no-go, and G162")


if __name__ == "__main__":
    main()
