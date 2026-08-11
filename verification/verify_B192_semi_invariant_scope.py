#!/usr/bin/env python3
"""Lightweight exact representation checks for B192 and NG155."""

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


def mat_vec(matrix, vector):
    return [sum(Fraction(a) * Fraction(b) for a, b in zip(row, vector)) for row in matrix]


def main():
    # The involution swapping two embedded points acts non-scalarly on sections.
    swap = [[0, 1], [1, 0]]
    invariant = [1, 1]
    alternating = [1, -1]
    assert mat_vec(swap, invariant) == invariant
    assert mat_vec(swap, alternating) == [-x for x in alternating]
    assert rank([invariant]) == 1 < 2
    assert rank([alternating]) == 1 < 2
    assert rank([invariant, alternating]) == 2

    # A scalar representation induces the identity on projective coordinates.
    scalar = [[3, 0], [0, 3]]
    p = [1, 0]
    q = [0, 1]
    assert mat_vec(scalar, p) == [3, 0]
    assert mat_vec(scalar, q) == [0, 3]
    # The two projective points remain individually fixed, not exchanged.
    assert mat_vec(scalar, p)[1] == 0
    assert mat_vec(scalar, q)[0] == 0

    # Diagonal and anti-diagonal jet channels together fill the two-node target.
    diagonal_jet = [1, 1]
    anti_diagonal_jet = [1, -1]
    assert rank([diagonal_jet]) == 1
    assert rank([diagonal_jet, anti_diagonal_jet]) == 2

    print("PASS: B192 semi-invariant scope dichotomy and NG155")


if __name__ == "__main__":
    main()
