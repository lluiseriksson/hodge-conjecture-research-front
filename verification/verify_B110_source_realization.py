"""Finite exact countermodel for B110 and NG086."""

from fractions import Fraction


# Coordinates: C=Q, A=Q, S=Q, P=Q^2.
def q_c(t):
    return t


def u(s):
    return (s, Fraction(0))


def q_p(v):
    x, y = v
    return x + y


t = Fraction(1)
c = q_c(t)
rho_liftable = (Fraction(1), Fraction(0))
rho_not_liftable = (Fraction(0), Fraction(1))

assert q_p(rho_liftable) == c
assert q_p(rho_not_liftable) == c
assert rho_liftable == u(Fraction(1))
assert all(u(s) != rho_not_liftable for s in map(Fraction, range(-5, 6)))

print("PASS: B110 equal ambient data do not determine nearby liftability")
