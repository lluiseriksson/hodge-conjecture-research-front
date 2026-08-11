---
brick_id: G144
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex 2n-fold with very ample H, a specified primitive rational middle Hodge class, and a class-directed reduced point scheme Z
smoothness: X and Z are smooth; the central degree-m section must have isolated ODPs and reduced incidence smoothness remains downstream
projectivity: X, all H^k through m, mixed finite jet schemes, the full tangent system, Z through 3Z, and the detector family are projective
dimension: dim X=2n; c_(2n)=binom(2n+2,2); length Z=N>=D_(2n)(m) from B215
codimension: realize G143 inside the simultaneous mixed-second-jet interpolation window while retaining the strongly defective adjacent profile
coefficient_field: C for sections, jets, values, relations, ranks, profiles, and Kuranishi tensors; Q for the Hodge class, detector, and specified pairing
cohomology_theory: coherent mixed-jet interpolation, principal parts through order two, graded value multiplication, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the detector must be rational type (0,0) with nonzero pairing against the specified class
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B215, G013, G090-G143, NG106-NG177, S065-S076
claim: For arbitrary (X,zeta), construct every G143 clause with N>=D_(2n)(m) from B215, lower ranks at least L_(2n)(k) in every 2<=k<m, all complementary relation-transport maps, the distinguished central profile, G130 holonomy and congruence, and every rational detector clause.
falsifier: a node count below D_(2n)(m), failure of a mixed-jet rank or relation-transport map, a degenerate profile, failure of G130, or loss of any detector clause
---

# G144 — Construct inside the simultaneous second-jet window

Let

\[
 c_{2n}=\binom{2n+2}{2}.
\]

For arbitrary \((X,\zeta)\), construct the complete G143 package with

\[
 N\ge D_{2n}(2)=2(2n+1), \tag{1}
\]

and, for \(m\ge3\),

\[
 N\ge D_{2n}(m)=
 \begin{cases}
 c_{2n}m/3+2n+1,&3\mid m,\\
 c_{2n}\left\lfloor\dfrac{m+2}{3}\right\rfloor
 +((m+2)\bmod3),&3\nmid m.
 \end{cases} \tag{2}
\]

Every lower degree \(2\le k<m\) must have point-span rank at least

\[
 L_{2n}(k)=
 c_{2n}\left\lfloor\frac{k+1}{3}\right\rfloor
 +((k+1)\bmod3), \tag{3}
\]

and the same full-support degree-\(m\) relation must realize every B213
transport map.

These numerical obligations do not replace the adjacent fat-point birth,
distinguished nondegenerate central profile, G130 congruence and holonomy,
full system, rational detector, specified pairing, pure cubic closure, or
later Kuranishi rungs.
