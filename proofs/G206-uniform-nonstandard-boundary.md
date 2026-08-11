---
brick_id: G206
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex d-fold X of even dimension d=2n>=14 with a specified nonzero primitive rational middle Hodge target zeta and a to-be-chosen very ample A, with H=A^2
smoothness: X and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: X, the complete A and H embeddings, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim X=d=2n>=14; m=2; AF(d)=7d+7; h_Z(1)=AF(d); delta_1=6d+6; slack s_18(d)=12d+12; N=14d+14
codimension: B286 excludes the only standard tie and B287 excludes every nonstandard polarization, so no complete G144 package exists at this boundary
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for zeta, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with zeta
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of zeta is not assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B007-B010, B134-B287, G013, G090-G148, G172, G207-G208, NG106-NG244, S081-S085
claim: The proposed uniform G144 package at h_Z(1)=7d+7 cannot exist: B286 excludes the standard tie and B287 excludes every nonstandard polarization on the valid even-quadric inputs.
falsifier: a valid G206 package on every primitive input, a standard or nonstandard quadric survivor at rank 7d+7, or failure of B286 or B287
---

# G206 — Uniform boundary closed

\[
d\ge14\text{ even},\qquad AF(d)=7d+7,\qquad
s_{18}(d)=12d+12,\qquad A=O_Q(k),\ k\ge2. \tag{1}
\]

G206 would have to classify the uniform equality \(7d+7\) for every
even \(d\ge14\), retaining every G144 detector clause. B286 removes the
only standard tie. B287 then iterates tangent absorption for every
nonstandard polarization and forces rank at least \((d+1)^2>7d+7\).
Thus G206 is NO-GO and passes to the standard piecewise frontier G208.
No ODP package, rational detector, specified pairing, cycle, proof, or
disproof of HC is produced.
