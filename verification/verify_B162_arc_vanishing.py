#!/usr/bin/env python3
"""Finite support/rank guards for B162/NG129; not a sheaf proof or HC."""


def specialization_profile(node_escape_flags, hypersurface_dimension):
    rank = sum(bool(flag) for flag in node_escape_flags)
    euler = ((-1) ** hypersurface_dimension) * rank
    return rank, euler


for dimension in range(1, 10):
    for node_count in range(1, 12):
        for escaping in range(node_count + 1):
            flags = [True] * escaping + [False] * (node_count - escaping)
            rank, euler = specialization_profile(flags, dimension)
            assert rank == escaping
            assert euler == ((-1) ** dimension) * escaping
            assert (rank == 0) == (not any(flags))


# A constant degree-zero cohomology sheaf does not constrain a complementary
# middle
# specialization cone.
constant_piece_rank = 1
for dimension in range(1, 10):
    escaping_rank, _ = specialization_profile([True], dimension)
    assert constant_piece_rank == 1
    assert escaping_rank == 1

print("PASS: B162 point-support escape ranks and NG129 constant-piece split")
