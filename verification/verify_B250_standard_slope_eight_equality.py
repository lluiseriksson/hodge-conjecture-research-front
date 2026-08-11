#!/usr/bin/env python3
"""Exact lightweight checks for B250, G173-G174, and NG208; not a proof of HC."""


def main() -> None:
    for d in range(8, 82, 2):
        equality_rank = 5 * d - 3

        # Residual-U branch is B236 on dimension D=d-2.
        residual_dimension = d - 2
        residual_budget = equality_rank - 2 * (d + 1)
        assert residual_budget == 3 * residual_dimension + 1

        # Nonorthogonal-third branch.
        three_tangents = 3 * d + 2
        assert three_tangents + (d - 1) + (d - 3) == 5 * d - 2
        assert three_tangents + (d - 2) == 4 * d
        assert equality_rank - 4 * d == d - 3

        k_dimension = d - 2
        assert k_dimension - 1 == d - 3
        assert k_dimension == d - 2

        # J has dimension d-3, hence J-perp has vector dimension five.
        j_dimension = d - 3
        ambient_vector_dimension = d + 2
        assert ambient_vector_dimension - j_dimension == 5
        assert 15 < equality_rank

        # Next balanced signature.
        slack = 8 * d - 6
        delta_1 = 4 * d - 3
        length = 2 * (d + 1) + slack
        h_1 = d + 1 + delta_1
        assert length == 10 * d - 4
        assert h_1 == 5 * d - 2 == length // 2
        assert slack - 2 * delta_1 == 0

        # G173 and its odd neighbor share the excluded equality rank.
        for old_slack in (8 * d - 8, 8 * d - 7):
            assert d + 1 + old_slack // 2 == equality_rank

    print("PASS: B250 standard equality exclusion, G173-G174, and NG208")


if __name__ == "__main__":
    main()
