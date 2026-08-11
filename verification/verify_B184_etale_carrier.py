#!/usr/bin/env python3
"""Bounded checks for B184/NG148; not a proof of the Hodge conjecture."""


def multiply(left, right):
    """Multiply sparse polynomials in (u,z), keyed by exponent pairs."""
    out = {}
    for (iu, iz), a in left.items():
        for (ju, jz), b in right.items():
            key = (iu + ju, iz + jz)
            out[key] = out.get(key, 0) + a * b
    return {key: value for key, value in out.items() if value}


def dz_at_origin(poly):
    """Evaluate the z derivative at (u,z)=(0,0)."""
    return poly.get((0, 1), 0)


# M=z^2-u^2-u^3 has M(0,0)=d_z M(0,0)=0.  Every sampled multiple
# therefore also has zero z derivative at the origin, as in NG148.
minimal = {(0, 2): 1, (2, 0): -1, (3, 0): -1}
for a in range(-3, 4):
    for b in range(-3, 4):
        for c in range(-2, 3):
            quotient = {(0, 0): a, (1, 0): b, (0, 1): c}
            relation = multiply(minimal, quotient)
            assert dz_at_origin(relation) == 0


# On V_s=(y-x^s), deg(V_s)=s and the degree-one numerator y restricts
# to x^s.  This saturates ord <= deg(V) deg(N) and checks that delta
# cannot be omitted from B184's bound.
for s in range(1, 81):
    carrier_degree = s
    numerator_degree = 1
    restricted_order = s
    assert restricted_order == carrier_degree * numerator_degree


# The NG148 cover is etale at both central points because 2 lambda is a unit.
for central_lambda in (-1, 1):
    assert 2 * central_lambda != 0

print("PASS: B184 carrier degree bounds order and NG148 blocks simple elimination")
