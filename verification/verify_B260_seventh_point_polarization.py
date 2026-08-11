from itertools import combinations, permutations
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


def good_edges(class_sizes: tuple[int, ...]):
    class_of = {}
    cursor = 0
    for index, size in enumerate(class_sizes):
        for vertex in range(cursor, cursor + size):
            class_of[vertex] = index
        cursor += size
    return {
        frozenset(edge)
        for edge in combinations(range(6), 2)
        if class_of[edge[0]] != class_of[edge[1]]
    }


def has_six_cycle(class_sizes: tuple[int, ...]) -> bool:
    good = good_edges(class_sizes)
    for tail in permutations(range(1, 6)):
        order = (0,) + tail
        cycle = [
            frozenset((order[index], order[(index + 1) % 6]))
            for index in range(6)
        ]
        if all(edge in good for edge in cycle):
            return True
    return False


partitions_max_three = (
    (3, 3),
    (3, 2, 1),
    (3, 1, 1, 1),
    (2, 2, 2),
    (2, 2, 1, 1),
    (2, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1),
)
for partition in partitions_max_three:
    assert has_six_cycle(partition), partition

for partition in ((4, 2), (4, 1, 1)):
    good = good_edges(partition)
    cover = {
        frozenset((left, right))
        for left in range(4)
        for right in range(4, 6)
    }
    assert len(cover) == 8
    assert cover <= good
    degrees = [sum(vertex in edge for edge in cover) for vertex in range(6)]
    assert degrees == [2, 2, 2, 2, 4, 4]

assert comb(9, 4) == 126

for d in range(14, 102, 2):
    standard = 7 * d - 12
    square = 7 * d + 7 if d >= 22 else 6 * d + 6
    cubic = 6 * d + 7
    quartic = 6 * d + 7
    higher = 7 * d + 7
    floor = min(standard, square, cubic, quartic, higher)

    if d in (14, 16):
        expected = 7 * d - 12
        survivors = {1}
    elif d == 18:
        expected = 114
        survivors = {1, 2}
    elif d == 20:
        expected = 126
        survivors = {2}
    else:
        expected = 6 * d + 7
        survivors = {3, 4}

    assert floor == expected
    values = {1: standard, 2: square, 3: cubic, 4: quartic, 5: higher}
    assert {key for key, value in values.items() if value == floor} == survivors

    delta = floor - (d + 1)
    slack = 2 * delta
    length = 2 * (d + 1) + slack
    assert length == 2 * floor

require(
    "proofs/B260-seventh-point-polarization-reduction.md",
    (
        "brick_id: B260",
        "status: PROVED",
        "h^0(\\mathbf P^5,O(4))=\\binom94=126",
        "k\\ge5",
        "h_Z(1)\\ge7(d+1)=7d+7",
        "proof, or disproof of HC",
    ),
)
require(
    "proofs/G186-piecewise-post-standard-band-boundary.md",
    ("brick_id: G186", "status: NO-GO", "B260", "G187"),
)
require(
    "proofs/G187-reduced-piecewise-seventh-point-boundary.md",
    ("brick_id: G187", "status: EXPLORATORY", "H(d)", "A=O_Q(3),O_Q(4)"),
)
require(
    "proofs/NG218-seventh-point-polarization-survival.md",
    ("brick_id: NG218", "status: NO-GO", "126<6d+6", "G187"),
)

print("PASS: B260 seventh-point polarization reduction, G186-G187, and NG218")
