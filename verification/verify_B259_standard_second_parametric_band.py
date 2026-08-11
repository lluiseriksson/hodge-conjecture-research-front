from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


for d in range(14, 102, 2):
    for r in range(0, d - 7):
        q = d - 4 + r
        target = 5 * d - 1 + q
        assert d - 4 <= q <= 2 * d - 12
        assert 6 * d - 5 <= target <= 7 * d - 13

        residual = 3 * d - 3 + q
        max_budget = q + 2
        first_minimum = d - 4
        remaining = max_budget - first_minimum
        second_minimum = d - 5
        assert residual <= 5 * d - 15 < 5 * d - 13
        assert max_budget == d - 2 + r
        assert remaining == r + 2 <= d - 6 < second_minimum

    standard_floor = 7 * d - 12
    nonstandard_floor = 6 * d + 6
    common_floor = min(standard_floor, nonstandard_floor)
    delta = common_floor - (d + 1)
    slack = 2 * delta
    length = 2 * (d + 1) + slack
    assert slack == min(12 * d - 26, 10 * d + 10)
    assert length == 2 * common_floor

    if d in (14, 16):
        assert standard_floor < nonstandard_floor
    elif d == 18:
        assert standard_floor == nonstandard_floor == 114
        assert slack == 190
    else:
        assert standard_floor > nonstandard_floor

require(
    "proofs/B259-standard-second-parametric-band-exclusion.md",
    (
        "brick_id: B259",
        "status: PROVED",
        "0\\le r\\le d-8",
        "r+2\\le d-6<d-5",
        "h_Z(1)\\ge7d-12",
        "s\\ge\\min\\{12d-26,10d+10\\}",
        "proof, or disproof of HC",
    ),
)
require(
    "proofs/G185-standard-third-slope-ten-boundary.md",
    ("brick_id: G185", "status: NO-GO", "B259", "G186"),
)
require(
    "proofs/G186-piecewise-post-standard-band-boundary.md",
    ("brick_id: G186", "status: NO-GO", "B260", "N=2F(d)"),
)
require(
    "proofs/NG217-standard-second-parametric-band-survival.md",
    ("brick_id: NG217", "status: NO-GO", "7d-13", "G186"),
)

print("PASS: B259 second standard parametric band, G185-G186 transition, and NG217")
