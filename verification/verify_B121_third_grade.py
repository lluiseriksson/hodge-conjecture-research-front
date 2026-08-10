"""Shift and countermodel checks for B121, B122, NG097, and NG098."""

from fractions import Fraction


for n in range(1, 31):
    d = 2 * n - 1
    total_shift = d + 2

    positions = {
        "ambient": (-2, 1, d + 1),
        "relation": (-1, 0, d),
        "point": (0, -1, d - 1),
    }
    for stalk_degree, perverse_degree, generic_q in positions.values():
        assert stalk_degree + perverse_degree == -1
        assert generic_q == d + perverse_degree

    # The ambient position is raw H^(d+1) in normalized total degree -1.
    assert (d + 1) - total_shift == -1


# NG097: a nonzero pure type-(0,0) lift may be entirely ambient.
beta = {"E(-2,1)": Fraction(1), "E(-1,0)": Fraction(0), "E(0,-1)": Fraction(0)}
assert any(beta.values())
assert beta["E(-1,0)"] == 0


# NG098: raw monodromy defect is nonzero while quotient monodromy is trivial.
def raw_monodromy(vector: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    e, j = vector
    return e, j + e


raw = (Fraction(1), Fraction(0))
assert raw_monodromy(raw) != raw
assert raw_monodromy(raw)[0] == raw[0]  # quotient coordinate is fixed


print("PASS: B121 third grade and B122 target-vs-raw distinction are exact")
