from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


assert comb(7, 2) == 21

for d in range(14, 102, 2):
    q = d - 6
    target = 6 * d - 7
    assert target == 5 * d - 1 + q
    assert 3 * d - 3 + q == 4 * d - 9 < 5 * d - 13
    assert q < d - 4
    assert q + 1 < d - 4
    assert q + 2 == d - 4

    dim_j = d - 3
    final_budget = d - 4
    rank_outside_j = dim_j
    rank_inside_j = dim_j - 1
    dim_j_prime = dim_j - 1
    assert rank_outside_j > final_budget
    assert rank_inside_j == final_budget
    assert dim_j_prime == d - 4
    assert target > 21

    next_floor = 6 * d - 6
    delta = next_floor - (d + 1)
    slack = 2 * delta
    length = 2 * (d + 1) + slack
    assert delta == 5 * d - 7
    assert slack == 10 * d - 14
    assert length == 12 * d - 12 == 2 * next_floor
    assert (10 * d - 15) // 2 == 5 * d - 8

require(
    "proofs/B257-standard-first-slope-ten-equality-exclusion.md",
    (
        "brick_id: B257",
        "status: PROVED",
        "d-3,&x\\notin J",
        "\\dim J'=d-4",
        "h^0(\\mathbf P^5,O(2))=21<6d-7",
        "s\\ge10d-14",
        "proof, or disproof of HC",
    ),
)
require(
    "proofs/G183-standard-first-slope-ten-boundary.md",
    ("brick_id: G183", "status: NO-GO", "B257", "G184"),
)
require(
    "proofs/G184-standard-second-slope-ten-boundary.md",
    ("brick_id: G184", "status: NO-GO", "B258", "N=12d-12"),
)
require(
    "proofs/NG215-standard-first-slope-ten-equality-survival.md",
    ("brick_id: NG215", "status: NO-GO", "twenty-one", "G184"),
)

print("PASS: B257 first standard slope-ten equality, G183-G184 transition, and NG215")
