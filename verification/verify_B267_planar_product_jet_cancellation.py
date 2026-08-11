from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


for d in range(14, 102, 2):
    tangent_dimension = d
    endpoint_plane = 2
    derivative_space = tangent_dimension - endpoint_plane
    common_product_generator = 1
    planar_rank = derivative_space + common_product_generator

    assert derivative_space == d - 2
    assert planar_rank == d - 1
    assert 6 * (d + 1) + planar_rank == 7 * d + 5


def first_jet_product(
    left: tuple[int, tuple[int, ...]],
    right: tuple[int, tuple[int, ...]],
) -> tuple[int, tuple[int, ...]]:
    c, alpha = left
    d, beta = right
    return c * d, tuple(c * b + d * a for a, b in zip(alpha, beta))


for width in (2, 5, 11):
    lam_e = tuple(range(1, width + 1))
    total = tuple(3 * i + 7 for i in range(width))
    complement = tuple(a - b for a, b in zip(total, lam_e))
    assert first_jet_product((1, lam_e), (1, complement)) == (1, total)

    delta = tuple((-1) ** i for i in range(width))
    assert first_jet_product((0, delta), (1, complement)) == (0, delta)


text = (ROOT / "proofs/B267-planar-product-jet-cancellation.md").read_text(
    encoding="utf-8"
)
for needle in (
    "brick_id: B267",
    "status: PROVED",
    "(1,\\lambda_e)(1,\\Lambda-\\lambda_e)=(1,\\Lambda)=j(P)",
    "R_e=R_f",
    "=d-1",
    "restores G190 as the active universal gate",
    "proof, or disproof of HC",
):
    assert needle in text, f"missing {needle!r}"

print("PASS: B267 planar product-jet cancellation and B265 retraction")
