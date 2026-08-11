---
brick_id: G142
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex 2n-fold with very ample H, a specified primitive rational middle Hodge class, and a class-directed reduced point scheme Z
smoothness: X and Z are smooth; the central degree-m section must have isolated ODPs and reduced incidence smoothness remains downstream
projectivity: X, every H^k through m, the schemes Z through 3Z, the full tangent system, and detector family are projective
dimension: dim X=2n; length Z=N>=2n+1+max(m,2n+1); every complementary pair of value ranks has sum at most N
codimension: realize G141 together with B213's full-support relation-transport injections in every complementary degree
coefficient_field: C for sections, values, relations, jets, profiles, and Kuranishi tensors; Q for the Hodge class, detector, and specified pairing
cohomology_theory: graded value multiplication, fat-point interpolation, principal parts through order two, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the detector must be rational type (0,0) with nonzero pairing against the specified class
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B213, G013, G090-G141, NG106-NG175, S065-S076
claim: For arbitrary (X,zeta), construct all G141 data with N>=2n+1+max(m,2n+1) and h_Z(a)+h_Z(m-a)<=N for every 1<=a<m, realized by one full-support degree-m relation under the exact B213 transport maps, while retaining the distinguished ODP profile, G130 holonomy and congruence, and every rational detector clause.
falsifier: failure of a complementary-rank inequality or transport map, node count below the B213 floor, a value coloop, a degenerate profile, failure of G130, or loss of any detector clause
---

# G142 — Construct the relation-transport critical window

For arbitrary \((X,\zeta)\), construct the complete G141 package with

\[
 N\ge 2n+1+\max\{m,2n+1\}. \tag{1}
\]

For one full-support degree-\(m\) value relation \(\lambda\), require the
actual multiplication-induced injections

\[
 E_a\hookrightarrow\mathcal R_{m-a},\qquad
 e\longmapsto\bigl[x\mapsto\lambda(ex)\bigr]
 \qquad(1\le a<m), \tag{2}
\]

and hence

\[
 h_Z(a)+h_Z(m-a)\le N. \tag{3}
\]

Equations (1)--(3) are necessary shadows of G141, not substitutes for its
adjacent \(Z\subset2Z\subset3Z\) table. The distinguished nondegenerate
central profile, full-system congruence and holonomy, no-coloop rational
detector, specified pairing, pure cubic closure, and later rungs all
remain mandatory.
