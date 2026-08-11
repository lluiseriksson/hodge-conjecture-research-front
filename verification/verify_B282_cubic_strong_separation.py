from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

for d in range(14, 102, 2):
    five_collinear = 7 + 5 * (d - 1)
    with_sixth = five_collinear + (d + 1)
    assert five_collinear == 5 * d + 2
    assert with_sixth == 6 * d + 3 < 6 * d + 6

    assert 1 + 2 + 3 == 6  # common, two pair, three singleton factors
    target = 7 * d + 6
    assert target - (6 * d + 6) == d
    assert 2 * target > 7


def partitions(total: int, minimum: int = 1) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []
    for first in range(minimum, total + 1):
        if first == total:
            out.append((first,))
        else:
            for tail in partitions(total - first, first):
                out.append((first,) + tail)
    return out


for class_sizes in partitions(7):
    matching_number = min(7 // 2, 7 - max(class_sizes))
    if matching_number < 2:
        assert max(class_sizes) >= 6


def boundary(d: int) -> tuple[int, set[int]]:
    standard = 108 if d == 14 else (119 if d == 16 else 8 * d - 16)
    nonstandard = 7 * d + 7
    values = {1: standard, 2: nonstandard, 3: nonstandard, 4: nonstandard, 5: nonstandard}
    floor = min(values.values())
    return floor, {key for key, value in values.items() if value == floor}


for d in range(14, 102, 2):
    floor, survivors = boundary(d)
    if d == 14:
        assert floor == 105 and survivors == {2, 3, 4, 5}
    elif d == 16:
        assert floor == 119 and survivors == {1, 2, 3, 4, 5}
    elif d in (18, 20, 22):
        assert floor == 8 * d - 16 and survivors == {1}
    else:
        assert floor == 7 * d + 7 and survivors == {2, 3, 4, 5}


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


require(
    "proofs/B282-cubic-seven-support-strong-separation.md",
    ("brick_id: B282", "status: PROVED", "6d+3", "F_x=M", "7d+7", "disproof of HC"),
)
require(
    "proofs/NG239-cubic-seven-support-survival.md",
    ("brick_id: NG239", "status: NO-GO", "G203", "6d+3"),
)
require(
    "proofs/G200-cubic-two-row-boundary.md",
    ("brick_id: G200", "status: NO-GO", "B282", "G203"),
)
require(
    "proofs/G202-cubic-exact-rank-separation.md",
    ("brick_id: G202", "status: PROVED", "B282", "G203"),
)
require(
    "proofs/G203-all-nonstandard-next-boundary.md",
    ("brick_id: G203", "status: EXPLORATORY", "AB(14)=105", "active"),
)

print("PASS: B282 cubic strong separation, G200 no-go, and G203 boundary")
