#!/usr/bin/env python3
"""Exact rank model for B090's fixed positive-boundary obstruction."""

from fractions import Fraction

# In a symplectic four-space take delta_1=e_1, delta_2=e_2,
# delta_3=e_1+e_2.  For alpha, its three pairings have form (a,b,a+b).
# Fixed total monodromy requires a*delta_1+b*delta_2+(a+b)*delta_3=0.
for a_num in range(-10, 11):
    for b_num in range(-10, 11):
        a = Fraction(a_num)
        b = Fraction(b_num)
        c = (a, b, a + b)
        fixed = (c[0] + c[2] == 0 and c[1] + c[2] == 0)
        if fixed:
            assert c == (0, 0, 0)
        assert sum(x * x for x in c) == 0 if fixed else True

print("PASS: B090 positive local boundary has no nonzero fixed coefficient relation")
