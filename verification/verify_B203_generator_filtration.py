#!/usr/bin/env python3
"""Exact linear checks for B203, G133, and NG165."""

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
    # K=C^3, rho(x,y,z)=(x,y), T=ker rho=<e3>.
    rho_rows = [[1, 0, 0], [0, 1, 0]]
    assert rank(rho_rows) == 2
    triple = [0, 0, 1]
    assert [sum(row[i] * triple[i] for i in range(3)) for row in rho_rows] == [0, 0]

    # P=<e2,e3>: it contains T, while rho(P)=<e2>.
    p_basis = [[0, 1, 0], [0, 0, 1]]
    assert rank(p_basis) == 2
    assert rank(p_basis + [triple]) == 2

    # The quadratic-new profile e1 spans ker(partial)/rho(P), so D=K/P is one-dimensional.
    quadratic_new = [1, 0, 0]
    assert rank(p_basis + [quadratic_new]) == 3
    assert 3 - rank(p_basis) == 1

    # A decomposable profile e2 and every triple correction stay in P.
    decomposable_lift = [0, 1, 5]
    assert rank(p_basis + [decomposable_lift]) == 2

    print("PASS: B203 generator filtration, G133, and NG165")


if __name__ == "__main__":
    main()
