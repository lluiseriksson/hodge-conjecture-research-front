"""Extremal projective-evaluation models used by B137 and NG110."""

from sympy import Matrix


def monomials(point: tuple[int, int], degree: int) -> list[int]:
    x, y = point
    return [x**i * y**j for i in range(degree + 1) for j in range(degree + 1 - i)]


def evaluation(points: list[tuple[int, int]], degree: int) -> Matrix:
    return Matrix([monomials(point, degree) for point in points])


for t in range(2, 8):
    # t+2 collinear points have exactly the expected one-dimensional defect.
    line = [(u, 0) for u in range(t + 2)]
    assert evaluation(line, t).rank() == t + 1

    # The conic exception first occurs at 2t+2 points.
    conic_boundary = [(u, u * u) for u in range(2 * t + 2)]
    assert evaluation(conic_boundary, t).rank() == 2 * t + 1

    # Removing one point restores independence on the same conic.
    assert evaluation(conic_boundary[:-1], t).rank() == 2 * t + 1

    for n in range(2, 6):
        c = 3
        m = max(8, c + 2)
        threshold = 2 * (m * n - c) + 2
        assert threshold > 2 * m
        assert threshold - 1 == 2 * (m * n - c) + 1


print("PASS: B137 line/conic postulation thresholds and linear node floor")
