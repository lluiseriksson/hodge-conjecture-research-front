from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


assert comb(7, 4) == 35
assert comb(8, 4) == 70

for d in range(14, 102, 2):
    old_square_floor = 5 * d + 3
    square_floor = 6 * d + 6
    standard_floor = 6 * d - 7
    higher_floor = 5 * d + 5
    assert old_square_floor > 70
    assert square_floor == 6 * (d + 1)
    assert min(standard_floor, square_floor, higher_floor) == higher_floor
    assert standard_floor > higher_floor
    assert higher_floor - (d + 1) == 4 * d + 4
    assert 2 * (4 * d + 4) == 8 * d + 8
    assert 2 * higher_floor == 10 * d + 10

    signatures = (
        (8 * d + 4, 4 * d + 2, 10 * d + 6, 5 * d + 3),
        (8 * d + 6, 4 * d + 3, 10 * d + 8, 5 * d + 4),
        (8 * d + 8, 4 * d + 4, 10 * d + 10, 5 * d + 5),
    )
    for slack, delta, length, rank in signatures:
        assert delta == slack // 2
        assert rank == d + 1 + delta
        assert length == 2 * (d + 1) + slack == 2 * rank
        assert (slack + 1) // 2 == delta

require(
    "proofs/B254-square-six-double-floor.md",
    (
        "brick_id: B254",
        "status: PROVED",
        "\\binom74=35",
        "\\binom84=70",
        "h_Z(1)\\ge6(d+1)=6d+6",
        "s\\ge8d+8",
        "proof, or disproof of HC",
    ),
)
require(
    "proofs/G179-square-five-double-boundary.md",
    ("brick_id: G179", "status: NO-GO", "B254", "G181"),
)
require(
    "proofs/G180-one-beyond-square-boundary.md",
    ("brick_id: G180", "status: NO-GO", "h_Z(1)=5d+4"),
)
require(
    "proofs/G181-higher-power-five-double-boundary.md",
    ("brick_id: G181", "status: EXPLORATORY", "k\\ge3", "N=10d+10"),
)
require(
    "proofs/NG212-square-boundary-survival.md",
    ("brick_id: NG212", "status: NO-GO", "h_Z(1)\\ge6d+6", "G181"),
)

print("PASS: B254 square six-double floor, G179-G181, and NG212")
