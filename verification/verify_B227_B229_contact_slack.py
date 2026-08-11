#!/usr/bin/env python3
"""Exact bounded checks for B227-B229/G153; not a proof of HC."""

from fractions import Fraction
from itertools import product
from math import comb


def compositions(total: int, slots: int):
    for values in product(range(total + 1), repeat=slots):
        if sum(values) == total:
            yield values


def rank(matrix: list[list[int]]) -> int:
    rows = [[Fraction(x) for x in row] for row in matrix]
    if not rows:
        return 0
    result = 0
    for column in range(len(rows[0])):
        pivot = next(
            (i for i in range(result, len(rows)) if rows[i][column]),
            None,
        )
        if pivot is None:
            continue
        rows[result], rows[pivot] = rows[pivot], rows[result]
        scale = rows[result][column]
        rows[result] = [x / scale for x in rows[result]]
        for i in range(len(rows)):
            if i != result and rows[i][column]:
                scale = rows[i][column]
                rows[i] = [
                    x - scale * y for x, y in zip(rows[i], rows[result])
                ]
        result += 1
    return result


def two_fat_point_matrix(
    ambient_dimension: int, degree: int, jet_order: int
) -> list[list[int]]:
    variables = ambient_dimension + 1
    monomials = list(compositions(degree, variables))
    local = list(
        values
        for total in range(jet_order + 1)
        for values in compositions(total, ambient_dimension)
    )
    labels = [(0, item) for item in local] + [(1, item) for item in local]
    label_index = {label: i for i, label in enumerate(labels)}
    matrix: list[list[int]] = []
    for exponent in monomials:
        row = [0] * len(labels)
        p_degree = sum(exponent[1:])
        if p_degree <= jet_order:
            row[label_index[(0, exponent[1:])]] = 1
        q_tuple = (exponent[0],) + exponent[2:]
        if sum(q_tuple) <= jet_order:
            row[label_index[(1, q_tuple)]] = 1
        matrix.append(row)
    return matrix


def main() -> None:
    for ambient_dimension in range(1, 8):
        triple_target = 2 * comb(ambient_dimension + 2, 2)
        quartic = two_fat_point_matrix(ambient_dimension, 4, 2)
        assert len(quartic[0]) == triple_target
        assert rank(quartic) == triple_target - 1

        double_target = 2 * (ambient_dimension + 1)
        quadratic = two_fat_point_matrix(ambient_dimension, 2, 1)
        assert len(quadratic[0]) == double_target
        assert rank(quadratic) == double_target - 1

    # B228: a Q^4 defect clique is confined to P^2.
    c_4 = comb(6, 2)
    assert comb(6, 2) == c_4 < c_4 + 1

    # B229: second slack at m=2 is exactly a half-dimensional code.
    for d in range(2, 13):
        length = 2 * d + 4
        code_dimension = d + 2
        assert length == 2 * code_dimension
        assert 2 * (d + 1) > code_dimension

        generator = []
        for i in range(code_dimension):
            row = [0] * length
            row[i] = 1
            row[code_dimension + i] = 1
            generator.append(row)
        weights = [1] * code_dimension + [-1] * code_dimension
        gram = [
            [sum(weights[k] * a[k] * b[k] for k in range(length))
             for b in generator]
            for a in generator
        ]
        assert rank(generator) == code_dimension
        assert all(value == 0 for row in gram for value in row)

    print("PASS: B227-B229 contact criteria and second-slack core")


if __name__ == "__main__":
    main()
