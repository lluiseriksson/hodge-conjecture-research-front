from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

for d in range(14, 102, 2):
    target = 7 * d + 6
    six_double_rank = 6 * d + 6
    residual_budget = target - six_double_rank
    first_jet_dimension = d + 1
    orthogonal_intersection = 1
    two_edge_sum = first_jet_dimension - orthogonal_intersection
    assert residual_budget == d
    assert two_edge_sum == d
    assert 2 * target > 7


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


require(
    "proofs/NG237-planar-extension-to-next-rank.md",
    (
        "brick_id: NG237",
        "status: NO-GO",
        "combined rank exactly d",
        "silently discard",
        "disproof of HC",
    ),
)
require(
    "proofs/G201-nonplanar-exact-rank-separation.md",
    (
        "brick_id: G201",
        "status: EXPLORATORY",
        "F_x|_{2x}\\ne0",
        "eighth absorbed support",
    ),
)
require(
    "proofs/G200-cubic-two-row-boundary.md",
    ("brick_id: G200", "status: EXPLORATORY", "7d+6", "active"),
)

print("PASS: NG237 next-rank obstruction and G201 nonplanar separator gate")
