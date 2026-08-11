#!/usr/bin/env python3
"""Exact lightweight checks for B207, G137, NG169, and NG170."""

from fractions import Fraction


def dot(left, right):
    return sum(Fraction(x) * Fraction(y) for x, y in zip(left, right))


def coordinate_product(left, right):
    return [Fraction(x) * Fraction(y) for x, y in zip(left, right)]


def partial(profile):
    return Fraction(profile[0]) - Fraction(profile[1])


def contracted_node_values(profile):
    """A one-coefficient nodewise contraction used in the countermodel."""
    return [Fraction(profile[0]), Fraction(0)]


def main():
    # S_m and E_(m-k) are diagonal; R_m is the anti-diagonal relation.
    multiplier = [1, 1]
    relation = [1, -1]
    assert dot(relation, [4, 4]) == 0

    # e star r spans the annihilator of the diagonal colon.
    e_star_r = coordinate_product(multiplier, relation)
    assert e_star_r == [1, -1]
    assert dot(e_star_r, [3, 3]) == 0
    assert dot(e_star_r, [1, 2]) == -1

    # W=ker(partial) is diagonal and partial^*(1)=(1,-1).
    assert partial([5, 5]) == 0
    absorbed_functional = [1, -1]
    assert absorbed_functional == e_star_r
    assert dot(absorbed_functional, [5, 5]) == 0

    # A relation-weighted nodewise contraction can lie outside im(partial^*).
    nonabsorbed_functional = [1, 0]
    test_profile = [5, 5]
    assert dot(relation, coordinate_product(multiplier, contracted_node_values(test_profile))) == 5
    assert dot(nonabsorbed_functional, [5, 5]) == 5

    print("PASS: B207 dual connecting criterion, G137, NG169, and NG170")


if __name__ == "__main__":
    main()
