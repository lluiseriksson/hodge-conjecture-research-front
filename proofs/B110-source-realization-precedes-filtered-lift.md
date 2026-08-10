---
brick_id: B110
status: PROVED
base_field: C with all comparison vector spaces and Hodge structures over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, its B058 distributed detector, and a proposed projective plane-net collision
smoothness: X and generic hyperplane fibers smooth; the proposed target may be clean nodal; the theorem itself is exact rational linear algebra and a source-target audit
projectivity: X, the hyperplane family, and any collision used in the application must be projective
dimension: dim_C X = 2n; hyperplane fibers have dimension 2n-1; plane base dimension 2
codimension: middle codimension n; the proposed target is a point of the plane base
coefficient_field: Q
cohomology_theory: relative thimble homology, nearby and special mixed Hodge-module stalks, special-to-nearby maps, primitive ambient homology, and rational linear algebra
hodge_type: all detector, nearby, special, and ambient classes restricted to rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B057-B059, B082-B084, B109, G047-G055, G072, NG059-NG067
claim: The filtered obstruction [s] in S/(S_0+ker u) is defined for the B058 detector only after a collision-induced source realization rho sends the distributed detector t to a nearby class t_psi and t_psi is proved ordinarily liftable. Its ambient quotient and nonzero pairing do not determine either the nearby class or its liftability.
falsifier: a canonical construction of t_psi and an ordinary lift from the ambient B058 class alone, or a proof that equal ambient quotient and pairing force equal membership in im(u)
---

# B110 — Source realization precedes the filtered-lift obstruction

**Status:** PROVED

Let $C_{\mathrm{dist}}$ carry B057's selected distributed class $t$, let
$A$ be the primitive ambient target, and let

\[
 q_C:H(C_{\mathrm{dist}})\longrightarrow A
\]

be the composite of the two B022 quotients. For an actual collision, the
filtered obstruction of B109 requires additional data

\[
 \rho:H(C_{\mathrm{dist}})\longrightarrow P_\psi,
 \qquad
 u:S\longrightarrow P_\psi,
 \qquad
 t_\psi=\rho(t)\in\operatorname{im}u.
\]

Only after choosing $s\in S$ with $u(s)=t_\psi$ is

\[
 [s]\in S/(S_0+\ker u)
\]

defined. B022 provides $q_C$, not the reverse or lateral arrow $\rho$.
B084 supplies an ordinary lift only after an actual nearby class has been
placed in its proper intersection-cohomology model and proved invariant
under collision monodromy. Thus G072 cannot construct its own input merely
by naming the ambient detector $c=q_C(t)$.

## Exact countermodel

Take pure Tate rational vector spaces

\[
 C=\mathbf Q t,
 \quad A=\mathbf Q c,
 \quad S=\mathbf Q s,
 \quad P=\mathbf Q x\oplus\mathbf Q y,
\]

with

\[
 q_C(t)=c,
 \qquad u(s)=x,
 \qquad q_P(x)=q_P(y)=c.
\]

There are two source realizations preserving exactly the same nonzero
ambient value and hence every fixed nonzero pairing with it:

\[
 \rho_0(t)=x,
 \qquad
 \rho_1(t)=y.
\]

The first nearby class lies in $\operatorname{im}u$ and has an ordinary
lift; the second does not. Therefore even exact ambient recovery, not merely
a nonzero pairing, does not determine ordinary liftability. It follows a
fortiori that it does not determine B109's filtered-lift class.

## Dependency correction

G072 remains the exact filtered calculation once its inputs exist, but it is
not the first attackable geometric gate. G073 must first construct a
collision-certified realization of the selected class, its nearby class, and
an ordinary lift while retaining a nonzero prescribed pairing. B111 shows
that a map on every unrelated distributed class is unnecessary. This is the
typed core of G047-G049 and the topology-changing correction sought in G055.

## Scope guard

B110 is a dependency and non-implication theorem. It constructs no collision,
nearby class, local relation, or algebraic cycle and therefore gives no
actual progress toward the general Hodge Conjecture.
