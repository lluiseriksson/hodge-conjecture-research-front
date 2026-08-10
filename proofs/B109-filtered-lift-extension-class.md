---
brick_id: B109
status: PROVED
base_field: C with filtered rational vector spaces and Hodge structures over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, an actual projective plane-net collision, and its filtered special-to-nearby stalk map
smoothness: X and generic hyperplane fibers smooth; target clean nodal; the theorem is exact filtered linear algebra
projectivity: X, hyperplane family, and collision projective in the application
dimension: dim_C X = 2n; hyperplane fibers have dimension 2n-1; plane base dimension 2
codimension: middle codimension n; target is a point of the plane base with finite nodal singular support
coefficient_field: Q
cohomology_theory: perverse-filtered stalks, quotient and dual vector spaces, associated-graded maps, and extension data between filtration grades
hodge_type: all spaces, maps, and detector classes restricted to rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B081, B107-B108, G071, S037
claim: For any ordinary lift s of t, omega_fil(t) corresponds canonically to [s] in S/(S_0+ker u), and it is nonzero exactly when a dual functional annihilates u(S_0) but not t. The associated-graded maps of u do not determine this class because off-diagonal filtration-extension data can change filtered liftability while leaving every graded map fixed.
falsifier: lift-dependence of [s] modulo S_0+ker u, failure of the quotient isomorphism, failure of the dual separation criterion, or identical filtered graded maps forcing identical omega_fil in the explicit model
---

# B109 — The filtered obstruction is an off-diagonal extension class

**Status:** PROVED

Let $u:S\to P$, let $S_0\subseteq S$ be B107's canonical filtration step,
and let $t\in\operatorname{im}u$. The first isomorphism theorem induces

\[
 \frac{S}{S_0+\ker u}
 \xrightarrow{\sim}
 \frac{\operatorname{im}u}{u(S_0)},
 \qquad
 [s]\longmapsto[u(s)].
\]

Indeed, the map is surjective and its kernel is precisely
$S_0+\ker u$. For any ordinary lift $u(s)=t$, B108's obstruction therefore
corresponds to

\[
 \widetilde\omega_{\mathrm{fil}}(t)
 =[s]\in S/(S_0+\ker u).
\]

Changing $s$ by an element of $\ker u$ does not change this class. Its
vanishing is exactly the existence of $s_0\in S_0$ with $u(s_0)=t$.

Finite-dimensional duality gives the equivalent witness:

\[
 \omega_{\mathrm{fil}}(t)\ne0
\]

if and only if there is
$\ell\in(\operatorname{im}u)^*$ such that

\[
 \ell(u(S_0))=0,
 \qquad
 \ell(t)\ne0.
\]

Thus either an explicit corrected lift or one separating functional decides
the obstruction.

## Associated grades are insufficient

Let

\[
 S=\mathbf Q a\oplus\mathbf Q b\oplus\mathbf Q e,
 \qquad
 F_{-1}S=\mathbf Q a,
 \qquad
 S_0=F_0S=\mathbf Q a\oplus\mathbf Q b,
\]

and

\[
 P=F_0P=\mathbf Q x\oplus\mathbf Q y,
 \qquad
 F_{-1}P=\mathbf Q x.
\]

For $c\in\mathbf Q$, define the filtered map

\[
 u_c(a)=0,
 \qquad
 u_c(b)=y+cx,
 \qquad
 u_c(e)=x.
\]

Every associated-graded map is independent of $c$:

- on grade $-1$, $a\mapsto0$;
- on grade $0$, $b\mapsto y\bmod\mathbf Qx$;
- on the higher grade, $e$ maps to zero because $P=F_0P$.

Fix $t=y$. For $c=0$, $t=u_0(b)$ has a filtered lift. For $c=1$,
$t=u_1(b-e)$ has an ordinary lift but

\[
 u_1(S_0)=\mathbf Q(y+x),
 \qquad y\notin u_1(S_0).
\]

Hence $\omega_{\mathrm{fil}}(t)$ is zero for $u_0$ and nonzero for $u_1$,
although all associated-graded maps agree. The missing datum is the
off-diagonal coefficient $c$, i.e. the extension data between filtration
grades.

## Scope guard

B109 does not compute the off-diagonal extension for the actual collision.
It proves that ranks, support dimensions, and the $E_\infty$ maps alone cannot
close G071.

