#!/usr/bin/env python3
"""Exact lightweight checks for B248, G171-G172, and NG206; not a proof of HC."""

from math import comb


def first_even_dimension(j: int) -> int:
    cap = comb(2 * j + 10, j + 3)
    rank_threshold = (cap - 4 - j) // 4 + 1
    d = max(8, j + 8, rank_threshold)
    if d % 2:
        d += 1
    return d


def main() -> None:
    for j in range(0, 16):
        cap = comb(2 * j + 10, j + 3)
        d = first_even_dimension(j)
        rank = 4 * d + 4 + j

        assert d % 2 == 0 and d >= 8
        assert d > j + 7
        assert rank > cap
        assert rank < 5 * d - 3

        # The balanced and adjacent odd layers have the asserted rank.
        for slack in (6 * d + 6 + 2 * j, 6 * d + 7 + 2 * j):
            assert d + 1 + slack // 2 == rank
        assert 2 * rank == 8 * d + 8 + 2 * j

        # B215's high-power scheme has one condition too many.
        interpolation_degree = 2 * 4 + (j + 1) - 1
        assert interpolation_degree == 8 + j
        assert 4 * (d + 1) + (j + 1) == rank + 1

        # In the complementary finite power range, every intermediate
        # span rank is bounded by the displayed cap.
        for k in range(2, (j + 7) // 2 + 1):
            assert 2 * k <= j + 7
            for ell in range(0, j + 1):
                projective_dimension = 3 + ell
                assert comb(
                    projective_dimension + 2 * k,
                    projective_dimension,
                ) <= cap
            assert 2 * k - 2 >= 2

    # G171 is j=1; Q^124 is an explicit valid falsifying input.
    assert first_even_dimension(1) == 124
    assert 4 * 124 + 5 == 501 > comb(12, 4) == 495

    # The exact necessary inverse-binomial threshold grows.
    def inverse_threshold(d: int) -> int:
        j = 1
        while 4 * d + 4 + j > comb(2 * j + 10, j + 3):
            j += 1
        return min(d - 7, j)

    samples = [128, 512, 10_000, 1_000_000]
    thresholds = [inverse_threshold(d) for d in samples]
    assert thresholds == [2, 3, 5, 8]

    print("PASS: B248 fixed-additive exclusion, G171-G172, and NG206")


if __name__ == "__main__":
    main()
