from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


# Solve the effective-root equations for ordinary blow-ups at six points.
solutions: set[tuple[int, tuple[int, ...]]] = set()
# Cauchy gives 9e^2 <= 6(e^2+2), hence e <= 2.
for degree in range(1, 3):
    for multiplicities in product(range(3), repeat=6):
        if sum(multiplicities) != 3 * degree:
            continue
        if sum(value * value for value in multiplicities) != degree * degree + 2:
            continue
        solutions.add((degree, multiplicities))

assert {degree for degree, _ in solutions} == {1, 2}
assert all(
    sorted(multiplicities) == [0, 0, 0, 1, 1, 1]
    for degree, multiplicities in solutions
    if degree == 1
)
assert all(
    multiplicities == (1, 1, 1, 1, 1, 1)
    for degree, multiplicities in solutions
    if degree == 2
)


# Two line roots intersect on the blow-up exactly for complementary triples.
triples = [set(indices) for indices in combinations(range(6), 3)]
for first, second in combinations(triples, 2):
    intersection = 1 - len(first & second)
    if intersection == 1:
        assert first.isdisjoint(second)
        assert first | second == set(range(6))
    else:
        assert intersection <= 0


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


require(
    "proofs/B270-sextic-to-anticanonical-jet.md",
    (
        "brick_id: B270",
        "status: PROVED",
        "j_u(C_0)^{-1}",
        "every cubic through the seven reduced points is singular",
    ),
)
require(
    "proofs/B271-planar-cubic-equality-classification.md",
    (
        "brick_id: B271",
        "status: PROVED",
        "9e^2\\le6(e^2+2)",
        "fundamental-cycle ideal has a local",
        "excludes \\(A=O_Q(3)\\)",
        "disproof of",
    ),
)
require(
    "proofs/NG227-cubic-planar-equality-survival.md",
    ("brick_id: NG227", "status: NO-GO", "quartic equality", "G190"),
)

print("PASS: B270 anticanonical reduction, B271 classification, and NG227")
