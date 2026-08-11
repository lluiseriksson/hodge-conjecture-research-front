---
brick_id: G161
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n; m=2; slack s=4d+4=8n+4; N=6d+6=12n+6; h_Z(1)=3d+3=6n+3=N/2
codimension: construct the complete G144 package with delta_1=2d+2 and an isomorphic degree-one relation transport at the first rank not excluded by B237
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B238, G013, G090-G148, NG106-NG196, S081-S083
claim: For every arbitrary primitive target (X,zeta) of dimension d=2n, choose a very ample A and construct H=A^2 plus a reduced Z of N=6d+6 points satisfying the complete G144 package with slack s=4d+4, h_Z(1)=3d+3, an isomorphic full-support relation transport, a diagonally self-dual degree-one code, every ODP-profile, holonomy and finite-Kuranishi clause, rational type (0,0), and nonzero specified pairing.
falsifier: one primitive target for which no choice of A realizes the three-double balanced code together with every geometric, rationality, Hodge-type, and pairing obligation
---

# G161 — Construct the three-double balanced core

B237 excludes G160 and its adjacent odd layer. The first remaining
degree-two signature is

\[
 m=2,\qquad s=4d+4,\qquad \delta_1=2d+2. \tag{1}
\]

It has

\[
 N=6d+6,\qquad h_Z(1)=3d+3=N/2,\qquad
 s-2\delta_1=0. \tag{2}
\]

The relation transport is an isomorphism and the degree-one code is
diagonally self-dual.

G161 asks for this code on every primitive target together with the full
ODP, adjacent-profile, holonomy, finite-Kuranishi, rational
type-\((0,0)\), and specified-pairing package. This is the first quadric
threshold at which three independent tangent osculators fit exactly and
the square and higher polarizations are no longer excluded by B235.

G161 remains only a sufficient specialization of G148. No marked scheme,
detector, pairing, algebraic cycle, proof, or disproof of HC is currently
constructed.

B238 exhausts all quadric polarizations. Higher powers separate three
doubles plus a fourth point by B215. Under the square polarization,
products of four hyperplanes give the same separation. Under the standard
polarization, a fourth point outside the plane contact conic contributes
at least \(d-2\) tangent dimensions, while only one is available.

Thus G161 and the adjacent odd layer \(4d+5\) are **NO-GO**. The next
gate is G162 at \(s=4d+6,\delta_1=2d+3\). G148 and HC remain open.
