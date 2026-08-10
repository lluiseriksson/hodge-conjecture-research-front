"""Exact finite checks for B105 and NG081."""

from fractions import Fraction


def ambient(pair):
    """The compatible primitive ambient realization Q^2 -> Q."""
    return pair[0]


def pairing(value):
    """A rational detector functional on the ambient target."""
    return value


b_zeta = Fraction(5)

# Nonzero bordism coset in the kernel of ambient realization.
omega_kernel = (Fraction(0), Fraction(7))
assert omega_kernel != (0, 0)
d_kernel = pairing(ambient(omega_kernel))
assert d_kernel == 0
assert b_zeta - d_kernel != 0  # the Saito relation still detects

# A discrepancy equal to b_zeta is exactly the nondetecting case.
omega_nondetecting = (b_zeta, Fraction(0))
d_nondetecting = pairing(ambient(omega_nondetecting))
assert d_nondetecting == b_zeta
assert b_zeta - d_nondetecting == 0

# A general nonzero discrepancy can still detect when it differs from b_zeta.
omega_detecting = (Fraction(2), Fraction(3))
d_detecting = pairing(ambient(omega_detecting))
assert d_detecting != b_zeta
assert b_zeta - d_detecting == 3

print("PASS: B105 exact scalar discrepancy and NG081 kernel countermodel")
