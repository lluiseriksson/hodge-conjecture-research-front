---
brick_id: B105
status: PROVED
base_field: C with all homology, Hodge structures, and pairings over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, a nonzero primitive rational middle Hodge class zeta, a B058 detector c, and an isolated clean nodal hyperplane section Y_0 with a rational local relation beta
smoothness: X smooth; the nearby hyperplane fiber smooth; Y_0 has finitely many ordinary double points
projectivity: X, its hyperplane family, and the collision projective
dimension: dim_C X = 2n; dim_C Y_0 = 2n-1
codimension: middle codimension n; singular support of Y_0 finite
coefficient_field: Q
cohomology_theory: primitive rational Hodge homology and cohomology, Saito's local-relation map, relative homology, and the B104 obstruction quotient
hodge_type: zeta, c, beta, and Phi_(Y_0)(beta) are rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B010, B058, B100, B104, S022 Proposition 1 and Theorem 1
claim: The exact terminal obstruction for a fixed detector c and local relation beta is the scalar discrepancy D_zeta(c,beta)=<zeta,c-Phi_(Y_0)(beta)>; Saito detection holds exactly when D_zeta(c,beta) differs from <zeta,c>. If a compatible B104 collision pair exists, this scalar is the pairing of the ambient image of the bordism coset, so vanishing of the coset is sufficient but not necessary.
falsifier: a Saito relation detecting zeta while D_zeta equals <zeta,c>, a nondetecting relation while those scalars differ, or a compatible collision realization for which the ambient image of the B104 coset has a different zeta-pairing
---

# B105 — The terminal collision obstruction is scalar

**Status:** PROVED

Fix

\[
 0\ne\zeta\in
 H^{2n}_{\mathrm{prim}}(X,\mathbf Q(n))^{(0,0)}
\]

and B058's rational Hodge-homology detector

\[
 c\in H_{2n}(X,\mathbf Q(n))_{\mathrm{prim}}^{(0,0)},
 \qquad
 b_\zeta:=\langle\zeta,c\rangle\ne0.
\]

For a rational type-$(0,0)$ local relation $\beta$ on an isolated clean
nodal hyperplane section $Y_0$, let $\Phi_{Y_0}(\beta)$ be Saito's primitive
ambient class. Define the scalar discrepancy

\[
 D_\zeta(c,\beta)
 :=\left\langle\zeta,c-\Phi_{Y_0}(\beta)\right\rangle.
\]

By linearity,

\[
 \left\langle\zeta,\Phi_{Y_0}(\beta)\right\rangle
 =b_\zeta-D_\zeta(c,\beta).
\]

S022 Proposition 1 and Theorem 1 say that $Y_0$ detects $\zeta$ through
$\beta$ exactly when the left-hand side is nonzero. Therefore the exact
terminal condition is

\[
 \boxed{D_\zeta(c,\beta)\ne b_\zeta.}
\]

In particular, $D_\zeta=0$ is sufficient because $b_\zeta\ne0$, but equality
of the full ambient classes is not required.

## Relation with B104

Suppose a collision pair $(W,N)$ and compatible ambient realization exist
as in B104. Put

\[
 H=H_{2n}(W,N;\mathbf Q(n)),
 \qquad
 J=j_*\operatorname{im}\bigl(H_{2n}(Y_c)\to H_{2n}(Y_c,Z_c)\bigr).
\]

B100 says that absolute nearby-fiber ambiguity has zero primitive ambient
image. Hence the ambient realization $Q:H\to PH_{2n}(X,\mathbf Q(n))$
annihilates $J$ and descends to

\[
 \overline Q:H/J\longrightarrow PH_{2n}(X,\mathbf Q(n)).
\]

For B104's class $\overline\Omega(t,\beta)$, compatibility gives

\[
 \overline Q\bigl(\overline\Omega(t,\beta)\bigr)
 =c-\Phi_{Y_0}(\beta),
\]

and therefore

\[
 D_\zeta(c,\beta)
 =\left\langle\zeta,
   \overline Q\bigl(\overline\Omega(t,\beta)\bigr)
  \right\rangle.
\]

Thus $\overline\Omega=0$ implies $D_\zeta=0$ and closes the detector, but it
is not necessary. Both $\overline Q$ and pairing with $\zeta$ may have
nontrivial kernels. For example, take $H/J=\mathbf Q^2$,
$\overline Q(x,y)=x$, and $\overline\Omega=(0,1)$. The bordism coset is
nonzero while its complete primitive ambient discrepancy is zero.

## Scope guard

B105 does not construct $Y_0$, $\beta$, or a collision comparison. It
corrects the logical endpoint: a proof must establish the scalar inequality
$D_\zeta\ne b_\zeta$; it need not kill a stronger relative-bordism class.
