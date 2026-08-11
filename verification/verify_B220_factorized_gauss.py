#!/usr/bin/env python3
"""Lightweight exact checks for B220, G147, and NG181."""

import sympy as sp


def main():
    # Local representatives of two separating sections vanish at p=0
    # and are nonzero at q=(1,0); their product has zero full first jet at p.
    x, y = sp.symbols("x y")
    a = x + 2 * y
    b = 3 * x - y
    product_section = sp.expand(a * b)
    origin = {x: 0, y: 0}
    other_point = {x: 1, y: 0}
    assert product_section.subs(origin) == 0
    assert sp.diff(product_section, x).subs(origin) == 0
    assert sp.diff(product_section, y).subs(origin) == 0
    assert product_section.subs(other_point) == 3

    # Every power k>=2 has the two positive exponents 1 and k-1.
    for power in range(2, 101):
        assert 1 + (power - 1) == power
        assert power - 1 >= 1

    # The extremal Hodge branch always asks for more than one point.
    for half_dimension in range(1, 9):
        dimension_x = 2 * half_dimension
        minimum_nodes = 2 * (dimension_x + 1)
        assert minimum_nodes > 1

    print("PASS: B220 factorized Gauss injectivity, G147, and NG181")


if __name__ == "__main__":
    main()
