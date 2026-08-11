#!/usr/bin/env python3
"""Lightweight exact checks for B189, B190, and NG153."""

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


def dot(x, y):
    return sum(Fraction(a) * Fraction(b) for a, b in zip(x, y))


def main():
    # Rank-two Vandermonde value image in C^4; lambda=(1,1,1,1) lies in S.
    one = [1, 1, 1, 1]
    linear = [0, 1, 2, 3]
    relation = [1, -1, -1, 1]
    assert rank([one, linear]) == 2
    assert dot(relation, one) == 0
    assert dot(relation, linear) == 0
    assert all(relation)

    # Diagonal hyperbolic gradients have Hessian span C*lambda, hence A has rank R.
    hessian_values = [one, one]  # B(e,f)=B(f,e)=1; squares vanish.
    assert rank([one, linear] + hessian_values) == 2 < 4
    assert all(dot(relation, h) == 0 for h in hessian_values)

    # A nondegenerate node-supported pair creates the first value axis.
    first_axis = [1, 0, 0]
    value_image = [1, 1, 1]
    assert rank([value_image, first_axis]) == 2
    every_augmented_relation_example = [0, 1, -1]
    assert dot(every_augmented_relation_example, first_axis) == 0
    assert every_augmented_relation_example[0] == 0

    # Full isolated-gradient interpolation makes all value axes Hessian values.
    axes = [[int(i == j) for j in range(3)] for i in range(3)]
    assert rank(axes) == 3
    assert rank([value_image] + axes) == 3

    print("PASS: B189 local-axis filter, B190 conformal synchronization, and NG153")


if __name__ == "__main__":
    main()
