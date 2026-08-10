#!/usr/bin/env python3
"""Finite matrix checks for B095's dual obstruction dichotomy."""

from fractions import Fraction

# u(x,y)=x.  im(u^*) is the line of functionals (a,0).
detector_ambiguity = (Fraction(0), Fraction(1))
assert detector_ambiguity[1] != 0  # nonzero cokernel class: success branch 1.

detector_descended = (Fraction(3), Fraction(0))
t = Fraction(2)
assert detector_descended[1] == 0
lambda_on_t = detector_descended[0] * t
assert lambda_on_t != 0  # descended-evaluation branch 2.

detector_failure = (Fraction(0), Fraction(0))
assert detector_failure[1] == 0
assert detector_failure[0] * t == 0

print("PASS: B095 dual cokernel/evaluation alternatives")
