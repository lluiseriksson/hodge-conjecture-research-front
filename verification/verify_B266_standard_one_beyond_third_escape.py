from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


for d in range(16, 102, 2):
    q = 3 * d - 16
    target = 5 * d - 1 + q
    residual = 3 * d - 3 + q
    budget = q + 2
    first_three = (d - 4) + (d - 5) + (d - 6)
    remaining = budget - first_three
    fourth = d - 7

    assert target == 8 * d - 17
    assert residual == 6 * d - 19 < 7 * d - 26
    assert budget == 3 * d - 14
    assert first_three == 3 * d - 15
    assert remaining == 1 < fourth
    assert 36 < target

for d in range(14, 102, 2):
    standard = 8 * d - 16 if d >= 16 else 8 * d - 17
    square = 7 * d + 7 if d >= 22 else 6 * d + 6
    cubic = 7 * d + 6
    quartic = 7 * d + 6
    higher = 7 * d + 7
    values = {1: standard, 2: square, 3: cubic, 4: quartic, 5: higher}
    floor = min(values.values())

    if d in (14, 16, 18, 20):
        expected = 6 * d + 6
        survivors = {2}
    elif d == 22:
        expected = 7 * d + 6
        survivors = {1, 3, 4}
    else:
        expected = 7 * d + 6
        survivors = {3, 4}

    assert floor == expected
    assert {key for key, value in values.items() if value == floor} == survivors


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


require(
    "proofs/B266-standard-one-beyond-third-escape.md",
    (
        "brick_id: B266",
        "status: PROVED",
        "(3d-14)-(3d-15)=1",
        "d-7>1",
        "h_Z(1)\\ge8d-16",
        "keeps G190 open",
        "proof, or disproof of HC",
    ),
)
require(
    "proofs/G191-square-standard-cubic-boundary.md",
    ("brick_id: G191", "status: NO-GO", "B271-B272", "B266"),
)
require(
    "proofs/G192-square-cubic-boundary.md",
    ("brick_id: G192", "status: EXPLORATORY", "P(d)", "active"),
)
require(
    "proofs/NG224-standard-one-beyond-third-escape-survival.md",
    ("brick_id: NG224", "status: NO-GO", "d-7>1", "G190"),
)

print("PASS: B266 standard exclusion, G191 no-go, G192 transition, and NG224")
