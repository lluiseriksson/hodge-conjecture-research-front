---
brick_id: G165
status: NO-GO
base_field: C
variety: the even quadrics Q^d with d=2n>=4 and primitive ruling difference a-b, at the G164 signature; B241 forces A=O_Q(2) for d>=6 and permits A=O_Q(1) only when d=4
smoothness: Q^d and Z are smooth and reduced; the central H^2 divisor must have prescribed isolated ODPs and every retained G144 incidence-smoothness clause
projectivity: the complete O_Q(4) embedding in d>=6, the O_Q(2) or O_Q(4) embedding on Q^4, the degree-two nodal system, evaluation code, and detector data are projective
dimension: dim Q=d=2n; m=2; slack s=4d+10; N=6d+12; h_Z(1)=3d+6=N/2
codimension: survive the universal-quantifier quadric test at delta_1=2d+5 after B241's polarization reduction
coefficient_field: C for polarizations, tangent jets, codes, ODP profiles, and Kuranishi tensors; Q for a-b, the relation, detector, and specified pairing
cohomology_theory: coherent restrictions to Z and 2Z, primitive rational singular cohomology, vanishing-cycle mixed Hodge structures, and Saito pairing
hodge_type: the full-support degree-two relation must be rational type (0,0) and pair nontrivially with a-b
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); algebraicity of a-b is known but is not used as a substitute for the required detector
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B007-B010, B134-B242, G013, G090-G164, NG106-NG200, S081-S083
claim: For every even d>=6, construct the complete G164 package on (Q^d,a-b) with A=O_Q(2); for d=4, construct it with A=O_Q(1) or O_Q(2). Every ODP-profile, holonomy, finite-Kuranishi, rational type-(0,0), and specified-pairing clause must hold.
falsifier: one even d>=6 for which no square-polarized G164 configuration exists, or d=4 for which neither surviving polarization realizes every G164 obligation
---

# G165 — Survive the square-polarized quadric gate

B241 proves that G164 can survive its necessary quadric test only through

\[
 A=O_Q(2)\quad(d\ge6),\qquad
 A\in\{O_Q(1),O_Q(2)\}\quad(d=4). \tag{1}
\]

G165 asks for the full balanced G164 configuration at

\[
 s=4d+10,\qquad N=6d+12,\qquad h_Z(1)=3d+6=N/2, \tag{2}
\]

including every ODP, adjacent-profile, holonomy, finite-Kuranishi,
rational type-\((0,0)\), and nonzero specified-pairing clause.

This is a necessary survival gate, not a special-family proof of HC.
Failure for one even quadric falsifies G164's arbitrary-variety claim;
success on all quadrics would not prove G164 for general varieties.

No marked scheme, detector, pairing, algebraic cycle, proof, or disproof
of HC is currently constructed.

B242 excludes the square polarization in every even dimension. Therefore
G165 fails already on \(Q^6\), where B241 permits no other polarization.
The exceptional standard \(Q^4\) case cannot rescue a universal claim.
G164 and G165 are **NO-GO**; move to G166 at slack \(4d+12\).
