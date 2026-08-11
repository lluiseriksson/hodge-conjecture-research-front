#!/usr/bin/env python3
"""Exact finite rank guards for B152/NG122; not a proof of HC."""

from fractions import Fraction


def matrix_rank(matrix):
    rows = [[Fraction(entry) for entry in row] for row in matrix]
    if not rows:
        return 0
    row_count = len(rows)
    column_count = len(rows[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if rows[row][column]),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [entry / scale for entry in rows[pivot_row]]
        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = rows[row][column]
            if factor:
                rows[row] = [
                    left - factor * right
                    for left, right in zip(rows[row], rows[pivot_row])
                ]
        pivot_row += 1
    return pivot_row


for n in range(1, 6):
    for node_count in range(2, 10):
        for value_rank in range(1, node_count):
            relation_dimension = node_count - value_rank

            # A relation space K with basis [I | B]. Coordinate restrictions
            # span K*. Each cross-pairing block T_i is an invertible scalar
            # multiple of the identity; build F explicitly.
            relation_basis = [
                [
                    Fraction(
                        int(column == row)
                        if column < relation_dimension
                        else (row + 1) * (column + 1)
                    )
                    for column in range(node_count)
                ]
                for row in range(relation_dimension)
            ]

            rows = relation_dimension * n
            columns = node_count * n
            mixed = [[Fraction(0) for _ in range(columns)] for _ in range(rows)]
            for relation in range(relation_dimension):
                for node in range(node_count):
                    scalar = relation_basis[relation][node] * (node + 1)
                    for coordinate in range(n):
                        mixed[relation * n + coordinate][node * n + coordinate] = scalar

            assert matrix_rank(mixed) == n * relation_dimension
            kernel_dimension = columns - matrix_rank(mixed)
            assert kernel_dimension == n * value_rank

            projected_rank = n
            conormal_rank_bound = n * value_rank
            full_gradient_rank_bound = projected_rank + conormal_rank_bound
            full_jet_rank_bound = value_rank + full_gradient_rank_bound
            assert full_jet_rank_bound == (n + 1) * value_rank + n
            assert n * node_count > conormal_rank_bound

print("PASS: B152 mixed Hessian rank, conormal corank, and full-jet bound")
