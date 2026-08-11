"""Finite exact model for B124 and NG100."""

from fractions import Fraction


# L_beta is an affine line gamma_0 + A.  Primitive realization kills A.
gamma_0 = (Fraction(1), Fraction(1))
ambiguities = [(Fraction(0), Fraction(a)) for a in (-5, -1, 0, 2, 9)]


def add(left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]):
    return (left[0] + right[0], left[1] + right[1])


def primitive_realization(relative_lift: tuple[Fraction, Fraction]):
    first, _nearby_ambiguity = relative_lift
    return (first, first)


values = {primitive_realization(add(gamma_0, ambiguity)) for ambiguity in ambiguities}
assert values == {(Fraction(1), Fraction(1))}

# The fixed relation detects zeta(x,y)=x, but cannot be tuned to c=(1,0).
phi_beta = values.pop()
c = (Fraction(1), Fraction(0))
assert phi_beta[0] != 0
assert phi_beta != c
assert all(primitive_realization(add(gamma_0, ambiguity)) != c for ambiguity in ambiguities)

print("PASS: B124 relative-lift ambiguity cannot tune the primitive target")
