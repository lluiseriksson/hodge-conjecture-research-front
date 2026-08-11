---
brick_id: NG224
status: NO-GO
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=16, primitive ruling difference zeta=a-b, standard A=O_Q(1), and H=O_Q(2)
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: the standard quadratic embedding, residual orthogonal quadrics, five nested tangent quotient spaces, rank-one self-adjoint maps, and contact loci are projective
dimension: dim X=d=2n>=16; no standard candidate has h_Z(1)=8d-17; the standard floor is at least 8d-16 and the common floor is B266's P(d)
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the failed route is survival with one residual dimension after B263's third escape
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to the reduced and double marked schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B253, B259-B266, G191, S081
claim: The route in which the standard polarization survives at h_Z(1)=8d-17 is impossible on every even Q^d with d>=16; after three minimal escapes only one dimension remains, below the fourth rank d-7, while any filled branch has quadratic point rank at most 36.
falsifier: a residual configuration below B259, more than one remaining dimension after three minimal escapes, a fourth escape of rank at most one, or a filled P^7 contact locus of point rank above 36
---

# NG224 — One residual dimension after the third escape

- **Label:** NO-GO
- **Route:** retain \(A=O_Q(1)\) at \(h_Z(1)=8d-17\).
- **Valid premise:** the three minimal contractions total \(3d-15\)
  against a budget \(3d-14\).
- **Invalid inference:** the remaining one dimension can absorb another
  marked tangent.
- **Residual obstruction:** B259 excludes the projected
  \(Q^{d-2}\) branch for every even \(d\ge16\).
- **Filled-span obstruction:** any fill after the first three escapes
  confines the points to \(\mathbf P^5\), \(\mathbf P^6\), or
  \(\mathbf P^7\), with quadratic point rank at most 36.
- **Fourth-escape obstruction:** in the only unfilled case,
  \(\operatorname{Sym}^2J_3\) survives with \(\dim J_3=d-6\), so the
  next tangent contributes at least \(d-7>1\).
- **Floor consequence:** the standard floor is \(h_Z(1)\ge8d-16\).
- **Common-floor consequence:** B260-B266 give \(P(d)=6d+6\) for
  \(d=14,16,18,20\) and \(P(d)=7d+6\) for every even \(d\ge22\).
- **Universal-quantifier guard:** every even \(Q^d\), \(d\ge16\), is a
  valid input. No special-family result is promoted upward.
- **Detector guard:** no ODP package, rational detector, specified
  pairing, cycle, proof, or disproof of HC is produced.
- **Conclusion:** G191 is closed as a universal gate; the surviving
  regimes pass to G192. G148 and HC remain open.
- **Re-entry condition:** G192 uses B266's \(P(d)\) and survivor table.
