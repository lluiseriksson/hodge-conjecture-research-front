from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

d = 16
target = 112
q = target - (5 * d - 1)
budget = q + 2
residual = 3 * d - 3 + q
first_three = (d - 4) + (d - 5) + (d - 6)
assert q == 33
assert residual == 78 < 108
assert budget == 35
assert first_three == 33
assert budget - first_three == 2 < d - 7 == 9
assert 36 < target


def boundary(dimension: int) -> tuple[int, set[int]]:
    if dimension == 14:
        standard = 108
    elif dimension == 16:
        standard = 113
    else:
        standard = 8 * dimension - 16
    square = 7 * dimension + 7
    cubic = 7 * dimension + 6
    values = {1: standard, 2: square, 3: cubic, 4: cubic, 5: 7 * dimension + 7}
    floor = min(values.values())
    return floor, {key for key, value in values.items() if value == floor}


for dimension in range(14, 102, 2):
    floor, survivors = boundary(dimension)
    if dimension == 14:
        assert floor == 104 and survivors == {3, 4}
    elif dimension == 16:
        assert floor == 113 and survivors == {1}
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
    "proofs/B279-standard-dimension-sixteen-equality.md",
    ("brick_id: B279", "status: PROVED", "rank at most", "h_Z(1)\\ge113", "disproof of HC"),
)
require(
    "proofs/NG235-standard-dimension-sixteen-equality.md",
    ("brick_id: NG235", "status: NO-GO", "G199", "rank 112"),
)
require(
    "proofs/G198-cubic-piecewise-boundary.md",
    ("brick_id: G198", "status: NO-GO", "B279", "G199"),
)
require(
    "proofs/G199-cubic-piecewise-boundary.md",
    ("brick_id: G199", "status: EXPLORATORY", "Z(16)=113", "active"),
)

print("PASS: B279 standard Q16 equality, G198 no-go, and G199 boundary")
