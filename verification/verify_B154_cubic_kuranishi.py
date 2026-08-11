#!/usr/bin/env python3
"""Exact scalar and local-model guards for B154/NG124; not a proof of HC."""

from fractions import Fraction


# Check the repeated-direction critical-value formula by exact truncated
# expansion in one spatial variable:
# s(z)=h z^2/2+t z^3/6 and a(z)=l z+A z^2/2.
for h in range(1, 7):
    for third_spatial in range(-3, 4):
        for linear in range(-3, 4):
            for second_direction in range(-2, 3):
                hq = Fraction(h)
                tq = Fraction(third_spatial)
                lq = Fraction(linear)
                aq = Fraction(second_direction)

                v = lq / hq
                # x(u)=-u v+u^2 w/2 from the critical equation.
                w = (2 * aq * v - tq * v * v) / hq

                # Coefficient of u^3 in s(x(u))+u a(x(u)).
                coefficient = (
                    -Fraction(1, 2) * hq * v * w
                    -Fraction(1, 6) * tq * v**3
                    +Fraction(1, 2) * lq * w
                    +Fraction(1, 2) * aq * v**2
                )
                third_derivative = 6 * coefficient
                expected = 3 * aq * v**2 - tq * v**3
                assert third_derivative == expected


# NG124: tau=(x,x+y^3). The value relation kills linear and quadratic
# y-coefficients but not the cubic coefficient.
tau_1 = [Fraction(0), Fraction(0), Fraction(0), Fraction(0)]
tau_2 = [Fraction(0), Fraction(0), Fraction(0), Fraction(1)]
relation_series = [right - left for left, right in zip(tau_1, tau_2)]
assert relation_series[0] == 0
assert relation_series[1] == 0
assert relation_series[2] == 0
assert relation_series[3] == 1

print("PASS: B154 cubic critical-value formula and NG124 nonreduced model")
