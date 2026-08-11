from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


for d in range(14, 102, 2):
    for r in range(0, d - 6):
        q = 2 * d - 11 + r
        target = 5 * d - 1 + q
        assert 2 * d - 11 <= q <= 3 * d - 18
        assert 7 * d - 12 <= target <= 8 * d - 19

        residual = 3 * d - 3 + q
        first_remaining = q + 2 - (d - 4)
        second_remaining = first_remaining - (d - 5)
        third_minimum = d - 6
        assert residual <= 6 * d - 21
        if d == 14:
            assert residual < 6 * d - 19
        else:
            assert residual < 7 * d - 26
        assert first_remaining == d - 5 + r
        assert second_remaining == r <= d - 7 < third_minimum

    standard = 8 * d - 18
    square = 7 * d + 7 if d >= 22 else 6 * d + 6
    cubic = 7 * d + 5
    quartic = 7 * d + 5
    higher = 7 * d + 7
    floor = min(standard, square, cubic, quartic, higher)

    if d in (14, 16, 18, 20):
        expected = 6 * d + 6
        survivors = {2}
    elif d == 22:
        expected = 158
        survivors = {1}
    else:
        expected = 7 * d + 5
        survivors = {3, 4}

    assert floor == expected
    values = {1: standard, 2: square, 3: cubic, 4: quartic, 5: higher}
    assert {key for key, value in values.items() if value == floor} == survivors

    delta = floor - (d + 1)
    slack = 2 * delta
    length = 2 * (d + 1) + slack
    assert length == 2 * floor

require(
    "proofs/B262-standard-third-parametric-band-exclusion.md",
    (
        "brick_id: B262",
        "status: PROVED",
        "0\\le r\\le d-7",
        "r\\le d-7<d-6",
        "h_Z(1)\\ge8d-18",
        "proof, or disproof of HC",
    ),
)
require(
    "proofs/G188-mostly-standard-seventh-jet-boundary.md",
    ("brick_id: G188", "status: NO-GO", "B262", "G189"),
)
require(
    "proofs/G189-square-standard-cubic-piecewise-boundary.md",
    ("brick_id: G189", "status: EXPLORATORY", "L(d)", "A=O_Q(3),O_Q(4)"),
)
require(
    "proofs/NG220-standard-third-parametric-band-survival.md",
    ("brick_id: NG220", "status: NO-GO", "8d-19", "G189"),
)

print("PASS: B262 third standard parametric band, G188-G189, and NG220")
