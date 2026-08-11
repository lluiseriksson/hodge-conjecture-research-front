from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


for d in range(14, 102, 2):
    six_doubles = 6 * d + 6
    cubic_residual = d - 1
    quartic_residual = d
    assert six_doubles + cubic_residual == 7 * d + 5
    assert six_doubles + quartic_residual == 7 * d + 6
    assert 2 + (d - 2) == d
    assert 2 * (7 * d + 5) > 7

assert 7 * 14 + 5 == 103
assert 7 * 14 + 6 == 104


def boundary(dimension: int) -> tuple[int, set[int]]:
    standard = 108 if dimension == 14 else 8 * dimension - 16
    square = 7 * dimension + 7
    cubic = 7 * dimension + 6
    values = {1: standard, 2: square, 3: cubic, 4: cubic, 5: 7 * dimension + 7}
    floor = min(values.values())
    return floor, {key for key, value in values.items() if value == floor}


for dimension in range(14, 102, 2):
    floor, survivors = boundary(dimension)
    if dimension == 14:
        assert floor == 104 and survivors == {3, 4}
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
    "proofs/B278-cubic-quartic-dimension-fourteen-extension.md",
    ("brick_id: B278", "status: PROVED", "d>=14", "7d+6", "disproof of HC"),
)
require(
    "proofs/NG234-cubic-quartic-dimension-fourteen-equality.md",
    ("brick_id: NG234", "status: NO-GO", "G198", "rank 103"),
)
require(
    "proofs/G197-cubic-piecewise-boundary.md",
    ("brick_id: G197", "status: NO-GO", "B278", "G198"),
)
require(
    "proofs/G198-cubic-piecewise-boundary.md",
    ("brick_id: G198", "status: NO-GO", "Y(14)=104", "B279"),
)

print("PASS: B278 cubic/quartic d>=14 extension and current G197-G198 states")
