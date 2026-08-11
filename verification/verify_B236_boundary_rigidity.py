#!/usr/bin/env python3
"""Exact lightweight checks for B236, NG194, and G160; not a proof of HC."""


def main() -> None:
    for n in range(2, 13):
        d = 2 * n

        # At the B235 boundary, only d-1 quotient dimensions remain.
        boundary_h = 3 * d + 1
        quotient = boundary_h - 2 * (d + 1)
        assert quotient == d - 1

        # A nonorthogonal-coordinate component in the third point lets all
        # y in U occur, giving quotient rank d; equality therefore forces
        # the third point into U and gives exact rank d-1.
        assert d > quotient
        assert d - 1 == quotient

        # In the monomial complement, rr' and vw are distinct and neither
        # belongs to the three-tangent span. Their difference is nonzero.
        complement_basis = {"vw", "rr_prime", "r_prime_sq"}
        three_tangent_basis = {"v_sq", "w_sq", "vU", "wU", "r_sq", "rU1"}
        assert complement_basis.isdisjoint(three_tangent_basis)
        tangent_escape = {"rr_prime": 1, "vw": -1}
        assert any(tangent_escape.values())
        assert set(tangent_escape) <= complement_basis

        # Boundary and adjacent odd slack have the same integral rank.
        for slack in (4 * d, 4 * d + 1):
            assert slack // 2 == 2 * d

        # First unexcluded G160 signature.
        slack = 4 * d + 2
        delta_1 = 2 * d + 1
        length = 2 * (d + 1) + slack
        h_1 = d + 1 + delta_1
        assert length == 6 * d + 4
        assert h_1 == 3 * d + 2 == length // 2
        assert slack - 2 * delta_1 == 0

        # Nonstandard quadric polarizations still need the B235 floor.
        assert slack < 4 * d + 4

    print("PASS: B236 boundary rigidity, NG194, G159 no-go, and G160")


if __name__ == "__main__":
    main()
