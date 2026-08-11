---
brick_id: G186
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n>=14 with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n>=14; m=2; F(d)=min(7d-12,6d+6); slack s_*(d)=2(F(d)-d-1)=min(12d-26,10d+10); N=2F(d); h_Z(1)=F(d)=N/2
codimension: construct the complete G144 package with delta_1=F(d)-d-1 and an isomorphic degree-one relation transport at B259's piecewise post-band boundary
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B259, G013, G090-G148, G172, NG106-NG217, S081-S083
claim: For every arbitrary primitive target (X,zeta) of even dimension d>=14, choose A and construct the complete G144 package at m=2, h_Z(1)=F(d)=min(7d-12,6d+6), delta_1=F(d)-d-1, slack s_*(d)=2(F(d)-d-1), and N=2F(d), retaining the full relation, ODP, Kuranishi, rational-type, and nonzero specified-pairing clauses.
falsifier: one primitive target for which no polarization realizes the piecewise boundary package; on even quadrics B259 leaves only A=O_Q(1) for d=14,16, all polarization types at d=18, and only k>=2 for d>=20
---

# G186 — The piecewise post-standard-band boundary

B259 raises the standard quadric floor to \(7d-12\), while B254-B256
give the nonstandard floor \(6d+6\). Define

\[
 F(d)=\min\{7d-12,6d+6\}. \tag{1}
\]

The next balanced degree-two signature is

\[
 h_Z(1)=F(d),\qquad
 \delta_1=F(d)-d-1,\qquad
 s_*(d)=2(F(d)-d-1),\qquad
 N=2F(d). \tag{2}
\]

Equivalently,

\[
\begin{array}{c|c|c|c}
 d & h_Z(1) & s_*(d) & \text{polarizations not yet excluded}\\ \hline
 14,16 & 7d-12 & 12d-26 & A=O_Q(1)\\
 18 & 114 & 190 & A=O_Q(k),\ k\ge1\\
 d\ge20\text{ even} & 6d+6 & 10d+10 & A=O_Q(k),\ k\ge2
\end{array} \tag{3}
\]

G186 is the next falsifiable gate: classify equality in each branch of
(3), then retain every G144 relation, ODP, Kuranishi, rational-type,
and nonzero specified-pairing clause. Rank survival alone would not
construct an algebraic cycle or prove or disprove HC.
