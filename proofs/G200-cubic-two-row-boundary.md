---
brick_id: G200
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n>=14 with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n>=14; m=2; AA(14)=104, AA(16)=118, AA(d)=8d-16 for d=18,20,22, and AA(d)=7d+6 for even d>=24; h_Z(1)=AA(d); delta_1=AA(d)-d-1; slack s_14(d)=2(AA(d)-d-1); N=2AA(d)
codimension: B281-B282 exclude the quartic and cubic survivors on the valid Q^14 input, so the proposed universal G144 package at AA(d) cannot exist
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B282, G013, G090-G148, G172, G201-G203, NG106-NG239, S081-S085
claim: The proposed universal G144 package at AA(d) cannot exist: B281-B282 exclude the quartic and cubic rank-104 survivors on the valid Q^14 input.
falsifier: a valid cubic or quartic G200 package of rank 104 on Q^14, failure of B281 or B282, or a different post-G200 boundary
---

# G200 — Cubic two-row boundary (closed)

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

G200 would classify cubic equality at rank 104 on \(Q^{14}\), cubic
equality at rank 118 on \(Q^{16}\), standard equality in dimensions
\(18,20\), the standard/cubic tie at \(d=22\), and cubic equality in
every even dimension at least 24, while retaining every G144 detector
clause. B281 removes the quartic survivor in every row, and B282 removes
the cubic survivor. Thus G200 is NO-GO and passes to G203. No ODP
package, rational detector, specified pairing, cycle, proof, or
disproof of HC is produced.
