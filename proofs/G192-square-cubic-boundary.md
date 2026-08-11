---
brick_id: G192
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n>=14 with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n>=14; m=2; P(d)=6d+6 for d=14,16,18,20 and P(d)=7d+6 for even d>=22; h_Z(1)=P(d); delta_1=P(d)-d-1; slack s_6(d)=2(P(d)-d-1); N=2P(d)
codimension: B273 excludes the sole square equality survivor in dimensions 14,16,18,20, so the proposed universal G144 package at P(d) cannot exist
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B273, G013, G090-G148, G172, NG106-NG229, S081-S084
claim: The proposed universal G144 package at P(d) cannot exist: B273 excludes square equality h_Z(1)=6d+6 on every valid even-quadric input in dimensions 14,16,18,20.
falsifier: a valid square G192 package on one of Q^14,Q^16,Q^18,Q^20, failure of B273, or a different post-G192 boundary
---

# G192 — Square/cubic boundary (closed)

The valid B271-B272 replacement for B265, followed by B266, gives the
balanced signature

\[
 h_Z(1)=P(d),\quad
 \delta_1=P(d)-d-1,\quad
 s_6(d)=2(P(d)-d-1),\quad N=2P(d), \tag{1}
\]

where

\[
\begin{array}{c|c|c|c}
 d & P(d) & s_6(d) & \text{polarizations not yet excluded}\\ \hline
 14,16,18,20 & 6d+6 & 10d+10 & A=O_Q(2)\\
 22 & 160 & 274 & A=O_Q(1),O_Q(3),O_Q(4)\\
 d\ge24\text{ even} & 7d+6 & 12d+10 & A=O_Q(3),O_Q(4).
\end{array} \tag{2}
\]

G192 must classify square equality in the four low
dimensions, the standard/cubic/quartic tie at \(d=22\), and
cubic/quartic equality in every even dimension at least 24, retaining
every G144 detector clause.

B271-B272 close G190 at the former \(7d+5\) boundary, and B266 closes
G191 at \(d=22\). B273 then excludes the only square survivor in each
of dimensions \(14,16,18,20\): tangent absorption prevents confinement
to the span of six supports, while escape from that span contributes a
full seventh double block. One valid quadric input therefore falsifies
the universal G192 claim, so G192 is NO-GO and passes to G193. No ODP
package, rational detector, specified pairing, cycle, proof, or
disproof of HC is produced.
