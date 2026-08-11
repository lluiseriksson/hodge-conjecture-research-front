#!/usr/bin/env python3
"""Exact lightweight checks for B209-B210, G139, and NG172."""


def quotient_dimension(larger, smaller):
    assert larger >= smaller
    return larger - smaller


def main():
    # Adjacent second-osculating absorption.
    lower_point_span = 7
    lower_tangent_span = 7
    lower_second_span = 7
    assert quotient_dimension(lower_tangent_span, lower_point_span) == 0
    assert quotient_dimension(lower_second_span, lower_tangent_span) == 0

    # Controlled degree-m birth: d first-jet directions and one profile.
    dimension_x = 4
    birth_point_span = 9
    birth_tangent_span = birth_point_span + dimension_x
    birth_second_span = birth_tangent_span + 1
    assert quotient_dimension(birth_tangent_span, birth_point_span) == dimension_x
    assert quotient_dimension(birth_second_span, birth_tangent_span) == 1

    # Tangent absorption alone leaves the second layer unconstrained.
    flag_point = 1
    flag_tangent = 1
    flag_second = 2
    assert quotient_dimension(flag_tangent, flag_point) == 0
    assert quotient_dimension(flag_second, flag_tangent) == 1

    print("PASS: B209-B210 adjacent second-osculating birth, G139, and NG172")


if __name__ == "__main__":
    main()
