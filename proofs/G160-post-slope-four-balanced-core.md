---
brick_id: G160
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n; m=2; slack s=4d+2=8n+2; N=6d+4=12n+4; h_Z(1)=3d+2=6n+2=N/2
codimension: construct the complete G144 package with delta_1=2d+1 and an isomorphic degree-one relation transport at the first rank not excluded by B236
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B237, G013, G090-G148, NG106-NG195, S081-S083
claim: For every arbitrary primitive target (X,zeta) of dimension d=2n, choose a very ample A and construct H=A^2 plus a reduced Z of N=6d+4 points satisfying the complete G144 package with slack s=4d+2, h_Z(1)=3d+2, an isomorphic full-support relation transport, a diagonally self-dual degree-one code, every ODP-profile, holonomy and finite-Kuranishi clause, rational type (0,0), and nonzero specified pairing.
falsifier: one primitive target for which no choice of A realizes the post-slope-four balanced code together with every geometric, rationality, Hodge-type, and pairing obligation
---

# G160 — Construct the post-slope-four balanced core

B236 excludes the exact B235 boundary and its adjacent odd layer. The
first remaining degree-two signature is

\[
 m=2,\qquad s=4d+2,\qquad \delta_1=2d+1. \tag{1}
\]

It has

\[
 N=6d+4,\qquad h_Z(1)=3d+2=N/2,\qquad
 s-2\delta_1=0. \tag{2}
\]

The relation transport is an isomorphism and the degree-one code is
diagonally self-dual.

G160 asks for this code on every primitive target together with the full
ODP, adjacent-profile, holonomy, finite-Kuranishi, rational
type-\((0,0)\), and specified-pairing package. On the even-quadric test,
B235 still excludes every nonstandard polarization until slack
\(4d+4\), so only \(O_Q(1)\) remains at this gate.

This remains a sufficient specialization of G148. No marked scheme,
detector, pairing, algebraic cycle, proof, or disproof of HC is currently
constructed.

B237 exhausts the standard-quadric geometry. If a third point meets the
initial hyperbolic plane, the tangential contact locus is one plane conic
of point rank at most five. If every residual point is orthogonal to that
plane, their quotient tangents force pairwise orthogonality and then fail
full tangent absorption.

Thus G160 and the adjacent odd layer \(4d+3\) are **NO-GO**. The next
gate is G161 at \(s=4d+4,\delta_1=2d+2\), where all quadric
polarizations re-enter. G148 and HC remain open.
