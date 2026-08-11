#!/usr/bin/env python3
"""Finite B165-B166/NG131 logic; not a microlocal proof or HC."""


def positive_certificate(node_counts):
    coefficients = tuple(node_counts)
    assert all(count >= 0 for count in coefficients)
    zero_internal_support = all(count == 0 for count in coefficients)
    return coefficients, zero_internal_support


for counts in ((), (0,), (1,), (0, 2, 0), (3, 1, 4)):
    coefficients, zero = positive_certificate(counts)
    assert zero == (sum(coefficients) == 0)
    assert zero == (not any(coefficients))


# Product with an elliptic curve: hard-Lefschetz-symmetric Betti data has
# zero alternating class but a positive non-alternating package.
elliptic_betti = {0: 1, 1: 2, 2: 1}
alternating_class = sum((-1) ** degree * rank for degree, rank in elliptic_betti.items())
positive_rank = sum(elliptic_betti.values())
assert elliptic_betti[0] == elliptic_betti[2]
assert alternating_class == 0
assert positive_rank == 4

# A nonzero support copied into these shifts remains present as a union even
# though its signed characteristic-cycle coefficient cancels.
support_present_in_shift = tuple(rank > 0 for rank in elliptic_betti.values())
assert any(support_present_in_shift)

print("PASS: B165 positive certificate and NG131 elliptic cancellation guard")
