from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


for d in range(10, 102, 2):
    D = d - 2
    h = 5 * d - 1
    residual_budget = h - (2 * d + 2)
    assert residual_budget == 3 * D + 3
    assert 5 * D - 3 > residual_budget
    assert d - 4 > 2
    assert 8 * d - 4 == 2 * (4 * d - 2)
    assert 10 * d - 2 == 2 * h
    assert 8 * d - 2 == 2 * (4 * d - 1)
    assert 10 * d == 2 * (5 * d)

require(
    "proofs/B252-standard-two-beyond-slope-eight-exclusion.md",
    (
        "brick_id: B252",
        "status: PROVED",
        "5D-3=5d-13>3d-3",
        "d-4>2",
        "s=8d-2",
        "proof, or disproof of HC",
    ),
)
require(
    "proofs/G175-two-beyond-slope-eight.md",
    ("brick_id: G175", "status: NO-GO", "B252", "NG210", "G176"),
)
require(
    "proofs/G176-three-beyond-slope-eight.md",
    ("brick_id: G176", "status: EXPLORATORY", "N=10d", "h_Z(1)=5d"),
)
require(
    "proofs/NG210-standard-two-beyond-slope-eight-survival.md",
    ("brick_id: NG210", "status: NO-GO", "d-4>2", "G176"),
)

print("PASS: B252 two-beyond exclusion, G175-G176, and NG210")
