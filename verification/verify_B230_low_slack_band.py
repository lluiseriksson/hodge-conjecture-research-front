#!/usr/bin/env python3
"""Exact bounded checks for B230/NG188/G154; not a proof of HC."""

from fractions import Fraction


def rank(matrix: list[list[int]]) -> int:
    rows = [[Fraction(x) for x in row] for row in matrix]
    result = 0
    for column in range(len(rows[0])):
        pivot = next(
            (i for i in range(result, len(rows)) if rows[i][column]),
            None,
        )
        if pivot is None:
            continue
        rows[result], rows[pivot] = rows[pivot], rows[result]
        scale = rows[result][column]
        rows[result] = [x / scale for x in rows[result]]
        for i in range(len(rows)):
            if i != result and rows[i][column]:
                scale = rows[i][column]
                rows[i] = [
                    x - scale * y for x, y in zip(rows[i], rows[result])
                ]
        result += 1
    return result


def main() -> None:
    # Q^4, m=2: h_1=5+delta_1 stays below two double jets through s=9.
    for slack in range(2, 10):
        delta_max = slack // 2
        assert 5 + delta_max < 10

    # Q^4, m>=3: h_2=15+delta_2 stays below two triple jets through s=14.
    for slack in range(1, 15):
        assert 15 + slack < 30

    # An explicit hyperbolic six-space: W=<e0,e1,e2> is isotropic.
    # At p=e0, u=f1 lies in p^perp but p*u is outside Sym^2(W).
    # Coordinates index symmetric pairs among e0,e1,e2,f0,f1,f2.
    pairs = [(i, j) for i in range(6) for j in range(i, 6)]
    sym_w = []
    for i in range(3):
        for j in range(i, 3):
            sym_w.append([int(pair == (i, j)) for pair in pairs])
    p_times_u = [int(pair == (0, 4)) for pair in pairs]
    assert rank(sym_w) == 6
    assert rank(sym_w + [p_times_u]) == 7

    # The first Q^4-surviving m=2 signature is slack ten, delta_1=5.
    d = 4
    slack = 10
    delta_1 = 5
    length = 2 * (d + 1) + slack
    h_1 = d + 1 + delta_1
    assert length == 20
    assert h_1 == 10 == length // 2
    assert slack - 2 * delta_1 == 0

    # General even dimension d=2n has the G154 dimensions.
    for n in range(1, 9):
        d = 2 * n
        length = 2 * (d + 1) + 10
        h_1 = d + 1 + 5
        assert length == 4 * n + 12
        assert h_1 == 2 * n + 6 == length // 2

    print("PASS: B230 low-slack exclusion and G154 first survivor")


if __name__ == "__main__":
    main()
