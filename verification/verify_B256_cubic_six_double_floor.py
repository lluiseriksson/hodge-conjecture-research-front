from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


def has_hamiltonian_cycle(class_sizes: tuple[int, ...]) -> bool:
    class_of = {}
    cursor = 0
    for index, size in enumerate(class_sizes):
        for vertex in range(cursor, cursor + size):
            class_of[vertex] = index
        cursor += size
    good = {
        frozenset(edge)
        for edge in combinations(range(5), 2)
        if class_of[edge[0]] != class_of[edge[1]]
    }
    for order_tail in __import__("itertools").permutations(range(1, 5)):
        order = (0,) + order_tail
        cycle = [
            frozenset((order[index], order[(index + 1) % 5]))
            for index in range(5)
        ]
        if all(edge in good for edge in cycle):
            return True
    return False


for partition in ((1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1)):
    assert has_hamiltonian_cycle(partition), partition

assert 7 + 2 == 9
assert 2 * 7 == 14

for d in range(14, 102, 2):
    old_cubic_floor = 5 * d + 6
    cubic_floor = 6 * d + 6
    standard_floor = 6 * d - 7
    nonstandard_floor = 6 * d + 6
    assert 5 * d + 5 > 14
    assert cubic_floor == 6 * (d + 1)
    assert min(standard_floor, nonstandard_floor) == standard_floor
    assert standard_floor - (d + 1) == 5 * d - 8
    assert 2 * (5 * d - 8) == 10 * d - 16
    assert 2 * standard_floor == 12 * d - 14
    assert old_cubic_floor < cubic_floor
    assert (10 * d - 17) // 2 == 5 * d - 9

require(
    "proofs/B256-cubic-six-double-floor.md",
    (
        "brick_id: B256",
        "status: PROVED",
        "form a matching of size at most two",
        "h_Z(1)\\ge6(d+1)=6d+6",
        "s\\ge10d-16",
        "proof, or disproof of HC",
    ),
)
require(
    "proofs/G182-sextic-six-point-boundary.md",
    ("brick_id: G182", "status: NO-GO", "B256", "G183"),
)
require(
    "proofs/G183-standard-first-slope-ten-boundary.md",
    ("brick_id: G183", "status: NO-GO", "B257", "N=12d-14"),
)
require(
    "proofs/NG214-cubic-six-point-survival.md",
    ("brick_id: NG214", "status: NO-GO", "h_Z(1)\\ge6d+6", "G183"),
)

print("PASS: B256 cubic six-double floor, G182-G183 transition, and NG214")
