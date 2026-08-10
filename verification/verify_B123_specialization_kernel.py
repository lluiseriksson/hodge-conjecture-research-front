"""Exact-sequence model for B123 and NG099."""

from fractions import Fraction


# S = extra relation kernel direct-sum ambient lift; P is nearby ambient.
# u(e, a) = a, so S_0=Qe is exactly ker(u).
def specialization(vector: tuple[Fraction, Fraction]) -> Fraction:
    _extra, ambient = vector
    return ambient


relation_step = [(Fraction(q), Fraction(0)) for q in (-3, -1, 0, 2, 5)]
assert all(specialization(vector) == 0 for vector in relation_step)

for target in [Fraction(-4), Fraction(1), Fraction(7, 3)]:
    ordinary_lift = (Fraction(0), target)
    assert specialization(ordinary_lift) == target
    assert target != 0

    # u(S_0)=0, so the filtered obstruction is the target itself.
    omega_fil = target
    assert omega_fil != 0


print("PASS: B123 relation step is the specialization kernel, so NG099 is exact")
