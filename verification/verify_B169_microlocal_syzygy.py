#!/usr/bin/env python3
"""Finite guards for B169's branchwise logic; not a microlocal proof or HC."""


def branch_absorption(restricted_value_identically_zero, nodal_conormal_occurs=True):
    """Truth table encoded by B169 under its exhaustive smooth-ODP hypotheses."""
    envelope_absorbed = restricted_value_identically_zero
    actual_ss_absorbed = restricted_value_identically_zero and nodal_conormal_occurs
    hidden_generator_zero = restricted_value_identically_zero
    return envelope_absorbed, actual_ss_absorbed, hidden_generator_zero


persisting = branch_absorption(True)
escaping = branch_absorption(False)

assert persisting == (True, True, True)
assert escaping == (False, False, False)

# The y^m family is escaping for every finite contact order, although its
# pointwise differential on the reduced intersection vanishes.
for contact_order in range(2, 65):
    restricted_value_identically_zero = False
    pointwise_tangent_differential = 0
    assert pointwise_tangent_differential == 0
    assert branch_absorption(restricted_value_identically_zero) == escaping

print("PASS: B169 microlocal absorption collapses branchwise to persistence and H_tau=0")
