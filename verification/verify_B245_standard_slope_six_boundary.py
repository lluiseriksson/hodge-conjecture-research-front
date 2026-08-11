#!/usr/bin/env python3
"""Exact lightweight checks for B245, G168-G169, and NG203; not a proof of HC."""


def main() -> None:
    for d in range(8, 42, 2):
        boundary_h = 4 * d + 1

        # B244 removes every nonstandard polarization.
        assert 4 * d + 4 > boundary_h

        # Residual-U branch.
        residual_quotient = boundary_h - 2 * (d + 1)
        residual_pair = 2 * (d - 1)
        assert residual_quotient == 2 * d - 1
        assert residual_quotient - residual_pair == 1
        smaller_quadric_third_rank = (d - 2) - 1
        assert smaller_quadric_third_rank == d - 3 > 1

        # Branch meeting the hyperbolic plane.
        after_three = boundary_h - (3 * d + 2)
        assert after_three == d - 1
        assert (d - 1) == after_three
        assert (d - 2) + 1 == after_three
        k_dim = d - 2
        assert k_dim - 1 == d - 3 > 1
        assert (d + 2) - k_dim == 4
        assert 10 < boundary_h

        # G168 and its odd neighbor share the same integral rank.
        for slack in (6 * d, 6 * d + 1):
            assert slack // 2 == 3 * d
            assert d + 1 + slack // 2 == boundary_h

        # Next balanced G169 signature.
        slack = 6 * d + 2
        delta_1 = 3 * d + 1
        length = 2 * (d + 1) + slack
        h_1 = d + 1 + delta_1
        assert length == 8 * d + 4
        assert h_1 == 4 * d + 2 == length // 2
        assert slack - 2 * delta_1 == 0

    print("PASS: B245 standard slope-six boundary, G168-G169, and NG203")


if __name__ == "__main__":
    main()
