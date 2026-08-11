"""Exact checks for B135's residue-cokernel criterion."""

from fractions import Fraction as F

from sympy import Matrix, Rational


def q(x: int | F) -> Rational:
    if isinstance(x, F):
        return Rational(x.numerator, x.denominator)
    return Rational(x)


def assert_duality(delta: Matrix, polarization: Matrix) -> None:
    """Check im(Delta*)=(ker Delta)^perp and the dimension identity."""
    delta_star = delta.T * polarization
    relations = delta.nullspace()
    assert delta.cols - delta.rank() == len(relations)
    assert delta_star.rank() == delta.rank()
    assert delta.cols - delta_star.rank() == len(relations)

    for b in relations:
        assert (b.T * delta_star).is_zero_matrix

    # The annihilator of ker(Delta) has the same dimension as im(Delta*).
    relation_matrix = Matrix.hstack(*relations) if relations else Matrix.zeros(delta.cols, 0)
    annihilator_dimension = delta.cols - relation_matrix.rank()
    assert annihilator_dimension == delta_star.rank()


# A nondegenerate alternating polarization, appropriate to odd middle homology.
J = Matrix(
    [
        [0, 1, 0, 0],
        [-1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, -1, 0],
    ]
)

# Independent, proportional, and multipart-dependent cycle systems.
assert_duality(Matrix([[1, 0], [0, 1], [0, 0], [0, 0]]), J)
assert_duality(Matrix([[1, 3], [0, 0], [0, 0], [0, 0]]), J)
assert_duality(
    Matrix([[1, 0, 1, 2], [0, 1, 1, -1], [0, 0, 0, 0], [0, 0, 0, 0]]),
    J,
)

# Two proportional branches: delta_2=c delta_1.
c = q(F(3, 2))
delta = Matrix([[1, c], [0, 0], [0, 0], [0, 0]])
delta_star = delta.T * J
relation = Matrix([c, -1])
assert delta * relation == Matrix.zeros(4, 1)
assert (relation.T * delta_star).is_zero_matrix

# Lift changes add Delta*(v), and c*a_1-a_2 is invariant.
a = Matrix([q(5), q(-2)])
v = Matrix([q(0), q(7), q(0), q(0)])
shifted = a + delta_star * v
rho = (relation.T * a)[0]
rho_shifted = (relation.T * shifted)[0]
assert rho == rho_shifted
assert rho == c * a[0] - a[1]
assert rho != 0

# NG108 countermodel: nonzero individual residues can be a coboundary.
v_boundary = Matrix([q(0), q(4), q(0), q(0)])
boundary = delta_star * v_boundary
assert boundary[0] != 0 and boundary[1] != 0
assert (relation.T * boundary)[0] == 0

print("PASS: B135 residue cokernel, lift invariance, and two-branch mismatch")
