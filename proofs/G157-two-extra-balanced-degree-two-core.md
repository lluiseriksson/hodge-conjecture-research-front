---
brick_id: G157
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n; m=2; slack s=2d+6=4n+6; N=4d+8=8n+8; h_Z(1)=2d+4=4n+4=N/2
codimension: construct the complete G144 package with delta_1=d+3 and an isomorphic degree-one relation transport at the first rank not excluded by B233
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z, 2Z, and mixed double-plus-point schemes, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B234, G013, G090-G148, NG106-NG192, S081-S083
claim: For every arbitrary primitive target (X,zeta) of dimension d=2n, choose a very ample A and construct H=A^2 plus a reduced Z of N=4d+8 points satisfying the complete G144 package with slack s=2d+6, h_Z(1)=2d+4, an isomorphic full-support relation transport, a diagonally self-dual degree-one code, every ODP-profile, holonomy and finite-Kuranishi clause, rational type (0,0), and nonzero specified pairing.
falsifier: one primitive target for which no choice of A realizes the displayed two-extra-dimensional balanced code together with every geometric, rationality, Hodge-type, and pairing obligation
---

# G157 — Construct the two-extra-dimensional balanced core

B233 excludes G156 and its adjacent odd slack. The first remaining
degree-two signature is

\[
 m=2,\qquad s=2d+6,\qquad \delta_1=d+3. \tag{1}
\]

It has

\[
 N=4d+8,\qquad h_Z(1)=2d+4=N/2,\qquad
 s-2\delta_1=0. \tag{2}
\]

The relation transport is therefore an isomorphism and the degree-one
evaluation code is diagonally self-dual.

G157 asks for this code on every primitive target together with the
central ODP generator, adjacent profile, conformal holonomy, finite
Kuranishi closure, rational type-\((0,0)\) relation, and specified
nonzero pairing. B233 excludes polarizations \(A=B^\ell\) with
\(\ell\ge3\) at this threshold; primitive and square polarizations
remain to be tested.

This is a sufficient specialization of G148. No marked scheme, detector,
pairing, algebraic cycle, proof, or disproof of the Hodge Conjecture is
currently constructed.

B234 tests this rank on \(Q^d\). The standard polarization still has
third-tangent quotient rank at least \(d-1>2\). Under \(O_Q(2)\), any
fifth dependent point lies on a line containing three of four base
points; all marked points are therefore contained in that line plus at
most one point and have rank at most six. The higher powers are excluded
in this band by B233.

Thus G157 and the adjacent odd layer \(2d+7\) are **NO-GO**. The next
gate is G158 at \(s=2d+8,\delta_1=d+4\). G148 and HC remain open.
