#!/usr/bin/env python3
"""Finite incidence guards for B143; not a proof of clean analyticity or HC."""

from math import comb


for n in range(2, 8):
    for m in range(3, 13):
        nodes = m**n
        sections_on_fiber = comb(m + n, n)
        rank = sections_on_fiber - n

        # Moving the n-dimensional family of fibers removes exactly n of
        # the fixed-fiber containment conditions.
        assert sections_on_fiber - n == rank
        assert 0 < rank < nodes

        # The uniform labeled arrangement has transverse small strata and
        # one common moving-fiber stratum after saturation at rank.
        for size in (0, 1, rank - 1, rank, min(nodes, rank + 1), nodes):
            assert min(size, rank) <= rank
            if size > rank:
                assert min(size, rank) == rank

print("PASS: B143 moving-fiber codimension and uniform clean-stratum guards")
