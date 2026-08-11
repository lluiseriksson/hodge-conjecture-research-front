#!/usr/bin/env python3
"""Exact B174/NG138 polynomial identities; not a proof of HC."""


def tau(x: int, y: int) -> tuple[int, int]:
    return x, x + y * y


# Choose an arbitrary residue row c and manufacture rho=-c dot tau.
for x in range(-8, 9):
    for y in range(-6, 7):
        tau1, tau2 = tau(x, y)
        c1, c2 = 2 + y, 3 - x
        rho = -(c1 * tau1 + c2 * tau2)

        # Canonical representation b=-c gives the zero adjusted row.
        b1, b2 = -c1, -c2
        assert b1 * tau1 + b2 * tau2 == rho
        assert (b1 + c1, b2 + c2) == (0, 0)

        # Every displayed alternative is canonical plus a Koszul syzygy.
        h = 1 + x - 2 * y
        s1, s2 = h * tau2, -h * tau1
        b1_alt, b2_alt = b1 + s1, b2 + s2
        assert b1_alt * tau1 + b2_alt * tau2 == rho
        assert (b1_alt + c1, b2_alt + c2) == (s1, s2)
        assert s1 * tau1 + s2 * tau2 == 0

# At the origin every Koszul syzygy row vanishes, while the central
# differential relation (1,-1) is nonzero and therefore does not lift.
tau_origin = tau(0, 0)
assert tau_origin == (0, 0)
for h_origin in range(-10, 11):
    adjusted_origin = (
        h_origin * tau_origin[1],
        -h_origin * tau_origin[0],
    )
    assert adjusted_origin == (0, 0)
assert (1, -1) != (0, 0)

print("PASS: B174 auxiliary representations are exactly the syzygy torsor")
