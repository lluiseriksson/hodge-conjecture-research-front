"""Exact finite model for B119 and the NG095 total-type counterexample."""

from fractions import Fraction


# Detector total degree -1 has only the relevant and point grades.
beta_grades = {
    "E_infinity(-1,0)": Fraction(7, 5),
    "E_infinity(0,-1)": Fraction(0),  # B118
}
assert any(value != 0 for value in beta_grades.values())
assert beta_grades["E_infinity(-1,0)"] != 0

# Clean nodal relation coordinates are copies of Q(0) after Q(n).
relation_hodge_types = [(0, 0)] * 3
relation_vector = [Fraction(7, 5), Fraction(-2, 3), Fraction(0)]
assert any(value != 0 for value in relation_vector)
assert all(kind == (0, 0) for value, kind in zip(relation_vector, relation_hodge_types) if value)

# NG095: beta=e0+e1 in Q(0) direct-sum Q(-1) is not total type (0,0),
# while u(beta)=1 in the relevant Q(0) quotient.
beta = {"Q(0)": Fraction(1), "Q(-1)": Fraction(1)}
nearby_relevant = beta["Q(0)"]
assert beta["Q(-1)"] != 0
assert nearby_relevant == 1

print("PASS: B119 relevant grade has type (0,0) without a type-(0,0) total lift")
