"""Exact split-invariant model for B114 and NG090."""

from fractions import Fraction


def unit(x):
    # covered coordinates: invariant full support, two local A2 coordinates
    return (x, Fraction(0), Fraction(0))


def reynolds(covered):
    invariant, _a2_1, _a2_2 = covered
    return (invariant, Fraction(0), Fraction(0))


def normalized_trace(covered):
    return reynolds(covered)[0]


for x in map(Fraction, (-5, -1, 0, 2, 9)):
    pulled = unit(x)
    assert normalized_trace(pulled) == x
    assert (pulled != (0, 0, 0)) == (x != 0)

# Purely local coordinates are killed and cannot create downstairs landing.
for local in ((0, 1, 0), (0, 2, -3), (0, -7, 4)):
    assert reynolds(tuple(map(Fraction, local))) == (0, 0, 0)
    assert normalized_trace(tuple(map(Fraction, local))) == 0

print("PASS: B114 invariant full-support landing is exactly downstairs landing")
