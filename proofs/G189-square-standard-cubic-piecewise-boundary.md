---
brick_id: G189
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n>=14 with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n>=14; m=2; L(d)=6d+6 for d=14,16,18,20, L(22)=158, and L(d)=7d+5 for even d>=24; h_Z(1)=L(d); delta_1=L(d)-d-1; slack s_3(d)=2(L(d)-d-1); N=2L(d)
codimension: construct the complete G144 package with delta_1=L(d)-d-1 and an isomorphic degree-one relation transport at B262's square-standard-cubic piecewise boundary
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B262, G013, G090-G148, G172, NG106-NG220, S081-S083
claim: For every arbitrary primitive target (X,zeta) of even dimension d>=14, choose A and construct the complete G144 package at m=2, h_Z(1)=L(d), delta_1=L(d)-d-1, slack s_3(d)=2(L(d)-d-1), and N=2L(d), retaining the full relation, ODP, Kuranishi, rational-type, and nonzero specified-pairing clauses.
falsifier: one primitive target for which no polarization realizes the piecewise package; on even quadrics B262 leaves k=2 for d=14,16,18,20, k=1 for d=22, and k=3 or 4 for even d>=24
---

# G189 — The square/standard/cubic piecewise boundary

B262 reduces the next balanced signature to

\[
 h_Z(1)=L(d),\qquad
 \delta_1=L(d)-d-1,\qquad
 s_3(d)=2(L(d)-d-1),\qquad N=2L(d), \tag{1}
\]

where

\[
\begin{array}{c|c|c|c}
 d & L(d) & s_3(d) & \text{polarizations not yet excluded}\\ \hline
 14,16,18,20 & 6d+6 & 10d+10 & A=O_Q(2)\\
 22 & 158 & 270 & A=O_Q(1)\\
 d\ge24\text{ even} & 7d+5 & 12d+8 & A=O_Q(3),O_Q(4).
\end{array} \tag{2}
\]

G189 is the next falsifiable gate: classify equality in the square
low-dimensional cases, the single standard dimension 22 case, and the
high-dimensional cubic/quartic cases, then retain every G144 relation,
ODP, Kuranishi, rational-type, and nonzero specified-pairing clause.
Rank survival alone would not construct an algebraic cycle or prove or
disprove HC.
