"""Exact checks for B106's cancellation and G059 branch restoration."""

from fractions import Fraction


def discrepancy(b_detector, saito_pairing):
    return b_detector - saito_pairing


# The truth of the terminal inequality is independent of the auxiliary c.
saito_value = Fraction(3)
for b_detector in (Fraction(5), Fraction(11), Fraction(-2), Fraction(0)):
    d_value = discrepancy(b_detector, saito_value)
    assert (d_value != b_detector) == (saito_value != 0)

for b_detector in (Fraction(5), Fraction(11), Fraction(-2), Fraction(0)):
    d_value = discrepancy(b_detector, Fraction(0))
    assert d_value == b_detector


# u(x,y)=x, t_psi=1. Lifts are (1,y).
def u(vector):
    return vector[0]


t_psi = Fraction(1)

# Favorable cokernel/ambiguity branch: F(x,y)=y is nonzero on ker(u).
def f_ambiguity(vector):
    return vector[1]


assert u((1, 0)) == t_psi
assert f_ambiguity((0, 1)) != 0
assert f_ambiguity((1, 1)) != 0

# Descended branch: F(x,y)=2x=u^*(lambda), lambda(t_psi)=2.
def f_descended(vector):
    return 2 * vector[0]


assert f_descended((0, 1)) == 0
assert f_descended((1, 0)) == f_descended((1, 9)) == 2

# Failure of both branches is exactly failure of detection.
def f_zero(vector):
    return Fraction(0)


assert f_zero((0, 1)) == 0
assert f_zero((1, 0)) == 0

print("PASS: B106 detector cancellation and exact G059 collision branches")
