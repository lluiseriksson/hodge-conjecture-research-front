#!/usr/bin/env python3
"""Finite arithmetic guards for B149/NG120; not a proof of HC."""


for n in range(1, 8):
    for node_count in range(2, 16):
        length = (n + 1) * node_count
        for value_rank in range(1, node_count):
            for projected_rank in range(0, n + 1):
                jet_rank = value_rank + projected_rank
                value_defect = node_count - value_rank
                oriented_defect = length - jet_rank
                additional_defect = oriented_defect - value_defect

                assert oriented_defect == (
                    (n + 1) * node_count
                    - value_rank
                    - projected_rank
                )
                assert additional_defect == n * node_count - projected_rank
                assert additional_defect >= n * (node_count - 1)
                assert jet_rank < length

print("PASS: B149 oriented half-double length, rank, and defect identities")
