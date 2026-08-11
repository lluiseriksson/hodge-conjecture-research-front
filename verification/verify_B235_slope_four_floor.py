#!/usr/bin/env python3
"""Exact lightweight checks for B235, NG193, and G159; not a proof of HC."""


def order_at_vertex(exponents: tuple[int, ...], vertex: int) -> int:
    return sum(exponents) - exponents[vertex]


def main() -> None:
    for n in range(2, 13):
        d = 2 * n
        variable_count = d + 2

        # Coordinate quartics isolate every constant/linear jet at each of
        # three noncollinear coordinate vertices.
        for vertex in range(3):
            constant = tuple(4 if j == vertex else 0 for j in range(variable_count))
            assert order_at_vertex(constant, vertex) == 0
            for other_vertex in range(3):
                if other_vertex != vertex:
                    assert order_at_vertex(constant, other_vertex) >= 2

            for direction in range(variable_count):
                if direction == vertex:
                    continue
                exponents = [0] * variable_count
                exponents[vertex] = 3
                exponents[direction] = 1
                monomial = tuple(exponents)
                assert order_at_vertex(monomial, vertex) == 1
                for other_vertex in range(3):
                    if other_vertex != vertex:
                        assert order_at_vertex(monomial, other_vertex) >= 2

        # Standard polarization: two tangents plus quotient rank d-1.
        standard_h_floor = 2 * (d + 1) + (d - 1)
        assert standard_h_floor == 3 * d + 1
        standard_delta_floor = standard_h_floor - (d + 1)
        assert standard_delta_floor == 2 * d
        assert 2 * standard_delta_floor == 4 * d

        # Square/higher polarizations: three independent double jets.
        powered_h_floor = 3 * (d + 1)
        powered_delta_floor = powered_h_floor - (d + 1)
        assert powered_delta_floor == 2 * d + 2
        assert 2 * powered_delta_floor == 4 * d + 4

        # Exact G159 boundary.
        slack = 4 * d
        delta_1 = 2 * d
        length = 2 * (d + 1) + slack
        h_1 = d + 1 + delta_1
        assert length == 6 * d + 2
        assert h_1 == 3 * d + 1 == length // 2
        assert slack - 2 * delta_1 == 0

        if d >= 6:
            assert 2 * d + 8 < 4 * d  # G158 is below the floor.

    # B215 separates three doubles from exponent five.
    for k in range(3, 10):
        assert 2 * k >= 5

    print("PASS: B235 slope-four floor, NG193, G158 no-go, and G159")


if __name__ == "__main__":
    main()
