---
brick_id: B209
status: PROVED
base_field: C
variety: a smooth projective complex variety with very ample H and a nonempty finite reduced point scheme Z
smoothness: X and Z are smooth; no nodal divisor or incidence smoothness is inferred
projectivity: X, all powers of H through degree m, and the first three infinitesimal neighborhoods of Z are projective coherent data
dimension: dim X=d; V_k measures conditional first jets and W_k measures quadratic profiles
codimension: simultaneous extinction of both conormal layers below m is equivalent to their vanishing in the single adjacent degree m-1
coefficient_field: C for sections, jets, profiles, and multiplication; Q remains required separately for the detector
cohomology_theory: coherent first and second jets, finite point evaluation, and graded section multiplication
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B194-B208 and G125-G138
claim: For m>=2, V_k=W_k=0 for every 0<=k<m if and only if V_(m-1)=W_(m-1)=0. Equivalently, the equalities H0(I_Z H^k)=H0(I_Z^2 H^k)=H0(I_Z^3 H^k) in every lower degree reduce to the single adjacent degree m-1.
falsifier: a lower nonzero V_k or W_k with both adjacent spaces zero, failure of multiplication by a section nowhere zero on Z to inject either quotient, or adjacent vanishing without equality of the three degree-(m-1) section spaces
---

# B209 — Two-layer extinction is an adjacent condition

Put

\[
 J_k=H^0(I_ZH^k),\qquad
 K_k=H^0(I_Z^2H^k),\qquad
 T_k=H^0(I_Z^3H^k).
\]

Then

\[
 V_k=J_k/K_k,\qquad W_k=K_k/T_k. \tag{1}
\]

B197 proves that multiplication by a section of a positive power of \(H\)
which is nowhere zero on \(Z\) injects \(V_k\) into every higher \(V_j\).
B204 proves the identical injection for \(W_k\). Such a multiplier exists
because the base field is infinite, \(H\) is globally generated, and \(Z\)
is finite.

Consequently, for \(m\ge2\),

\[
 V_{m-1}=W_{m-1}=0
 \quad\Longleftrightarrow\quad
 V_k=W_k=0\quad(0\le k<m). \tag{2}
\]

Using (1), equation (2) is equivalent to

\[
 J_k=K_k=T_k\quad(0\le k<m). \tag{3}
\]

Thus G138's entire lower ladder is one adjacent two-layer condition. B209
does not construct the adjacent vanishing, the degree-\(m\) jump, the ODP
package, a detector, or a cycle.
