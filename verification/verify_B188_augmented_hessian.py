#!/usr/bin/env python3
"""Bounded checks for B188/G121/NG152; not a proof of HC."""

from fractions import Fraction


def rank(columns):
    """Rank of a matrix supplied as equal-length column vectors."""
    if not columns:
        return 0
    matrix = [list(row) for row in zip(*columns)]
    rows = len(matrix)
    cols = len(columns)
    pivot_row = 0
    for col in range(cols):
        pivot = next(
            (row for row in range(pivot_row, rows) if matrix[row][col]),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = matrix[pivot_row][col]
        matrix[pivot_row] = [entry / scale for entry in matrix[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            factor = matrix[row][col]
            if factor:
                matrix[row] = [
                    entry - factor * base
                    for entry, base in zip(matrix[row], matrix[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


value_column = (Fraction(1), Fraction(1))

# NG151's diagonal model: Hessian pairings lie in the value image, so the
# augmented rank stays one and c=(1,-1) annihilates both.
diagonal_hessian = (Fraction(1), Fraction(1))
assert rank([value_column, diagonal_hessian]) == 1
full_support_relation = (Fraction(1), Fraction(-1))
assert sum(a * b for a, b in zip(full_support_relation, value_column)) == 0
assert (
    sum(a * b for a, b in zip(full_support_relation, diagonal_hessian))
    == 0
)


# NG152's one-node model: its Hessian span adds (1,0), making the augmented
# map surjective even though dim(U)=nN.
one_node_hessian = (Fraction(1), Fraction(0))
assert rank([value_column, one_node_hessian]) == 2
assert (
    sum(a * b for a, b in zip(full_support_relation, one_node_hessian))
    != 0
)


# Rank-nullity check for representative augmented maps in N coordinates.
for target_dimension in range(2, 10):
    standard_columns = [
        tuple(Fraction(int(i == j)) for i in range(target_dimension))
        for j in range(target_dimension)
    ]
    for used in range(target_dimension + 1):
        augmented_rank = rank(standard_columns[:used])
        annihilator_dimension = target_dimension - augmented_rank
        assert augmented_rank == used
        assert annihilator_dimension == target_dimension - used

print("PASS: B188 identifies the augmented defect; NG152 blocks rank-only isotropy")
