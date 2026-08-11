#!/usr/bin/env python3
"""Exact finite dimension/rank guards for B153/NG123; not a proof of HC."""

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


for n in range(1, 7):
    symmetric_dimension = n * (n + 1) // 2
    for node_count in range(2, 10):
        for value_rank in range(1, node_count):
            relation_dimension = node_count - value_rank

            # Relation basis [I | B]. Applying all relations independently
            # to every symmetric coefficient is the pure obstruction map.
            relation_basis = [
                [
                    Fraction(
                        int(column == row)
                        if column < relation_dimension
                        else (row + 2) * (column + 1)
                    )
                    for column in range(node_count)
                ]
                for row in range(relation_dimension)
            ]
            rows = relation_dimension * symmetric_dimension
            columns = node_count * symmetric_dimension
            obstruction = [
                [Fraction(0) for _ in range(columns)]
                for _ in range(rows)
            ]
            for relation in range(relation_dimension):
                for node in range(node_count):
                    scalar = relation_basis[relation][node]
                    for coefficient in range(symmetric_dimension):
                        obstruction[
                            relation * symmetric_dimension + coefficient
                        ][node * symmetric_dimension + coefficient] = scalar

            expected_rank = relation_dimension * symmetric_dimension
            assert matrix_rank(obstruction) == expected_rank
            assert columns - expected_rank == value_rank * symmetric_dimension
            assert expected_rank == (
                (node_count - value_rank) * n * (n + 1) // 2
            )
            assert expected_rank > 0

print("PASS: B153 pure Hessian obstruction rank and allowed-space dimension")
