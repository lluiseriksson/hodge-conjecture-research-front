---
brick_id: G200
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n>=14 with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n>=14; m=2; AA(14)=104, AA(16)=118, AA(d)=8d-16 for d=18,20,22, and AA(d)=7d+6 for even d>=24; h_Z(1)=AA(d); delta_1=AA(d)-d-1; slack s_14(d)=2(AA(d)-d-1); N=2AA(d)
codimension: construct the complete G144 package with delta_1=AA(d)-d-1 and an isomorphic degree-one relation transport at the valid B273/B277/B278/B280/B281 piecewise boundary; B281 removes the quartic branch
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B281, G013, G090-G148, G172, G201-G202, NG106-NG238, S081-S085
claim: For every arbitrary primitive target, construct the complete G144 package at h_Z(1)=AA(d), delta_1=AA(d)-d-1, slack s_14(d)=2(AA(d)-d-1), and N=2AA(d), retaining every relation, ODP, Kuranishi, rational-type, and nonzero specified-pairing clause.
falsifier: one primitive target for which no polarization realizes the AA(d) package or a different boundary after the valid closure of G199
---

# G200 — Active cubic two-row boundary

B280 raises the \(d=16\) standard floor through the cubic boundary:

\[
\begin{array}{c|c|c|c}
 d & AA(d) & s_{14}(d) & \text{polarizations not yet excluded}\\ \hline
 14 & 104 & 178 & A=O_Q(3)\\
 16 & 118 & 202 & A=O_Q(3)\\
 18 & 128 & 218 & A=O_Q(1)\\
 20 & 144 & 246 & A=O_Q(1)\\
 22 & 160 & 274 & A=O_Q(1),O_Q(3)\\
 d\ge24\text{ even} & 7d+6 & 12d+10 & A=O_Q(3).
\end{array} \tag{1}
\]

G200 must classify cubic equality at rank 104 on \(Q^{14}\), cubic
equality at rank 118 on \(Q^{16}\), standard equality in dimensions
\(18,20\), the standard/cubic tie at \(d=22\), and cubic equality in
every even dimension at least 24, while retaining every G144 detector
clause. B281 removes the quartic survivor in every row. G200 remains
EXPLORATORY and active. Rank survival supplies no ODP package, rational
detector, specified pairing, cycle, proof, or disproof of HC.
