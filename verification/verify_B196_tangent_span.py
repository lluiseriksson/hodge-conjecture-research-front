#!/usr/bin/env python3
"""Exact lightweight linear checks for B196, G127, and NG159."""

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
    # Point span S in W*=C^5, with vector dimension d+1=3.
    point_span = [
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
    ]
    tangent_1 = point_span
    tangent_2 = [point_span[0], point_span[1], [1, 1, 1, 0, 0]]
    assert rank(point_span) == 3
    assert rank(point_span + tangent_1 + tangent_2) == 3

    # Hyperplanes annihilating S (coordinates 4,5) annihilate absorbed tangents.
    annihilator_4 = [0, 0, 0, 1, 0]
    annihilator_5 = [0, 0, 0, 0, 1]
    for tangent in tangent_1 + tangent_2:
        assert sum(Fraction(a) * Fraction(b) for a, b in zip(annihilator_4, tangent)) == 0
        assert sum(Fraction(a) * Fraction(b) for a, b in zip(annihilator_5, tangent)) == 0

    # A tangent direction outside S creates a value-zero section with nonzero derivative.
    escaping_tangent = [0, 0, 0, 1, 0]
    assert rank(point_span + [escaping_tangent]) == 4
    assert sum(Fraction(a) * Fraction(b) for a, b in zip(annihilator_4, escaping_tangent)) == 1

    # The proper absorbing span obeys the d+1 floor.
    variety_dimension = 2
    assert rank(point_span) >= variety_dimension + 1

    print("PASS: B196 tangent-span criterion and NG159 Terracini scope guard")


if __name__ == "__main__":
    main()
