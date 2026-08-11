---
brick_id: G192
status: CONDITIONAL
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n>=14 with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n>=14; m=2; P(d)=6d+6 for d=14,16,18,20 and P(d)=7d+6 for even d>=22; h_Z(1)=P(d); delta_1=P(d)-d-1; slack s_6(d)=2(P(d)-d-1); N=2P(d)
codimension: construct the complete G144 package with delta_1=P(d)-d-1 and an isomorphic degree-one relation transport at B266's square-cubic piecewise boundary
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B267, G013, G090-G148, G172, NG106-NG224, S081-S083
claim: Conditional on first replacing B265 and closing G190, then applying B266 at the resulting boundary, the later complete G144 package would have h_Z(1)=P(d), delta_1=P(d)-d-1, slack s_6(d)=2(P(d)-d-1), and N=2P(d). This is not an active gate.
falsifier: failure of the upstream assumed cubic/quartic floor 7d+6 or any different boundary after a valid closure of G190
---

# G192 — Conditional square/cubic boundary

Under a valid replacement for B265 followed by B266, a later balanced
signature would be

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

Conditional G192 would classify square equality in the four low
dimensions, the standard/cubic/quartic tie at \(d=22\), and
cubic/quartic equality in every even dimension at least 24, retaining
every G144 detector clause. It is not the active gate.

B267 retracts the upstream floor needed to reach (1)-(2). G192 is
therefore CONDITIONAL and inactive until a valid replacement closes
G190. Its table is retained only as a falsifiable downstream boundary,
not as current progress.
