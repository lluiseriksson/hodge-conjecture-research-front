from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def rank(matrix: list[list[int]]) -> int:
    data = [list(map(Fraction, row)) for row in matrix]
    rows = len(data)
    cols = len(data[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next(
            (row for row in range(pivot_row, rows) if data[row][col]),
            None,
        )
        if pivot is None:
            continue
        data[pivot_row], data[pivot] = data[pivot], data[pivot_row]
        scale = data[pivot_row][col]
        data[pivot_row] = [entry / scale for entry in data[pivot_row]]
        for row in range(rows):
            if row != pivot_row and data[row][col]:
                scale = data[row][col]
                data[row] = [
                    entry - scale * basis
                    for entry, basis in zip(data[row], data[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


# Every complete multipartite graph on six vertices with largest part <=3
# has a perfect matching. Enumerate every set partition, not merely a
# bipartite coarsening.
def set_partitions(items: tuple[int, ...]):
    if not items:
        yield ()
        return
    first, *rest = items
    for partition in set_partitions(tuple(rest)):
        yield ((first,),) + partition
        for index in range(len(partition)):
            enlarged = list(partition)
            enlarged[index] = tuple(sorted((first,) + enlarged[index]))
            yield tuple(sorted(enlarged))


def has_perfect_matching(edges: set[frozenset[int]], remaining: frozenset[int]) -> bool:
    if not remaining:
        return True
    first = min(remaining)
    return any(
        frozenset((first, other)) in edges
        and has_perfect_matching(edges, remaining - {first, other})
        for other in remaining - {first}
    )


partitions = {
    tuple(sorted(tuple(sorted(part)) for part in partition))
    for partition in set_partitions(tuple(range(6)))
}
for partition in partitions:
    if max(map(len, partition)) > 3:
        continue
    class_of = {vertex: index for index, part in enumerate(partition) for vertex in part}
    edges = {
        frozenset((left, right))
        for left, right in combinations(range(6), 2)
        if class_of[left] != class_of[right]
    }
    assert has_perfect_matching(edges, frozenset(range(6)))


# Exact 4+2 collinear sample for the polynomial G in B272.
alpha = (1, 2, 3, 4)
beta = (1, 2)


def polynomial_coefficients() -> dict[tuple[int, int], Fraction]:
    # Expand R(x), S(y), and xy V(y) for the sample.
    result: dict[tuple[int, int], Fraction] = {}

    def add(i: int, j: int, value: Fraction) -> None:
        result[(i, j)] = result.get((i, j), Fraction(0)) + value

    # R(x)=(x-1)(x-2)(x-3)(x-4).
    r_coeff = {0: 24, 1: -50, 2: 35, 3: -10, 4: 1}
    # S(y)=(y-1)^2(y-2)^2.
    s_coeff = {0: 4, 1: -12, 2: 13, 3: -6, 4: 1}
    r0 = Fraction(r_coeff[0])
    c = r0 / Fraction(s_coeff[0])
    for i, value in r_coeff.items():
        add(i, 0, Fraction(value))
    add(0, 0, -r0)
    for j, value in s_coeff.items():
        add(0, j, c * value)

    # V(1)=50 and V(2)=25 because R'(0)=-50.
    # Thus V(y)=75-25y.
    add(1, 1, Fraction(75))
    add(1, 2, Fraction(-25))
    return result


coeff = polynomial_coefficients()


def value(x: int, y: int) -> Fraction:
    return sum(c * x**i * y**j for (i, j), c in coeff.items())


def dx(x: int, y: int) -> Fraction:
    return sum(
        c * i * x ** (i - 1) * y**j
        for (i, j), c in coeff.items()
        if i
    )


def dy(x: int, y: int) -> Fraction:
    return sum(
        c * j * x**i * y ** (j - 1)
        for (i, j), c in coeff.items()
        if j
    )


assert all(value(a, 0) == 0 for a in alpha)
for b in beta:
    assert value(0, b) == dx(0, b) == dy(0, b) == 0
assert value(0, 0) != 0


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


require(
    "proofs/B272-quartic-planar-equality-exclusion.md",
    (
        "brick_id: B272",
        "status: PROVED",
        "G(x,y)=R(x)-R(0)+cS(y)+xyV(y)",
        "2+(d-2)=d",
        "7d+6",
        "disproof of HC",
    ),
)
require(
    "proofs/NG228-quartic-planar-equality-survival.md",
    ("brick_id: NG228", "status: NO-GO", "G192", "quartic equality"),
)
require(
    "proofs/G204-nonstandard-three-row-boundary.md",
    ("brick_id: G204", "status: EXPLORATORY", "B283", "active"),
)

print("PASS: B272 quartic exclusion, NG228, and current downstream boundary")
