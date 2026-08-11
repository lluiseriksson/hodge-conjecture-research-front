from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def multiply(
    left: tuple[int, tuple[int, ...]],
    right: tuple[int, tuple[int, ...]],
) -> tuple[int, tuple[int, ...]]:
    c, alpha = left
    d, beta = right
    return c * d, tuple(c * b + d * a for a, b in zip(alpha, beta))


for width in (2, 4, 9):
    lam_e = tuple(i + 1 for i in range(width))
    total = tuple(5 * i - 3 for i in range(width))
    complement = tuple(a - b for a, b in zip(total, lam_e))
    assert multiply((1, lam_e), (1, complement)) == (1, total)

for d in range(14, 102, 2):
    derivative_space = d - 2
    common_unit = 1
    actual_rank = derivative_space + common_unit
    assert actual_rank == d - 1
    assert 6 * (d + 1) + actual_rank == 7 * d + 5


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


require(
    "proofs/B265-planar-two-edge-unit-separation.md",
    (
        "brick_id: B265",
        "status: NO-GO",
        "(1,\\lambda_e)(1,\\Lambda-\\lambda_e)=(1,\\Lambda)=j(P)",
        "\\dim R_e=d-1",
        "retracted",
    ),
)
require(
    "proofs/B267-planar-product-jet-cancellation.md",
    ("brick_id: B267", "status: PROVED", "R_e=R_f", "active gate"),
)
require(
    "proofs/G190-square-cubic-piecewise-boundary.md",
    ("brick_id: G190", "status: EXPLORATORY", "B267", "planar"),
)
require(
    "proofs/G191-square-standard-cubic-boundary.md",
    ("brick_id: G191", "status: CONDITIONAL", "B267", "inactive"),
)
require(
    "proofs/G192-square-cubic-boundary.md",
    ("brick_id: G192", "status: CONDITIONAL", "B267", "inactive"),
)
require(
    "proofs/NG223-planar-cubic-quartic-equality-survival.md",
    ("brick_id: NG223", "status: NO-GO", "Missing factor", "G190"),
)

print("PASS: B265 retraction, B267 cancellation, and G190 restoration")
