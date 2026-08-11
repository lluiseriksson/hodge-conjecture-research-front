from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


for d in range(10, 102, 2):
    D = d - 2
    for q in range(0, d - 6):
        h = 5 * d - 1 + q
        residual = h - (2 * d + 2)
        assert residual == 3 * d - 3 + q
        assert residual <= 4 * d - 10
        assert residual < 5 * D - 3
        assert q + 2 <= d - 5 < d - 4

    standard_floor = 6 * d - 7
    square_floor = 5 * d + 3
    higher_floor = 5 * d + 5
    assert min(standard_floor, square_floor, higher_floor) == square_floor
    assert square_floor - (d + 1) == 4 * d + 2
    assert 2 * (4 * d + 2) == 8 * d + 4
    assert 2 * square_floor == 10 * d + 6

    signatures = (
        (8 * d - 2, 4 * d - 1, 10 * d, 5 * d),
        (8 * d, 4 * d, 10 * d + 2, 5 * d + 1),
        (8 * d + 2, 4 * d + 1, 10 * d + 4, 5 * d + 2),
        (8 * d + 4, 4 * d + 2, 10 * d + 6, 5 * d + 3),
    )
    for slack, delta, length, rank in signatures:
        assert delta == slack // 2
        assert rank == d + 1 + delta
        assert length == 2 * (d + 1) + slack == 2 * rank
        assert (slack + 1) // 2 == delta

    if d >= 12:
        assert standard_floor > square_floor

require(
    "proofs/B253-standard-parametric-band-exclusion.md",
    (
        "brick_id: B253",
        "status: PROVED",
        "0\\le q\\le d-7",
        "q+2\\le d-5<d-4",
        "h_Z(1)\\ge6d-7",
        "s\\ge8d+4",
        "proof, or disproof of HC",
    ),
)
require(
    "proofs/G176-three-beyond-slope-eight.md",
    ("brick_id: G176", "status: NO-GO", "B253", "G179"),
)
require(
    "proofs/G177-four-beyond-slope-eight.md",
    ("brick_id: G177", "status: NO-GO", "h_Z(1)=5d+1"),
)
require(
    "proofs/G178-five-beyond-slope-eight.md",
    ("brick_id: G178", "status: NO-GO", "h_Z(1)=5d+2"),
)
require(
    "proofs/G179-square-five-double-boundary.md",
    ("brick_id: G179", "status: NO-GO", "B254", "G181", "N=10d+6"),
)
require(
    "proofs/NG211-standard-parametric-band-survival.md",
    ("brick_id: NG211", "status: NO-GO", "q+2\\le d-5<d-4", "G179"),
)

print("PASS: B253 parametric band, G176-G179, and NG211")
