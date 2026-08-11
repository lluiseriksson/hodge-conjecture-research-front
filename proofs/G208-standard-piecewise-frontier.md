---
brick_id: G208
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n>=14 with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2; on quadric test inputs only standard A=O_Q(1) remains
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n>=14; m=2; E(14)=108, E(16)=120, E(18)=134, E(20)=148, E(22)=162, and E(d)=8d-16 for even d>=24; h_Z(1)=E(d); delta_1=E(d)-d-1; slack=2(E(d)-d-1); N=2E(d)
codimension: construct the complete G144 package with the displayed piecewise standard rank and an isomorphic degree-one relation transport after B287 excludes every nonstandard polarization below (d+1)^2
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B287, G013, G090-G148, G172, G206-G207, NG106-NG244, S081-S085
claim: For every arbitrary primitive target and every even d>=14, construct the complete G144 package at the first currently unexcluded standard quadric ranks E(d), retaining every relation, ODP, Kuranishi, rational-type, and nonzero specified-pairing clause.
falsifier: one primitive target for which the standard piecewise package cannot be realized, a stronger standard floor, or failure of any retained G144 clause
---

# G208 — Active standard piecewise frontier

B287 raises every nonstandard quadric polarization to rank at least
\((d+1)^2\). The first currently unexcluded ranks are therefore
standard-polarized and piecewise:

\[
\begin{array}{c|c|c}
 d & E(d) & \text{surviving test polarization}\\ \hline
 14 & 108 & O_Q(1)\\
 16 & 120 & O_Q(1)\\
 18 & 134 & O_Q(1)\\
 20 & 148 & O_Q(1)\\
 22 & 162 & O_Q(1)\\
 d\ge24\text{ even} & 8d-16 & O_Q(1).
\end{array} \tag{1}
\]

The low-dimensional rows use B277 and B283--B286; the stable row uses
B266. G208 must classify equality in (1) while retaining every G144
detector clause. It is EXPLORATORY and is the operational gate after
G206--G207. Rank survival supplies no ODP package, rational detector,
specified pairing, cycle, proof, or disproof of HC.
