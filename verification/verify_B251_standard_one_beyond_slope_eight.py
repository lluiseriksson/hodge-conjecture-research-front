#!/usr/bin/env python3
"""Exact lightweight checks for B251, G174-G175, and NG209; not a proof of HC."""


def main() -> None:
    for d in range(8, 82, 2):
        rank = 5 * d - 2

        # Residual-U branch is B237 on D=d-2.
        residual_dimension = d - 2
        residual_budget = rank - 2 * (d + 1)
        assert residual_budget == 3 * residual_dimension + 2

        three_tangents = 3 * d + 2
        not_w_span = three_tangents + (d - 1)
        in_w_span = three_tangents + (d - 2)
        assert not_w_span == 4 * d + 1
        assert in_w_span == 4 * d
        assert rank - not_w_span == d - 3
        assert rank - in_w_span == d - 2

        # K has dimension d-2; quotienting its contraction by a point
        # inside K loses one dimension.
        k_dimension = d - 2
        assert k_dimension - 1 == d - 3

        # J has dimension d-3 and J-perp has vector dimension five.
        j_dimension = d - 3
        assert (d + 2) - j_dimension == 5
        assert j_dimension - 1 == d - 4 > 1
        assert 15 < rank

        # Next balanced signature.
        slack = 8 * d - 4
        delta_1 = 4 * d - 2
        length = 2 * (d + 1) + slack
        h_1 = d + 1 + delta_1
        assert length == 10 * d - 2
        assert h_1 == 5 * d - 1 == length // 2
        assert slack - 2 * delta_1 == 0

        for old_slack in (8 * d - 6, 8 * d - 5):
            assert d + 1 + old_slack // 2 == rank

    print("PASS: B251 one-beyond exclusion, G174-G175, and NG209")


if __name__ == "__main__":
    main()
