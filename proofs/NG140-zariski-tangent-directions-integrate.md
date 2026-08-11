---
brick_id: NG140
status: NO-GO
base_field: C
variety: a smooth analytic parameter germ carrying a labelled ODP critical-value ideal I_tau
smoothness: the parameter germ is smooth; the simultaneous-node scheme may be nonreduced or singular
projectivity: irrelevant to the local obstruction; finite ODP jets are projectively realizable but do not give a full-system theorem
dimension: failure occurs for parameter dimension 2, N=2, and central differential rank R=1
codimension: the Zariski tangent kernel has dimension 1, but the ideal-preserving logarithmic evaluation has dimension 0
coefficient_field: C; Q enters only in downstream detector clauses
cohomology_theory: convergent analytic local algebra and ideal-preserving logarithmic derivations
hodge_type: none produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is not used
cycle_equivalence: rational equivalence
scope: relative
dependencies: B156-B157, B175-B176, G100, G109
claim: Every vector in ker(d tau_0) automatically extends to an analytic derivation preserving I_tau, so the central tangent kernel integrates to a logarithmic orbit without further geometry.
falsifier: for I_tau=(x,y^2), every ideal-preserving derivation has zero value at the origin although ker(d tau_0)=C partial_y
---

# NG140 — Zariski tangent directions need not integrate logarithmically

Take again

\[
 \tau=(x,x+y^2),\qquad I_\tau=(x,y^2).
\]

Its central differential rank is one and

\[
 \ker d\tau_0=\mathbf C\partial_y. \tag{1}
\]

Write an arbitrary analytic vector field as

\[
 \delta=a(x,y)\partial_x+b(x,y)\partial_y.
\]

Preservation of \(I_\tau\) is equivalent to

\[
 a=\delta(x)\in(x,y^2),
 \qquad
 2yb=\delta(y^2)\in(x,y^2). \tag{2}
\]

Reducing the second condition modulo \(x\) gives

\[
 yb(0,y)\in(y^2),
\]

so \(b\in(x,y)=\mathfrak m\). Conversely these conditions are sufficient.
Therefore

\[
 \Theta(-\log I_\tau)
 =(x,y^2)\partial_x+\mathfrak m\partial_y,
\]

and hence

\[
 \operatorname{ev}_0\Theta(-\log I_\tau)=0
 \subsetneq \mathbf C\partial_y=\ker d\tau_0. \tag{3}
\]

The nonzero Zariski tangent direction is only an infinitesimal tangent
vector. It does not extend to a vector field whose flow preserves the
nonreduced simultaneous ideal.

## Re-entry condition

G109 must construct ideal-preserving vector fields to all analytic orders
from genuine full-complete-system geometry. Central tangent dimensions,
branchwise logarithmicity of the reduced product, Lie closure after the
fields exist, and any fixed finite jet order do not provide that
construction. Every detector clause remains separate.
