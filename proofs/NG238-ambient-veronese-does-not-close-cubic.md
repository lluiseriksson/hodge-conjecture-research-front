---
brick_id: NG238
status: NO-GO
base_field: C
variety: the smooth split even-dimensional quadric Q^d with d=2n>=14, cubic A=O_Q(3), H=O_Q(6), and seven distinct supports in the exact-rank branch of G200
smoothness: Q^d and the reduced supports are smooth; no central ODP package is constructed
projectivity: the ambient degree-six Veronese embedding, its strong base locus, the restricted sextic quadric embedding, and tangent spans are projective
dimension: dim X=d=2n>=14; the support count is r=7 while the ambient Veronese degree is six
codimension: the failed route attempts to deduce cubic seven-support separation solely from the ambient Veronese strong-base-locus threshold
coefficient_field: Q for zeta and C for sections, tangent jets, and strong base loci
cohomology_theory: rational singular cohomology and coherent restriction to double finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); no arbitrary Hodge class is assumed algebraic
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B281, G200-G202, NG237, S085
claim: S085 cannot prove cubic G201/G202 by an emptiness threshold: for the degree-six Veronese, strong base loci are already nonempty when r>=6, while the cubic gate has r=7; moreover the theorem concerns the ambient complete Veronese rather than the quadric exact-rank subclass.
falsifier: an S085 theorem implying strong-base-locus emptiness for every seven-point degree-six configuration relevant to Q^d, or an independent proof of G202
---

# NG238 — The ambient Veronese threshold does not close the cubic gate

- **Label:** NO-GO
- **Route:** apply the ambient Veronese strong-base-locus emptiness
  theorem to the cubic seven-support span.
- **Threshold obstruction:** S085, Theorem 3.8, says that the strong
  base locus for the degree-\(m\) Veronese is nonempty exactly when
  \(r\ge m\). The cubic branch uses \(m=6\) and \(r=7\), on the
  nonempty side of the threshold.
- **Scope obstruction:** S085 treats arbitrary ambient Veronese
  configurations. G202 imposes six independent quadric double blocks,
  exact residual rank \(d\), B260's selected graph, and restriction to
  \(Q^d\). Neither existence nor emptiness in that subclass follows
  from the ambient threshold.
- **Boundary consequence:** B281 closes the quartic half of G201, but
  G200 remains EXPLORATORY through its cubic branch. G202 is the
  smallest current separator gate.
- **Detector guard:** no relation, ODP package, Kuranishi vanishing,
  rational detector, specified pairing, cycle, proof, or disproof of HC
  is produced.
- **Re-entry condition:** exploit the B260/B264 exact-rank geometry,
  not ambient Veronese emptiness alone.
