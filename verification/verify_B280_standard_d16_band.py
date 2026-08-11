from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

d = 16
for r in range(6):
    target = 113 + r
    q = target - (5 * d - 1)
    budget = q + 2
    residual = 3 * d - 3 + q
    first_three = (d - 4) + (d - 5) + (d - 6)
    assert q == 34 + r
    assert residual == 79 + r < 108
    assert budget == 36 + r
    assert first_three == 33
    assert budget - first_three == 3 + r < d - 7 == 9
    assert 36 < target


def boundary(dimension: int) -> tuple[int, set[int]]:
    if dimension == 14:
        standard = 108
    elif dimension == 16:
        standard = 119
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
        assert floor == 118 and survivors == {3, 4}
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
    "proofs/B280-standard-dimension-sixteen-six-rank-band.md",
    ("brick_id: B280", "status: PROVED", "79+r", "h_Z(1)\\ge119", "disproof of HC"),
)
require(
    "proofs/NG236-standard-dimension-sixteen-six-rank-band.md",
    ("brick_id: NG236", "status: NO-GO", "G200", "113 through 118"),
)
require(
    "proofs/G199-cubic-piecewise-boundary.md",
    ("brick_id: G199", "status: NO-GO", "B280", "G200"),
)
require(
    "proofs/G200-cubic-two-row-boundary.md",
    ("brick_id: G200", "status: EXPLORATORY", "AA(16)=118", "active"),
)

print("PASS: B280 standard Q16 six-rank band, G199 no-go, and G200 boundary")
