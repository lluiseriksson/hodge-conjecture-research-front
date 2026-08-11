#!/usr/bin/env python3
"""Exact lightweight checks for B237, NG195, and G161; not a proof of HC."""


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def transpose(a: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*a)]


def main() -> None:
    for n in range(2, 13):
        d = 2 * n
        size = d + 2

        # G160 quotient and the two residual-branch contradictions.
        h_1 = 3 * d + 2
        quotient = h_1 - 2 * (d + 1)
        assert quotient == d
        assert 2 * (d - 1) > d
        assert d - 1 > d // 2
        assert 5 < h_1

        # Hyperbolic B with pairs (e_i,f_i).
        b_form = [[0] * size for _ in range(size)]
        for i in range(n + 1):
            b_form[i][n + 1 + i] = 1
            b_form[n + 1 + i][i] = 1

        # R=<e0,f0,e1>, z=e2 in R^perp, t=f2 outside R.
        z = [0] * size
        t = [0] * size
        z[2] = 1
        t[n + 3] = 1
        z_col = [[entry] for entry in z]
        z_row_b = [[sum(z[k] * b_form[k][j] for k in range(size)) for j in range(size)]]
        e_z = matmul(z_col, z_row_b)

        # B-self-adjointness: E^T B = B E.
        assert matmul(transpose(e_z), b_form) == matmul(b_form, e_z)

        # E_z kills e0,f0,e1 and moves t to z, not a multiple of t.
        basis_indices_r = (0, n + 1, 1)
        for index in basis_indices_r:
            image = [e_z[i][index] for i in range(size)]
            assert image == [0] * size
        image_t = [sum(e_z[i][j] * t[j] for j in range(size)) for i in range(size)]
        assert image_t == z and image_t != t

        # G160 and its odd neighbor have the same rank budget.
        for slack in (4 * d + 2, 4 * d + 3):
            assert slack // 2 == 2 * d + 1

        # Exact G161 boundary.
        slack = 4 * d + 4
        delta_1 = 2 * d + 2
        length = 2 * (d + 1) + slack
        h_1 = d + 1 + delta_1
        assert length == 6 * d + 6
        assert h_1 == 3 * d + 3 == length // 2
        assert slack - 2 * delta_1 == 0

    print("PASS: B237 contact dichotomy, NG195, G160 no-go, and G161")


if __name__ == "__main__":
    main()
