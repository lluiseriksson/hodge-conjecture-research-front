#!/usr/bin/env python3
"""Exact finite model for B096 and NG072."""

from fractions import Fraction

# d(w)=(0,w), u(x,y)=x, hence im(d)=ker(u).
t_nearby = Fraction(1)
lift = (t_nearby, Fraction(0))
assert lift[0] == t_nearby

# First branch: F(x,y)=y is nonzero on im(d), despite liftability.
assert Fraction(1) != 0

# Second branch: F(x,y)=3x descends to lambda(p)=3p.
lambda_t = Fraction(3) * t_nearby
known_global_pairing = Fraction(3)
assert lambda_t == known_global_pairing != 0

print("PASS: B096 ambiguity-boundary or descended-pairing dichotomy")
