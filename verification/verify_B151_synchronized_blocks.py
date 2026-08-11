#!/usr/bin/env python3
"""Finite rank guards for B151's block dichotomy; not a proof of HC."""

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


for n in range(1, 7):
    domain_dimension = n + 3
    common = [
        [Fraction(int(row == column)) for column in range(domain_dimension)]
        for row in range(n)
    ]
    synchronized_blocks = []
    for node in range(2, 9):
        phi = [
            [
                Fraction(
                    (node + 1) if row == column
                    else int(column == row + 1)
                )
                for column in range(n)
            ]
            for row in range(n)
        ]
        block = multiply(phi, common)
        assert matrix_rank(block) == n
        synchronized_blocks.extend(block)
    assert matrix_rank(synchronized_blocks) == n

    if n > 1:
        local_defect = [row[:] for row in common]
        local_defect[-1] = [Fraction(0)] * domain_dimension
        assert matrix_rank(local_defect) == n - 1

print("PASS: B151 surjective blocks synchronize at total rank n; alternate is local defect")
