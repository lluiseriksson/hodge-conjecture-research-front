from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


for d in range(14, 102, 2):
    q = 3 * d - 17
    target = 5 * d - 1 + q
    residual = 3 * d - 3 + q
    budget = q + 2
    ranks = (d - 4, d - 5, d - 6)

    assert target == 8 * d - 18
    assert residual == 6 * d - 20
    if d == 14:
        assert residual < 6 * d - 19
    else:
        assert residual < 7 * d - 26
    assert sum(ranks) == budget == 3 * d - 15
    assert 36 < target

    standard = 8 * d - 17
    square = 7 * d + 7 if d >= 22 else 6 * d + 6
    cubic = 7 * d + 5
    quartic = 7 * d + 5
    higher = 7 * d + 7
    values = {1: standard, 2: square, 3: cubic, 4: quartic, 5: higher}
    floor = min(values.values())

    if d in (14, 16, 18, 20):
        expected = 6 * d + 6
        survivors = {2}
    elif d == 22:
        expected = 7 * d + 5
        survivors = {1, 3, 4}
    else:
        expected = 7 * d + 5
        survivors = {3, 4}

    assert floor == expected
    assert {key for key, value in values.items() if value == floor} == survivors
    delta = floor - (d + 1)
    slack = 2 * delta
    assert 2 * (d + 1) + slack == 2 * floor

require(
    "proofs/B263-standard-third-escape-equality.md",
    (
        "brick_id: B263",
        "status: PROVED",
        "(d-4)+(d-5)+(d-6)=3d-15",
        "h^0(\\mathbf P^7,O(2))=36",
        "proof, or disproof of HC",
    ),
)
require(
    "proofs/G189-square-standard-cubic-piecewise-boundary.md",
    ("brick_id: G189", "status: NO-GO", "B263", "G190"),
)
require(
    "proofs/G190-square-cubic-piecewise-boundary.md",
    ("brick_id: G190", "status: NO-GO", "K(d)", "B272"),
)
require(
    "proofs/NG221-standard-third-escape-equality-survival.md",
    ("brick_id: NG221", "status: NO-GO", "P^7", "G190"),
)

print("PASS: B263 third-escape equality, G189-G190 state, and NG221")
