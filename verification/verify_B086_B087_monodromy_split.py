#!/usr/bin/env python3
"""Verify finite Reynolds lifting and the residual unipotent obstruction."""

from fractions import Fraction

# C2 acts on A=V direct-sum J by (v,j)->(v,-j).
t = (Fraction(1), Fraction(3))
sigma_t = (t[0], -t[1])
average = tuple((a + b) / 2 for a, b in zip(t, sigma_t))
assert average == (1, 0)

# Unipotent extension: N(e0)=e1 and N(e1)=0.
def nilpotent(vector):
    x, _y = vector
    return (Fraction(0), x)


assert nilpotent((1, 0)) == (0, 1)
assert nilpotent((0, 1)) == (0, 0)

# Adding any kernel vector cannot cancel N(e0), since N|J=0.
for k in range(-5, 6):
    assert nilpotent((1, Fraction(k))) == (0, 1)

print("PASS: finite averaging splits, while the unipotent residue obstruction can survive")
