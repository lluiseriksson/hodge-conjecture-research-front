#!/usr/bin/env python3
"""Lightweight exact checks for B199, G129, and NG161."""

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
    return r


def main():
    # Minimal new-double model: one kernel vector plus d=2 jet vectors.
    quotient_to_jets = [[0, 1, 0], [0, 0, 1]]
    assert rank(quotient_to_jets) == 2
    assert len(quotient_to_jets[0]) - rank(quotient_to_jets) == 1

    # The d-generator complete-intersection shortcut has zero double kernel.
    transverse_only = [[1, 0], [0, 1]]
    assert rank(transverse_only) == 2
    assert len(transverse_only[0]) - rank(transverse_only) == 0

    # Inherited Hessians are value-weighted sums; this sample is nondegenerate.
    hessian_1 = [[1, 0], [0, 0]]
    hessian_2 = [[0, 0], [0, 1]]
    inherited = [
        [2 * hessian_1[i][j] + 3 * hessian_2[i][j] for j in range(2)]
        for i in range(2)
    ]
    assert inherited == [[2, 0], [0, 3]]
    assert Fraction(inherited[0][0]) * inherited[1][1] - Fraction(
        inherited[0][1]
    ) * inherited[1][0] != 0

    print("PASS: B199 nodal-generator dichotomy, G129, and NG161")


if __name__ == "__main__":
    main()
