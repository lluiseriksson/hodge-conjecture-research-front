---
brick_id: G155
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the chosen A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n; m=2; slack s=2d+2=4n+2; N=4d+4=8n+4; h_Z(1)=2d+2=4n+2=N/2
codimension: construct the complete G144 package with delta_1=d+1 and an isomorphic degree-one relation transport at the first even-quadric-compatible degree-two threshold
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B232, G013, G090-G148, NG106-NG190, S081-S083
claim: For every arbitrary primitive target (X,zeta) of dimension d=2n, choose a very ample A and construct H=A^2 plus a reduced Z of N=4d+4 points satisfying the complete G144 package with slack s=2d+2, h_Z(1)=2d+2, full-support relation transport E_1 isomorphic to R_1, a diagonally self-dual degree-one code, every ODP-profile, holonomy and finite-Kuranishi clause, rational type (0,0), and nonzero specified pairing.
falsifier: one primitive target for which no choice of A realizes the displayed dimension-scaled balanced code together with all geometric, rationality, Hodge-type, and pairing obligations
---

# G155 — Construct the dimension-scaled balanced degree-two core

B231 proves that a degree-two universal candidate in dimension \(d=2n\)
must have

\[
 s\ge2d+2. \tag{1}
\]

The smallest signature not excluded by that necessary test takes equality:

\[
 m=2,\qquad s=2d+2=4n+2,\qquad \delta_1=d+1=2n+1. \tag{2}
\]

Since \(D_d(2)=2(d+1)\), its exact ranks are

\[
 N=4d+4=8n+4,\qquad
 h_Z(1)=2d+2=4n+2=N/2. \tag{3}
\]

B222 then gives

\[
 \dim\operatorname{coker}M_{\lambda,1}
   =s-2\delta_1=0,\qquad
 E_1=E_1^{\perp_\lambda}. \tag{4}
\]

Thus G155 asks for the balanced self-dual code at the first
dimension-scaled threshold, not merely its rank table. On the same marked
scheme it requires every remaining G144 clause: the central ODP generator,
adjacent profile, conformal holonomy, finite Kuranishi closure, a full-support
rational type-\((0,0)\) relation, and nonzero specified Saito pairing with
\(\zeta\).

For \(d=4\), equations (2)-(3) recover the numerical signature formerly
called G154. The correction is that its slack must grow with \(d\); fixing
\(s=10\) for all dimensions is falsified by \(Q^6\). G155 is a sufficient
specialization of G148. No marked scheme, detector, pairing, algebraic cycle,
proof, or disproof of the Hodge Conjecture is currently constructed.

B232 tests the threshold itself. On \(Q^d\), if every pair of marked
points is orthogonal, the resulting isotropic span cannot absorb a full
tangent osculator. Otherwise a nonorthogonal pair has disjoint
\((d+1)\)-dimensional tangent osculators. They fill the entire
\((2d+2)\)-dimensional point span, but the symmetric-square decomposition
shows that this span contains no third quadric point. Powered
polarizations are contradicted directly by B215 interpolation on two
double neighborhoods plus a third point.

Thus G155 is **NO-GO**. The same rank persists at odd slack \(2d+3\),
so B232 excludes that layer as well. G156 is the next re-entry gate at
\(s=2d+4,\delta_1=d+2\). G148 and HC remain open.
