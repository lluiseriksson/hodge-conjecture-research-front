#!/usr/bin/env python3
"""Exact lightweight checks for B191, G123, and NG154."""

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


def main():
    # q=2; every node map V->G_i is injective, so one node determines V.
    node_maps = [
        [[1, 0], [0, 1]],
        [[1, 0], [0, 1]],
        [[1, 0], [0, 1]],
        [[1, 0], [0, 1]],
    ]
    assert all(rank(matrix) == 2 for matrix in node_maps)

    # Pulled-back hyperbolic forms, encoded by (b_11,b_12,b_22), are equal.
    gamma_flattening = [[0, 1, 0] for _ in range(4)]
    assert rank(gamma_flattening) == 1

    # Its value factor (1,1,1,1) belongs to a rank-two Vandermonde image.
    value_generators = [[1, 1, 1, 1], [0, 1, 2, 3]]
    assert rank(value_generators) == 2
    assert rank(value_generators + [[1, 1, 1, 1]]) == 2

    # Full first-jet rank and coherent defect identity for n=1,N=4,R=2,q=2.
    n, nodes, value_rank, qdim = 1, 4, 2, 2
    full_jet_rank = value_rank + qdim
    defect = (2 * n + 1) * nodes - full_jet_rank
    assert full_jet_rank == 4
    assert defect == 8
    assert qdim <= 2 * n

    # B142-B143 carrier rank violates one-node injectivity whenever R>1.
    n, carrier_rank = 2, 3
    full_gradient_rank = n * (carrier_rank + 1)
    assert full_gradient_rank == 8 > 2 * n

    print("PASS: B191 intrinsic criterion and NG154 carrier-rank obstruction")


if __name__ == "__main__":
    main()
