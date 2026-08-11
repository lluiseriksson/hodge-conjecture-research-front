#!/usr/bin/env python3
"""Exact block-rank guards for B145; not an analytic proof or HC."""

from fractions import Fraction


def rank(matrix):
    rows = [[Fraction(value) for value in row] for row in matrix]
    if not rows:
        return 0
    row_count = len(rows)
    col_count = len(rows[0])
    pivot_row = 0
    for column in range(col_count):
        pivot = next(
            (r for r in range(pivot_row, row_count) if rows[r][column]),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [entry / scale for entry in rows[pivot_row]]
        for r in range(row_count):
            if r != pivot_row and rows[r][column]:
                factor = rows[r][column]
                rows[r] = [
                    left - factor * right
                    for left, right in zip(rows[r], rows[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


for node_count in range(1, 7):
    for ambient_dimension in (2, 4, 6):
        for value_rank in range(1, node_count + 1):
            section_dimension = node_count + 2

            # A value matrix of the prescribed rank.
            values = [
                [1 if column == row else 0 for column in range(section_dimension)]
                for row in range(value_rank)
            ]
            values += [[0] * section_dimension for _ in range(node_count - value_rank)]

            # Linearized equations have value rows E and, for every node,
            # gradient rows with an identity Hessian in the node-motion block.
            total_columns = section_dimension + ambient_dimension * node_count
            matrix = []
            for row in values:
                matrix.append(row + [0] * (ambient_dimension * node_count))
            for node in range(node_count):
                for coordinate in range(ambient_dimension):
                    row = [0] * total_columns
                    row[
                        section_dimension
                        + node * ambient_dimension
                        + coordinate
                    ] = 1
                    matrix.append(row)

            assert rank(values) == value_rank
            assert rank(matrix) == value_rank + ambient_dimension * node_count
            kernel_dimension = total_columns - rank(matrix)
            assert kernel_dimension == section_dimension - value_rank

print("PASS: B145 Hessian blocks leave exactly the value-evaluation kernel")
