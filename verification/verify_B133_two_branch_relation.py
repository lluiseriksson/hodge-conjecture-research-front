"""Exact rank checks for the B133 two-branch relation criterion."""

from fractions import Fraction


def rank_2xn(columns):
    """Rational rank of a list of two-coordinate columns."""

    nonzero = [v for v in columns if v != (0, 0)]
    if not nonzero:
        return 0
    first = nonzero[0]
    for second in nonzero[1:]:
        determinant = first[0] * second[1] - first[1] * second[0]
        if determinant != 0:
            return 2
    return 1


examples = {
    "independent": [(Fraction(1), Fraction(0)), (Fraction(0), Fraction(1))],
    "equal": [(Fraction(1), Fraction(0)), (Fraction(1), Fraction(0))],
    "proportional": [(Fraction(2), Fraction(3)), (Fraction(-4), Fraction(-6))],
}

assert 2 - rank_2xn(examples["independent"]) == 0
assert 2 - rank_2xn(examples["equal"]) == 1
assert 2 - rank_2xn(examples["proportional"]) == 1

# If delta_2=c delta_1, the coefficient vector (c,-1) is a relation.
c = Fraction(-2)
delta_1 = (Fraction(2), Fraction(3))
delta_2 = tuple(c * coordinate for coordinate in delta_1)
relation_value = tuple(
    c * delta_1[i] - delta_2[i] for i in range(2)
)
assert relation_value == (0, 0)

print("PASS: B133 two-branch relation ranks and NG106 independence guard")
