---
brick_id: G194
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n>=14 with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n>=14; m=2; T(d)=8d-16 for d=14,16,18,20,22 and T(d)=7d+6 for even d>=24; h_Z(1)=T(d); delta_1=T(d)-d-1; slack s_8(d)=2(T(d)-d-1); N=2T(d)
codimension: construct the complete G144 package with delta_1=T(d)-d-1 and an isomorphic degree-one relation transport at the valid B266/B271/B272/B273/B274 standard-cubic piecewise boundary
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B274, G013, G090-G148, G172, NG106-NG230, S081-S084
claim: For every arbitrary primitive target, construct the complete G144 package at h_Z(1)=T(d), delta_1=T(d)-d-1, slack s_8(d)=2(T(d)-d-1), and N=2T(d), retaining every relation, ODP, Kuranishi, rational-type, and nonzero specified-pairing clause.
falsifier: one primitive target for which no polarization realizes the T(d) package or a different boundary after the valid closure of G193
---

# G194 — Active standard/cubic piecewise boundary

B274 raises the \(d=14\) standard floor by one and gives

\[
 h_Z(1)=T(d),\quad
 \delta_1=T(d)-d-1,\quad
 s_8(d)=2(T(d)-d-1),\quad N=2T(d), \tag{1}
\]

where

\[
\begin{array}{c|c|c|c}
 d & T(d) & s_8(d) & \text{polarizations not yet excluded}\\ \hline
 14 & 96 & 162 & A=O_Q(1)\\
 16 & 112 & 190 & A=O_Q(1)\\
 18 & 128 & 218 & A=O_Q(1)\\
 20 & 144 & 246 & A=O_Q(1)\\
 22 & 160 & 274 & A=O_Q(1),O_Q(3),O_Q(4)\\
 d\ge24\text{ even} & 7d+6 & 12d+10 & A=O_Q(3),O_Q(4).
\end{array} \tag{2}
\]

Equivalently, \(T(d)=8d-16\) for \(d=14,16,18,20,22\), and
\(T(d)=7d+6\) for every even \(d\ge24\).

G194 must classify standard equality in dimensions \(14,16,18,20\),
the standard/cubic/quartic tie at \(d=22\), and cubic/quartic equality
in every even dimension at least 24, while retaining every G144
detector clause. It is EXPLORATORY and active. Rank survival supplies
no ODP package, rational detector, specified pairing, cycle, proof, or
disproof of HC.
