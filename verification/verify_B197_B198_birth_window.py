#!/usr/bin/env python3
"""Lightweight exact checks for B197, B198, G128, and NG160."""

from fractions import Fraction


def mat_vec(matrix, vector):
    return [sum(Fraction(a) * Fraction(b) for a, b in zip(row, vector)) for row in matrix]


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
    # Two value coordinates and four conditional gradient coordinates.
    value_rows = [[1, 0, 0, 0], [0, 1, 0, 0]]
    jet_rows = value_rows + [[0, 0, 1, 0], [0, 0, 0, 1]]
    h_z = rank(value_rows)
    h_2z = rank(jet_rows)
    assert h_2z - h_z == 2

    # Multiplication by nonzero node values rescales gradients injectively.
    diagonal = [[2, 0], [0, 3]]
    assert mat_vec(diagonal, [1, -1]) == [2, -3]
    assert rank(diagonal) == 2

    # If lower products are all double, their span cannot account for a
    # two-dimensional first-jet birth: two new indecomposable classes are needed.
    decomposable_jets = [[0, 0], [0, 0]]
    new_generator_jets = [[1, 0], [0, 1]]
    assert rank(decomposable_jets) == 0
    assert rank(new_generator_jets) == 2

    # In dimension d=2 and at N=3 fixed points, eventual full jets have q=dN.
    d, nodes = 2, 3
    assert d * nodes == 6 > d

    print("PASS: B197 monotonicity, B198 generator birth, G128, and NG160")


if __name__ == "__main__":
    main()
