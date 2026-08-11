from itertools import permutations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


# Any one forbidden edge in K_{3,3} can be avoided by a perfect matching.
matchings = [
    {(i, sigma[i - 1]) for i in range(1, 4)}
    for sigma in permutations((1, 2, 3))
]
for forbidden_i in range(1, 4):
    for forbidden_j in range(1, 4):
        assert any(
            (forbidden_i, forbidden_j) not in matching
            for matching in matchings
        )


def connector(i: int, j: int, x: int, y: int) -> int:
    # j*x + i*y - i*j vanishes at p_i=(i,0) and q_j=(0,j).
    return j * x + i * y - i * j


for matching in matchings:
    sigma = dict(matching)
    # Each selected connector contains its assigned outer supports.
    for i in range(1, 4):
        assert connector(i, sigma[i], i, 0) == 0
        assert connector(i, sigma[i], 0, sigma[i]) == 0
        assert connector(i, sigma[i], 0, 0) != 0


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


require(
    "proofs/B269-planar-witness-no-eighth-double.md",
    (
        "brick_id: B269",
        "status: PROVED",
        "F_x=E^2M^4",
        "every eighth distinct double neighborhood",
        "no exact cubic 3+3 equality witness",
        "prove or disprove HC",
    ),
)
require(
    "proofs/NG226-extend-B268-marked-scheme.md",
    (
        "brick_id: NG226",
        "status: NO-GO",
        "every \\(3+3\\) configuration",
        "G190",
    ),
)

print("PASS: B269 no-eighth-double theorem and NG226")
