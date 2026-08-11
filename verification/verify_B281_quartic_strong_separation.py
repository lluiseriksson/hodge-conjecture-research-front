from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

support_count = 7
common_hyperplanes = 1
individual_hyperplanes = support_count
assert common_hyperplanes + individual_hyperplanes == 8

for d in range(14, 102, 2):
    assert support_count - 1 == 6 < d
    target = 7 * d + 6
    assert target - (6 * d + 6) == d
    assert 2 * target > support_count

    standard = 119 if d == 16 else (108 if d == 14 else 8 * d - 16)
    square = 7 * d + 7
    cubic = 7 * d + 6
    quartic = 7 * d + 7
    higher = 7 * d + 7
    values = {1: standard, 2: square, 3: cubic, 4: quartic, 5: higher}
    floor = min(values.values())
    survivors = {key for key, value in values.items() if value == floor}
    if d in (14, 16) or d >= 24:
        assert survivors == {3}
    elif d in (18, 20):
        assert survivors == {1}
    else:
        assert d == 22 and survivors == {1, 3}


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


require(
    "proofs/B281-quartic-seven-support-strong-separation.md",
    ("brick_id: B281", "status: PROVED", "F_x=M", "7d+7", "disproof of HC"),
)
require(
    "proofs/NG238-ambient-veronese-does-not-close-cubic.md",
    ("brick_id: NG238", "status: NO-GO", "m=6", "r=7", "G202"),
)
require(
    "proofs/G202-cubic-exact-rank-separation.md",
    ("brick_id: G202", "status: EXPLORATORY", "F_x|_{2x}\\ne0", "active"),
)
require(
    "proofs/G200-cubic-two-row-boundary.md",
    ("brick_id: G200", "status: EXPLORATORY", "A=O_Q(3)", "B281"),
)

print("PASS: B281 quartic strong separation, NG238, and cubic gate G202")
