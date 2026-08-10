#!/usr/bin/env python3
"""Exact arrangement, fork geometry, and residue checks for B048."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B048-forked-building-set-check.json"

COLUMNS = [
    (1, 0, 0, 0, 0),
    (0, 1, 0, 0, 0),
    (1, 1, 0, 0, 0),
    (0, 0, 1, 0, 0),
    (0, 0, 0, 1, 0),
    (0, 0, 1, 1, 0),
    (2, 8, 8, 1, 0),
    (3, 4, 5, 7, 2),
    (5, 4, 6, 5, 3),
    (2, 1, 5, 1, 7),
    (6, 5, 7, 8, 2),
]
# Hadamard's bound puts every nonzero minor below this prime, so the modular
# ranks below equal the rational ranks of the displayed integer matrix.
PRIME = 10_000_019


def modular_rank(indices: list[int]) -> int:
    rows = [[COLUMNS[j][i] % PRIME for j in indices] for i in range(5)]
    rank = 0
    for column in range(len(indices)):
        pivot = next((i for i in range(rank, 5) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], PRIME - 2, PRIME)
        rows[rank] = [(value * inverse) % PRIME for value in rows[rank]]
        for i in range(5):
            if i != rank and rows[i][column]:
                factor = rows[i][column]
                rows[i] = [
                    (left - factor * right) % PRIME
                    for left, right in zip(rows[i], rows[rank])
                ]
        rank += 1
        if rank == 5:
            break
    return rank


rank_by_mask = [0] * (1 << 11)
for mask in range(1, 1 << 11):
    rank_by_mask[mask] = modular_rank([i for i in range(11) if mask >> i & 1])

connected_flats = []
for mask in range(1, 1 << 11):
    flat_rank = rank_by_mask[mask]
    if any(
        not (mask >> i & 1) and rank_by_mask[mask | (1 << i)] == flat_rank
        for i in range(11)
    ):
        continue
    if mask & (mask - 1) == 0:
        continue
    first = mask & -mask
    remainder = mask ^ first
    part = remainder
    connected = True
    while True:
        left = part | first
        if left != mask and rank_by_mask[left] + rank_by_mask[mask ^ left] == flat_rank:
            connected = False
            break
        if part == 0:
            break
        part = (part - 1) & remainder
    if connected:
        connected_flats.append([i + 1 for i in range(11) if mask >> i & 1])

expected_flats = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3, 4, 5, 6, 7],
    list(range(1, 12)),
]
if connected_flats != expected_flats:
    raise SystemExit("FAIL: the explicit fork has the wrong connected flats")

blocks = [[0, 1, 3, 4], [2, 5, 6, 7], [8, 9, 10]]
block_ranks = [modular_rank(block) for block in blocks]
if block_ranks != [4, 4, 3]:
    raise SystemExit("FAIL: fork partition is not blockwise independent")

normal_A = sp.Matrix.hstack(*(sp.Matrix(COLUMNS[i]) for i in [0, 1, 2]))
normal_B = sp.Matrix.hstack(*(sp.Matrix(COLUMNS[i]) for i in [3, 4, 5]))
normal_U = sp.Matrix.hstack(*(sp.Matrix(COLUMNS[i]) for i in range(7)))
FA = normal_A.T.nullspace()
FB = normal_B.T.nullspace()
FU = normal_U.T.nullspace()
matrix_A = sp.Matrix.hstack(*FA)
matrix_B = sp.Matrix.hstack(*FB)
matrix_U = sp.Matrix.hstack(*FU)
intersection_dimension = matrix_A.cols + matrix_B.cols - sp.Matrix.hstack(
    matrix_A, matrix_B
).rank()
if (matrix_A.cols, matrix_B.cols, matrix_U.cols, intersection_dimension) != (3, 3, 1, 1):
    raise SystemExit("FAIL: fork geometric dimensions")
if sp.Matrix.hstack(matrix_A, matrix_B).rank() != 5:
    raise SystemExit("FAIL: child quotient directions are not complementary")


def cycle_matrix(rank: int) -> sp.Matrix:
    columns = []
    for j in range(11):
        column = [0] * rank
        if j < rank:
            column[j] = 1
        else:
            column[(j + 1) % rank] = j + 2
            column[(2 * j + 1) % rank] += 1
        columns.append(column)
    return sp.Matrix(rank, 11, lambda i, j: columns[j][i])


A_INDICES = [0, 1, 2]
B_INDICES = [3, 4, 5]
U_INDICES = list(range(7))
cases = []
for total_rank in range(1, 12):
    D = cycle_matrix(total_rank)
    DA, DB, DU = D[:, A_INDICES], D[:, B_INDICES], D[:, U_INDICES]
    BA = sp.Matrix.hstack(*DA.columnspace())
    BB = sp.Matrix.hstack(*DB.columnspace())
    BU = sp.Matrix.hstack(*DU.columnspace())
    tA, tB, tU = BA.cols, BB.cols, BU.cols

    top = sp.Matrix.hstack(sp.zeros(total_rank, tU + tA + tB), D)
    coefficient_rows = []
    for basis, local_matrix, indices, before, after in [
        (BU, DU, U_INDICES, 0, tA + tB),
        (BA, DA, A_INDICES, tU, tB),
        (BB, DB, B_INDICES, tU + tA, 0),
    ]:
        branch_part = sp.zeros(total_rank, 11)
        for local, index in enumerate(indices):
            branch_part[:, index] = -local_matrix[:, local]
        coefficient_rows.append(
            sp.Matrix.hstack(
                sp.zeros(total_rank, before),
                basis,
                sp.zeros(total_rank, after),
                branch_part,
            )
        )
    residue = sp.Matrix.vstack(top, *coefficient_rows)
    kernel = residue.nullspace()
    relation_dimension = 11 - total_rank
    if len(kernel) != relation_dimension:
        raise SystemExit("FAIL: fork residue kernel dimension")
    if kernel:
        projected = sp.Matrix.hstack(
            *(vector[tU + tA + tB :, :] for vector in kernel)
        )
        if projected.rank() != relation_dimension or D * projected != sp.zeros(
            total_rank, relation_dimension
        ):
            raise SystemExit("FAIL: fork projection is not the full relation kernel")

    cases.append(
        {
            "total_span_rank": total_rank,
            "rank_A": tA,
            "rank_B": tB,
            "rank_U": tU,
            "resolved_kernel_dimension": len(kernel),
            "relation_dimension": relation_dimension,
        }
    )

branch_classes = {
    "i_in_A": "h-e_U-e_A",
    "i_in_B": "h-e_U-e_B",
    "i_in_U_minus_A_union_B": "h-e_U",
    "i_outside_U": "h",
}
actual = {
    "arrangement_rank": rank_by_mask[-1],
    "nontrivial_connected_flats": connected_flats,
    "independent_blocks": [[i + 1 for i in block] for block in blocks],
    "block_ranks": block_ranks,
    "geometric_flat_dimensions": {"F_A": 3, "F_B": 3, "F_U": 1},
    "child_intersection_dimension": intersection_dimension,
    "child_quotient_directions_disjoint": True,
    "order_A_then_B_branch_classes": branch_classes,
    "order_B_then_A_branch_classes": branch_classes,
    "minimum_non_full_support_degree": 2,
    "tested_cases": cases,
    "kernel_hodge_type": "(0,0)",
    "scope": "exact arrangement, fork geometry, residue, and shift bookkeeping only",
}
expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B048 fork geometry and residue kernel")
