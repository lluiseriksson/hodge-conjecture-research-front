from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


# B257 specialized to the Q^12 rank-65 equality.
D = 12
q = D - 6
target_12 = 6 * D - 7
residual_10 = 4 * D - 9
floor_10 = 5 * D - 13
escape = D - 4
assert q == 6
assert target_12 == 65
assert residual_10 == 39 < floor_10 == 47
assert q < escape and q + 1 < escape
assert target_12 - (5 * D - 3) == escape == 8
assert 21 < target_12

# B266 specialized to Q^14 after the Q^12 floor is raised.
d = 14
target_14 = 8 * d - 17
residual_12 = 6 * d - 19
budget = 3 * d - 14
first_three = (d - 4) + (d - 5) + (d - 6)
fourth = d - 7
assert target_14 == 95
assert residual_12 == 65 < 66
assert budget == 28
assert first_three == 27
assert budget - first_three == 1 < fourth == 7
assert 36 < target_14


def boundary(dimension: int) -> tuple[int, set[int]]:
    standard = 8 * dimension - 16
    square = 7 * dimension + 7
    cubic = 7 * dimension + 6 if dimension >= 22 else 7 * dimension + 5
    quartic = cubic
    higher = 7 * dimension + 7
    values = {1: standard, 2: square, 3: cubic, 4: quartic, 5: higher}
    floor = min(values.values())
    return floor, {key for key, value in values.items() if value == floor}


for dimension in range(14, 102, 2):
    floor, survivors = boundary(dimension)
    if dimension <= 20:
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
    "proofs/B274-standard-dimension-fourteen-residual.md",
    ("brick_id: B274", "status: PROVED", "39<5D-13=47", "h_Z(1)\\ge96", "disproof of HC"),
)
require(
    "proofs/NG230-standard-dimension-fourteen-equality.md",
    ("brick_id: NG230", "status: NO-GO", "G194", "rank 95"),
)
require(
    "proofs/G193-standard-cubic-piecewise-boundary.md",
    ("brick_id: G193", "status: NO-GO", "B274", "G194"),
)
require(
    "proofs/G194-standard-cubic-piecewise-boundary.md",
    ("brick_id: G194", "status: EXPLORATORY", "T(d)=8d-16", "active"),
)

print("PASS: B274 Q12/Q14 standard exclusion, G193 no-go, and G194 boundary")
