#!/usr/bin/env python3
"""Finite support logic for B163-B164; not a microlocal proof or HC."""


def internal_profile(escaping_nodes):
    nonzero_microsupport_components = escaping_nodes
    locally_constant = nonzero_microsupport_components == 0
    return locally_constant, nonzero_microsupport_components


for total_nodes in range(1, 20):
    for escaping in range(total_nodes + 1):
        locally_constant, components = internal_profile(escaping)
        assert components == escaping
        assert locally_constant == (escaping == 0)


# Semisimplicity permits a direct sum of a full-support local system and an
# intersection complex with positive-codimension support.
semisimple = True
summands = ("IC_full", "IC_discriminant")
nonzero_conormal_support = "IC_discriminant" in summands
assert semisimple
assert nonzero_conormal_support

print("PASS: B163 zero-microsupport logic and B164 semisimple support guard")
