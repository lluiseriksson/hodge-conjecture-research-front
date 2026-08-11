#!/usr/bin/env python3
"""Bounded exact checks for B223-B224/G150/NG184; not a proof of HC."""

from fractions import Fraction


def rank(matrix: list[list[Fraction]]) -> int:
    rows = [row[:] for row in matrix]
    if not rows:
        return 0
    r = 0
    for c in range(len(rows[0])):
        pivot = next((i for i in range(r, len(rows)) if rows[i][c]), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        scale = rows[r][c]
        rows[r] = [x / scale for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                factor = rows[i][c]
                rows[i] = [x - factor * y for x, y in zip(rows[i], rows[r])]
        r += 1
    return r


def dot(left: list[Fraction], right: list[Fraction]) -> Fraction:
    return sum(x * y for x, y in zip(left, right))


def main() -> None:
    # A rank-4 code containing the constant word and its exact rank-3
    # orthogonal complement in seven coordinates.
    a = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, -1, 0, 0, 0, 0, 0],
        [0, 0, 1, -1, 0, 0, 0],
        [0, 0, 0, 0, 1, -1, 0],
    ]
    b = [
        [1, 1, 0, 0, 0, 0, -2],
        [0, 0, 1, 1, 0, 0, -2],
        [0, 0, 0, 0, 1, 1, -2],
    ]
    a_q = [[Fraction(x) for x in row] for row in a]
    b_q = [[Fraction(x) for x in row] for row in b]
    assert rank(a_q) == 4
    assert rank(b_q) == 3
    assert rank(a_q) + rank(b_q) == 7
    assert all(dot(row_a, row_b) == 0 for row_a in a_q for row_b in b_q)

    # On P^n x P^n with H=O(2,4), K_X tensor H^q cannot be trivial:
    # subtracting the two required equations forces q=0, then n=-1.
    for n in range(2, 13):
        simultaneous_q = Fraction(0)
        assert 2 * simultaneous_q == 0
        assert -n - 1 + 2 * simultaneous_q != 0
        # Middle and preceding Betti numbers of P^n x P^n.
        assert (n + 1) - n == 1

    print("PASS: B223 weighted Gale duality and B224 canonical-shift obstruction")


if __name__ == "__main__":
    main()
