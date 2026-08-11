---
brick_id: G166
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n; m=2; slack s=4d+12=8n+12; N=6d+14=12n+14; h_Z(1)=3d+7=6n+7=N/2
codimension: construct the complete G144 package with delta_1=2d+6 and an isomorphic degree-one relation transport at the first balanced signature after G164
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B243, G013, G090-G148, NG106-NG201, S081-S083
claim: For every arbitrary primitive target (X,zeta) of dimension d=2n, choose a very ample A and construct H=A^2 plus a reduced Z of N=6d+14 points satisfying the complete G144 package with slack s=4d+12, h_Z(1)=3d+7, an isomorphic full-support relation transport, a diagonally self-dual degree-one code, every ODP-profile, holonomy and finite-Kuranishi clause, rational type (0,0), and nonzero specified pairing.
falsifier: one primitive target for which no choice of A realizes the four-beyond-three-double balanced code together with every geometric, rationality, Hodge-type, and pairing obligation
---

# G166 — Construct four dimensions beyond three doubles

B241-B242 close G164 and G165 through the valid \(Q^6\) input. The next
balanced signature is

\[
 m=2,\qquad s=4d+12,\qquad \delta_1=2d+6. \tag{1}
\]

It has

\[
 N=6d+14,\qquad h_Z(1)=3d+7=N/2,\qquad
 s-2\delta_1=0. \tag{2}
\]

The relation transport is an isomorphism and the degree-one code is
diagonally self-dual.

G166 asks for this code on every primitive target together with the full
ODP, adjacent-profile, holonomy, finite-Kuranishi, rational
type-\((0,0)\), and specified-pairing package. The surviving
polarizations must be re-audited at this larger rank; B242 does not
exclude the standard \(Q^4\) configuration as a special case.

B243 excludes every polarization on the valid input \(Q^8\): four-double
interpolation removes \(k\ge4\), sextic first-jet separation removes
\(k=3\), residual quartic rank removes \(k=2\), and the standard tangent
quotients remove \(k=1\). Therefore G166 and its adjacent odd layer are
**NO-GO**. Move to G167 at
\(s=4d+14,\delta_1=2d+7,N=6d+16,h_Z(1)=3d+8\).

This closes only a sufficient specialization of G148. No marked scheme,
detector, pairing, algebraic cycle, proof, or disproof of HC is
constructed.
