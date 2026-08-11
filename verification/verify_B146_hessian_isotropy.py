#!/usr/bin/env python3
"""Finite rank guards for B146; not an analytic proof or HC."""

from fractions import Fraction


def matrix_rank(matrix):
    rows = [[Fraction(entry) for entry in row] for row in matrix]
    if not rows:
        return 0
    row_count = len(rows)
    col_count = len(rows[0])
    pivot_row = 0
    for column in range(col_count):
        pivot = next(
            (row for row in range(pivot_row, row_count)
             if rows[row][column]),
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


for middle_index in range(1, 5):
    ambient_dimension = 2 * middle_index
    for node_count in range(2, 9):
        for value_rank in range(1, node_count):
            support = value_rank + 1
            total_gradient_dimension = ambient_dimension * node_count

            # Identity Hessians and a relation supported on a circuit of
            # size R+1 give a block-diagonal quadratic form of exact rank
            # 2n(R+1).
            quadratic_matrix = [
                [
                    1 if row == column and row < ambient_dimension * support
                    else 0
                    for column in range(total_gradient_dimension)
                ]
                for row in range(total_gradient_dimension)
            ]
            quadratic_rank = matrix_rank(quadratic_matrix)
            assert quadratic_rank == ambient_dimension * support

            maximal_isotropic_dimension = (
                total_gradient_dimension - quadratic_rank
                + quadratic_rank // 2
            )
            forced_corank = (
                total_gradient_dimension - maximal_isotropic_dimension
            )
            assert forced_corank == middle_index * support
            assert forced_corank >= middle_index * (value_rank + 1)

            # Conditional gradient surjectivity contains a coordinate
            # vector on which the relation quadratic is nonzero.
            coordinate = [0] * total_gradient_dimension
            coordinate[0] = 1
            value = sum(
                quadratic_matrix[i][j] * coordinate[i] * coordinate[j]
                for i in range(total_gradient_dimension)
                for j in range(total_gradient_dimension)
            )
            assert value == 1

print("PASS: B146 Hessian obstruction and uniform isotropic-corank floor")
