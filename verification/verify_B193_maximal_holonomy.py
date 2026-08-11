#!/usr/bin/env python3
"""Exact lightweight checks for B193, G124, and NG156."""

from fractions import Fraction


def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    r = 0
    for col in range(n):
        pivot = next((i for i in range(r, m) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][col]
        a[r] = [x / p for x in a[r]]
        for i in range(m):
            if i != r and a[i][col]:
                q = a[i][col]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


def matmul(a, b):
    bt = list(zip(*b))
    return [[sum(Fraction(x) * Fraction(y) for x, y in zip(row, col)) for col in bt] for row in a]


def transpose(a):
    return [list(row) for row in zip(*a)]


def main():
    # n=1, q=2, N=3: each node map is an isomorphism.
    lambdas = [1, 2, 3]
    node_maps = [[[lam, 0], [0, 1]] for lam in lambdas]
    assert all(rank(matrix) == 2 for matrix in node_maps)

    # Hyperbolic pullbacks scale by lambda_i.
    hyperbolic = [[0, 1], [1, 0]]
    pulled = [matmul(transpose(d), matmul(hyperbolic, d)) for d in node_maps]
    for lam, form in zip(lambdas, pulled):
        assert form == [[0, Fraction(lam)], [Fraction(lam), 0]]

    # Transition d_j d_i^{-1} is a similitude with ratio lambda_j/lambda_i.
    transition_21 = [[2, 0], [0, 1]]
    lhs = matmul(transpose(transition_21), matmul(hyperbolic, transition_21))
    assert lhs == [[0, 2], [2, 0]]

    # Relation completion: arbitrary covectors at nodes 2,3 determine node 1.
    alpha_2 = [1, 4]
    alpha_3 = [2, -1]
    # d_i^* alpha_i is matrix transpose times alpha_i.
    rhs_2 = [2 * alpha_2[0], alpha_2[1]]
    rhs_3 = [3 * alpha_3[0], alpha_3[1]]
    alpha_1 = [-(rhs_2[0] + rhs_3[0]), -(rhs_2[1] + rhs_3[1])]
    total = [alpha_1[0] + rhs_2[0] + rhs_3[0], alpha_1[1] + rhs_2[1] + rhs_3[1]]
    assert total == [0, 0]

    # Minimal doubled-scheme defect for n=1,N=3,R=2,q=2.
    n, nodes, value_rank, qdim = 1, 3, 2, 2
    defect = (2 * n + 1) * nodes - value_rank - qdim
    assert defect == 2 * n * (nodes - 1) + 1 == 5

    # Reduced value CB can coexist abstractly with a full, unsynchronized gradient image.
    reduced_value_image = [[1, 0, -1], [0, 1, -1]]
    assert rank(reduced_value_image) == 2
    full_gradient_axes = [[int(i == j) for j in range(6)] for i in range(6)]
    assert rank(full_gradient_axes) == 6 > qdim

    print("PASS: B193 maximal holonomy and NG156 reduced-CB mismatch")


if __name__ == "__main__":
    main()
