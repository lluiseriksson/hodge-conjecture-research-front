---
brick_id: B225
status: PROVED
base_field: C
variety: a smooth projective complex d-fold with an injective H-Gauss map and a hypothetical G149 first-slack configuration
smoothness: X and the marked scheme Z are smooth and reduced; no ODP or incidence configuration is constructed
projectivity: X, the H^2 point configuration, all evaluation systems, and the Gauss map are projective
dimension: dim X=d; first slack excludes m<=4; at m=5, c_d=binom(d+2,2), N=2c_d+2, and dim E_2=dim E_3=c_d+1
codimension: multiplication by a nowhere-zero-on-Z H-section identifies E_2 and E_3, turning their weighted Gale duality into self-association of the H^2 point configuration
coefficient_field: C for sections, diagonal weights, codes, and self-association; Q detector data remain separate
cohomology_theory: coherent restriction to Z, graded section multiplication, and finite-dimensional orthogonal duality
hodge_type: none asserted; self-association over C does not imply rational type (0,0)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B213-B223, G149-G150, S082
claim: A first-slack G149 candidate with injective Gauss must have m>=5. At the first viable degree m=5, N=2c_d+2 and E_2,E_3 both have dimension c_d+1. Multiplication by any H-section nonzero on Z is an isomorphism E_2->E_3; after absorbing its diagonal values into lambda, E_2 is a maximal self-orthogonal code and its N columns in P^c_d form a self-associated configuration.
falsifier: an injective-Gauss first-slack candidate in degree at most four, failure of the m=5 dimensions, a noninjective multiplication by a section nonzero at every marked point, or a non-self-associated resulting degree-two configuration
---

# B225 — The first viable slack degree is self-associated

B222 already excludes \(m=2\). At one-node slack it also excludes the
two remaining low degrees:

- \(m=3\) forces \(h_Z(1)=d+1\), so tangent absorption makes all marked
  tangent spaces equal, contradicting injective Gauss;
- \(m=4\) has complementary split \((2,2)\), hence
  \(2(h_Z(2)-c_d)\le1\), while injective Gauss requires
  \(h_Z(2)-c_d\ge1\).

Thus a G149 candidate must satisfy

\[
m\ge5. \tag{1}
\]

At \(m=5\),

\[
L_d(3)=c_d+1,\qquad
D_d(5)=2c_d+1,\qquad
N=D_d(5)+1=2(c_d+1). \tag{2}
\]

B222-B223 give

\[
\dim E_2=\dim E_3=c_d+1,\qquad
E_3=E_2^{\perp_\lambda}. \tag{3}
\]

Choose \(t\in H^0(X,H)\) nonzero at every point of \(Z\); the forbidden
sections form only finitely many hyperplanes. Coordinatewise
multiplication gives

\[
D_tE_2\subset E_3. \tag{4}
\]

The diagonal \(D_t\) is invertible and the two spaces in (4) have equal
dimension, so equality holds. Substituting into (3), and absorbing the
nonzero values \(t_i\) into the diagonal weights, gives a nondegenerate
diagonal symmetric pairing \(B_{\lambda t}\) with

\[
E_2=E_2^{\perp_{\lambda t}}. \tag{5}
\]

The code has half the coordinate dimension. In the classical matrix
definition audited in S082, (5) says that the \(2c_d+2\) columns of the
degree-two evaluation matrix in \(\mathbf P^{c_d}\) are
self-associated.

B225 constructs no such points. It identifies the exact first possible
projective configuration and supplies no osculator incidence, ODP
profile, rational detector, specified pairing, or cycle.
