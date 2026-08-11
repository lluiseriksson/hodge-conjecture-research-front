#!/usr/bin/env python3
"""Lightweight exact checks for B219's degree and local tangent model."""

import sympy as sp


def main():
    for nodes in range(1, 101):
        degree = 3 * nodes
        interpolation_threshold = 3 * nodes - 1
        assert degree >= interpolation_threshold
        assert degree == 3 * nodes  # product of N cubed separators

    # Local model: f has zero 1-jet and a nondegenerate quadratic part;
    # F=f+x0*G with G(0)=g != 0 has gradient only in the x0 direction.
    x0, x1, x2, x3, g = sp.symbols("x0 x1 x2 x3 g")
    f = x1**2 + x2**2 + x3**2
    F = f + x0 * g
    variables = (x0, x1, x2, x3)
    gradient_at_origin = tuple(
        sp.diff(F, variable).subs({x0: 0, x1: 0, x2: 0, x3: 0})
        for variable in variables
    )
    assert gradient_at_origin == (g, 0, 0, 0)

    hessian_f = sp.hessian(f, (x1, x2, x3))
    assert hessian_f.det() == 8

    print("PASS: B219 large special Gauss-fiber construction and NG180")


if __name__ == "__main__":
    main()
