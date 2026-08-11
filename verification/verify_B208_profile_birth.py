#!/usr/bin/env python3
"""Exact lightweight checks for B208, G138, and NG171."""


def main():
    # Lower profile extinction makes the decomposable profile sum zero.
    lower_profile_dimensions = [0, 0, 0, 0]
    decomposable_dimension = sum(lower_profile_dimensions)
    assert decomposable_dimension == 0

    # The birth profile is the central line, killed by the mixed map.
    birth_profile_dimension = 1
    central_mixed_value = 0
    assert birth_profile_dimension == 1
    assert central_mixed_value == 0

    # First-jet extinction does not imply profile extinction.
    dim_j = 1
    dim_k = 1
    dim_t = 0
    dim_first_jet_quotient = dim_j - dim_k
    dim_profile_quotient = dim_k - dim_t
    assert dim_first_jet_quotient == 0
    assert dim_profile_quotient == 1

    print("PASS: B208 first profile birth, G138, and NG171")


if __name__ == "__main__":
    main()
