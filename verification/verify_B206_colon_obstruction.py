#!/usr/bin/env python3
"""Exact lightweight checks for B206, G136, and NG168."""

from fractions import Fraction


def coordinate_product(left, right):
    return [Fraction(x) * Fraction(y) for x, y in zip(left, right)]


def in_diagonal_line(vector):
    return Fraction(vector[0]) == Fraction(vector[1])


def main():
    # Two-node model: E_(m-k)=E_k=S_m is the diagonal line.
    multiplier = [1, 1]
    global_value = [3, 3]
    assert in_diagonal_line(coordinate_product(multiplier, global_value))

    # Its colon is again the diagonal line.
    escaping_contraction = [1, 2]
    assert not in_diagonal_line(
        coordinate_product(multiplier, escaping_contraction)
    )

    # Hence the colon-quotient obstruction detects the mixed failure.
    delta_nonzero = not in_diagonal_line(escaping_contraction)
    assert delta_nonzero

    # A colon can be strictly larger than the lower value space.
    # E_a=S_m=span(1,0): every y multiplies into S_m.
    sparse_multiplier = [1, 0]
    arbitrary_y = [5, 7]
    assert coordinate_product(sparse_multiplier, arbitrary_y) == [5, 0]

    print("PASS: B206 colon obstruction, G136, and NG168")


if __name__ == "__main__":
    main()
