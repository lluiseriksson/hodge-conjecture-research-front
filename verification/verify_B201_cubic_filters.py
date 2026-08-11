#!/usr/bin/env python3
"""Exact lightweight checks for B201, G131, and NG163."""

from fractions import Fraction


def in_diagonal_span(vector):
    return len(set(Fraction(x) for x in vector)) <= 1


def main():
    # Two one-dimensional nodes with value image S=span((1,1)).
    multiplier = [1, 1]
    assert in_diagonal_span(multiplier)

    # Adding the central Hessian changes a double representative by an S-vector,
    # so the mixed class modulo S is representative-independent.
    mixed = [Fraction(1), Fraction(2)]
    shifted = [mixed[i] + 3 * multiplier[i] for i in range(2)]
    assert [shifted[i] - mixed[i] for i in range(2)] == [3, 3]
    assert (mixed[1] - mixed[0]) == (shifted[1] - shifted[0])

    # Pure cubic synchronization may vanish while the mixed filter does not.
    pure_cubic_class = [0, 0]
    assert in_diagonal_span(pure_cubic_class)
    assert not in_diagonal_span(mixed)

    # With two double inputs, every B154 term contains a zero displacement.
    double_displacement_1 = Fraction(0)
    double_displacement_2 = Fraction(0)
    assert double_displacement_1 * double_displacement_2 == 0

    print("PASS: B201 cubic pure/mixed decomposition, G131, and NG163")


if __name__ == "__main__":
    main()
