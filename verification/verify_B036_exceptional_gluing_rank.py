#!/usr/bin/env python3
"""Exact matrix checks for B036; not an IC or Hodge-theoretic proof."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "artifacts" / "B036-exceptional-gluing-rank-check.json"


def example_columns(span_rank: int) -> sp.Matrix:
    """Five nonzero columns spanning Q^span_rank."""
    cols = []
    for i in range(5):
        if i < span_rank:
            col = [0] * span_rank
            col[i] = 1
        else:
            col = [j + i + 1 for j in range(span_rank)]
        cols.append(col)
    return sp.Matrix(span_rank, 5, lambda i, j: cols[j][i])


checks = []
for span_rank in range(1, 6):
    d = example_columns(span_rank)
    if d.rank() != span_rank:
        raise SystemExit(f"FAIL: cycle matrix rank for s={span_rank}")

    zero = sp.zeros(span_rank)
    ident = sp.eye(span_rank)
    symplectic = zero.row_join(ident).col_join((-ident).row_join(zero))
    deltas = sp.zeros(2 * span_rank, 5)
    deltas[:span_rank, :] = d

    nilpotents = []
    for i in range(5):
        delta = deltas[:, i]
        n_i = delta * (delta.T * symplectic)
        if n_i * n_i != sp.zeros(2 * span_rank):
            raise SystemExit(f"FAIL: N_{i + 1}^2 != 0 for s={span_rank}")
        nilpotents.append(n_i)

    n_e = sum(nilpotents, sp.zeros(2 * span_rank))
    if n_e.rank() != span_rank:
        raise SystemExit(f"FAIL: rank N_E != s for s={span_rank}")

    crossing_cokernels = []
    for n_i in nilpotents:
        # Rank of v -> (N_E v, N_i v). The codomain is im(N_E) direct sum
        # im(N_i), of dimension s+1.
        stacked_rank = n_e.col_join(n_i).rank()
        cokernel_dim = span_rank + 1 - stacked_rank
        if cokernel_dim != 1:
            raise SystemExit(f"FAIL: crossing cokernel != 1 for s={span_rank}")
        crossing_cokernels.append(cokernel_dim)

    relation_dim = 5 - d.rank()
    excess = sum(crossing_cokernels) - relation_dim
    if excess != span_rank:
        raise SystemExit(f"FAIL: excess != cycle-span rank for s={span_rank}")

    checks.append(
        {
            "cycle_span_rank": span_rank,
            "relation_dimension": relation_dim,
            "exceptional_log_rank": n_e.rank(),
            "crossing_cokernel_dimensions": crossing_cokernels,
            "crossing_sum_dimension": sum(crossing_cokernels),
            "required_global_constraints": excess,
        }
    )

actual = {
    "branches": 5,
    "cases": checks,
    "identity": "0 -> relations -> Q^5 -> span(delta_i) -> 0",
    "scope": "exact rational matrix checks only",
}
expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
if actual != expected:
    raise SystemExit("FAIL: computed result differs from audited artifact")

print("PASS: B036 crossing excess equals vanishing-cycle span rank")
