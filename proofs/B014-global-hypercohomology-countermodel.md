---
brick_id: B014
status: PROVED
base_field: C
variety: a smooth projective elliptic curve E used as an abstract base-space countermodel, not as a universal hyperplane parameter space
smoothness: E is smooth
projectivity: E is projective
dimension: dim E = 1
codimension: not a cycle-construction statement; the tested local cohomology-sheaf degree is -dim(E)+1 = 0
coefficient_field: Q
cohomology_theory: rational singular cohomology, hypercohomology, intersection cohomology, and perverse sheaves
hodge_type: unrestricted; the example refutes only a formal sheaf-theoretic implication and is not a Hodge-class counterexample
cycle_class_map: CH^p(E)_Q -> H^{2p}(E,Q(p)) is not used
cycle_equivalence: rational equivalence
scope: absolute
dependencies: the intersection-cohomology normalization in S024 equations (2.1)-(2.2); standard cohomology of an elliptic curve
claim: Nonzero degree-one intersection hypercohomology of a perverse intersection complex does not formally imply nonzero cohomology sheaves in local degree -d+1 at any point.
falsifier: vanishing of H^1(E,Q) or nonvanishing of the degree-zero cohomology sheaf of Q_E[1]
---

# B014 - Global hypercohomology countermodel

Let \(E/\mathbf C\) be a smooth projective elliptic curve and normalize its
intersection complex perversely:

\[
 IC_E(\mathbf Q)=\mathbf Q_E[1].
\]

With the convention
\[
 IH^k(E,\mathbf Q)=\mathbb H^{k-1}(E,IC_E(\mathbf Q)),
\]
we have

\[
 IH^1(E,\mathbf Q)=\mathbb H^0(E,\mathbf Q_E[1])
                  =H^1(E,\mathbf Q)\ne0.
\]

On the other hand, \(IC_E(\mathbf Q)\) has a single ordinary cohomology sheaf
in degree \(-1\). Therefore, at every \(p\in E\),

\[
 \mathcal H^{-\dim E+1}(IC_E(\mathbf Q))_p
 =\mathcal H^0(\mathbf Q_E[1])_p=0.
\]

Thus the abstract implication

\[
 \mathbb H^{1-\dim B}(B,IC_B(V))\ne0
 \Longrightarrow
 \exists p\;\mathcal H^{-\dim B+1}(IC_B(V))_p\ne0
\]

is false.

## Scope guard

The base \(E\) and constant local system are not the dual projective space and
vanishing-cohomology local system of G008. This is not a counterexample to the
Hodge Conjecture or to G008. It proves only that G008 cannot follow from the
formal definitions of hypercohomology and perverse stalks; a theorem must use
the special geometric origin of \(s(\zeta)\).

B129/NG103 later remove most of this caveat: the same separation occurs for
full-support geometric polarizable weight-\(-1\) Hodge coefficients on every
\(\mathbf P^d\), even with a nonzero rational type-\((0,0)\) global class.
What remains special in G008 is the universal-hyperplane coefficient and the
incidence origin of \(s_m(\zeta)\).
