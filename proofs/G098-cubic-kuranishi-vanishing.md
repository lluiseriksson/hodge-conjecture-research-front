---
brick_id: G098
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X, a nonzero primitive rational middle Hodge class zeta, and a G097 synchronized ordered-node candidate with value rank R<N
smoothness: X and central nodes are smooth/ordinary double points; the desired simultaneous-node germ must be reduced and smooth
projectivity: X and the linear system are projective; Kuranishi reduction is local analytic
dimension: tangent kernel V=ker E; obstruction target coker E of dimension N-R; cubic obstruction lies in coker(E) tensor Sym^3(V^*)
codimension: second-order obstruction is zero; cubic and all higher Kuranishi tensors must vanish for a height-R smooth excess germ
coefficient_field: C for analytic deformation tensors; Q for zeta, vanishing cycles, and the terminal pairing
cohomology_theory: analytic Kuranishi theory, local nodal deformation theory, rational vanishing-cycle homology, Saito local intersection cohomology, and rational Betti cohomology
hodge_type: the final local relation functional must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative of zeta may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B134-B154, G090-G097, and NG118-NG124
claim: Construct from (X,zeta), without an algebraic carrier, G097 data with zero second-order obstruction and zero canonical cubic Kuranishi tensor; then prove the entire analytic Kuranishi germ vanishes, yielding a reduced smooth height-R nodal germ whose Saito functional pairs nontrivially with zeta.
falsifier: nonzero cubic tensor, any nonzero higher Kuranishi term, a nonreduced or singular node germ, or zero specified Saito pairing
---

# G098 — Kill the cubic tensor and integrate all orders

After G097, the reduced Kuranishi map has no linear or quadratic term:

\[
 \kappa:(\ker E,0)\longrightarrow(\operatorname{coker}E,0),
 \qquad d\kappa_0=d^2\kappa_0=0.
\]

The first new obligation is

\[
 \kappa_3=0.
\]

B154 gives its exact formula from the node Hessians, spatial third jets, and
second-order implicit correction. Vanishing of \(\kappa_3\) is still only
the first higher-order test. Closure of G098 requires:

1. \(\kappa_j=0\) for every \(j\ge3\), equivalently
   \(\kappa\equiv0\) by analyticity;
2. the resulting germ to have height exactly \(R\) and carry the G097
   uniform value matroid, adjoint defect, and primitive ambient image;
3. the rational type-\((0,0)\) local Saito functional to pair nontrivially
   with \(\zeta\).

No carrier-free all-order vanishing mechanism is known. An algebraic carrier
supplies it by an actual moving incidence, which remains circular for an
arbitrary specified Hodge class.
