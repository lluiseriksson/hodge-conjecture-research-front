---
brick_id: G188
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n>=14 with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n>=14; m=2; J(d)=7d-12 except J(20)=126; h_Z(1)=J(d); delta_1=J(d)-d-1; slack s_2(d)=2(J(d)-d-1); N=2J(d)
codimension: construct the complete G144 package with delta_1=J(d)-d-1 and an isomorphic degree-one relation transport at B261's mostly-standard seventh-jet boundary
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B262, G013, G090-G148, G172, NG106-NG220, S081-S083
claim: No universal G144 package exists at B261's mostly-standard floor J(d); B262 excludes the standard equality and the full band through 8d-19 on every even quadric Q^d with d>=14.
falsifier: one complete G188 package on every valid primitive input, in particular a standard candidate in B262's excluded band
---

# G188 — The mostly-standard seventh-jet boundary

B261 reduces the next balanced signature to

\[
 h_Z(1)=J(d),\qquad
 \delta_1=J(d)-d-1,\qquad
 s_2(d)=2(J(d)-d-1),\qquad N=2J(d), \tag{1}
\]

where

\[
\begin{array}{c|c|c|c}
 d & J(d) & s_2(d) & \text{polarizations not yet excluded}\\ \hline
 14,16 & 7d-12 & 12d-26 & A=O_Q(1)\\
 18 & 114 & 190 & A=O_Q(1),O_Q(2)\\
 20 & 126 & 210 & A=O_Q(2)\\
 d\ge22\text{ even} & 7d-12 & 12d-26 & A=O_Q(1).
\end{array} \tag{2}
\]

B262 closes the standard equality and the entire band through
\(8d-19\). The residual branch recurses to B253 or B259 on
\(Q^{d-2}\); every mixed branch fails a uniform three-step rank-one
escape.

Thus G188 is NO-GO as a universal gate. The square low-dimensional
cases, the single standard dimension 22 case, and high-dimensional
cubic/quartic cases pass to G189. No ODP package, rational detector,
specified pairing, algebraic cycle, proof, or disproof of HC is
produced.
