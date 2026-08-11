---
brick_id: G193
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n>=14 with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n>=14; m=2; R(14)=95, R(d)=8d-16 for d=16,18,20,22, and R(d)=7d+6 for even d>=24; h_Z(1)=R(d); delta_1=R(d)-d-1; slack s_7(d)=2(R(d)-d-1); N=2R(d)
codimension: B274 excludes the sole standard equality survivor at R(14)=95, so the proposed universal G144 package at R(d) cannot exist
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B274, G013, G090-G148, G172, NG106-NG230, S081-S084
claim: The proposed universal G144 package at R(d) cannot exist: B274 excludes the sole standard rank-95 survivor on the valid Q^14 input.
falsifier: a valid standard G193 package of rank 95 on Q^14, failure of B274, or a different post-G193 boundary
---

# G193 — Standard/cubic piecewise boundary (closed)

B273 excludes the last square equality at G192. Combining the valid
polarization floors gives

\[
 h_Z(1)=R(d),\quad
 \delta_1=R(d)-d-1,\quad
 s_7(d)=2(R(d)-d-1),\quad N=2R(d), \tag{1}
\]

where

\[
\begin{array}{c|c|c|c}
 d & R(d) & s_7(d) & \text{polarizations not yet excluded}\\ \hline
 14 & 95 & 160 & A=O_Q(1)\\
 16 & 112 & 190 & A=O_Q(1)\\
 18 & 128 & 218 & A=O_Q(1)\\
 20 & 144 & 246 & A=O_Q(1)\\
 22 & 160 & 274 & A=O_Q(1),O_Q(3),O_Q(4)\\
 d\ge24\text{ even} & 7d+6 & 12d+10 & A=O_Q(3),O_Q(4).
\end{array} \tag{2}
\]

The \(d=14\) standard floor is B263's \(8d-17\); B266 raises it to
\(8d-16\) for every even \(d\ge16\). B271-B272 give the cubic/quartic
floor \(7d+6\) in even dimensions at least 22, and B273 raises the
square floor to \(7d+7\).

G193 would classify standard equality in dimensions \(14,16,18,20\),
the standard/cubic/quartic tie at \(d=22\), and cubic/quartic equality
in every even dimension at least 24, while retaining every G144
detector clause.

B274 excludes the \(d=14\) standard equality: its only residual branch
would be a rank-65 standard configuration on \(Q^{12}\), and the
dimension-12 specialization of B257 excludes that equality. One valid
quadric input therefore falsifies the universal G193 claim. G193 is
NO-GO and passes to G194; no ODP package, rational detector, specified
pairing, cycle, proof, or disproof of HC is produced.
