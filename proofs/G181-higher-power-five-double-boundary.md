---
brick_id: G181
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n; m=2; slack s=8d+8=16n+8; N=10d+10=20n+10; h_Z(1)=5d+5=10n+5=N/2
codimension: construct the complete G144 package with delta_1=4d+4 and an isomorphic degree-one relation transport at B254's first higher-power boundary
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B255, G013, G090-G148, G172, NG106-NG213, S081-S083
claim: No universal G144 package exists at m=2, slack s=8d+8, delta_1=4d+4, N=10d+10, and h_Z(1)=5d+5=N/2; B255 excludes the last higher-power branch on every even quadric Q^d with d>=14.
falsifier: one complete G181 package on every valid primitive input, in particular a higher-power equality candidate on one even quadric Q^d with d>=14
---

# G181 — The higher-power five-double boundary

B254 raises the common quadric floor to

\[
 m=2,\qquad s=8d+8,\qquad \delta_1=4d+4,\qquad
 N=10d+10,\qquad h_Z(1)=5d+5=N/2. \tag{1}
\]

On every even quadric of dimension at least fourteen, B253 excludes
\(A=O_Q(1)\) and B254 excludes \(A=O_Q(2)\) at equality. B249 leaves
exactly the powers \(A=O_Q(k)\), \(k\ge3\). Its four-cycle product
proves five double neighborhoods are independent, but does not exclude
equality or construct the full marked configuration.

B255 closes the equality case. For any sixth marked point, the five
supports split into line-through-point classes of size at most three. A
six-edge minimum-degree-two subgraph of the complementary complete
multipartite graph yields a sextic product that vanishes on all five
doubles and is a unit at the sixth point. This contradicts equality for
\(k=3\); for \(k\ge4\), the residual system supplies the entire sixth
double neighborhood. Hence every polarization has

\[
 h_Z(1)\ge5d+6,\qquad s\ge8d+10. \tag{2}
\]

Thus G181 and its adjacent odd layer are NO-GO. The next gate is G182 at
\(s=8d+10\), where only \(A=O_Q(3)\) survives the quadric rank audit.
No ODP package, rational detector, specified pairing, algebraic cycle,
proof, or disproof of HC is produced.
