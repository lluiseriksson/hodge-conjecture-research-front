---
brick_id: G203
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n>=14 with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n>=14; m=2; AB(14)=105, AB(16)=119, AB(d)=8d-16 for d=18,20,22, and AB(d)=7d+7 for even d>=24; h_Z(1)=AB(d); delta_1=AB(d)-d-1; slack s_15(d)=2(AB(d)-d-1); N=2AB(d)
codimension: construct the complete G144 package with delta_1=AB(d)-d-1 and an isomorphic degree-one relation transport at the valid B273/B280/B281/B282 boundary
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B282, G013, G090-G148, G172, NG106-NG239, S081-S085
claim: For every arbitrary primitive target, construct the complete G144 package at h_Z(1)=AB(d), delta_1=AB(d)-d-1, slack s_15(d)=2(AB(d)-d-1), and N=2AB(d), retaining every relation, ODP, Kuranishi, rational-type, and nonzero specified-pairing clause.
falsifier: one primitive target for which no polarization realizes the AB(d) package or a different boundary after the valid closure of G200
---

# G203 — Active all-nonstandard next boundary

B281-B282 raise both cubic and quartic floors to \(7d+7\):

\[
\begin{array}{c|c|c|c}
 d & AB(d) & s_{15}(d) & \text{polarizations not yet excluded}\\ \hline
 14 & 105 & 180 & A=O_Q(2),O_Q(3),O_Q(4),O_Q(k),\ k\ge5\\
 16 & 119 & 204 & A=O_Q(k),\ k\ge1\\
 18 & 128 & 218 & A=O_Q(1)\\
 20 & 144 & 246 & A=O_Q(1)\\
 22 & 160 & 274 & A=O_Q(1)\\
 d\ge24\text{ even} & 7d+7 & 12d+12 &
 A=O_Q(2),O_Q(3),O_Q(4),O_Q(k),\ k\ge5.
\end{array} \tag{1}
\]

G203 must classify the common nonstandard equality rank 105 on
\(Q^{14}\), the all-polarization tie at rank 119 on \(Q^{16}\),
standard equality in dimensions \(18,20,22\), and the common
nonstandard equality \(7d+7\) for every even \(d\ge24\), while
retaining every G144 detector clause. It is EXPLORATORY and active.
Rank survival supplies no ODP package, rational detector, specified
pairing, cycle, proof, or disproof of HC.
