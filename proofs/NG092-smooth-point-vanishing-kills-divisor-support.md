---
brick_id: NG092
status: NO-GO
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X, its plane-net hyperplane family, and the smooth locus of a discriminant divisor D
smoothness: X and generic hyperplane fibers smooth; the tested point is smooth on D
projectivity: X and the hyperplane family projective
dimension: dim_C X = 2n; hyperplane fibers dimension 2n-1; plane base dimension 2
codimension: middle codimension n; D has base codimension one
coefficient_field: Q
cohomology_theory: rational Hodge modules, local intersection cohomology, perverse filtration, and strict-support decomposition
hodge_type: desired selected coordinate rational type (0,0) after Q(n); no coordinate is produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B008, B080-B081, B116, G077-G078
claim: B008's vanishing of the smooth-discriminant local intersection-cohomology relation group forces every divisor-supported coordinate of G077's selected class to vanish.
falsifier: B116's pure semisimple Hodge-module model with zero full-support H^(-1) stalk and nonzero divisor-supported H^(-1) stalk
---

# NG092 — Smooth-point relation vanishing does not kill divisor support

**Status:** NO-GO

- **Route:** at a generic smooth point of each discriminant divisor, apply
  B008 to obtain \(IH^1_p(\mathcal H)=0\), then conclude that the
  divisor-supported term in \(E_\infty^{-1,0}\) is zero.
- **Valid input:** B008 does annihilate the degree-\(-1\) stalk of the
  full-support intermediate extension at such a point.
- **Invalid inference:** this also annihilates the strict-support summand
  whose support is the divisor itself.
- **Precise obstruction:** B116 gives the exact pure semisimple model
  \(K=\mathbf Q_B^H[2]\oplus i_*\mathbf Q_D^H[1]\). Its full-support
  degree-\(-1\) stalk is zero while its divisor-supported degree-\(-1\)
  stalk is \(\mathbf Q\). B008 and the divisor multiplicity are different
  coordinates of the strict-support decomposition.
- **Re-entry condition:** execute G078 on the actual proper pushdown:
  restrict noncharacteristically to a generic transverse disk, isolate the
  punctual strict-support summand, and compute the selected class's
  projection to it.
