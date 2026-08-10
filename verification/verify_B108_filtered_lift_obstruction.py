"""Exact finite checks for B108, NG084, and G071."""

from fractions import Fraction


# Pure Tate model: S=Q^2, S0=span(e0), P=Q^2.
def u_bad(vector):
    _x0, x1 = vector
    return (x1, Fraction(0))


t = (Fraction(1), Fraction(0))
ordinary_lift = (Fraction(0), Fraction(1))
assert u_bad(ordinary_lift) == t

# Every element of S0=(a,0) maps to zero, so [t] in im(u)/u(S0) is nonzero.
for a in (Fraction(-2), Fraction(0), Fraction(3)):
    assert u_bad((a, Fraction(0))) == (0, 0)
assert t != (0, 0)

# Positive comparison: changing the map so u(S0) contains t kills the coset.
def u_good(vector):
    x0, _x1 = vector
    return (x0, Fraction(0))


filtered_lift = (Fraction(1), Fraction(0))
assert u_good(filtered_lift) == t

print("PASS: B108 filtered-lift obstruction and NG084 Tate countermodel")
