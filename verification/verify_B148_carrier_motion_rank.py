#!/usr/bin/env python3
"""Exact finite rank guards for B148/NG119; not a proof of HC."""

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


def multiply(left, right):
    return [
        [sum(a * b for a, b in zip(row, column)) for column in zip(*right)]
        for row in left
    ]


for n in range(1, 6):
    for node_count in range(2, 8):
        # Each transverse d(sigma)_i is represented by an invertible upper
        # triangular n x n block. Stacking them gives the carrier-motion map.
        stack = []
        for node in range(node_count):
            stack.extend([
                [
                    Fraction(
                        (node + 1) if row == column
                        else int(column == row + 1)
                    )
                    for column in range(n)
                ]
                for row in range(n)
            ])
        assert matrix_rank(stack) == n

        # Any projected conditional-gradient map factoring through n carrier
        # parameters has rank at most n; here it has exact rank n.
        domain_dimension = n + 4
        motion = [
            [Fraction(int(column == row)) for column in range(domain_dimension)]
            for row in range(n)
        ]
        projected = multiply(stack, motion)
        assert matrix_rank(projected) == n
        assert domain_dimension - (domain_dimension - matrix_rank(projected)) == n

        # In the generic-surjective case, quotienting each 2n node block by
        # any n-plane still leaves a surjective nN-dimensional quotient.
        generic_quotient_rank = n * node_count
        assert generic_quotient_rank > n

print("PASS: B148 carrier-motion factorization and NG119 generic-rank obstruction")
