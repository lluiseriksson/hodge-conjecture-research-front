---
brick_id: NG186
status: NO-GO
base_field: C
variety: arbitrary smooth projective complex 2n-folds with fixed powered primitive polarizations A=B^ell, including P^n x P^n with B=O(1,1)
smoothness: X is smooth; the two triple neighborhoods are disjoint for p!=q; no ODP family is constructed
projectivity: all B and A power embeddings and finite jet restriction maps are projective
dimension: dim X=2n; every G149-G151 marked set would need 2binom(2n+2,2)+2 or more points
codimension: B215 makes the A^4 two-triple defect correspondence empty when ell>=2
coefficient_field: C for jet interpolation; Q for the valid primitive algebraic test class on P^n x P^n
cohomology_theory: coherent finite-jet restriction and rational singular cohomology on the test product
hodge_type: the product test class is nonzero primitive rational type (n,n); no unknown class is assumed algebraic
cycle_class_map: CH^n(P^n x P^n)_Q -> H^(2n)(P^n x P^n,Q(n)); the test class is already algebraic only to certify a valid input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B226, G149-G151
claim: Fix any primitive very ample A, replace it by or choose it as a sufficiently positive power, and use that positivity to realize G149-G151.
falsifier: if A=B^ell with ell>=2, then A^4=B^(4ell) has exponent at least eight and B215 makes every two-triple restriction surjective, while B226 requires failure for every marked pair
---

# NG186 — Powered polarizations erase the required defect clique

- **Route:** improve positivity by replacing a primitive polarization by
  a high power, then seek the G151 self-associated osculator set.
- **Valid input:** primitivity is unchanged by scaling the Lefschetz
  operator, and powers improve jet separation.
- **Invalid inference:** improved separation creates the pairwise
  second-jet defect forced by first slack.
- **Precise obstruction:** for \(A=B^\ell\), \(\ell\ge2\), B215 makes
  \(A^4=B^{4\ell}\) surjective on \(3p\sqcup3q\) for every
  \(p\ne q\), whereas B226 requires nonsurjectivity for all marked pairs.
- **Universal-quantifier witness:** on
  \(\mathbf P^n\times\mathbf P^n\), \(B=O(1,1)\) has a nonzero rational
  algebraic primitive middle class; taking \(A=B^2\) gives a legitimate
  fixed primitive input with no candidate.
- **Detector guard:** this falsifies G149-G151's fixed-A universal
  formulations, not G148, G152, or the Hodge Conjecture.
- **Re-entry condition:** B228/NG187 close first slack and B230 closes
  every layer through nine; move to G154 at slack ten.
