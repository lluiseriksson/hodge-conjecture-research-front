---
brick_id: NG139
status: NO-GO
base_field: C
variety: a smooth analytic parameter germ with a reduced union of labelled ODP discriminant branches
smoothness: the parameter germ and the individual branches may be smooth; the reduced union may be a free divisor
projectivity: irrelevant to the local-algebra counterexample; projective finite-jet realizability does not upgrade it to a full-system theorem
dimension: already fails in parameter dimension 2 with N=2 and central differential rank R=1
codimension: divisor freeness controls a codimension-one reduced union, whereas G100 controls the higher-codimension scheme-theoretic intersection ideal
coefficient_field: C; Q remains required only for the downstream Hodge detector
cohomology_theory: logarithmic derivations and analytic critical-value syzygies
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used
cycle_equivalence: rational equivalence
scope: relative
dependencies: B156-B157, B174-B175, G100, S071
claim: Freeness of the reduced total discriminant, possibly together with a logarithmic basis preserving all labelled branches, forces H_tau=0 and lifts every central critical-value relation.
falsifier: B175 gives a free reduced divisor F=x(x+y^2) with a branch-preserving Saito basis, but I_tau=(x,y^2), dim H_tau=1, and no lift of (1,-1)
---

# NG139 — Free-divisor logarithmicity does not lift node relations

The proposed route was to use freeness of the discriminant and a basis of
logarithmic vector fields as a global source of analytic relations among
the tracked critical values.

B175 falsifies the implication at the precise local-algebra interface.
For

\[
 \tau=(x,x+y^2),\qquad F=\tau_1\tau_2,
\]

the reduced divisor \(V(F)\) is free. It has an explicit Saito basis, and
each basis derivation sends every labelled \(\tau_i\) to a multiple of
that same \(\tau_i\). Nevertheless

\[
 I_\tau=(x,y^2),\qquad \dim H_\tau=1,
\]

and all syzygies vanish at the origin. The central relation
\((1,-1)\) therefore does not lift.

## Precise obstruction

Saito freeness is a property of the principal reduced ideal \((F)\) and
the tangent module of the union \(V(F)\). G100 is a property of the
labelled tuple and the scheme-theoretic intersection ideal
\((\tau_1,\ldots,\tau_N)\). Passing to \(F=\prod_i\tau_i\) loses the
nilpotent thickness of that intersection. Even branchwise logarithmic
cofactors such as (1) in B175 do not supply syzygies among different
branches.

## Re-entry condition

A logarithmic route may re-enter only with an additional proved theorem
that controls the labelled simultaneous ideal, not merely the reduced
union. Concretely it must independently make

\[
 \operatorname{Syz}(\tau)\longrightarrow
 \ker(d\tau_0)^*
\]

surjective in the full complete-linear-system geometry and retain the
uniform matroid, positive adjoint defect, nonzero primitive ambient image,
rational type \((0,0)\), and specified nonzero Saito pairing. That is the
existing G100 obligation; free-divisor theory alone supplies no smaller
gate.
