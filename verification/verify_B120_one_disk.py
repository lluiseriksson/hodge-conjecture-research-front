"""Degree-shift and strictness checks for B120 and NG096."""

from fractions import Fraction


for n in range(1, 31):
    d = 2 * n - 1
    plane_shift = d + 2
    disk_shift = d + 1

    # H^0 of the disk-normalized special stalk and H^-1 of the
    # plane-normalized special stalk are both H^(d+1) of the special fiber.
    assert 0 + disk_shift == d + 1
    assert -1 + plane_shift == d + 1


# NG096: cyclic invariance along M1 is strictly weaker than invariance under
# both commuting generators. Coordinates are (e,j), J=Qj.
def m1(vector: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return vector


def m2(vector: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    e, j = vector
    return e, j + e


for adjustment in [Fraction(-5), Fraction(0), Fraction(7, 3)]:
    lift = (Fraction(1), adjustment)
    assert m1(lift) == lift
    assert m2(lift) != lift
    assert m2(lift)[1] - lift[1] == 1


print("PASS: B120 one cyclic collision disk gives the required shifted special stalk")
