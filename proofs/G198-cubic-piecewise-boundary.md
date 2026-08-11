---
brick_id: G198
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n>=14 with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n>=14; m=2; Y(14)=104, Y(d)=8d-16 for d=16,18,20,22, and Y(d)=7d+6 for even d>=24; h_Z(1)=Y(d); delta_1=Y(d)-d-1; slack s_12(d)=2(Y(d)-d-1); N=2Y(d)
codimension: B279 excludes the sole standard equality survivor at Y(16)=112, so the proposed universal G144 package at Y(d) cannot exist
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B279, G013, G090-G148, G172, NG106-NG235, S081-S084
claim: The proposed universal G144 package at Y(d) cannot exist: B279 excludes the sole standard rank-112 survivor on the valid Q^16 input.
falsifier: a valid standard G198 package of rank 112 on Q^16, failure of B279, or a different post-G198 boundary
---

# G198 — Cubic piecewise boundary (closed)

B278 raises the \(d=14\) cubic/quartic floor by one:

\[
\begin{array}{c|c|c|c}
 d & Y(d) & s_{12}(d) & \text{polarizations not yet excluded}\\ \hline
 14 & 104 & 178 & A=O_Q(3),O_Q(4)\\
 16 & 112 & 190 & A=O_Q(1)\\
 18 & 128 & 218 & A=O_Q(1)\\
 20 & 144 & 246 & A=O_Q(1)\\
 22 & 160 & 274 & A=O_Q(1),O_Q(3),O_Q(4)\\
 d\ge24\text{ even} & 7d+6 & 12d+10 & A=O_Q(3),O_Q(4).
\end{array} \tag{1}
\]

G198 would classify cubic/quartic equality at rank 104 on \(Q^{14}\),
standard equality in dimensions \(16,18,20\), the
standard/cubic/quartic tie at \(d=22\), and cubic/quartic equality in
every even dimension at least 24, while retaining every G144 detector
clause.

B279 excludes the sole rank-112 standard survivor on \(Q^{16}\), so
one valid input falsifies the universal G198 claim. G198 is NO-GO and
passes to G199. No ODP package, rational detector, specified pairing,
cycle, proof, or disproof of HC is produced.
