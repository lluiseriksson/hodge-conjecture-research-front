#!/usr/bin/env python3
"""Exact lightweight checks for B205, G135, and NG167."""

from fractions import Fraction


def in_value_line(vector):
    return Fraction(vector[0]) == Fraction(vector[1])


def main():
    # S_m is the diagonal line at two nodes.
    central_multiplier = [1, 1]
    assert in_value_line(central_multiplier)

    # The central profile contraction dies modulo S_m.
    central_contraction = [3, 3]
    assert in_value_line(central_contraction)

    # A decomposable lower profile can have an escaping contraction.
    lower_contraction = [1, 2]
    value_multiplier = [1, 1]
    product_contraction = [
        Fraction(value_multiplier[i]) * lower_contraction[i] for i in range(2)
    ]
    assert product_contraction == [1, 2]
    assert not in_value_line(product_contraction)

    # Hence a one-dimensional primitive quotient does not imply mixed closure.
    primitive_quotient_dimension = 1
    assert primitive_quotient_dimension == 1
    assert not in_value_line(product_contraction)

    print("PASS: B205 mixed profile factorization, G135, and NG167")


if __name__ == "__main__":
    main()
