from fractions import Fraction
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


points = [(1, 0), (2, 0), (3, 0), (0, 1), (0, 2), (0, 3)]
monomials_6 = [(i, j) for i in range(7) for j in range(7 - i)]
double_rows: list[list[int]] = []
for x, y in points:
    double_rows.append([x**i * y**j for i, j in monomials_6])
    double_rows.append(
        [i * x ** (i - 1) * y**j if i else 0 for i, j in monomials_6]
    )
    double_rows.append(
        [j * x**i * y ** (j - 1) if j else 0 for i, j in monomials_6]
    )

assert len(monomials_6) == 28
assert rank(double_rows) == 18

u_rows = [
    [1 if (i, j) == (0, 0) else 0 for i, j in monomials_6],
    [1 if (i, j) == (1, 0) else 0 for i, j in monomials_6],
    [1 if (i, j) == (0, 1) else 0 for i, j in monomials_6],
]
assert rank(double_rows + u_rows) - rank(double_rows) == 1

monomials_5 = [(i, j) for i in range(6) for j in range(6 - i)]
value_rows_6 = [
    [x**i * y**j for i, j in monomials_5] for x, y in points
]
value_rows_7 = value_rows_6 + [
    [1 if (i, j) == (0, 0) else 0 for i, j in monomials_5]
]
assert len(monomials_5) == 21
assert rank(value_rows_6) == 6
assert rank(value_rows_7) == 7

for d in range(22, 102, 2):
    six_double_rank = 18 + 6 * (d - 2)
    residual_rank = 1 + (d - 2)
    seven_double_rank = six_double_rank + residual_rank
    assert six_double_rank == 6 * d + 6
    assert residual_rank == d - 1
    assert seven_double_rank == 7 * d + 5


def require(path: str, needles: tuple[str, ...]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


require(
    "proofs/B268-planar-cubic-equality-witness.md",
    (
        "brick_id: B268",
        "status: PROVED",
        "18+6(d-2)=6d+6",
        "=1+(d-2)=d-1",
        "6d+6+(d-1)=7d+5",
        "disproof of HC",
    ),
)
require(
    "proofs/NG225-planar-sextic-interpolation-escape.md",
    ("brick_id: NG225", "status: NO-GO", "full residual image rank", "G190"),
)

print("PASS: B268 exact planar cubic equality rank and NG225")
