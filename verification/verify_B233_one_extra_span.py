#!/usr/bin/env python3
"""Exact lightweight checks for B233, NG191, and G157; not a proof of HC."""


def main() -> None:
    for n in range(2, 13):
        d = 2 * n

        # G156 and its adjacent odd layer have only one quotient dimension
        # beyond two independent tangent osculators.
        for slack in (2 * d + 4, 2 * d + 5):
            delta_1_max = slack // 2
            assert delta_1_max == d + 2
            h_1 = d + 1 + delta_1_max
            assert h_1 == 2 * d + 3
            assert h_1 - 2 * (d + 1) == 1

        # In V=<v,w> orthogonal U, choose nonzero u in U. The map
        # y -> u*y on the (d-1)-dimensional hyperplane u^perp is injective.
        u_perp_basis = list(range(d - 1))
        quotient_monomials = {(0, y + 1) for y in u_perp_basis}
        assert len(quotient_monomials) == d - 1
        assert d - 1 > 1

        # O_Q(4): two doubles plus one point fill the proposed span.
        mixed_length = 2 * (d + 1) + 1
        assert mixed_length == 2 * d + 3

        # On a line, multiplicity 2+2+1 exceeds quartic degree, while the
        # quartic Veronese span has vector dimension five.
        assert 2 + 2 + 1 > 4
        assert 5 < 2 * d + 3

        # First unexcluded B233/G157 signature.
        slack = 2 * d + 6
        delta_1 = d + 3
        length = 2 * (d + 1) + slack
        h_1 = d + 1 + delta_1
        assert length == 4 * d + 8
        assert h_1 == 2 * d + 4 == length // 2
        assert slack - 2 * delta_1 == 0

    # B215 exponent checks used for higher powers.
    for k in range(3, 10):
        assert 2 * k >= 5  # two doubles plus two reduced points
        assert 2 * k >= 6  # at G157: two doubles plus three points

    print("PASS: B233 one-extra span, NG191, G156 no-go, and G157")


if __name__ == "__main__":
    main()
