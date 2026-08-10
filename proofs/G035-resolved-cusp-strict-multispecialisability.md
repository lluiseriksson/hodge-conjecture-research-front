---
brick_id: G035
status: EXPLORATORY
base_field: C
variety: the B065 three-blowup resolution of the A2 cusp together with the resolved pullback of the B064 family
smoothness: the resolved base is smooth with SNC boundary; the total pulled-back family requires an explicit resolution or stratified model
projectivity: the local modification is proper; global application requires compatible projective algebraization
dimension: two-dimensional base and arbitrary suspended fiber dimension
codimension: local boundary components are divisors; terminal cycles have the original middle codimension p
coefficient_field: Q for mixed Hodge modules and C for filtered D-modules
cohomology_theory: mixed Hodge modules, canonical V-multifiltrations, nearby cycles, and proper direct image
hodge_type: rational type (0,0) after Tate twist
cycle_class_map: CH^p(X)_Q -> H^(2p)(X,Q(p))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B063-B065, G034, NG044, and S042
claim: On every double-crossing chart of the resolved cusp, the exact pulled-back family Hodge module is strictly R-multispecialisable, the local comparisons glue, and their pushdown retains the detector map.
falsifier: incompatible F and V filtrations on one chart, failure of gluing around E3, failure of a proper-direct-image hypothesis, or loss of the detector under pushdown
---

# G035 — Strict multispecialisability on the resolved cusp

**Status:** EXPLORATORY  
**Parent gate:** G034

## Falsifiable local theorem

Let \(\rho:\widetilde B\to B\) be B065's three-blowup resolution and let \(\widetilde{\mathcal M}\) be the precisely defined mixed Hodge module obtained from the pulled-back \(A_2\) family after resolving its total space. Prove:

1. on every chart where two components of \(\rho^{-1}(C)_{red}\) meet, the Hodge filtration and the two canonical \(V\)-filtrations are compatible;
2. equivalently, under the hypotheses of S042 Theorem B, \(\widetilde{\mathcal M}\) is strictly \(R\)-multispecialisable there;
3. the comparison isomorphisms glue around \(E_3\), respecting component multiplicities \((2,3,6)\) and monodromy;
4. the applicable proper direct image has exactly the product or graph form required by S042, or a separately proved base-modification analogue;
5. the pushed-down morphism agrees with the detector map rather than only with an exceptional-support summand.

## Current result

B065 proves the SNC base geometry and shows that at most two reduced boundary
components meet at any point. B066 proves that the raw pulled-back total
family is nevertheless singular over \(E_3\cup E_2\), so the coefficient
Hodge module cannot yet be specified as a smooth constant module. G036 must
construct and descend a semistable total-space model first. Even then, S042
Theorem B makes filtration compatibility an explicit additional hypothesis.
NG044 prevents replacing the two-coordinate calculation by the
one-coordinate quasi-ordinary cusp application.

## Smallest unresolved check

First complete G036. Then choose the chart \(b=ac\), where the total cusp
equation is \(a^6c^3(4+27c)\), write the graph-pushed filtered
\(\mathcal D\)-module of the resulting semistable family, and compute whether
\((F,V^a,V^c)\) is compatible near \(a=c=0\).
