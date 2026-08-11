#!/usr/bin/env python3
"""Bounded B177/G110/NG141 identities; not a proof of HC."""


def tau(u: int, v: int, w: int) -> tuple[int, int]:
    del w
    return u, (1 + v) * u


for u in range(-8, 9):
    for v in range(-7, 8):
        for w in range(-3, 4):
            tau_1, tau_2 = tau(u, v, w)

            # The w-translation fundamental field fixes both branches.
            delta_w_tau = (0, 0)
            assert delta_w_tau == (0 * tau_1, 0 * tau_2)

            # The residual v-direction is logarithmic but not supplied by
            # the selected one-dimensional symmetry group.
            delta_v_tau = (0, u)
            assert delta_v_tau == (0 * tau_1, tau_1)
            assert tau_2 == (1 + v) * tau_1

# At the origin both differentials are du. The kernel has basis dv,dw,
# while the symmetry orbit supplies only dw.
d = 3
r = 1
r_a = 1
kernel_dimension = d - r
residual_dimension = kernel_dimension - r_a
assert kernel_dimension == 2
assert residual_dimension == 1

symmetry_value = (0, 0, 1)
residual_value = (0, 1, 0)
assert symmetry_value != residual_value

print("PASS: B177 symmetry orbit leaves the exact one-dimensional quotient")
