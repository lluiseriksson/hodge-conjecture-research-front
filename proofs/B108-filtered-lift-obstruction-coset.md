---
brick_id: B108
status: PROVED
base_field: C with filtered rational Hodge structures and maps over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a projective plane-net collision, its special-to-nearby stalk map, and a clean nodal target
smoothness: X and generic hyperplane fibers smooth; target clean nodal; the exact theorem is filtered linear algebra
projectivity: X, hyperplane family, and collision projective in the application
dimension: dim_C X = 2n; hyperplane fibers have dimension 2n-1; plane base dimension 2
codimension: middle codimension n; target is a point of the plane base with finite nodal singular support
coefficient_field: Q
cohomology_theory: perverse-filtered special stalks, nearby cycles, images and quotient vector spaces, pure rational Hodge structures, and local invariant cycles
hodge_type: all spaces and the specified nearby detector restricted to rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B081, B083-B084, B107, G070, S037
claim: For u:S->P and the canonical relation-grade filtration step S_0, an ordinarily liftable nearby class t has a filtered lift exactly when its canonical coset omega_fil(t)=[t] in im(u)/u(S_0) vanishes. Local invariant-cycle surjectivity and purity of rational Hodge structures do not force this coset to vanish.
falsifier: dependence of the quotient coset on a chosen ordinary lift, coset vanishing without a lift in S_0, or a theorem under B084's printed hypotheses forcing u(S_0)=im(u)
---

# B108 — Filtered liftability is one quotient coset

**Status:** PROVED

Let

\[
 u:S\longrightarrow P
\]

be the type-$(0,0)$ special-to-nearby map, and let $S_0\subseteq S$ be
B107's canonical relation-grade filtration step. For an ordinarily liftable
nearby class $t\in\operatorname{im}u$, define

\[
 \omega_{\mathrm{fil}}(t)
 :=[t]\in\operatorname{im}u/u(S_0).
\]

This class uses only $t$, $u$, and the canonical subspace $S_0$; it is
independent of any chosen lift.

By definition,

\[
 \omega_{\mathrm{fil}}(t)=0
 \quad\Longleftrightarrow\quad
 t\in u(S_0).
\]

The right-hand side is exactly existence of a filtered lift. Thus the first
obligation in G070 is neither a choice nor an unspecified spectral-sequence
condition: it is vanishing of one canonical quotient class.

## Why ordinary liftability and Hodge strictness do not kill it

Take pure type-$(0,0)$ rational Hodge structures

\[
 S=\mathbf Qe_0\oplus\mathbf Qe_1,
 \qquad P=\mathbf Qf_0\oplus\mathbf Qf_1,
 \qquad S_0=\mathbf Qe_0,
\]

and the Hodge morphism

\[
 u(e_0)=0,
 \qquad u(e_1)=f_0.
\]

Then $t=f_0$ lies in $\operatorname{im}u$ and has an ordinary lift $e_1$,
but

\[
 u(S_0)=0,
 \qquad
 \omega_{\mathrm{fil}}(t)=f_0\ne0.
\]

Every Hodge and weight filtration here is pure and strict. The failure is in
the independent perverse filtration represented by $S_0$. Therefore strictness
of rational mixed-Hodge morphisms for their Hodge filtration does not imply
the perverse strictness needed by G070.

If a target filtration step $P_0$ is fixed with $u(S_0)\subseteq P_0$ and
$t\in P_0$, strictness at that step would state

\[
 \operatorname{im}u\cap P_0=u(S_0)
\]

and would kill the obstruction. B084's local invariant-cycle theorem asserts
surjectivity onto monodromy invariants, not this filtered equality.

## Scope guard

B108 does not compute $\omega_{\mathrm{fil}}(t_\psi)$ for the actual
collision. It proves the exact computation required before G070's dual
certificate is defined.

