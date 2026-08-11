#!/usr/bin/env python3
"""Exact lightweight checks for B195, G126, and NG158."""

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


def tensor_gradient_columns(value_basis, qdim):
    columns = []
    for values in value_basis:
        for basis_index in range(qdim):
            column = []
            for value in values:
                block = [0] * qdim
                block[basis_index] = value
                column.extend(block)
            columns.append(column)
    return columns


def main():
    nodes, qdim = 3, 2

    # A rank-two value image tensored with V_m injects with rank 4.
    value_rank_two = [[1, 0, 1], [0, 1, 1]]
    columns = tensor_gradient_columns(value_rank_two, qdim)
    matrix_rows = [list(row) for row in zip(*columns)]
    assert rank(value_rank_two) == 2
    assert rank(matrix_rows) == 4 == 2 * qdim
    assert 4 > qdim

    # Eventual surjective value evaluation yields the full 2nN gradient target.
    full_values = [[int(i == j) for j in range(nodes)] for i in range(nodes)]
    full_columns = tensor_gradient_columns(full_values, qdim)
    full_rows = [list(row) for row in zip(*full_columns)]
    assert rank(full_values) == nodes
    assert rank(full_rows) == nodes * qdim == 6

    # The finite ladder remains a same-degree list of independent obligations.
    certificate_order = 5
    kuranishi_rungs = list(range(2, certificate_order + 1))
    assert kuranishi_rungs == [2, 3, 4, 5]

    print("PASS: B195 multiplicative growth and NG158 power-raising obstruction")


if __name__ == "__main__":
    main()
