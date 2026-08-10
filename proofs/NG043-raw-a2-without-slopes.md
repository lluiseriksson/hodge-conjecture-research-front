---
brick_id: NG043
status: NO-GO
base_field: C
variety: the local A2 two-parameter unfolding Y_r mapped to the (s,t)-plane
smoothness: the total space is smooth, the generic discriminant fiber is nodal, and the central fiber has an A2 singularity
projectivity: no; this is a local chart
dimension: arbitrary suspended fiber dimension r
codimension: the cusp discriminant has codimension one in the base
coefficient_field: Q for mixed Hodge modules and C for D-modules
cohomology_theory: mixed Hodge modules and iterated nearby cycles
hodge_type: the conditional comparison would preserve Hodge type, but its hypothesis fails in raw coordinates
cycle_class_map: none
cycle_equivalence: none
scope: relative
dependencies: B063, B064, and S042
claim: The without-slopes mixed-Hodge commutation theorem cannot be applied directly to the raw coordinate A2 recollision chart.
falsifier: a direct b-function proof that the exact graph-pushed coefficient object satisfies the pairwise without-slopes definition despite failure of the simpler geometric morphism condition
---

# NG043 — Direct without-slopes treatment of the raw \(A_2\) collision

**Status:** NO-GO

## Rejected route

Model recollision by the miniversal \(A_2\) unfolding and immediately invoke B063 for the two base coordinates \((s,t)\).

## Precise obstruction

B064 computes a cusp discriminant and a one-dimensional critical locus whose general point maps to \(s\ne0\) and \(t\ne0\). The critical locus is therefore not contained over the coordinate boundary \(st=0\), a necessary feature in the without-slopes setup audited in S042. The theorem's hypothesis is not a consequence of smoothness of the total space or of the fact that general discriminant points are nodal.

## Re-entry condition

Either directly verify the graph-pushed module's \(V\)-multifiltration/Bernstein-Sato condition, or resolve the target boundary, specify the pulled-back mixed Hodge module, verify without slopes or strict \(R\)-multispecialisability there, and prove that the comparison descends without losing the B022 quotient class or the nonzero Saito pairing. The resolution branch is G034.
