"""Finite extremal carrier models used in B138 and NG111."""

from sympy import Matrix


def monomials(point: tuple[int, int], degree: int) -> list[int]:
    x, y = point
    return [x**i * y**j for i in range(degree + 1) for j in range(degree + 1 - i)]


def evaluation(points: list[tuple[int, int]], degree: int) -> Matrix:
    return Matrix([monomials(point, degree) for point in points])


for t in range(2, 8):
    line = [(u, 0) for u in range(t + 2)]
    line_matrix = evaluation(line, t)
    assert line_matrix.rank() == t + 1
    assert all(value != 0 for value in line_matrix.T.nullspace()[0])

    conic = [(u, u * u) for u in range(2 * t + 2)]
    conic_matrix = evaluation(conic, t)
    assert conic_matrix.rank() == 2 * t + 1
    assert all(value != 0 for value in conic_matrix.T.nullspace()[0])

    two_lines = [(u, 0) for u in range(t + 1)] + [(u, 1) for u in range(t + 1)]
    two_line_matrix = evaluation(two_lines, t)
    assert two_line_matrix.rank() == 2 * t + 1
    assert all(value != 0 for value in two_line_matrix.T.nullspace()[0])

    for n in range(2, 6):
        m, c = 9, 3
        tm = m * n - c
        assert 3 * tm > 2 * tm + 2
        assert tm + 1 > m
        assert 2 * tm + 2 > 2 * m


print("PASS: B138 Cayley-Bacharach line/conic carriers and triple-linear floor")
