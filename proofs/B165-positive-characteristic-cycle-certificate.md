---
brick_id: B165
status: PROVED
base_field: C
variety: a smooth complex analytic basis germ F_B carrying a rational constructible complex K_B obtained as the proper direct image of a projective hypersurface family
smoothness: F_B is smooth; a finite complex Whitney stratification adapted to every perverse cohomology sheaf is fixed after shrinking
projectivity: used only to supply constructibility and the geometric direct image; the microlocal statement itself is local on F_B
dimension: arbitrary base dimension b; every characteristic-cycle component is a b-dimensional conic Lagrangian in T^*F_B
codimension: every off-zero component is the closure of a conormal to a positive-codimension stratum
coefficient_field: Q
cohomology_theory: rational constructible derived categories, perverse cohomology, characteristic cycles, microsupport, and microlocal Morse groups
hodge_type: none asserted; the rational type-(0,0) detector condition remains separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) only downstream; no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B163-B164, S037, S066-S067
claim: For K_B in D^b_c(F_B,Q), the positive perverse characteristic cycle CC^+(K_B)=sum_j CC({}^pH^j K_B) is effective and has support SS(K_B). Hence K_B has zero internal microsupport exactly when every off-zero microlocal multiplicity of every perverse cohomology sheaf vanishes. On a sufficiently small representative this is a finite list, and each entry is falsified by a generic normal Morse group.
falsifier: a perverse characteristic cycle with a negative generic microlocal multiplicity, an SS component absent from every perverse cohomology sheaf, or a nonzero off-zero component with zero generic normal Morse group
---

# B165 — A positive characteristic-cycle certificate

Let \(M=F_B\) be a sufficiently small smooth representative and
\(K=K_B\in D_c^b(M,\mathbf Q)\). Choose one finite complex Whitney
stratification adapted to all the perverse cohomology sheaves

\[
 P_j={}^pH^j(K).
\]

For every \(P_j\), its characteristic cycle has the form

\[
 CC(P_j)=\sum_a m_{a,j}[\Lambda_a],\qquad m_{a,j}\in\mathbf Z_{\ge0},
\]

where the \(\Lambda_a\) are closures of conormals to strata. At a generic
smooth covector of \(\Lambda_a\), the microlocal index theorem identifies
\(m_{a,j}\), up to the fixed complex orientation convention, with the
dimension of the normal Morse group of \(P_j\). Perversity concentrates
that group in its normalized degree, so there is no alternating sign and
the coefficient is nonnegative.

Define the deliberately non-alternating cycle

\[
 CC^+(K)=\sum_j CC(P_j)
        =\sum_a M_a[\Lambda_a],\qquad
 M_a=\sum_j m_{a,j}\ge0. \tag{1}
\]

Perverse truncation detects microsupport:

\[
 SS(K)=\bigcup_jSS(P_j)=|CC^+(K)|. \tag{2}
\]

The zero section may occur with arbitrary positive rank. Removing that
allowed component, (1)--(2) give

\[
 SS(K)\subseteq T^*_M M
 \quad\Longleftrightarrow\quad
 M_a=0\text{ for every }\Lambda_a\not\subseteq T^*_M M. \tag{3}
\]

There are finitely many such \(\Lambda_a\) after shrinking. A generic local
holomorphic function whose differential meets one \(\Lambda_a\)
transversely and avoids the others tests \(M_a\) by its normal Morse
groups. Thus (3) is a finite, positive, falsifiable certificate rather than
an alternating Euler identity.

## Scope guard

\(CC^+\) is an auxiliary positive package, not the ordinary characteristic
cycle of the derived object in its Grothendieck group. B165 constructs no
class-directed germ, Hodge class, algebraic cycle, or nonzero Saito pairing.
