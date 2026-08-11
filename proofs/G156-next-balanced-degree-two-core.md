---
brick_id: G156
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n; m=2; slack s=2d+4=4n+4; N=4d+6=8n+6; h_Z(1)=2d+3=4n+3=N/2
codimension: construct the complete G144 package with delta_1=d+2 and an isomorphic degree-one relation transport at the first rank not excluded by B232
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z, 2Z, and mixed double-plus-point schemes, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B233, G013, G090-G148, NG106-NG191, S081-S083
claim: For every arbitrary primitive target (X,zeta) of dimension d=2n, choose a very ample A and construct H=A^2 plus a reduced Z of N=4d+6 points satisfying the complete G144 package with slack s=2d+4, h_Z(1)=2d+3, an isomorphic full-support relation transport, a diagonally self-dual degree-one code, every ODP-profile, holonomy and finite-Kuranishi clause, rational type (0,0), and nonzero specified pairing.
falsifier: one primitive target for which no choice of A realizes the displayed next-threshold balanced code together with every geometric, rationality, Hodge-type, and pairing obligation
---

# G156 — Construct the next balanced degree-two core

B232 excludes the B231 boundary and the adjacent odd slack. The first
remaining degree-two rank is

\[
 m=2,\qquad s=2d+4,\qquad \delta_1=d+2. \tag{1}
\]

Its exact dimensions are

\[
 N=4d+6,\qquad h_Z(1)=2d+3=N/2,\qquad
 s-2\delta_1=0. \tag{2}
\]

Therefore the full-support degree-two relation again makes
\(M_{\lambda,1}\) an isomorphism and
\(E_1=E_1^{\perp_\lambda}\).

G156 asks for existence of this next balanced point code on every fixed
primitive target, jointly with the central ODP generator, adjacent
profile, holonomy, finite Kuranishi closure, rational type-\((0,0)\)
relation, and specified nonzero pairing. B232 also shows that a
polarization \(A=B^\ell\), \(\ell\ge3\), cannot realize the threshold;
square or primitive exceptional polarizations remain to be tested.

This is a sufficient specialization of G148, not a consequence of the
rank table. No marked scheme, detector, pairing, algebraic cycle, proof,
or disproof of the Hodge Conjecture is currently constructed.

B233 tests the one-extra-dimensional span on \(Q^d\). For \(A=O_Q(1)\),
a third full tangent osculator has quotient rank at least \(d-1\), not
one. For \(A=O_Q(2)\), ambient quartics separate two doubles plus a
third point unless a fourth point lies on their common line; applying
this to every marked point collapses the rank to at most five. B215
excludes every \(O_Q(k)\), \(k\ge3\).

Thus G156 and the adjacent odd slack \(2d+5\) are **NO-GO**. The next
gate is G157 at \(s=2d+6,\delta_1=d+3\). G148 and HC remain open.
