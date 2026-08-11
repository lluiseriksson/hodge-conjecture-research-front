---
brick_id: NG175
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex 2n-fold with G141's proposed point scheme and no-coloop degree-m value matroid
smoothness: X and Z are smooth; no ODP divisor or incidence smoothness is inferred
projectivity: X, powers H^k through m, point evaluations, and graded multiplication are projective coherent data
dimension: dim X=2n; the excluded node range is m+2<=N<2n+1+max(m,2n+1)
codimension: B212's individual Hilbert-rank window omits the cross-degree constraints forced by one full-support degree-m relation
coefficient_field: C for value spaces and relations; Q detector data remain separate
cohomology_theory: coherent section multiplication, value-matroid duality, and tangent-span absorption
hodge_type: no rational type-(0,0) detector is produced by the excluded numerical route
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B187, B196-B197, B212-B213, G141-G142
claim: Treat satisfaction of B212's separate adjacent rank bounds as sufficient numerical feasibility for G141 while ignoring multiplication of its full-support relation.
falsifier: B213 injects E_a into R_(m-a) and forces N>=2n+1+max(m,2n+1), excluding the displayed range
---

# NG175 — Separate Hilbert bounds miss relation transport

- **Route:** choose ranks satisfying B212 and search for G141 anywhere in
  the interval \(N\ge m+2\), without coupling different degrees.
- **Valid input:** B212 gives necessary individual ranks in degrees
  \(m-1\) and \(m\).
- **Invalid inference:** those ranks can be chosen independently of the
  degree-\(m\) value relation.

A no-coloop value matroid supplies a full-support relation
\(\lambda\). B213 shows that multiplication by \(\lambda\) injects every
\(E_a\) into \(\mathcal R_{m-a}\). Tangent absorption at the two endpoint
degrees then forces

\[
 N\ge2n+1+\max\{m,2n+1\}. \tag{1}
\]

Thus the entire range

\[
 m+2\le N<2n+1+\max\{m,2n+1\} \tag{2}
\]

is impossible even before imposing the central profile or detector.

- **Precise obstruction:** cross-degree multiplication, absent from the
  separate B212 table.
- **Re-entry condition:** construct the actual B213 transport package in
  G142 and retain every profile and detector clause.
