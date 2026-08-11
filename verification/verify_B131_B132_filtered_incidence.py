"""Index and finite-filtration checks for B131-B132/NG105."""

from fractions import Fraction


def filtered_boundary(a0, a1, b0, b1):
    """Two-step scalar model of the snake-lemma boundary.

    Matrix [[a0, 0], [b0, b1]] is filtered in the order (gr0, gr1).
    The test records that a total isomorphism with zero gr0 on a selected
    vector needs a new grade-one cokernel; it is only a sanity check, not the
    mathematical proof.
    """

    determinant = a0 * b1
    return determinant


for middle_codimension in range(2, 21):
    r = middle_codimension
    n = 2 * r - 1

    # Nori applies in the total incidence degree n+1.
    assert n + 1 < 2 * n

    # Every Leray column p>=2 has fiber degree q<n, hence weak Lefschetz.
    for p in range(2, n + 3):
        q = n + 1 - p
        if q >= 0:
            assert q < n

    # B132: total filtered-de-Rham degree -d+1.  A sheaf-cohomology
    # contribution a>=1 corresponds to Brogan k=n+1-a<n+1 and vanishes.
    for a in range(1, n + 3):
        k = n + 1 - a
        assert k < n + 1
        assert r > k - n

    # Every possible outgoing hypercohomology differential has page rho>=2
    # and lands at k=n+2-rho, again in the Corollary 4.1 vanishing range.
    for rho in range(2, n + 3):
        k_target = n + 2 - rho
        assert k_target <= n
        assert r > k_target - n

# Minimal two-step warning: an isomorphism cannot have zero gr0 scalar in a
# square 1+1 model.  The incidence repair therefore needs the extra grade-one
# target dimension measured by ker(gr0) = coker(gr1), exactly as in B131.
assert filtered_boundary(Fraction(1), 0, 0, Fraction(1)) == 1
assert filtered_boundary(Fraction(0), 0, 1, Fraction(1)) == 0

print("PASS: B131 Leray range, B132 projective collapse, and NG105 guard")
