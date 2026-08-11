---
brick_id: NG174
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex 2n-fold with very ample H and a proposed sequence of G140 point schemes Z_m
smoothness: X and every reduced Z_m are smooth; no nodal divisor or incidence smoothness is inferred
projectivity: X, all powers of H, the schemes through 3Z_m, and their value and jet evaluations are projective
dimension: dim X=2n; degree m; node count N_m; the excluded range is N_m<=m+1
codimension: asymptotic positivity separates every length-at-most-m+1 scheme and destroys the value relation required by G140
coefficient_field: C for sections, Hilbert ranks, and relations; Q detector data remain separate
cohomology_theory: zero-dimensional Castelnuovo-Mumford regularity, very-ampleness of powers, and coherent restriction
hodge_type: no rational type-(0,0) detector is produced by the excluded route
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B198, B211-B212, G140-G141, S076
claim: Obtain G140 merely by raising the polarization degree while keeping the node count bounded or at most m+1.
falsifier: B212 makes H^m separate Z_m when N_m<=m+1, so the degree-m value-relation space is zero; lower extinction also forces m<=N_m
---

# NG174 — High powers with too few nodes erase the required relation

- **Route:** use increasing positivity of \(H^m\) while keeping a fixed or
  slowly growing marked scheme \(Z_m\), and count generic interpolation as
  a construction of G140.
- **Valid input:** higher powers separate progressively longer
  zero-dimensional schemes.
- **Invalid inference:** this positivity creates the special value
  relation and adjacent fat-point defect required by G140.

B212 proves that \(H^m\) separates every scheme of length at most \(m+1\).
Thus, when \(N_m\le m+1\), evaluation on \(Z_m\) is surjective and its
value-relation space is zero. Independently, the lower \(3Z_m\) extinction
forces \(m\le N_m\). The whole range relevant to the proposed shortcut is
therefore incompatible with G140's nonzero no-coloop relation.

- **Precise obstruction:** positivity removes, rather than constructs, the
  required evaluation defect.
- **Re-entry condition:** grow \(N_m\ge m+2\), satisfy B212's exact rank
  window and relation-support bound, and retain every G141 profile and
  detector clause.
