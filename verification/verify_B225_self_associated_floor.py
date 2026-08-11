#!/usr/bin/env python3
"""Exact bounded checks for B225/G151/NG185; not a proof of HC."""

from fractions import Fraction
from math import comb


def lower_rank(d: int, k: int) -> int:
    q, r = divmod(k + 1, 3)
    return comb(d + 2, 2) * q + (0, 1, d + 1)[r]


def transpose(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(column) for column in zip(*matrix)]


def multiply(
    left: list[list[Fraction]], right: list[list[Fraction]]
) -> list[list[Fraction]]:
    right_t = transpose(right)
    return [
        [sum(x * y for x, y in zip(row, column)) for column in right_t]
        for row in left
    ]


def main() -> None:
    for d in range(2, 13):
        c_d = comb(d + 2, 2)
        assert lower_rank(d, 3) == c_d + 1
        d_5 = c_d + lower_rank(d, 3)
        assert d_5 + 1 == 2 * (c_d + 1)

    # Abstract self-associated matrices exist abundantly: [I|M] is
    # self-dual for diag(I,-I) whenever M is rational orthogonal.
    for r in range(3, 12):
        vector = [Fraction(i + 1) for i in range(r)]
        norm = sum(x * x for x in vector)
        identity = [
            [Fraction(int(i == j)) for j in range(r)] for i in range(r)
        ]
        householder = [
            [identity[i][j] - 2 * vector[i] * vector[j] / norm for j in range(r)]
            for i in range(r)
        ]
        assert multiply(householder, transpose(householder)) == identity
        generator = [
            identity[i] + householder[i] for i in range(r)
        ]
        weighted_transpose = []
        for column_index, column in enumerate(transpose(generator)):
            weight = Fraction(1 if column_index < r else -1)
            weighted_transpose.append([weight * x for x in column])
        gram = multiply(generator, weighted_transpose)
        assert gram == [[Fraction(0) for _ in range(r)] for _ in range(r)]

    print("PASS: B225 first viable degree and abstract self-associated code")


if __name__ == "__main__":
    main()
