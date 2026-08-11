from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


# B259 specialized to all five Q^12 ranks.
D = 12
for r in range(5):
    q = D - 4 + r
    target = 5 * D - 1 + q
    residual = 3 * D - 3 + q
    remaining = (q + 2) - (D - 4)
    assert 67 <= target <= 71
    assert residual <= 45 < 47
    assert remaining == r + 2 <= 6 < D - 5 == 7

# Lift the excluded residual band to Q^14 and test the fourth escape.
d = 14
for target in range(97, 102):
    q = target - (5 * d - 1)
    budget = q + 2
    residual = 3 * d - 3 + q
    first_three = (d - 4) + (d - 5) + (d - 6)
    remaining = budget - first_three
    assert residual == target - 30
    assert 67 <= residual <= 71
    assert 3 <= remaining <= 7
    if target < 101:
        assert remaining < d - 7
    else:
        assert remaining == d - 7 == 7
        assert 45 < target


def boundary(dimension: int) -> tuple[int, set[int]]:
    standard = 102 if dimension == 14 else 8 * dimension - 16
    square = 7 * dimension + 7
    cubic = 7 * dimension + 6 if dimension >= 22 else 7 * dimension + 5
    values = {1: standard, 2: square, 3: cubic, 4: cubic, 5: 7 * dimension + 7}
    floor = min(values.values())
    return floor, {key for key, value in values.items() if value == floor}


for dimension in range(14, 102, 2):
    floor, survivors = boundary(dimension)
    if dimension == 14:
        assert floor == 102 and survivors == {1}
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
    "proofs/B276-standard-dimension-fourteen-five-rank-band.md",
    ("brick_id: B276", "status: PROVED", "67<=h_Z(1)<=71", "h_Z(1)\\ge102", "disproof of HC"),
)
require(
    "proofs/NG232-standard-dimension-fourteen-five-rank-band.md",
    ("brick_id: NG232", "status: NO-GO", "G196", "97 through 101"),
)
require(
    "proofs/G195-standard-cubic-piecewise-boundary.md",
    ("brick_id: G195", "status: NO-GO", "B276", "G196"),
)
require(
    "proofs/G196-standard-cubic-piecewise-boundary.md",
    ("brick_id: G196", "status: NO-GO", "V(14)=102", "B277"),
)

print("PASS: B276 Q12/Q14 five-rank band and current G195-G196 states")
