---
brick_id: NG071
status: NO-GO
base_field: C with rational type-(0,0) Hodge structures
variety: an arbitrary projective collision with special-to-nearby map u and canonical special-stalk detector functional F
smoothness: generic fiber smooth; special target clean nodal
projectivity: collision projective
dimension: ambient 2n; hyperplane fibers 2n-1
codimension: middle codimension n
coefficient_field: Q
cohomology_theory: nearby/special exactness, dual Hodge structures, perverse grade, B022 quotients, and Saito pairing
hodge_type: rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B094-B095, G058
claim: The canonical detector functional on the special stalk automatically descends through the special-to-nearby map to a functional on nearby classes.
falsifier: a nonzero cokernel class [F] in coker(u^*), equivalently a detector functional nonzero on lift ambiguity
---

# NG071 — The detector functional need not descend to nearby classes

**Status:** NO-GO

A scalar value on a special lift descends to the nearby class precisely when
it is independent of lift ambiguity. B095 identifies this with
$[F]=0$ in $\operatorname{coker}u^*$.

If $[F]\ne0$, descent fails—but this is favorable, not fatal: B094-B095 show
that an ambiguity direction then produces a detecting lift automatically.
Assuming descent would erase one entire success branch.

The re-entry condition is G059's two-case calculation of $[F]$ and, only
when it vanishes, the descended evaluation on the specified nearby detector.
