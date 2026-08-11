---
brick_id: G169
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n; m=2; slack s=6d+2=12n+2; N=8d+4=16n+4; h_Z(1)=4d+2=8n+2=N/2
codimension: construct the complete G144 package with delta_1=3d+1 and an isomorphic degree-one relation transport one dimension beyond the slope-six boundary
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B246, G013, G090-G148, NG106-NG204, S081-S083
claim: For every arbitrary primitive target (X,zeta) of dimension d=2n, choose a very ample A and construct H=A^2 plus a reduced Z of N=8d+4 points satisfying the complete G144 package with slack s=6d+2, h_Z(1)=4d+2, an isomorphic full-support relation transport, a diagonally self-dual degree-one code, every ODP-profile, holonomy and finite-Kuranishi clause, rational type (0,0), and nonzero specified pairing.
falsifier: one primitive target for which no choice of A realizes the one-beyond-slope-six balanced code together with every geometric, rationality, Hodge-type, and pairing obligation
---

# G169 — Construct one dimension beyond slope six

B245 closes the slope-six boundary and its adjacent odd layer on every
even quadric of dimension at least eight. The next balanced signature is

\[
 m=2,\qquad s=6d+2,\qquad \delta_1=3d+1, \tag{1}
\]

with

\[
 N=8d+4,\qquad h_Z(1)=4d+2=N/2,\qquad
 s-2\delta_1=0. \tag{2}
\]

B244 still excludes every nonstandard quadric polarization at this
rank, so the standard polarization is the first necessary test. Every
ODP, Kuranishi, rational-type, and specified-pairing clause remains
separate.

B246 proves that every standard-polarized quadric candidate has
\(h_Z(1)\ge5d-3\). Together with B244's nonstandard floor, every
polarization requires \(s\ge6d+6\). Thus G169 and all four layers
\(6d+2,\ldots,6d+5\) are **NO-GO**. Move to G170 at
\(s=6d+6,\delta_1=3d+3,N=8d+8,h_Z(1)=4d+4\).

This closes only a sufficient specialization of G148. No marked scheme,
ODP package, rational detector, specified pairing, algebraic cycle,
proof, or disproof of HC is constructed.
