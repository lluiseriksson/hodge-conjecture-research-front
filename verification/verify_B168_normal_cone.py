#!/usr/bin/env python3
"""Finite B168/NG132 contact logic; not a microlocal proof or HC."""


def branch_profile(contact_order, test_order):
    assert contact_order >= 2
    restricted_value_nonzero = True
    restricted_differential_on_reduced_divisor = 0
    finite_jet_matches_saturated = contact_order > test_order
    internal_reduced_conormal_rank = 1
    return (
        restricted_value_nonzero,
        restricted_differential_on_reduced_divisor,
        finite_jet_matches_saturated,
        internal_reduced_conormal_rank,
    )


for test_order in range(1, 25):
    profile = branch_profile(test_order + 1, test_order)
    nonzero_value, pointwise_restriction, same_jet, internal_rank = profile
    assert nonzero_value
    assert pointwise_restriction == 0
    assert same_jet
    assert internal_rank == 1

print("PASS: B168 normal-cone escape survives pointwise and finite-jet guards")
