---
brick_id: G191
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n>=14 with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n>=14; m=2; M(d)=6d+6 for d=14,16,18,20, M(22)=159, and M(d)=7d+6 for even d>=24; h_Z(1)=M(d); delta_1=M(d)-d-1; slack s_5(d)=2(M(d)-d-1); N=2M(d)
codimension: the valid B271-B272 replacement reaches the piecewise boundary M(d), but B266 excludes its d=22 standard equality and makes the proposed universal gate impossible
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B272, G013, G090-G148, G172, NG106-NG228, S081-S084
claim: B271-B272 validly prove the cubic/quartic floor h_Z(1)>=7d+6 and reach M(d), but B266 excludes the sole d=22 equality survivor at M(22)=159. Hence G191 is NO-GO as a universal gate.
falsifier: a valid G191 package at rank 159 on the d=22 even quadric, failure of the valid cubic/quartic floor, or a different post-G190 boundary
---

# G191 — The square/standard/cubic boundary

B271-B272 now supply a valid replacement for B265's retracted
cubic/quartic floor. The next balanced signature is

\[
 h_Z(1)=M(d),\quad
 \delta_1=M(d)-d-1,\quad
 s_5(d)=2(M(d)-d-1),\quad N=2M(d), \tag{1}
\]

where

\[
\begin{array}{c|c|c|c}
 d & M(d) & s_5(d) & \text{polarizations not yet excluded}\\ \hline
 14,16,18,20 & 6d+6 & 10d+10 & A=O_Q(2)\\
 22 & 159 & 272 & A=O_Q(1)\\
 d\ge24\text{ even} & 7d+6 & 12d+10 & A=O_Q(3),O_Q(4).
\end{array} \tag{2}
\]

G191 would classify square equality in the four low
dimensions, standard equality at \(d=22\), and cubic/quartic equality
in even dimensions at least 24, then retain every G144 relation, ODP,
Kuranishi, rational-type, and nonzero specified-pairing clause.

B266 excludes the sole \(d=22\) survivor at
\(M(22)=159=8d-17\). One valid test input therefore falsifies the
universal G191 claim, so G191 is NO-GO and passes to G192. No detector,
pairing, cycle, proof, or disproof of HC is produced.
