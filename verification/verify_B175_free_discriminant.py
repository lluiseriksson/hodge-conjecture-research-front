#!/usr/bin/env python3
"""Exact B175/NG139 identities; bounded check, not a proof of HC."""


def tau_1(x: int, y: int) -> int:
    return x


def tau_2(x: int, y: int) -> int:
    return x + y * y


def discriminant(x: int, y: int) -> int:
    return tau_1(x, y) * tau_2(x, y)


for x in range(-12, 13):
    for y in range(-10, 11):
        f = discriminant(x, y)
        f_x = 2 * x + y * y
        f_y = 2 * x * y

        # delta_E = 2x d_x + y d_y and
        # delta_H = 2xy d_x - (2x+y^2) d_y.
        delta_e_f = 2 * x * f_x + y * f_y
        delta_h_f = 2 * x * y * f_x - (2 * x + y * y) * f_y
        assert delta_e_f == 4 * f
        assert delta_h_f == 0

        # Saito determinant of the two coefficient columns.
        determinant = 2 * x * (-(2 * x + y * y)) - y * (2 * x * y)
        assert determinant == -4 * f

        # The same basis preserves both labelled branches separately.
        assert 2 * x == 2 * tau_1(x, y)
        assert 2 * x * y == 2 * y * tau_1(x, y)
        assert 2 * x + 2 * y * y == 2 * tau_2(x, y)
        delta_h_tau_2 = 2 * x * y - 2 * y * (2 * x + y * y)
        assert delta_h_tau_2 == -2 * y * tau_2(x, y)

# The Koszul generator vanishes at the origin, so it cannot lift (1,-1).
assert (tau_2(0, 0), -tau_1(0, 0)) == (0, 0)
assert (1, -1) != (0, 0)

# I_tau=(x,y^2): y^2 has zero linear part but is a necessary generator.
assert tau_2(0, 2) - tau_1(0, 2) == 4

print("PASS: B175 free reduced discriminant retains the hidden generator")
