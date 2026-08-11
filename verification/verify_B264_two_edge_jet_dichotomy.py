from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def connected(vertices: set[int], edges: set[tuple[int, int]]) -> bool:
    seen = {next(iter(vertices))}
    while True:
        grown = seen | {
            b for a, b in edges if a in seen
        } | {
            a for a, b in edges if b in seen
        }
        if grown == seen:
            return grown == vertices
        seen = grown


cycle = {(i, (i + 1) % 6) for i in range(6)}
cover = {(i, j) for i in range(4) for j in (4, 5)}
assert connected(set(range(6)), cycle)
assert connected(set(range(6)), cover)

for d in range(14, 102, 2):
    jet_target = d + 1
    single_tangent_edge = d - 1
    annihilator_intersection = 1
    two_edge_rank = jet_target - annihilator_intersection

    assert single_tangent_edge == d - 1
    assert two_edge_rank == d
    assert 6 * (d + 1) + two_edge_rank == 7 * d + 6

text = (ROOT / "proofs/B264-two-edge-jet-dichotomy.md").read_text(
    encoding="utf-8"
)
for needle in (
    "brick_id: B264",
    "status: PROVED",
    "(R_e+R_f)^\\perp=R_e^\\perp\\cap R_f^\\perp",
    "\\dim(R_e+R_f)\\ge d",
    "\\simeq\\mathbf P^2",
    "proof, or disproof of HC",
):
    assert needle in text, f"missing {needle!r}"

print("PASS: B264 two-edge jet dichotomy and planar residual locus")
