---
brick_id: G143
status: EXPLORATORY
base_field: C
variety: an arbitrary smooth projective complex 2n-fold with very ample H, a specified primitive rational middle Hodge class, and a class-directed reduced point scheme Z
smoothness: X and Z are smooth; the central degree-m section must have isolated ODPs and reduced incidence smoothness remains downstream
projectivity: X, all H^k through m, full point and jet systems, Z through 3Z, and the detector family are projective
dimension: dim X=2n; c_(2n)=binom(2n+2,2); length Z=N>=C_(2n)(m) from B214
codimension: realize G142 inside the universal full-second-jet transport window while retaining the strongly defective adjacent profile
coefficient_field: C for sections, jets, relations, ranks, profiles, and Kuranishi tensors; Q for the Hodge class, detector, and specified pairing
cohomology_theory: principal parts through order two, graded value multiplication, fat-point interpolation, primitive rational cohomology, vanishing cycles, and Saito pairing
hodge_type: the detector must be rational type (0,0) with nonzero pairing against the specified class
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); algebraicity of the input class is not assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007-B010, B134-B215, G013, G090-G142, NG106-NG177, S065-S076
claim: For arbitrary (X,zeta), construct every G142 clause with N>=C_(2n)(m), where C_d(2)=2(d+1), C_d(3)=binom(d+2,2)+d+1, and C_d(m)=binom(d+2,2)+max(binom(d+2,2),m-1) for m>=4, and realize the lower full second-osculating absorption, complementary relation transport, central profile, holonomy, congruence, and rational detector simultaneously.
falsifier: a node count below C_(2n)(m), failure of full lower second-osculating absorption or relation transport, a degenerate profile, failure of G130, or loss of any detector clause
---

# G143 — Construct inside the full second-jet transport window

Let

\[
 c_{2n}=\binom{2n+2}{2}.
\]

For arbitrary \((X,\zeta)\), construct the complete G142 package with

\[
 N\ge C_{2n}(m)=
 \begin{cases}
 2(2n+1),&m=2,\\
 c_{2n}+2n+1,&m=3,\\
 c_{2n}+\max\{c_{2n},m-1\},&m\ge4.
 \end{cases} \tag{1}
\]

The lower degree point spans must absorb the full \(c_{2n}\)-dimensional
second osculator in every degree \(2\le k<m\). The same full-support
degree-\(m\) relation must realize all B213 complementary transport maps.

Equation (1) is necessary only. The adjacent rank birth, distinguished
nondegenerate central profile, G130 congruence and holonomy, full system,
rational detector, specified pairing, pure cubic closure, and later
Kuranishi rungs remain mandatory.

B215 simultaneously interpolates several triple neighborhoods and
residual reduced points. It replaces the pointwise floor \(C_{2n}(m)\)
by the stronger \(D_{2n}(m)\) and the lower-rank function
\(L_{2n}(k)\). G144 is the refined gate; NG177 closes the interval left
by counting one second osculator at a time.
