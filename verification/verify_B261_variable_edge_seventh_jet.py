from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


for d in range(14, 102, 2):
    edge_space = d
    jet_target = d + 1
    kernel_upper = 1
    residual_rank = edge_space - kernel_upper
    assert residual_rank == d - 1
    assert 6 * (d + 1) + residual_rank == 7 * d + 5

    standard = 7 * d - 12
    square = 7 * d + 7 if d >= 22 else 6 * d + 6
    cubic = 7 * d + 5
    quartic = 7 * d + 5
    higher = 7 * d + 7
    floor = min(standard, square, cubic, quartic, higher)

    if d == 20:
        expected = 126
        survivors = {2}
    elif d == 18:
        expected = 114
        survivors = {1, 2}
    else:
        expected = 7 * d - 12
        survivors = {1}

    assert floor == expected
    values = {1: standard, 2: square, 3: cubic, 4: quartic, 5: higher}
    assert {key for key, value in values.items() if value == floor} == survivors

    delta = floor - (d + 1)
    slack = 2 * delta
    length = 2 * (d + 1) + slack
    assert length == 2 * floor

require(
    "proofs/B261-variable-edge-seventh-jet-floor.md",
    (
        "brick_id: B261",
        "status: PROVED",
        "\\dim V_e=d",
        "\\ge d-1",
        "h_Z(1)\\ge6d+6+(d-1)=7d+5",
        "proof, or disproof of HC",
    ),
)
require(
    "proofs/G187-reduced-piecewise-seventh-point-boundary.md",
    ("brick_id: G187", "status: NO-GO", "B261", "G188"),
)
require(
    "proofs/G188-mostly-standard-seventh-jet-boundary.md",
    ("brick_id: G188", "status: EXPLORATORY", "J(d)", "A=O_Q(2)"),
)
require(
    "proofs/NG219-cubic-quartic-one-residual-rank-survival.md",
    ("brick_id: NG219", "status: NO-GO", "d-1", "G188"),
)

print("PASS: B261 variable-edge seventh jets, G187-G188, and NG219")
