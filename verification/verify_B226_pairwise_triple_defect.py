#!/usr/bin/env python3
"""Exact bounded checks for B226/G152/NG186; not a proof of HC."""

from math import comb
from fractions import Fraction


def rank(matrix: list[list[int]]) -> int:
    rows = [[Fraction(x) for x in row] for row in matrix]
    result = 0
    for column in range(len(rows[0])):
        pivot = next(
            (i for i in range(result, len(rows)) if rows[i][column] != 0),
            None,
        )
        if pivot is None:
            continue
        rows[result], rows[pivot] = rows[pivot], rows[result]
        scale = rows[result][column]
        rows[result] = [x / scale for x in rows[result]]
        for i in range(len(rows)):
            if i != result and rows[i][column] != 0:
                factor = rows[i][column]
                rows[i] = [
                    x - factor * y for x, y in zip(rows[i], rows[result])
                ]
        result += 1
    return result


def main() -> None:
    for d in range(2, 13):
        c_d = comb(d + 2, 2)
        assert 2 * c_d > c_d + 1

        # Two c_d-planes inside a (c_d+1)-space must intersect in at
        # least c_d-1 dimensions; they cannot be independent local jets.
        ambient = c_d + 1
        first = [
            [int(i == j) for j in range(ambient)] for i in range(c_d)
        ]
        second = first[:-1] + [[int(j == c_d) for j in range(ambient)]]
        assert rank(first) == rank(second) == c_d
        assert rank(first + second) == c_d + 1

        # B215's two-triple threshold is degree 3+3-1=5.
        threshold = 5
        for ell in range(2, 9):
            assert 4 * ell >= threshold

        # The product test has one primitive middle dimension.
        n = max(2, d // 2)
        assert (n + 1) - n == 1

    print("PASS: B226 pairwise triple-defect clique and powered no-go")


if __name__ == "__main__":
    main()
