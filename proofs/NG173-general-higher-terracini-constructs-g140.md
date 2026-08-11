---
brick_id: NG173
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex 2n-fold with G140's special class-directed point scheme, compared with the general-point secant and osculating settings of S075
smoothness: the varieties in S075 are integral projective and the relevant points are general; G140 additionally needs smooth marked points and an isolated-ODP central section
projectivity: both settings use projective osculating spaces, but S075 studies osculating spaces of joins and secant varieties rather than containment in the point span across adjacent embeddings
dimension: G140 is arbitrary even dimension; S075's explicit interpolation applications concern Veronese surfaces or projective 3-space
codimension: general-point higher Terracini statements do not produce the extreme conditional rank defects d(N-1) and d(d+1)N/2-1
coefficient_field: C, matching S075; Q detector data are absent from S075
cohomology_theory: projective osculating and secant geometry versus class-directed fat-point restriction ranks and Hodge detectors
hodge_type: S075 supplies no rational type-(0,0) class-specific detector
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B210-B211, G139-G140, NG172, S075
claim: Invoke S075's higher Terracini lemmas or a general-point maximal-rank interpolation result as a construction of G140.
falsifier: S075 computes general secant/osculating geometry, while G140 requires a special point span absorbing second osculators and the nonmaximal adjacent signature (0,0) to (2n,1)
---

# NG173 — General higher Terracini theory does not construct G140

- **Route:** apply a higher Terracini lemma to general marked points and
  count its osculating-span formula as G140.
- **Valid input:** S075 relates osculating spaces of joins or secant
  varieties to spans of osculating spaces at general points.
- **Invalid inference:** the span of the point lines already contains all
  second osculating spaces and undergoes G140's adjacent rank jump.

B211 shows that G140 requires conditional first- and second-order defects

\[
 d(N-1),\qquad \binom{d+1}{2}N-1. \tag{1}
\]

A maximal-rank general-point construction gives the opposite regime:
conditional increments \(dN\) and \(\binom{d+1}{2}N\), not \(d\) and \(1\).
S075 also fixes general points in one embedding and studies the secant or
join built from them; it supplies no adjacent \(H^{m-1}\to H^m\)
comparison, distinguished central profile, or Hodge detector.

- **Precise obstruction:** the theorem's generality hypothesis excludes
  the extreme special dependence G140 is designed to construct.
- **Re-entry condition:** prove a special-point higher-contact theorem with
  the exact adjacent signature and every class-directed detector clause.
