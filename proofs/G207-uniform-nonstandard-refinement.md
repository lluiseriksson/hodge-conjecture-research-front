---
brick_id: G207
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n>=14 with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen nonstandard very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n>=14; m=2; AG(d)=7d+7; h_Z(1)=AG(d); delta_1=6d+6; slack s_19(d)=12d+12; N=14d+14
codimension: B287 excludes every nonstandard polarization by forcing d+1 independent double blocks and rank at least (d+1)^2
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B287, G013, G090-G148, G172, G206, G208, NG106-NG244, S081-S085
claim: No complete G144 package exists at h_Z(1)=7d+7 using a nonstandard polarization on every quadric test input; B287 forces h_Z(1)>=(d+1)^2.
falsifier: a valid nonstandard G207 package, a tangent-absorbing nonstandard rank below (d+1)^2, or failure of B287
---

# G207 — Uniform nonstandard refinement closed

B286 removes the only standard tie from G206. The survivor table is
now uniform:

\[
 d\ge14\text{ even},\qquad h_Z(1)=7d+7,\qquad
 A=O_Q(k),\ k\ge2. \tag{1}
\]

G207 would have to classify this equality while retaining every G144
detector clause. B287 shows instead that every nonstandard
tangent-absorbing span has rank at least \((d+1)^2>7d+7\). Hence G207
and its parent G206 are NO-GO, and G208 is operationally active. No
ODP package, rational detector, specified pairing, cycle, proof, or
disproof of HC is produced.
