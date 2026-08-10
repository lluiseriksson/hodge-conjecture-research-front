---
brick_id: B106
status: PROVED
base_field: C with all Hodge structures, stalks, and linear maps over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a specified nonzero primitive rational middle Hodge class zeta, a global B058 detector c, and a projective collision to a clean nodal hyperplane target
smoothness: X and generic hyperplane fibers smooth; target has finitely many ordinary double points
projectivity: X, its plane-net hyperplane family, and the collision projective
dimension: dim_C X = 2n; hyperplane fibers have dimension 2n-1
codimension: middle codimension n; target singular support finite
coefficient_field: Q
cohomology_theory: primitive Hodge pairing, Saito relation classes, nearby/special type-(0,0) stalks, lift torsors, and dual exact sequences
hodge_type: zeta, c, special lifts, local relations, and ambient detector classes rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B010, B058, B094-B096, B105, G059, S022-S023
claim: B105's inequality D_zeta(c,beta) != <zeta,c> cancels c identically and is exactly Saito's terminal pairing condition; it therefore carries no collision provenance by itself. On any canonically defined collision domain, B095's dual alternative—nonzero [F] in coker(u^*) or zero [F] with nonzero descended evaluation on t_psi—is the exact detector certificate; B107/G070 correct that domain to the relevant perverse-filtration step.
falsifier: dependence of B105's inequality on the chosen c, or finite-dimensional exact collision data in which a detecting special lift exists while both G059 branches fail, or conversely
---

# B106 — Cancel the auxiliary detector and restore the exact collision branch

**Status:** PROVED

## The detector cancels from G069

For any primitive rational Hodge-homology class $c$, put

\[
 b_c=\langle\zeta,c\rangle,
 \qquad
 D_\zeta(c,\beta)
 =\langle\zeta,c-\Phi_{Y_0}(\beta)\rangle.
\]

Then

\[
 D_\zeta(c,\beta)=b_c-\langle\zeta,\Phi_{Y_0}(\beta)\rangle,
\]

so

\[
 D_\zeta(c,\beta)\ne b_c
 \quad\Longleftrightarrow\quad
 \langle\zeta,\Phi_{Y_0}(\beta)\rangle\ne0.
\]

The right-hand side contains no $c$. Thus G069's scalar formulation is
exactly B010's terminal Saito condition for the chosen relation. Labeling the
scalar by B058's detector does not prove that the relation was obtained from
that detector or from any collision comparison. S023 supplies the global
tube class but, as its audited scope states, no map to a single Saito local
relation.

## Exact collision certificate

Retain the actual type-$(0,0)$ collision map

\[
 u:S\longrightarrow P
\]

and the specified nearby class $t_\psi\in\operatorname{im}u$. Let
$F\in S^*$ be the canonical Saito-pairing functional. For one lift $s_0$,
the lift torsor is

\[
 \mathcal L=s_0+\ker u.
\]

There is a detecting lift $s\in\mathcal L$ with $F(s)\ne0$ exactly when

\[
 F(s_0)\ne0
 \quad\text{or}\quad
 F(\ker u)\ne0.
\]

Dual exactness gives the intrinsic B095/G059 form:

\[
 \boxed{
 [F]\ne0\text{ in }\operatorname{coker}(u^*)
 \quad\text{or}\quad
 [F]=0\text{ and }\lambda(t_\psi)\ne0,
 }
\]

where $F=u^*\lambda$ in the second branch. If $[F]\ne0$, varying a lift
along $\ker u$ already produces a nonzero value. If $[F]=0$, every lift has
the common value $\lambda(t_\psi)$. These two cases are exhaustive and the
displayed disjunction is necessary and sufficient for a detecting special
lift.

Consequently G060-G068 remain valid sufficient attempts to prove the
descended second branch. B107 subsequently observes that G059 placed $F$ on
too large a domain: its exact alternative must be applied to the canonical
perverse-filtration step. G070 retains both branches there without forgetting
collision provenance.

## Scope guard

B106 is exact linear algebra plus an endpoint audit. It does not construct
the collision map $u$, the class $t_\psi$, or the functional $F$, and it does
not prove either G059 branch for arbitrary $X$ and $\zeta$.
