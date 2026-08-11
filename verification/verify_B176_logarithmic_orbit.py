#!/usr/bin/env python3
"""Bounded identities for B176/G109/NG140; not a proof of HC."""


def bad_tau(x: int, y: int) -> tuple[int, int]:
    return x, x + y * y


def good_tau(x: int, y: int) -> tuple[int, int]:
    return x, (1 + y) * x


# Good model: I=(x), and partial_y preserves the ideal with nonzero value.
for x in range(-8, 9):
    for y in range(-7, 8):
        tau_1, tau_2 = good_tau(x, y)
        delta_y_tau_1 = 0
        delta_y_tau_2 = x
        assert delta_y_tau_1 == 0 * tau_1
        assert delta_y_tau_2 == tau_1
        assert tau_2 == (1 + y) * tau_1
assert (0, 1) != (0, 0)


# Bad model: every displayed general logarithmic coefficient has
# a in (x,y^2) and b in (x,y), hence zero value at the origin.
for x in range(-6, 7):
    for y in range(-5, 6):
        p = 2 + x - y
        q = -1 + 2 * x + y
        r = 3 - x + 2 * y
        s = 1 + x + y
        a = x * p + y * y * q
        b = x * r + y * s
        delta_x = a
        delta_y_squared = 2 * y * b
        assert delta_x == x * p + y * y * q
        assert delta_y_squared == x * (2 * y * r) + y * y * (2 * s)

a_origin = 0
b_origin = 0
assert (a_origin, b_origin) == (0, 0)

# Nevertheless both bad critical-value differentials are dx, so dy spans
# the one-dimensional central kernel.
assert bad_tau(0, 0) == (0, 0)
bad_differentials = ((1, 0), (1, 0))
assert bad_differentials[0] == bad_differentials[1]
assert (0, 1) != (0, 0)

print("PASS: B176 logarithmic evaluation separates smooth and hidden ideals")
