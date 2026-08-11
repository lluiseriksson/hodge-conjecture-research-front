---
brick_id: B175
status: PROVED
base_field: C
variety: a smooth two-parameter analytic germ carrying two tracked ordinary-double-point critical-value branches; the exact local model is tau=(x,x+y^2)
smoothness: the parameter germ is smooth and both reduced discriminant branches are smooth; the two branches are tangent at the origin
projectivity: the theorem is local analytic; its finite ODP jets are realizable on sufficiently ample projective linear slices, but no full-complete-linear-system assertion is made
dimension: parameter dimension 2; N=2 tracked branches; central differential rank R=1
codimension: the reduced union is a hypersurface, while the simultaneous-node ideal has height 2, two minimal generators, and one-dimensional hidden-generator space
coefficient_field: C for logarithmic derivations and analytic local algebra; Q only in the downstream Hodge application
cohomology_theory: logarithmic vector fields, convergent analytic local rings, syzygy modules, and local ordinary-double-point deformation theory
hodge_type: none asserted; rational type (0,0) and the specified nonzero Saito pairing remain separate downstream obligations
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used; no algebraic cycle or detector is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B156-B157, B174, G100, S065, S071, Saito's criterion
claim: Freeness of the reduced total discriminant, even with an explicit Saito basis whose derivations preserve every labelled branch separately, does not force H_tau=0 or lift the central critical-value relations. The reduced divisor forgets the scheme-theoretic simultaneous intersection ideal.
falsifier: a failure of the displayed logarithmic identities or Saito determinant, reducibility or nonreducedness of F=x(x+y^2), or an analytic syzygy of tau whose value at the origin is (1,-1)
---

# B175 — A free reduced discriminant can retain a hidden generator

Let

\[
 \tau_1=x,\qquad \tau_2=x+y^2
\]

in \(\mathcal O=\mathbf C\{x,y\}\), and let the reduced total
discriminant be

\[
 D=V(F),\qquad F=\tau_1\tau_2=x(x+y^2).
\]

The factors \(x\) and \(x+y^2\) are distinct smooth prime germs, so
\(F\) is reduced. Consider the weighted Euler and Hamiltonian vector
fields

\[
 \delta_E=2x\partial_x+y\partial_y,
 \qquad
 \delta_H=2xy\partial_x-(2x+y^2)\partial_y.
\]

They are logarithmic along \(D\), since

\[
 \delta_E(F)=4F,
 \qquad
 \delta_H(F)=0.
\]

Their coefficient matrix relative to \((\partial_x,\partial_y)\) is

\[
 A=
 \begin{pmatrix}
 2x & 2xy\\
 y & -(2x+y^2)
 \end{pmatrix},
 \qquad
 \det A=-4x(x+y^2)=-4F.
\]

Because \(-4\) is a unit, Saito's criterion proves that \(D\) is a free
divisor and that \(\delta_E,\delta_H\) form a basis of
\(\operatorname{Der}(-\log D)\).

This basis does more than preserve the union. It preserves each labelled
branch separately:

\[
 \begin{array}{c|cc}
  &\tau_1&\tau_2\\ \hline
 \delta_E&2\tau_1&2\tau_2\\
 \delta_H&2y\tau_1&-2y\tau_2.
 \end{array} \tag{1}
\]

Thus neither total-divisor freeness nor branchwise logarithmicity is the
missing G100 certificate.

## The simultaneous scheme still has a hidden generator

The simultaneous-node ideal is

\[
 I_\tau=(x,x+y^2)=(x,y^2).
\]

It has height two and two minimal generators, while
\(\operatorname{rank}d\tau_0=1\). B156 therefore gives

\[
 \dim_{\mathbf C}H_\tau=\mu(I_\tau)-1=1,
\]

represented by the class of \(y^2\). Equivalently, the central relation
\((1,-1)\) does not lift. Since \(x,x+y^2\) is a regular sequence, every
analytic syzygy is a multiple of

\[
 (x+y^2,-x),
\]

and hence evaluates to zero at the origin.

The reduced union \(D\) records the two branch supports and their tangent
contact, but not the nonreduced simultaneous scheme
\(V(x,y^2)\). Logarithmic derivations of \(F\) therefore cannot by
themselves determine the minimal number of generators of \(I_\tau\) or
the surjectivity of syzygy evaluation.

## ODP and projective scope guard

The pair is an exact analytic critical-value model for two disjoint Morse
charts: take one local quadratic form with value \(x\), and a second
nondegenerate quadratic form with an affine-linear \(y\)-term chosen so
that its critical value is \(x+y^2\). B157 supplies the corresponding
projective finite-jet realization mechanism after sufficient twisting.
This does not assert that the model is a rank-deficient germ of the full
complete linear system. Consequently B175 blocks a formal implication
from free-divisor theory to G100; it does not exclude a stronger theorem
using global full-system incidence geometry.
