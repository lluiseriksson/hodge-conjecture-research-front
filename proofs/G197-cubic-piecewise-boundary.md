---
brick_id: G197
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n>=14 with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n>=14; m=2; W(14)=103, W(d)=8d-16 for d=16,18,20,22, and W(d)=7d+6 for even d>=24; h_Z(1)=W(d); delta_1=W(d)-d-1; slack s_11(d)=2(W(d)-d-1); N=2W(d)
codimension: construct the complete G144 package with delta_1=W(d)-d-1 and an isomorphic degree-one relation transport at the valid B266/B271/B272/B273/B277 cubic piecewise boundary
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B277, G013, G090-G148, G172, NG106-NG233, S081-S084
claim: For every arbitrary primitive target, construct the complete G144 package at h_Z(1)=W(d), delta_1=W(d)-d-1, slack s_11(d)=2(W(d)-d-1), and N=2W(d), retaining every relation, ODP, Kuranishi, rational-type, and nonzero specified-pairing clause.
falsifier: one primitive target for which no polarization realizes the W(d) package or a different boundary after the valid closure of G196
---

# G197 — Active cubic piecewise boundary

B277 removes standard equality from the \(d=14\) row:

\[
\begin{array}{c|c|c|c}
 d & W(d) & s_{11}(d) & \text{polarizations not yet excluded}\\ \hline
 14 & 103 & 176 & A=O_Q(3),O_Q(4)\\
 16 & 112 & 190 & A=O_Q(1)\\
 18 & 128 & 218 & A=O_Q(1)\\
 20 & 144 & 246 & A=O_Q(1)\\
 22 & 160 & 274 & A=O_Q(1),O_Q(3),O_Q(4)\\
 d\ge24\text{ even} & 7d+6 & 12d+10 & A=O_Q(3),O_Q(4).
\end{array} \tag{1}
\]

G197 must classify cubic/quartic equality at rank 103 on \(Q^{14}\),
standard equality in dimensions \(16,18,20\), the
standard/cubic/quartic tie at \(d=22\), and cubic/quartic equality in
every even dimension at least 24, while retaining every G144 detector
clause. It is EXPLORATORY and active. Rank survival supplies no ODP
package, rational detector, specified pairing, cycle, proof, or
disproof of HC.
