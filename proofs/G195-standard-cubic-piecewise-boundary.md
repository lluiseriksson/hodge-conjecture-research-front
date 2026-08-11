---
brick_id: G195
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n>=14 with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n>=14; m=2; U(14)=97, U(d)=8d-16 for d=16,18,20,22, and U(d)=7d+6 for even d>=24; h_Z(1)=U(d); delta_1=U(d)-d-1; slack s_9(d)=2(U(d)-d-1); N=2U(d)
codimension: B276 excludes the sole standard equality survivor at U(14)=97 and four following standard ranks, so the proposed universal G144 package at U(d) cannot exist
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B276, G013, G090-G148, G172, NG106-NG232, S081-S084
claim: The proposed universal G144 package at U(d) cannot exist: B276 excludes the sole standard rank-97 survivor on the valid Q^14 input.
falsifier: a valid standard G195 package of rank 97 on Q^14, failure of B276, or a different post-G195 boundary
---

# G195 — Standard/cubic piecewise boundary (closed)

B275 raises only the \(d=14\) standard floor:

\[
\begin{array}{c|c|c|c}
 d & U(d) & s_9(d) & \text{polarizations not yet excluded}\\ \hline
 14 & 97 & 164 & A=O_Q(1)\\
 16 & 112 & 190 & A=O_Q(1)\\
 18 & 128 & 218 & A=O_Q(1)\\
 20 & 144 & 246 & A=O_Q(1)\\
 22 & 160 & 274 & A=O_Q(1),O_Q(3),O_Q(4)\\
 d\ge24\text{ even} & 7d+6 & 12d+10 & A=O_Q(3),O_Q(4).
\end{array} \tag{1}
\]

G195 would classify standard equality in dimensions \(14,16,18,20\),
the standard/cubic/quartic tie at \(d=22\), and cubic/quartic equality
in every even dimension at least 24, while retaining every G144
detector clause.

B276 excludes every standard rank from 97 through 101 on \(Q^{14}\).
In particular the sole rank-97 survivor falsifies the universal G195
claim. G195 is NO-GO and passes directly to G196 at rank 102 in the
\(d=14\) row. No ODP package, rational detector, specified pairing,
cycle, proof, or disproof of HC is produced.
