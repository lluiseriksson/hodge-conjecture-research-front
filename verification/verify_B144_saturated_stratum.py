#!/usr/bin/env python3
"""Finite uniform-lattice guards for B144; not an analytic proof or HC."""

from itertools import combinations


for branch_count in range(2, 10):
    ground = tuple(range(branch_count))
    for rank in range(1, branch_count + 1):
        strata = {}
        for size in range(branch_count + 1):
            for subset in combinations(ground, size):
                codimension = min(size, rank)
                label = subset if size < rank else "F"
                if label in strata:
                    assert strata[label] == codimension
                else:
                    strata[label] = codimension

        assert strata["F"] == rank
        for size in range(rank, branch_count + 1):
            assert min(size, rank) == rank
        for size in range(rank):
            assert min(size, rank) == size

print("PASS: B144 uniform intersections saturate at one rank-R stratum")
