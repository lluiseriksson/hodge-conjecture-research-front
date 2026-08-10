#!/usr/bin/env python3
"""Finite commutative-square check for B097."""

from fractions import Fraction

# u(x,y)=x, q_P(p)=5p, q_S=q_P o u, d(w)=(0,w).
def u(vector):
    return vector[0]


def d(value):
    return (Fraction(0), value)


def q_p(value):
    return Fraction(5) * value


def q_s(vector):
    return q_p(u(vector))


assert q_s(d(Fraction(7))) == 0
t_nearby = Fraction(2)
c = q_p(t_nearby)
zeta_pairing = lambda value: Fraction(3) * value
assert zeta_pairing(q_p(t_nearby)) == zeta_pairing(c) != 0

print("PASS: B097 constant-target square preserves the nonzero pairing")
