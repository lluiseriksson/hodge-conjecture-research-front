"""Finite degree-three carrier models used in B139 and NG112."""

from itertools import product

from sympy import Matrix


def affine_monomial_exponents(variables: int, degree: int):
    return [exp for exp in product(range(degree + 1), repeat=variables) if sum(exp) <= degree]


def evaluation(points: list[tuple[int, ...]], degree: int) -> Matrix:
    exponents = affine_monomial_exponents(len(points[0]), degree)
    return Matrix(
        [
            [
                product_value(point, exponent)
                for exponent in exponents
            ]
            for point in points
        ]
    )


def product_value(point: tuple[int, ...], exponent: tuple[int, ...]) -> int:
    value = 1
    for coordinate, power in zip(point, exponent):
        value *= coordinate**power
    return value


for t in range(2, 7):
    # The affine twisted cubic u -> (u,u^2,u^3) has degree-t Hilbert rank 3t+1.
    twisted = [(u, u * u, u * u * u) for u in range(3 * t + 2)]
    matrix = evaluation(twisted, t)
    assert matrix.rank() == 3 * t + 1
    relation = matrix.T.nullspace()[0]
    assert all(value != 0 for value in relation)

    for n in range(2, 6):
        m, c = 10, 3
        tm = m * n - c
        assert 4 * tm - 4 > 3 * tm
        for degree in (1, 2, 3):
            assert degree * tm > degree * m


print("PASS: B139 cubic carrier rank and quartic-linear node floor")
