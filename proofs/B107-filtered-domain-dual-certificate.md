---
brick_id: B107
status: PROVED
base_field: C with filtered rational Hodge structures and all maps over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a projective plane-net collision, its special and nearby stalks, and a clean nodal target H
smoothness: X and generic hyperplane fibers smooth; target has finitely many ordinary double points; the exact theorem is filtered linear algebra
projectivity: X, the hyperplane family, and collision projective in the application
dimension: dim_C X = 2n; hyperplane fibers have dimension 2n-1; plane base dimension 2
codimension: middle codimension n; target H is a point of the plane base with finite nodal singular support
coefficient_field: Q
cohomology_theory: perverse filtration, associated-graded stalks, strict-support decomposition, nearby/special maps, dual vector spaces, and Saito's primitive pairing
hodge_type: all domains, maps, relation coordinates, and functionals restricted to rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B010, B081, B083, B093-B095, B106, B134, G057-G059, NG069, NG107, S037
claim: The perverse associated grade canonically maps the relevant filtration step S_0 to the dual relation space R(H)^vee, not to R(H); after an actual relation beta is selected, evaluation defines F_(0,beta) on S_0 and B095's exact lift certificate applies to u_0 and F_(0,beta), while neither the total-stalk projection nor beta is supplied by the filtration.
falsifier: a canonical map from the cohomological associated grade to an unpolarized relation vector without dualization, an admissible filtered lift outside im(u_0), or filtered finite-dimensional data for which the u_0 dual alternative disagrees with direct evaluation after beta is fixed
---

# B107 — The dual certificate lives on the filtered domain

**Status:** PROVED

Let

\[
 S=H^{-1}(i_H^*K)^{(0,0)}
\]

be the special stalk with its canonical perverse filtration. Write $S_0$ for
the filtration step whose quotient by the preceding step $S_{<0}$ is the
relevant grade

\[
 S_0/S_{<0}=E_\infty^{-1,0}.
\]

The index $0$ is only a name for this step and avoids changing conventions
between increasing and decreasing perverse filtrations.

B081 gives the quotient $S_0\to S_0/S_{<0}$ canonically. Inside that grade,
the strict-support decomposition canonically projects to the full-support
summand, and B093/B134 identify its stalk with the **dual** relation space.
Hence there is a canonical map

\[
 r^\vee:S_0\longrightarrow R(H)_1^{(0,0),\vee}.
\]

Only after choosing an actual relation

\[
 \beta\in R(H)_1^{(0,0)}
\]

does evaluation give a scalar functional

\[
 F_{0,\beta}(s)=r^\vee(s)(\beta):S_0\longrightarrow\mathbf Q.
\]

Perverse filtration does not select \(\beta\). NG107 forbids manufacturing
one by treating the cohomological stalk as its homological dual.

## No canonical extension to the total stalk

Perverse filtration does not give a map $S\to S_0/S_{<0}$. It gives a map
only from $S_0$. Even after \(\beta\) is supplied, extending
$F_{0,\beta}$ to $S$ requires choosing a complement. In
the elementary model

\[
 S=\mathbf Qe\oplus\mathbf Qz,
 \qquad S_0=\mathbf Qe,
 \qquad F_0(e)=1,
\]

every formula

\[
 F_a(xe+yz)=x+ay,
 \qquad a\in\mathbf Q,
\]

extends $F_0$. The filtered and associated-graded data distinguish none of
them. This is exactly the noncanonical-splitting warning of B081/S037.

Therefore G059's notation $F\in S^*$ is not canonical unless it first proves
$S_0=S$, chooses extra data and audits choice-independence, or restricts the
domain.

## Correct lift and dual criterion

Let

\[
 u:S\longrightarrow P_\psi
\]

be the special-to-nearby map and set $u_0=u|_{S_0}$. A nearby detector
$t_\psi$ has a lift whose relation grade is canonically defined exactly when

\[
 t_\psi\in\operatorname{im}u_0.
\]

If this holds, its admissible lift set is the affine torsor

\[
 \mathcal L_0=u_0^{-1}(t_\psi)
 =s_0+(\ker u\cap S_0).
\]

Apply B095 to $u_0:S_0\to P_\psi$ and
$F_{0,\beta}\in S_0^*$. A detecting
admissible lift exists exactly in the two disjoint cases

\[
 \boxed{
 [F_{0,\beta}]\ne0\text{ in }\operatorname{coker}(u_0^*)
 \quad\text{or}\quad
 [F_{0,\beta}]=0\text{ and }\lambda(t_\psi)\ne0,
 }
\]

where $F_{0,\beta}=u_0^*\lambda$ in the second branch. The value on $t_\psi$ is
independent of the choice of $\lambda$ because $t_\psi\in\operatorname{im}u_0$.

## Scope guard

B107 does not select \(\beta\), prove
$t_\psi\in\operatorname{im}u_0$, or compute either dual branch. It corrects
both the domain and the intrinsic dual typing of those obligations.
