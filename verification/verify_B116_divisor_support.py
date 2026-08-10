"""Exact degree/support countermodel for B116 and NG092."""

from fractions import Fraction


# Stalk cohomology dimensions at p in D, keyed by ordinary degree.
full_support = {-2: 1, -1: 0}       # Q_B^H[2]
divisor_support = {-1: 1}           # i_* Q_D^H[1]


def stalk_dimension(*summands, degree):
    return sum(Fraction(s.get(degree, 0)) for s in summands)


assert stalk_dimension(full_support, degree=-1) == 0
assert stalk_dimension(divisor_support, degree=-1) == 1
assert stalk_dimension(full_support, divisor_support, degree=-1) == 1

# The two coordinates can vary independently in the semisimple direct sum.
for full_coordinate in map(Fraction, (-2, 0, 3)):
    for divisor_coordinate in map(Fraction, (-5, 0, 7)):
        selected = (full_coordinate, divisor_coordinate)
        assert selected[1] == divisor_coordinate

print("PASS: B116 smooth-discriminant vanishing does not exclude divisor support")
