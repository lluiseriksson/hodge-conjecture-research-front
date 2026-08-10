#!/usr/bin/env python3
"""Exact finite arrangement and residue checks for B047; not an IC/MHM proof."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B047-three-level-nested-chain-check.json"

COLUMNS = [
    (1, 0, 0, 0, 0),
    (0, 1, 0, 0, 0),
    (1, 1, 0, 0, 0),
    (0, 0, 1, 0, 0),
    (1, 2, 3, 0, 0),
    (0, 0, 0, 1, 0),
    (7, 5, 2, 2, 0),
    (3, 3, 7, 5, 8),
    (2, 4, 8, 2, 7),
    (3, 1, 7, 5, 1),
    (9, 6, 5, 4, 5),
]

# Every nonzero minor has absolute value below this prime by Hadamard's
# inequality, so modular and rational ranks agree for this 5-by-11 matrix.
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
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 6, 7],
    list(range(1, 12)),
]
if connected_flats != expected_flats:
    raise SystemExit("FAIL: the explicit arrangement has the wrong connected flats")

blocks = [[0, 1, 3, 5], [2, 4, 6, 7], [8, 9, 10]]
block_ranks = [modular_rank(block) for block in blocks]
if block_ranks != [4, 4, 3]:
    raise SystemExit("FAIL: stated three-block partition is not independent")


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


S_INDICES = [0, 1, 2]
T_INDICES = list(range(5))
U_INDICES = list(range(7))
cases = []
for total_rank in range(1, 12):
    D = cycle_matrix(total_rank)
    DS, DT, DU = D[:, S_INDICES], D[:, T_INDICES], D[:, U_INDICES]
    BS = sp.Matrix.hstack(*DS.columnspace())
    BT = sp.Matrix.hstack(*DT.columnspace())
    BU = sp.Matrix.hstack(*DU.columnspace())
    tS, tT, tU = BS.cols, BT.cols, BU.cols

    top = sp.Matrix.hstack(sp.zeros(total_rank, tU + tT + tS), D)
    coefficient_rows = []
    for basis, local_matrix, indices, before, after in [
        (BU, DU, U_INDICES, 0, tT + tS),
        (BT, DT, T_INDICES, tU, tS),
        (BS, DS, S_INDICES, tU + tT, 0),
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
        raise SystemExit("FAIL: four-class residue kernel has the wrong dimension")
    if kernel:
        projected = sp.Matrix.hstack(
            *(vector[tU + tT + tS :, :] for vector in kernel)
        )
        if projected.rank() != relation_dimension or D * projected != sp.zeros(
            total_rank, relation_dimension
        ):
            raise SystemExit("FAIL: projection is not the full relation kernel")

    cases.append(
        {
            "total_span_rank": total_rank,
            "rank_S": tS,
            "rank_T": tT,
            "rank_U": tU,
            "resolved_kernel_dimension": len(kernel),
            "relation_dimension": relation_dimension,
        }
    )

actual = {
    "arrangement_rank": rank_by_mask[-1],
    "nontrivial_connected_flats": connected_flats,
    "independent_blocks": [[i + 1 for i in block] for block in blocks],
    "block_ranks": block_ranks,
    "exceptional_fiber": "Bl_strict_plane(Bl_strict_line(Bl_point(P^4)))",
    "branch_classes": {
        "i_in_S": "h-e_U-e_T-e_S",
        "i_in_T_minus_S": "h-e_U-e_T",
        "i_in_U_minus_T": "h-e_U",
        "i_outside_U": "h",
    },
    "minimum_non_full_support_degree": 2,
    "tested_cases": cases,
    "kernel_hodge_type": "(0,0)",
    "scope": "exact arrangement, residue-matrix, and support-shift bookkeeping only",
}
expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B047 three-level nested-chain checks")
