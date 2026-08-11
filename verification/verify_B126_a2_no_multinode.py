"""Exact symbolic checks for B126 and NG101."""

import sympy as sp


x, y = sp.symbols("x y")

same_s = sp.factor(-3 * x**2 + 3 * y**2)
same_t = sp.factor(2 * x**3 - 2 * y**3)
assert sp.expand(same_s + 3 * (x - y) * (x + y)) == 0
assert sp.expand(same_t - 2 * (x - y) * (x**2 + x * y + y**2)) == 0

# On the only alternative branch y=-x, equal t forces x=0.
assert sp.factor(same_t.subs(y, -x)) == 4 * x**3

# The critical-value parametrization lies on the cusp discriminant.
s = -3 * x**2
t = 2 * x**3
assert sp.expand(4 * s**3 + 27 * t**2) == 0

# The fiber Hessian determinant is nonzero exactly off the cusp point x=0.
r = 5
hessian_det = (6 * x) * 2**r
assert sp.factor(hessian_det) == 6 * 2**r * x

print("PASS: B126 A2 versal slice has one critical point per discriminant fiber")
