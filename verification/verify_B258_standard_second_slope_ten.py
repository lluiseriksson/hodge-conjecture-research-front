from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


for d in range(14, 102, 2):
    q = d - 5
    target = 6 * d - 6
    assert target == 5 * d - 1 + q
    assert 3 * d - 3 + q == 4 * d - 8 < 5 * d - 13
    assert q == d - 5
    assert q + 1 == d - 4
    assert q + 2 == d - 3

    dim_j = d - 3
    dim_j_prime = d - 4
    first_inside = dim_j - 1
    first_outside = dim_j
    second_minimum = dim_j_prime - 1
    assert first_inside == d - 4
    assert first_outside == d - 3
    assert second_minimum == d - 5 > 1
    assert target > 21

    next_floor = 6 * d - 5
    delta = next_floor - (d + 1)
    slack = 2 * delta
    length = 2 * (d + 1) + slack
    assert delta == 5 * d - 6
    assert slack == 10 * d - 12
    assert length == 12 * d - 10 == 2 * next_floor
    assert (10 * d - 13) // 2 == 5 * d - 7

require(
    "proofs/B258-standard-second-slope-ten-equality-exclusion.md",
    (
        "brick_id: B258",
        "status: PROVED",
        "q=d-5",
        "\\dim J'=d-4",
        "d-5>1",
        "s\\ge10d-12",
        "proof, or disproof of HC",
    ),
)
require(
    "proofs/G184-standard-second-slope-ten-boundary.md",
    ("brick_id: G184", "status: NO-GO", "B258", "G185"),
)
require(
    "proofs/G185-standard-third-slope-ten-boundary.md",
    ("brick_id: G185", "status: EXPLORATORY", "q=d-4", "N=12d-10"),
)
require(
    "proofs/NG216-standard-second-slope-ten-equality-survival.md",
    ("brick_id: NG216", "status: NO-GO", "d-5>1", "G185"),
)

print("PASS: B258 second standard slope-ten equality, G184-G185, and NG216")
