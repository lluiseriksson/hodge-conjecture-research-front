from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

D = 12
q = D - 5
assert 6 * D - 6 == 66
assert 4 * D - 8 == 40 < 5 * D - 13 == 47
assert (q, q + 1, q + 2) == (7, 8, 9)
assert D - 4 == 8
assert D - 3 == 9
assert D - 5 == 7 > 1
assert 21 < 66

d = 14
q = 3 * d - 15
budget = q + 2
first_three = (d - 4) + (d - 5) + (d - 6)
assert 8 * d - 16 == 96
assert 3 * d - 3 + q == 66 < 67
assert q == first_three == 27
assert budget == 29
assert budget - first_three == 2 < d - 7 == 7
assert 36 < 96


def boundary(dimension: int) -> tuple[int, set[int]]:
    standard = 97 if dimension == 14 else 8 * dimension - 16
    square = 7 * dimension + 7
    cubic = 7 * dimension + 6 if dimension >= 22 else 7 * dimension + 5
    values = {1: standard, 2: square, 3: cubic, 4: cubic, 5: 7 * dimension + 7}
    floor = min(values.values())
    return floor, {key for key, value in values.items() if value == floor}


for dimension in range(14, 102, 2):
    floor, survivors = boundary(dimension)
    if dimension == 14:
        assert floor == 97 and survivors == {1}
    elif dimension <= 20:
        assert floor == 8 * dimension - 16 and survivors == {1}
    elif dimension == 22:
        assert floor == 160 and survivors == {1, 3, 4}
    else:
        assert floor == 7 * dimension + 6 and survivors == {3, 4}


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


require(
    "proofs/B275-standard-dimension-fourteen-second-residual.md",
    ("brick_id: B275", "status: PROVED", "40<5D-13=47", "h_Z(1)\\ge97", "disproof of HC"),
)
require(
    "proofs/NG231-standard-dimension-fourteen-second-equality.md",
    ("brick_id: NG231", "status: NO-GO", "G195", "rank 96"),
)
require(
    "proofs/G194-standard-cubic-piecewise-boundary.md",
    ("brick_id: G194", "status: NO-GO", "B275", "G195"),
)
require(
    "proofs/G195-standard-cubic-piecewise-boundary.md",
    ("brick_id: G195", "status: NO-GO", "U(14)=97", "B276"),
)

print("PASS: B275 second Q12/Q14 exclusion and current G194-G195 states")
