"""Exact checks for B109, NG085, and G072."""

from fractions import Fraction


def u(c, vector):
    a, b, e = vector
    del a
    return (c * b + e, b)  # coordinates (x,y)


t = (Fraction(0), Fraction(1))  # y

# c=0: b is a filtered lift in S0=span(a,b).
s_filtered = (Fraction(0), Fraction(1), Fraction(0))
assert u(Fraction(0), s_filtered) == t

# c=1: b-e is an ordinary lift, but no vector (a,b,0) maps to y.
s_ordinary = (Fraction(0), Fraction(1), Fraction(-1))
assert u(Fraction(1), s_ordinary) == t
for a in (Fraction(-2), Fraction(0), Fraction(3)):
    for b in (Fraction(-2), Fraction(0), Fraction(1), Fraction(3)):
        image = u(Fraction(1), (a, b, Fraction(0)))
        assert image != t

# Associated graded maps are independent of c:
# gr_-1 sends a to 0; gr_0 sends b to y mod x; the higher e maps to F_0 P.
for c in (Fraction(0), Fraction(1), Fraction(7)):
    assert u(c, (1, 0, 0)) == (0, 0)
    x_coord, y_coord = u(c, (0, 1, 0))
    assert y_coord == 1  # same class modulo span(x)
    assert u(c, (0, 0, 1)) == (1, 0)  # zero in P/F_0 P

print("PASS: B109 off-diagonal extension class and NG085 graded-data guard")
