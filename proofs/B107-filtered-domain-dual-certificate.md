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
dependencies: B010, B081, B083, B093-B095, B106, G057-G059, NG069, S037
claim: The perverse associated grade defines the Saito detector functional canonically only on the relevant filtration step S_0, not on the entire special stalk S. A nearby class has an admissible relation-grade lift exactly when it lies in the image of u_0=u|_(S_0), and then B095's exact dual certificate must be formed with u_0 and F_0 on S_0.
falsifier: a canonical total-stalk projection supplied by perverse filtration alone, an admissible filtered lift outside im(u_0), or filtered finite-dimensional data for which the u_0 dual alternative disagrees with direct evaluation on the filtered lift torsor
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
summand, and B093 identifies its stalk with the relation space. Hence there
is a canonical map

\[
 r:S_0\longrightarrow R(H)_1^{(0,0)}.
\]

Composing with Saito's ambient map and pairing with the specified primitive
Hodge class gives

\[
 F_0:S_0\longrightarrow\mathbf Q.
\]

## No canonical extension to the total stalk

Perverse filtration does not give a map $S\to S_0/S_{<0}$. It gives a map
only from $S_0$. Extending $F_0$ to $S$ requires choosing a complement. In
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

Apply B095 to $u_0:S_0\to P_\psi$ and $F_0\in S_0^*$. A detecting
admissible lift exists exactly in the two disjoint cases

\[
 \boxed{
 [F_0]\ne0\text{ in }\operatorname{coker}(u_0^*)
 \quad\text{or}\quad
 [F_0]=0\text{ and }\lambda(t_\psi)\ne0,
 }
\]

where $F_0=u_0^*\lambda$ in the second branch. The value on $t_\psi$ is
independent of the choice of $\lambda$ because $t_\psi\in\operatorname{im}u_0$.

## Scope guard

B107 does not prove $t_\psi\in\operatorname{im}u_0$ or compute either dual
branch. It corrects the domain on which those obligations are well-defined.

