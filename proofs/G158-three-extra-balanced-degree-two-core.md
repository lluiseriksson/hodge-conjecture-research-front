---
brick_id: G158
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n; m=2; slack s=2d+8=4n+8; N=4d+10=8n+10; h_Z(1)=2d+5=4n+5=N/2
codimension: construct the complete G144 package with delta_1=d+4 and an isomorphic degree-one relation transport at the first rank not excluded by B234
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z, 2Z, and mixed double-plus-point schemes, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B234, G013, G090-G148, NG106-NG192, S081-S083
claim: For every arbitrary primitive target (X,zeta) of dimension d=2n, choose a very ample A and construct H=A^2 plus a reduced Z of N=4d+10 points satisfying the complete G144 package with slack s=2d+8, h_Z(1)=2d+5, an isomorphic full-support relation transport, a diagonally self-dual degree-one code, every ODP-profile, holonomy and finite-Kuranishi clause, rational type (0,0), and nonzero specified pairing.
falsifier: one primitive target for which no choice of A realizes the displayed three-extra-dimensional balanced code together with every geometric, rationality, Hodge-type, and pairing obligation
---

# G158 — Construct the three-extra-dimensional balanced core

B234 excludes G157 and its adjacent odd layer. The first remaining
degree-two signature is

\[
 m=2,\qquad s=2d+8,\qquad \delta_1=d+4. \tag{1}
\]

It has

\[
 N=4d+10,\qquad h_Z(1)=2d+5=N/2,\qquad
 s-2\delta_1=0. \tag{2}
\]

The relation transport is an isomorphism and the degree-one evaluation
code is diagonally self-dual.

G158 asks for this code on every primitive target together with the full
ODP, adjacent-profile, holonomy, finite-Kuranishi, rational
type-\((0,0)\), and specified-pairing package. Unlike at G157, B215 at
exponent six only makes two doubles plus three points fill the new span;
it does not exclude cube polarizations. Powers \(A=B^\ell\) with
\(\ell\ge4\) are excluded by the next mixed interpolation bound, so the
quadric audit retains precisely the primitive, square, and cube cases.

This remains only a sufficient specialization of G148. No marked scheme,
detector, pairing, algebraic cycle, proof, or disproof of HC is currently
constructed.
