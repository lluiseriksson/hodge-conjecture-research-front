#!/usr/bin/env python3
"""Exact lightweight checks for B231, NG189, and G155; not a proof of HC."""

from itertools import combinations_with_replacement
from math import comb


def monomial_basis(variables: range, degree: int) -> set[tuple[int, ...]]:
    return set(combinations_with_replacement(variables, degree))


def main() -> None:
    # B231's two branches and the threshold rank signature.
    for n in range(2, 13):
        d = 2 * n
        c_d = comb(d + 2, 2)
        degree_two_floor = 2 * d + 2
        assert c_d > degree_two_floor

        # Below the m=2 floor, even maximal delta_1 cannot fit two doubles.
        slack = degree_two_floor - 1
        delta_1_max = slack // 2
        h_1_max = d + 1 + delta_1_max
        assert delta_1_max == d
        assert h_1_max == 2 * d + 1 < 2 * (d + 1)

        # Below the m>=3 floor, even maximal delta_2 cannot fit two triples.
        slack = c_d - 1
        h_2_max = c_d + slack
        assert h_2_max == 2 * c_d - 1 < 2 * c_d

        # Exact G155 threshold.
        slack = degree_two_floor
        delta_1 = d + 1
        length = 2 * (d + 1) + slack
        h_1 = d + 1 + delta_1
        assert length == 4 * d + 4
        assert h_1 == 2 * d + 2 == length // 2
        assert slack - 2 * delta_1 == 0

        # Hyperbolic V=<e_0,...,e_n,f_0,...,f_n>, W=<e_0,...,e_n>.
        # For p=e_0 and u=f_1, u lies in p^perp but outside W.
        variables = range(2 * n + 2)
        w_variables = range(n + 1)
        u = n + 2
        assert u not in w_variables
        assert (0, u) not in monomial_basis(w_variables, 2)
        assert (0, 0, 0, u) not in monomial_basis(w_variables, 4)
        assert (0, u) in monomial_basis(variables, 2)
        assert (0, 0, 0, u) in monomial_basis(variables, 4)

    # G154's fixed slack ten survives Q^4 but fails already on Q^6.
    assert 10 == 2 * 4 + 2
    assert 10 < 2 * 6 + 2
    assert 6 + 1 + 5 == 12 < 14

    # Any fixed finite bound is defeated in some even dimension.
    for bound in range(0, 101):
        d = max(4, 2 * ((bound + 2) // 4 + 1))
        while 2 * d + 2 <= bound:
            d += 2
        assert d % 2 == 0 and 2 * d + 2 > bound
        assert comb(d + 2, 2) > 2 * d + 2 > bound

    # The powered-polarization contradictions use only bounded thresholds.
    for k in range(2, 10):
        assert 2 * k >= 3  # two double neighborhoods
        assert 4 * k >= 5  # two triple neighborhoods

    print("PASS: B231 dimension-scaled slack, NG189, G154 no-go, and G155")


if __name__ == "__main__":
    main()
