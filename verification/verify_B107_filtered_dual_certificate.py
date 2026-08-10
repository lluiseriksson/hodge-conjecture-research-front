"""Finite exact checks for B107, NG083, and G070's filtered criterion."""

from fractions import Fraction


def u(vector):
    x, y, z = vector
    return (x + y, z)


def in_s0(vector):
    return vector[2] == 0


# Full liftability need not imply liftability from the relevant filtration step.
t_bad = (Fraction(1), Fraction(1))
full_lift = (Fraction(1), Fraction(0), Fraction(1))
assert u(full_lift) == t_bad
assert not in_s0(full_lift)
assert all(u((Fraction(k), Fraction(1 - k), Fraction(0))) != t_bad for k in range(-3, 4))

# A functional on S0 has many extensions to S; filtration data chooses none.
def extension(a, vector):
    x, _y, z = vector
    return x + a * z


on_s0 = (Fraction(2), Fraction(5), Fraction(0))
assert extension(0, on_s0) == extension(7, on_s0) == 2
off_s0 = (Fraction(2), Fraction(5), Fraction(1))
assert extension(0, off_s0) != extension(7, off_s0)

# Filtered good class: t=(1,0), u0(x,y,0)=(x+y,0).
t_good = (Fraction(1), Fraction(0))
assert u((Fraction(1), Fraction(0), Fraction(0))) == t_good

# Cokernel branch: F0(x,y,0)=x is nonzero on ker(u0), e.g. (1,-1,0).
kernel_vector = (Fraction(1), Fraction(-1), Fraction(0))
assert u(kernel_vector) == (0, 0)
assert extension(0, kernel_vector) == 1

# Descended branch: F0(x,y,0)=x+y is lambda composed with u0.
def f_descended(vector):
    x, y, z = vector
    assert z == 0
    return x + y


assert f_descended((1, 0, 0)) == f_descended((4, -3, 0)) == 1

print("PASS: B107 filtered-domain certificate and NG083 total-stalk guard")
