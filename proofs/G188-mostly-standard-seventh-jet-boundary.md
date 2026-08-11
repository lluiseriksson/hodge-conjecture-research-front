---
brick_id: G188
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n>=14 with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n>=14; m=2; J(d)=7d-12 except J(20)=126; h_Z(1)=J(d); delta_1=J(d)-d-1; slack s_2(d)=2(J(d)-d-1); N=2J(d)
codimension: construct the complete G144 package with delta_1=J(d)-d-1 and an isomorphic degree-one relation transport at B261's mostly-standard seventh-jet boundary
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B261, G013, G090-G148, G172, NG106-NG219, S081-S083
claim: For every arbitrary primitive target (X,zeta) of even dimension d>=14, choose A and construct the complete G144 package at m=2, h_Z(1)=J(d), delta_1=J(d)-d-1, slack s_2(d)=2(J(d)-d-1), and N=2J(d), retaining the full relation, ODP, Kuranishi, rational-type, and nonzero specified-pairing clauses.
falsifier: one primitive target for which no polarization realizes the mostly-standard piecewise package; on even quadrics B261 leaves k=1 for d=14,16 and every even d>=22, k=1 or 2 for d=18, and k=2 for d=20
---

# G188 — The mostly-standard seventh-jet boundary

B261 reduces the next balanced signature to

\[
 h_Z(1)=J(d),\qquad
 \delta_1=J(d)-d-1,\qquad
 s_2(d)=2(J(d)-d-1),\qquad N=2J(d), \tag{1}
\]

where

\[
\begin{array}{c|c|c|c}
 d & J(d) & s_2(d) & \text{polarizations not yet excluded}\\ \hline
 14,16 & 7d-12 & 12d-26 & A=O_Q(1)\\
 18 & 114 & 190 & A=O_Q(1),O_Q(2)\\
 20 & 126 & 210 & A=O_Q(2)\\
 d\ge22\text{ even} & 7d-12 & 12d-26 & A=O_Q(1).
\end{array} \tag{2}
\]

G188 is the next falsifiable gate: classify the first equality beyond
B259's second standard band, while separately retaining the square
exceptions in dimensions 18 and 20, and then retain every G144
relation, ODP, Kuranishi, rational-type, and nonzero specified-pairing
clause. Rank survival alone would not construct an algebraic cycle or
prove or disprove HC.
