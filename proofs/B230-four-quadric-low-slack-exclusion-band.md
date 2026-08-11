---
brick_id: B230
status: PROVED
base_field: C
variety: the smooth four-dimensional quadric X=Q^4 with primitive rational middle class zeta=a-b and an arbitrary very ample A=O_Q(k), H=A^2
smoothness: Q^4 and every reduced marked scheme are smooth; central ODP and incidence conditions are only inherited hypotheses
projectivity: Q^4, every complete O_Q(k)-embedding, tangent and second-osculating spaces, finite jet restrictions, secant lines, and isotropic planes are projective
dimension: dim X=4; for m=2 the tangent-jet dimension is 5; for m>=3 the triple-jet dimension is c_4=15
codimension: no G144 candidate exists for m=2 with slack s<=9, or for m>=3 with slack s<=14; therefore no degree realizes any universal slack layer s<=9
coefficient_field: Q for zeta and C for sections, jets, quadratic forms, osculators, and ranks
cohomology_theory: rational singular cohomology for the primitive input and coherent restriction to finite jet schemes
hodge_type: zeta is nonzero primitive rational type (2,2); the obstruction constructs no rational type-(0,0) detector
cycle_class_map: CH^2(Q^4)_Q -> H^4(Q^4,Q(2)); the ruling difference only certifies a valid input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B221-B229, S081, S083
claim: On (Q^4,a-b), every m=2 G144 candidate with slack s<=9 and every m>=3 candidate with slack s<=14 is impossible for every very ample A. Consequently all equality and strict-slack specializations with 0<=s<=9 are universally false as sufficient mechanisms.
falsifier: an O_Q(k) candidate in the stated band, failure of the forced pairwise double or triple defect, a standard-polarization defect clique not contained in an isotropic P^2, containment of the full O_Q(2) tangent space in Sym^2(W) for an isotropic three-space W, or degree-four point rank above 15 on P(W)
---

# B230 — The four-quadric excludes the first nine slack layers

Fix the valid input \((Q^4,a-b)\). By B221 every very ample
polarization is \(A=O_Q(k)\).

## Degree two

For \(m=2\), B222 gives

\[
 h_Z(1)=5+\delta_1,\qquad
 1\le\delta_1,\qquad 2\delta_1\le s. \tag{1}
\]

If \(s\le9\), then \(h_Z(1)\le9\). Two independent double
neighborhoods would contribute a direct sum of dimension \(2(4+1)=10\)
inside the degree-one point span. Hence every pair is defective for
\(H=A^2\).

If \(k\ge2\), B215 gives the opposite surjectivity, as in B229. Thus
\(k=1\). The quadratic secant criterion in B229 makes every marked
secant tangent at both endpoints. On a quadric this means that the
secant line lies on \(Q\), so all point representatives span a totally
isotropic vector space \(W\) of dimension at most three.

The degree-one point span is contained in \(\operatorname{Sym}^2W\).
At \(p=[v]\in Z\), however, the full tangent osculator of the
\(O_Q(2)\)-embedding is

\[
 v\mathbin{\odot}v^\perp\subset\operatorname{Sym}^2V. \tag{2}
\]

Choose \(u\in v^\perp\setminus W\). Then
\(v\mathbin{\odot}u\notin\operatorname{Sym}^2W\), contradicting the
lower tangent-osculator absorption required by G144. This excludes
\(m=2\), \(s\le9\).

## Every degree at least three

For \(m\ge3\), B222 gives

\[
 h_Z(2)=15+\delta_2,\qquad 1\le\delta_2\le s. \tag{3}
\]

If \(s\le14\), then \(h_Z(2)\le29\). Surjectivity on
\(3p\sqcup3q\) would put a direct sum of two 15-dimensional second
osculators inside that span. Thus every pair is defective for
\(A^4=H^2\).

Again \(k\ge2\) is excluded by B226. For \(k=1\), B227 makes every
defect chord a line on \(Q\), so \(Z\subset\mathbf P(W)\simeq\mathbf
P^2\). But then

\[
 h_Z(2)\le h^0(\mathbf P^2,O(4))=15, \tag{4}
\]

contradicting \(h_Z(2)\ge16\). This excludes every \(m\ge3\) through
slack 14.

Combining the two degree ranges excludes every degree for
\(0\le s\le9\). B230 closes only these bounded-slack sufficient
specializations, not G148 or the Hodge Conjecture.
