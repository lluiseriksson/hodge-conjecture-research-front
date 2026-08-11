---
brick_id: G191
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n>=14 with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n>=14; m=2; M(d)=6d+6 for d=14,16,18,20, M(22)=159, and M(d)=7d+6 for even d>=24; h_Z(1)=M(d); delta_1=M(d)-d-1; slack s_5(d)=2(M(d)-d-1); N=2M(d)
codimension: construct the complete G144 package with delta_1=M(d)-d-1 and an isomorphic degree-one relation transport at B265's square-standard-cubic piecewise boundary
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B266, G013, G090-G148, G172, NG106-NG224, S081-S083
claim: No universal G144 package exists at B265's piecewise floor M(d); B266 excludes the unique d=22 standard candidate at h_Z(1)=159, while every other polarization already has larger rank.
falsifier: one complete G191 package on every valid primitive input, in particular a degree-two candidate of rank 159 on Q^22
---

# G191 — The square/standard/cubic boundary

B265 reduces the next balanced signature to

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

G191 is the next falsifiable gate: classify square equality in the four
low dimensions, standard equality at \(d=22\), and cubic/quartic
equality in even dimensions at least 24, then retain every G144
relation, ODP, Kuranishi, rational-type, and nonzero specified-pairing
clause. Rank survival alone would not construct an algebraic cycle or
prove or disprove HC.

B266 excludes the standard rank \(8d-17\) for every even \(d\ge16\).
In particular, the unique candidate at \(M(22)=159\) does not exist.
Thus G191 is NO-GO as a universal gate. The low-dimensional square and
all high-dimensional cubic/quartic regimes pass to G192. No detector,
pairing, cycle, proof, or disproof of HC is produced.
