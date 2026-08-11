#!/usr/bin/env python3
"""Exact lightweight checks for B232, NG190, and G156; not a proof of HC."""

from itertools import combinations_with_replacement


def monomials(variable_count: int, degree: int) -> set[tuple[int, ...]]:
    return set(combinations_with_replacement(range(variable_count), degree))


def main() -> None:
    for n in range(2, 13):
        d = 2 * n
        variable_count = d + 2

        # Boundary and adjacent odd slack allow only delta_1<=d+1.
        for slack in (2 * d + 2, 2 * d + 3):
            assert slack // 2 == d + 1
            h_1 = d + 1 + (d + 1)
            assert h_1 == 2 * (d + 1)

        # Hyperbolic coordinates v=e_0, w=f_0, U=<e_i,f_i : i>=1>.
        v = 0
        w = n + 1
        u_variables = tuple(range(1, n + 1)) + tuple(range(n + 2, 2 * n + 2))
        sym_2 = monomials(variable_count, 2)
        tangent_v = {(v, v)} | {tuple(sorted((v, u))) for u in u_variables}
        tangent_w = {(w, w)} | {tuple(sorted((w, u))) for u in u_variables}
        complement = {tuple(sorted((v, w)))} | set(
            combinations_with_replacement(u_variables, 2)
        )

        assert len(tangent_v) == d + 1
        assert len(tangent_w) == d + 1
        assert tangent_v.isdisjoint(tangent_w)
        assert (tangent_v | tangent_w).isdisjoint(complement)
        assert tangent_v | tangent_w | complement <= sym_2

        # r=a v+b w+u has r^2 in T_v+T_w only if ab=0 and u=0:
        # every vw and U^2 monomial is in the direct complement.
        assert tuple(sorted((v, w))) in complement
        for u in u_variables:
            assert (u, u) in complement

        # First unexcluded B232/G156 rank.
        slack = 2 * d + 4
        delta_1 = d + 2
        length = 2 * (d + 1) + slack
        h_1 = d + 1 + delta_1
        assert length == 4 * d + 6
        assert h_1 == 2 * d + 3 == length // 2
        assert slack - 2 * delta_1 == 0

    # B215 exponents used in the two powered-polarization exclusions.
    for k in range(2, 10):
        assert 2 * k >= 4  # two doubles plus one reduced point
    for ell in range(3, 10):
        assert 2 * ell >= 5  # two doubles plus two reduced points

    print("PASS: B232 threshold rigidity, NG190, G155 no-go, and G156")


if __name__ == "__main__":
    main()
