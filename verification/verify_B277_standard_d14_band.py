from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


D = 12
for r in range(6):
    q = 2 * D - 11 + r
    target = 5 * D - 1 + q
    residual = 3 * D - 3 + q
    first_remaining = q + 2 - (D - 4)
    second_remaining = first_remaining - (D - 5)
    assert 72 <= target <= 77
    assert residual <= 51 < 53
    assert second_remaining == r <= 5 < D - 6 == 6

d = 14
for target in range(102, 108):
    q = target - (5 * d - 1)
    budget = q + 2
    residual = 3 * d - 3 + q
    first_four = (d - 4) + (d - 5) + (d - 6) + (d - 7)
    remaining = budget - first_four
    assert residual == target - 30
    assert 72 <= residual <= 77
    assert 1 <= remaining <= 6
    if target < 107:
        assert remaining < d - 8
    else:
        assert remaining == d - 8 == 6
        assert 55 < target


def boundary(dimension: int) -> tuple[int, set[int]]:
    standard = 108 if dimension == 14 else 8 * dimension - 16
    square = 7 * dimension + 7
    cubic = 7 * dimension + 6 if dimension >= 22 else 7 * dimension + 5
    values = {1: standard, 2: square, 3: cubic, 4: cubic, 5: 7 * dimension + 7}
    floor = min(values.values())
    return floor, {key for key, value in values.items() if value == floor}


for dimension in range(14, 102, 2):
    floor, survivors = boundary(dimension)
    if dimension == 14:
        assert floor == 103 and survivors == {3, 4}
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
    "proofs/B277-standard-dimension-fourteen-six-rank-band.md",
    ("brick_id: B277", "status: PROVED", "72<=h_Z(1)<=77", "h_Z(1)\\ge108", "disproof of HC"),
)
require(
    "proofs/NG233-standard-dimension-fourteen-six-rank-band.md",
    ("brick_id: NG233", "status: NO-GO", "G197", "102 through 107"),
)
require(
    "proofs/G196-standard-cubic-piecewise-boundary.md",
    ("brick_id: G196", "status: NO-GO", "B277", "G197"),
)
require(
    "proofs/G197-cubic-piecewise-boundary.md",
    ("brick_id: G197", "status: NO-GO", "W(14)=103", "B278"),
)

print("PASS: B277 Q12/Q14 six-rank band and current G196-G197 states")
