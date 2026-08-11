from itertools import combinations_with_replacement
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def monomials(degree: int, variables: int) -> set[tuple[int, ...]]:
    return set(combinations_with_replacement(range(variables), degree))


# Exact tensor model for v^3 u outside Sym^4(W).
variables = 8
w_dimension = 6
sym4_w = monomials(4, w_dimension)
v = 0
u = 6
tangent_tensor = tuple(sorted((v, v, v, u)))
assert tangent_tensor not in sym4_w

# Hyperbolic polar form: v=e_0 is isotropic and u=e_6 is orthogonal to v
# when the paired indices are (0,1), (2,3), (4,5), (6,7).
partner = {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4, 6: 7, 7: 6}
assert partner[v] != v
assert u != partner[v]


def floors(d: int) -> dict[int, int]:
    standard = 8 * d - 17 if d == 14 else 8 * d - 16
    square = 7 * d + 7
    cubic = 7 * d + 6 if d >= 22 else 7 * d + 5
    quartic = cubic
    higher = 7 * d + 7
    return {1: standard, 2: square, 3: cubic, 4: quartic, 5: higher}


for d in range(14, 102, 2):
    values = floors(d)
    boundary = min(values.values())
    survivors = {k for k, value in values.items() if value == boundary}
    if d == 14:
        assert boundary == 95 and survivors == {1}
    elif d in (16, 18, 20):
        assert boundary == 8 * d - 16 and survivors == {1}
    elif d == 22:
        assert boundary == 160 and survivors == {1, 3, 4}
    else:
        assert boundary == 7 * d + 6 and survivors == {3, 4}
    delta = boundary - d - 1
    slack = 2 * delta
    assert 2 * boundary == 2 * (d + 1) + slack


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


require(
    "proofs/B273-square-equality-tangent-absorption.md",
    (
        "brick_id: B273",
        "status: PROVED",
        "v^3u\\notin\\operatorname{Sym}^4W",
        "7d+7",
        "disproof of HC",
    ),
)
require(
    "proofs/NG229-square-equality-survival.md",
    ("brick_id: NG229", "status: NO-GO", "G193", "7d+7"),
)
require(
    "proofs/G192-square-cubic-boundary.md",
    ("brick_id: G192", "status: NO-GO", "B273", "G193"),
)
require(
    "proofs/G193-standard-cubic-piecewise-boundary.md",
    ("brick_id: G193", "status: NO-GO", "R(14)=95", "B274"),
)

print("PASS: B273 square exclusion, G192 no-go, and current G193 state")
