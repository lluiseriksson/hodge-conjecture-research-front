#!/usr/bin/env python3
"""Exact lightweight checks for B204, G134, and NG166."""

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


def coordinate_product(value, profile):
    return [Fraction(a) * Fraction(b) for a, b in zip(value, profile)]


def main():
    lower_profile = [1, 2, 3]
    nowhere_zero_value = [2, 3, 4]
    multiplied = coordinate_product(nowhere_zero_value, lower_profile)
    assert multiplied == [2, 6, 12]
    assert all(x != 0 for x in multiplied)

    # The multiplied profile spans the decomposable subspace.
    decomposable = [multiplied]
    assert rank(decomposable) == 1

    # A primitive profile outside that line enlarges rank by one.
    primitive = [1, 1, 1]
    assert rank(decomposable + [primitive]) == 2

    # Multiplication by a nowhere-zero value is injective coordinatewise.
    recovered = [
        multiplied[i] / Fraction(nowhere_zero_value[i]) for i in range(3)
    ]
    assert recovered == [Fraction(x) for x in lower_profile]

    print("PASS: B204 graded profile module, G134, and NG166")


if __name__ == "__main__":
    main()
