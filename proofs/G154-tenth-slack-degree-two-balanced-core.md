---
brick_id: G154
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex 2n-fold X with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have the prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the chosen A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=2n; m=2; slack s=10; N=4n+12; h_Z(1)=2n+6; the degree-one code is half-dimensional
codimension: construct the complete G144 package with delta_1=5 and an isomorphic degree-one relation transport, without requiring a pairwise bitangent clique
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B231, G013, G090-G148, NG106-NG189, S081-S083
claim: For every arbitrary primitive target (X,zeta), choose a very ample A and construct H=A^2, m=2, and a reduced Z of N=4n+12 points satisfying the complete G144 package with h_Z(1)=2n+6, full-support relation transport E_1 isomorphic to R_1, a diagonally self-dual degree-one code, every ODP-profile, holonomy and finite-Kuranishi clause, rational type (0,0), and nonzero specified pairing.
falsifier: one primitive target for which no choice of A realizes the displayed tenth-slack balanced code together with all geometric, rationality, Hodge-type, and pairing obligations
---

# G154 — Construct the tenth-slack balanced degree-two core

B230/NG188 show that no degree can realize a universal slack layer
\(s\le9\). At \(s=10\), the \(m=2\) budget is

\[
 N=2(2n+1)+10=4n+12,\qquad
 h_Z(1)=2n+1+\delta_1,\qquad 2\delta_1\le10. \tag{1}
\]

On the four-quadric test, every \(\delta_1\le4\) still forces pairwise
double-jet defect and is excluded by B230's argument. The first
signature not excluded is therefore

\[
 \delta_1=5,\qquad h_Z(1)=2n+6=N/2. \tag{2}
\]

B222 makes \(M_{\lambda,1}:E_1\to\mathcal R_1\) an isomorphism. The
degree-two relation gives

\[
 E_1=E_1^{\perp_\lambda}. \tag{3}
\]

Unlike G153, the span in the \(Q^4\) test has dimension ten, so two full
tangent jet spaces may be independent; no bitangent clique is forced.
G154 asks for this first quadric-surviving balanced code together with
every central ODP, profile, holonomy, finite Kuranishi, rational
type-\((0,0)\), and specified-pairing clause.

This reasoning only tests \(Q^4\). G154 quantifies over every even
dimension. B231 applies the same rank budget to the valid input
\((Q^6,a-b)\). Here a double neighborhood has length seven, whereas

\[
 h_Z(1)=6+6=12<14. \tag{4}
\]

Every marked pair must therefore be double-jet defective. Powered
polarizations are excluded by B215. For \(A=O_Q(1)\), B229 makes every
chord bitangent, so the marked representatives span a totally isotropic
\(W\). Their \(O_Q(2)\) point span lies in
\(\operatorname{Sym}^2W\), but the full tangent osculator contains
\(v\mathbin{\odot}u\) for \(u\in v^\perp\setminus W\). This contradicts
G144 tangent absorption.

Thus G154 is **NO-GO**. Its error was promoting the first signature that
survives the four-dimensional quadric to a dimension-independent universal
signature. B231/NG189 show that every fixed finite slack bound fails in high
enough even dimension. G155 was the first dimension-scaled re-entry, but
B232 subsequently excludes it and the adjacent odd layer. The active gate
is G156 at \(s=2d+4\). G148 and the Hodge Conjecture remain open.
