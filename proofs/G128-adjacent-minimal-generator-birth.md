---
brick_id: G128
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex 2n-fold with very ample H, a specified primitive rational middle Hodge class, and a class-directed reduced point scheme Z
smoothness: X and Z are smooth; the degree-m member must have isolated ODPs and the simultaneous-node incidence germ must be reduced and smooth
projectivity: X, H^(m-1), H^m, the point and tangent spans, the ideal module, doubled scheme, and detector family are projective
dimension: dim X=2n; m>=2; V_(m-1)=0; V_m has dimension 2n; at least 2n new minimal generators map onto V_m
codimension: construct one adjacent tangent-span break and a rank-2n synchronized first-jet birth, then retain the finite Kuranishi and detector obligations
coefficient_field: C for embeddings, ideal generators, jets, and Hessians; Q for the Hodge class, detector, and specified pairing
cohomology_theory: graded coherent ideals, projective tangent spans, ODP Kuranishi theory, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the detector must be rational type (0,0) with nonzero pairing against the specified class
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B198, G013, G090-G127, NG106-NG160, and S065
claim: Construct from arbitrary (X,zeta) a point scheme Z and adjacent degrees m-1,m with m>=2 such that the H^(m-1) point span is full or tangent-absorbing, while at least 2n new degree-m minimal ideal generators map onto a 2n-dimensional V_m determined by every node, with conformal Hessian holonomy, the finite Kuranishi certificate, isolated ODPs, and the complete rational detector package.
falsifier: V_(m-1) nonzero, no degree-m minimal generators surviving first jets, dim V_m other than 2n, failure of one-node determination or holonomy, nonisolated singularities, a nonzero Kuranishi rung, or failure of any rational detector clause
---

# G128 — Construct the adjacent minimal-generator birth

For \(m\ge2\), B197 collapses G127's simultaneous lower conditions to

\[
 V_{m-1}=0. \tag{1}
\]

By B196, equation (1) says exactly that the \(H^{m-1}\)-span of \(Z\) is
full or contains every embedded tangent space at its marked points. At the
next degree require

\[
 \dim V_m=2n, \tag{2}
\]

with each node-gradient map
\(V_m\to T_{p_i}^*X\otimes H^m|_{p_i}\) an
isomorphism and with B193's conformal Hessian holonomy.

B198 adds the concrete construction obligation: the ideal module

\[
 J=\bigoplus_k H^0(I_ZH^k) \tag{3}
\]

must acquire at least \(2n\) genuinely new minimal generators in degree
\(m\), and their classes must map onto \(V_m\). Generators already in
\(H^0(I_{2Z}H^m)\) do not contribute.

The same degree-\(m\) full incidence must also close G126's finite Kuranishi
ladder, retain isolated ODPs, and carry the specified rational type-\((0,0)\)
detector with nonzero Saito pairing. G128 is the narrowest current geometric
gate; equations (1)--(3) alone do not imply any detector or algebraic cycle.
