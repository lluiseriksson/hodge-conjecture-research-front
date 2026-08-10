---
brick_id: G083
status: EXPLORATORY
base_field: C with all chain, Hodge, and filtration data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a specified primitive rational Hodge class zeta, its selected B058 detector, the original plane-net incidence family, and one transverse marked disk through a clean nodal target
smoothness: X, original incidence total space, and disk pullback total space smooth; nearby fibers smooth; central fiber clean nodal
projectivity: X, plane net, incidence family, and algebraic curve base change projective
dimension: dim_C X=2n; hyperplane fibers d=2n-1; plane base dimension 2; disk dimension 1
codimension: middle cycle codimension n; target is a point of the plane base
coefficient_field: Q
cohomology_theory: B022 relative thimble quotients, disk nearby cycles, special/nearby maps, canonical plane perverse filtration, and strict support
hodge_type: the total nearby class and ordinary lift need not be type (0,0); a lift in S_0 has a clean-nodal relation quotient of type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B057-B059, B083-B084, B092-B093, B107-B109, B117-B122, G071-G082, NG095-NG098, S022, S037
claim: Realize the selected B058 detector as a nonzero rational disk-nearby class t_Delta surviving both B022 quotients with the prescribed nonzero pairing, and prove the filtered obstruction omega_fil(t_Delta) vanishes so that t_Delta has a lift in the relation filtration step S_0.
falsifier: undefined selected chain-to-nearby map, zero image in either B022 quotient, zero prescribed pairing, or nonzero omega_fil(t_Delta) for every admissible transverse original disk
---

# G083 — Construct a selected relation-filtered disk lift

**Status:** EXPLORATORY

**Parent gates:** G071 / G080

On one B120 transverse original disk, construct

\[
 0\ne t_\Delta\in H^0(i_p^*\Psi K_\Delta)
\]

from the selected B058 distributed chain and prove that its image after both
B022 quotients is the prescribed primitive detector \(c\), with

\[
 \langle\zeta,c\rangle\ne0.
\]

B122 already supplies an ordinary special lift. Let

\[
 u_\Delta:S=H^{-1}(i_p^*K_B)\longrightarrow P_\Delta
\]

be the special-to-disk-nearby map under B120's shift, and let \(S_0\) be
B107's canonical relation filtration step. The exact remaining condition is

\[
 \omega_{\mathrm{fil}}(t_\Delta)
 =[t_\Delta]
 \in
 \operatorname{im}u_\Delta/u_\Delta(S_0)
\]

and the target theorem is

\[
 \boxed{\omega_{\mathrm{fil}}(t_\Delta)=0.}
\]

Equivalently, construct \(\beta_0\in S_0\) with

\[
 u_\Delta(\beta_0)=t_\Delta.
\]

Then B117 removes divisor support, B118 removes point support, and the
conditional B119 conclusion makes the nonzero relation coordinate
full-support and type \((0,0)\) after \(\mathbf Q(n)\).

## Current obstruction

The disk's ordinary specialization map is surjective, so neither cyclic
monodromy nor total-lift existence remains. The missing datum is the
off-diagonal extension between the constant
\(E_\infty^{-2,1}\) grade and the relation
\(E_\infty^{-1,0}\) grade for the *selected* class. B109 proves that
associated-graded ranks do not determine it. A valid computation must print
the actual filtered special-to-nearby matrix, the selected vector, and either
an explicit filtered lift or a proof that every B109 separating functional
vanishes on that vector.
