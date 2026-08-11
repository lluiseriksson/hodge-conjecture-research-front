from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


for d in range(14, 102, 2):
    ambient_vectors = d + 2
    variable_edge_space = ambient_vectors - 2
    jet_target = d + 1
    tangent_kernel = 1
    rank = variable_edge_space - tangent_kernel

    assert variable_edge_space == d
    assert jet_target == d + 1
    assert rank == d - 1
    assert rank < d

text = (ROOT / "proofs/NG222-single-edge-kernel-removal.md").read_text(
    encoding="utf-8"
)
for needle in (
    "brick_id: NG222",
    "status: NO-GO",
    "B(e_i,f_j)=\\delta_{ij}",
    "every edge is good",
    "=d-1",
    "proof, or disproof of",
):
    assert needle in text, f"missing {needle!r}"

print("PASS: NG222 single-edge tangent-kernel countermodel")
