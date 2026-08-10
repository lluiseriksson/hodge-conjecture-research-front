#!/usr/bin/env python3
"""Finite scope model for B103/NG079/G067."""

from fractions import Fraction

# Once the global good retraction is fixed, local and exterior coordinates
# are already assembled into one relative target.
relative_target = (Fraction(2), Fraction(5))  # local boundary, ambient value
retracted_target = relative_target
assert retracted_target == relative_target

# The unresolved datum is the preceding realization of the distributed
# detector; distinct realizations can have different local coordinates while
# the same global retraction remains fixed.
realization_one = (Fraction(2), Fraction(5))
realization_two = (Fraction(3), Fraction(5))
assert realization_one != realization_two
assert realization_one[1] == realization_two[1]

print("PASS: B103 global retraction fixed; G067 single-fiber realization remains")
