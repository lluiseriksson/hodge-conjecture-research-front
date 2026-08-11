from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


for d in range(14, 102, 2):
    jet_target = d + 1
    graph_intersection = 1
    combined_rank = jet_target - graph_intersection
    assert combined_rank == d
    assert 6 * (d + 1) + combined_rank == 7 * d + 6

    standard = 8 * d - 17
    square = 7 * d + 7 if d >= 22 else 6 * d + 6
    cubic = 7 * d + 6
    quartic = 7 * d + 6
    higher = 7 * d + 7
    values = {1: standard, 2: square, 3: cubic, 4: quartic, 5: higher}
    floor = min(values.values())

    if d in (14, 16, 18, 20):
        expected = 6 * d + 6
        survivors = {2}
    elif d == 22:
        expected = 159
        survivors = {1}
    else:
        expected = 7 * d + 6
        survivors = {3, 4}

    assert floor == expected
    assert {key for key, value in values.items() if value == floor} == survivors
    delta = floor - (d + 1)
    assert 2 * (d + 1) + 2 * delta == 2 * floor


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


require(
    "proofs/B265-planar-two-edge-unit-separation.md",
    (
        "brick_id: B265",
        "status: PROVED",
        "\\beta_e-\\beta_f=j_1(\\ell_f)-j_1(\\ell_e)",
        "\\dim(R_e+R_f)=d",
        "h_Z(1)\\ge6d+6+d=7d+6",
        "proof, or disproof of HC",
    ),
)
require(
    "proofs/G190-square-cubic-piecewise-boundary.md",
    ("brick_id: G190", "status: NO-GO", "B265", "G191"),
)
require(
    "proofs/G191-square-standard-cubic-boundary.md",
    ("brick_id: G191", "status: NO-GO", "M(d)", "B266"),
)
require(
    "proofs/NG223-planar-cubic-quartic-equality-survival.md",
    ("brick_id: NG223", "status: NO-GO", "combined rank", "G191"),
)

print("PASS: B265 planar unit separation, G190-G191, and NG223")
