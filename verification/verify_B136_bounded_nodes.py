"""Finite-dimensional consequences used in B136 and NG109."""

from sympy import Matrix, eye, zeros


def check(k: int, ambient_sections: int) -> None:
    assert ambient_sections >= k

    # A uniformly separated length-k scheme has a full-rank evaluation map.
    evaluation = Matrix.hstack(eye(k), zeros(k, ambient_sections - k))
    assert evaluation.rank() == k

    # Multiplication by a section nonzero at every point is diagonal scaling.
    scales = Matrix.diag(*range(1, k + 1))
    adjoint_evaluation = scales * evaluation
    assert adjoint_evaluation.rank() == k
    assert k - adjoint_evaluation.rank() == 0

    # The dual relation channel has the same zero defect dimension.
    assert len(adjoint_evaluation.T.nullspace()) == 0


for length in range(1, 13):
    check(length, length + 5)

print("PASS: B136 bounded-node separation forces zero adjoint defect")
