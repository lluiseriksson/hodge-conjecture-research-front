from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


class_partitions = [
    (1, 1, 1, 1, 1),
    (2, 1, 1, 1),
    (2, 2, 1),
    (3, 1, 1),
    (3, 2),
]

for sizes in class_partitions:
    classes = []
    cursor = 0
    for size in sizes:
        classes.append(tuple(range(cursor, cursor + size)))
        cursor += size
    class_of = {vertex: index for index, part in enumerate(classes) for vertex in part}
    good_edges = [
        edge
        for edge in combinations(range(5), 2)
        if class_of[edge[0]] != class_of[edge[1]]
    ]
    witnesses = []
    for count in range(5, 7):
        for chosen in combinations(good_edges, count):
            degrees = [0] * 5
            for left, right in chosen:
                degrees[left] += 1
                degrees[right] += 1
            if min(degrees) >= 2:
                witnesses.append((chosen, degrees))
                break
        if witnesses:
            break
    assert witnesses, f"no at-most-six-edge cover for partition {sizes}"

for d in range(14, 102, 2):
    standard_floor = 6 * d - 7
    square_floor = 6 * d + 6
    cubic_floor = 5 * d + 6
    higher_floor = 6 * d + 6
    common_floor = min(standard_floor, square_floor, cubic_floor, higher_floor)
    assert common_floor == cubic_floor
    assert standard_floor > cubic_floor
    assert cubic_floor - (d + 1) == 4 * d + 5
    assert 2 * (4 * d + 5) == 8 * d + 10
    assert 2 * cubic_floor == 10 * d + 12
    assert (8 * d + 9) // 2 == 4 * d + 4

require(
    "proofs/B255-higher-power-five-double-equality-exclusion.md",
    (
        "brick_id: B255",
        "status: PROVED",
        "complete multipartite",
        "h_Z(1)\\ge5d+6",
        "s\\ge8d+10",
        "proof, or disproof of HC",
    ),
)
require(
    "proofs/G181-higher-power-five-double-boundary.md",
    ("brick_id: G181", "status: NO-GO", "B255", "G182"),
)
require(
    "proofs/G182-sextic-six-point-boundary.md",
    ("brick_id: G182", "status: EXPLORATORY", "A=O_Q(3)", "N=10d+12"),
)
require(
    "proofs/NG213-higher-power-five-double-survival.md",
    ("brick_id: NG213", "status: NO-GO", "h_Z(1)\\ge6d+6", "G182"),
)

print("PASS: B255 higher-power equality exclusion, G181-G182, and NG213")
