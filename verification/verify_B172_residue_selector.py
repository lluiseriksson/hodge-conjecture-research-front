#!/usr/bin/env python3
"""Exact B172/NG136 residue arithmetic; not a proof of HC."""

from fractions import Fraction


# f_t=(z^2-1)^2+t has critical points -1,0,1 with Hessians 8,-4,8.
hessians = (8, -4, 8)

# The admissible constant numerator satisfies Jacobi's vanishing identity.
assert sum(Fraction(1, h) for h in hessians) == 0

for t in range(-12, 13):
    values = (t, 1 + t, t)

    # The tracked relation lifts exactly.
    assert values[0] - values[2] == 0

    # Q=f_t is outside the degree bound and leaves a residue at infinity.
    total = sum(Fraction(value, h) for value, h in zip(values, hessians))
    assert total == Fraction(-1, 4)

# In one variable deg(P)=3, so Jacobi permits deg(Q)<=1, whereas deg(fA)>=4
# for every nonzero polynomial A.
jacobi_degree_bound = 3 - 1 - 1
assert jacobi_degree_bound == 1
assert 4 > jacobi_degree_bound

print("PASS: B172 selector criterion and NG136 degree/infinity obstruction")
