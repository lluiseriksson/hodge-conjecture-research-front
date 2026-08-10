---
brick_id: G046
status: EXPLORATORY
base_field: C with all Hodge and descent data over Q
variety: the B058 plane-net family, B071 semistable stack, and proper pushdown to the original plane base
smoothness: smooth generic fibers, regular semistable source stack, and smooth base
projectivity: family, alterations, modifications, and pushdown are projective
dimension: ambient 2n, fiber 2n-1, base 2, and total space 2n+1
codimension: full support and discriminant-divisor support in perverse degree zero; point support in perverse degree minus one
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, nearby cycles, canonical perverse filtration, strict support, and Saito ambient map
hodge_type: the target component must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B057-B058, B071-B081, G043-G045, NG053-NG058
claim: The B058 nearby specialization has nonzero canonical associated-graded component in E_infinity^(-1,0), and its strict-support projection inside pH^0(K) to the full-support summand is nonzero and retains the prescribed pairing.
falsifier: the class lies entirely in the point-support grade E_infinity^(0,-1), lies in divisor support inside E_infinity^(-1,0), or its full-support grade is orthogonal to the prescribed Hodge class
---

# G046 — Canonical perverse-grade landing

**Status:** EXPLORATORY  
**Parent gates:** G043 / G045

Let $K=f_*\mathbf Q_{\mathcal Y}[2n+1]$ and let
$\operatorname{sp}(c)\in H^{-1}(i_p^*K)$ be the B058 specialization.
Use the canonical perverse filtration, not a chosen decomposition of $K$.

The falsifiable target is:

1. prove that the associated-graded class

   \[
   [\operatorname{sp}(c)]_{E_\infty^{-1,0}}
   \in E_\infty^{-1,0}
   \]

   is nonzero;
2. use the unique strict-support decomposition of
   ${}^pH^0(K)$ to remove the divisor-supported part of that grade;
3. prove the remaining full-support class is nonzero and its Saito ambient
   image pairs nontrivially with the prescribed B058 Hodge class.

The point-supported $b=-1$ term is $E_\infty^{0,-1}$. It is an
alternative grade in which the total specialization could be trapped, not a
component to subtract after choosing a noncanonical splitting.

The spectral-sequence position is used as the grade label throughout; no
unstated convention for writing it as $\operatorname{gr}^a_P$ is needed.

## Smallest calculation

Construct the filtered nearby-specialization morphism for the B057 extension
chain and compute its two edge components

\[
 H^{-1}(i_p^*K)\rightsquigarrow
 E_\infty^{-1,0},\ E_\infty^{0,-1}.
\]

Then compute only the divisor/full-support strict-support decomposition of
$E_\infty^{-1,0}$. This is strictly more canonical and narrower than G045's
original “subtract both supports” formulation.
