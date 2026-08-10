---
brick_id: NG058
status: NO-GO
base_field: C
variety: the B071 semistable stack and its proper pushdown to the plane-net base
smoothness: regular source stack and smooth two-dimensional base
projectivity: proper/projective pushdown
dimension: total space 2n+1, base 2, and fiber 2n-1
codimension: full, divisor, and point supports; terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: derived rational mixed Hodge modules, decomposition theorem, perverse filtration, and strict support
hodge_type: rational Hodge subquotients; no specified class projection is defined by an arbitrary splitting
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B077, B080-B081, G043-G045, S037
claim: B077 canonically furnishes a projection from the total derived pushdown onto the sum of all full-support constituents, so the value of that projection on the B058 class is splitting-independent.
falsifier: nonuniqueness of the derived decomposition splitting with only the perverse filtration and perverse-heart strict-support decomposition canonical
---

# NG058 — The total full-support projection is not canonical

**Status:** NO-GO

B077 proves existence of a decomposition into shifted semisimple perverse
cohomology objects. It does not canonically split the perverse filtration.
De Cataldo–Migliorini explicitly state that the decomposition-theorem
splitting is not unique.

Hence a symbol

\[
 \pi_{\mathrm{fs}}:K\longrightarrow K_{\mathrm{fs}}
\]

defined only by choosing a derived decomposition does not give an invariant
class coordinate. Different splittings can change the lift of an
associated-graded component inside the total cohomology group.

The valid replacement is B081/G046: take the canonical perverse-filtration
grade $E_\infty^{-1,0}$, then use the unique strict-support decomposition
inside ${}^pH^0(K)$. The point $b=-1$ term belongs to the different grade
$E_\infty^{0,-1}$.
