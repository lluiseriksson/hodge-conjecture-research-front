---
brick_id: NG221
status: NO-GO
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=14, primitive ruling difference zeta=a-b, standard A=O_Q(1), and H=O_Q(2)
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: the standard quadratic embedding, residual orthogonal quadrics, four nested tangent quotient spaces, rank-one self-adjoint maps, and contact loci are projective
dimension: dim X=d=2n>=14; no standard candidate has h_Z(1)=8d-18; the standard floor is at least 8d-17 and the common floor is B263's K(d)
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the failed route is equality in B262's third nested escape
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B253, B259-B263, G189, S081
claim: The route in which the standard polarization survives at h_Z(1)=8d-18 is impossible on every even Q^d with d>=14; survival forces three minimal contraction ranks and a filled span whose marked points lie in P^7, of quadratic rank at most 36.
falsifier: a valid standard equality candidate, a contraction-rank sum below 3d-15, failure of the descended Sym^2(J_3) annihilator, or quadratic point rank above 36 on P^7
---

# NG221 — Survival at the third-escape equality

- **Label:** NO-GO
- **Route:** retain \(A=O_Q(1)\) at \(h_Z(1)=8d-18\).
- **Valid premise:** B262 leaves equality when the third escape has
  budget exactly \(d-6\).
- **Invalid inference:** equality can fill the span without shrinking
  the contact locus.
- **Rank obstruction:** the three contractions have minimal ranks
  \(d-4,d-5,d-6\), whose sum is the full budget \(3d-15\); any larger
  contraction already contradicts the budget.
- **Contact obstruction:** equality leaves
  \(\operatorname{Sym}^2J_3\) in the annihilator with
  \(\dim J_3=d-6\), so every marked point lies in \(\mathbf P^7\), of
  quadratic point rank at most 36.
- **Floor consequence:** the standard floor is \(h_Z(1)\ge8d-17\).
- **Common-floor consequence:** B260-B263 give
  \(K(d)=6d+6\) for \(d=14,16,18,20\) and \(K(d)=7d+5\) for every
  even \(d\ge22\).
- **Universal-quantifier guard:** every even \(Q^d\), \(d\ge14\), is a
  valid input. No special-family result is promoted upward.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G189 is closed as a universal gate; the surviving
  equality regimes pass to G190. G148 and HC remain open.
- **Re-entry condition:** G190 uses B263's \(K(d)\) and survivor table.
