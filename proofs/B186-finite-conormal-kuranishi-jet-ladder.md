---
brick_id: B186
status: PROVED
base_field: C
variety: a smooth positive-dimensional basis-node carrier germ in the full labelled ODP incidence, with reduced Kuranishi escape map
smoothness: the basis carrier is smooth; the central singularities are ODPs; no smoothness of the full simultaneous-node germ is assumed
projectivity: the finite bound comes from B185's full projective incidence presentation; the jet equivalence itself is local analytic
dimension: carrier dimension q=d-R at least one; obstruction target dimension N-R; finite certificate degree D_car=E^(M+1)
codimension: the conormal jet through order D-1 vanishes exactly when every Kuranishi tensor of degree two through D vanishes
coefficient_field: C for analytic jets, conormal modules, and symmetric tensors; Q remains required for downstream Hodge detectors
cohomology_theory: regular local rings, Kahler differentials, conormal modules, critical-value Kuranishi maps, and ODP deformation theory
hodge_type: none asserted; rational type (0,0) and the specified nonzero Saito pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is only downstream; no algebraic cycle or detector is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B146, B153-B154, B179-B185, G097-G098, G118
claim: If K is the escape ideal on a smooth basis carrier and K is contained in the square of the maximal ideal, then for every D at least one, vanishing of the conormal jet through order D-1 is equivalent to K being contained in m^(D+1), equivalently to vanishing of all homogeneous Kuranishi tensors kappa_2 through kappa_D. For B185's D_car this is the exact finite ladder whose completion implies H_tau=0.
falsifier: a nonzero escape term of degree at most D with conormal jet zero through D-1, a conormal coefficient through D-1 when all escape generators lie in m^(D+1), or disagreement of the quadratic and cubic rungs with B146 and B154
---

# B186 — The finite conormal certificate is a Kuranishi ladder

Let

\[
 O=\mathbf C\{u_1,\ldots,u_q\},\qquad
 \mathfrak m=(u_1,\ldots,u_q),\qquad q\ge1,
\]

and let \(K\subset\mathfrak m^2\) be the escape ideal on a basis-node
carrier. The inclusion in \(\mathfrak m^2\) is automatic: choosing a basis
of the rank-\(R\) critical-value differentials kills every linear term of
the restricted nonbasis values.

Let

\[
 \beta_K:K/K^2\longrightarrow
 \Omega^1_O\otimes_O O/K
\]

be B179's conormal map.

## Exact finite-jet equivalence

For every integer \(D\ge1\),

\[
 j^{D-1}\beta_K=0
 \quad\Longleftrightarrow\quad
 K\subset\mathfrak m^{D+1}. \tag{1}
\]

If \(K\subset\mathfrak m^{D+1}\), then
\(dK\subset\mathfrak m^D\Omega^1_O\), so the left side of (1) follows.

Conversely, suppose \(K\not\subset\mathfrak m^{D+1}\), and let
\(r\le D\) be the minimum order of a nonzero element \(g\in K\). Its
leading homogeneous form \(g_r\) is nonzero. Since the characteristic is
zero, \(dg_r\ne0\) and has degree \(r-1\). Every element of
\(K\Omega^1_O\) has order at least \(r\), while every element of \(K^2\)
has order at least \(2r\). Therefore \([g]\ne0\) in \(K/K^2\), and
\(\beta_K([g])\) has the nonzero leading term \(dg_r\) in degree
\(r-1\le D-1\). This contradicts the left side and proves (1).

## Kuranishi tensors

Use B154's implicit reduction to write the restricted escape map as

\[
 \kappa=\kappa_2+\kappa_3+\kappa_4+\cdots:
 (\ker E,0)\longrightarrow(\operatorname{coker}E,0),
\]

where \(\kappa_j\) is homogeneous of degree \(j\). Its component ideal is
\(K\). Hence (1) is equivalently

\[
 j^{D-1}\beta_K=0
 \quad\Longleftrightarrow\quad
 \kappa_2=\kappa_3=\cdots=\kappa_D=0. \tag{2}
\]

The first nonautomatic rung is:

\[
 j^1\beta_K=0
 \quad\Longleftrightarrow\quad
 \kappa_2=0. \tag{3}
\]

B146 identifies \(\kappa_2\) with the relation-Hessian obstruction. In the
synchronized branch, B153 identifies it with the mixed condition together
with \(\Omega_Q=0\). If (3) holds, B154's canonical cubic tensor is exactly
the next rung:

\[
 j^2\beta_K=0
 \quad\Longleftrightarrow\quad
 \kappa_2=\kappa_3=0. \tag{4}
\]

Successively, once all lower tensors vanish, the next homogeneous tensor is
independent of the implicit source and target coordinate choices with
identity linear part.

## B185 certificate

For \(D=D_{\mathrm{car}}=E^{M+1}\), B185 and (2) give

\[
 \kappa_2=\cdots=\kappa_{D_{\mathrm{car}}}=0
 \Longrightarrow K=0
 \Longrightarrow H_\tau=0. \tag{5}
\]

Thus G118 is finite, but it consists of a genuine sequence of tensor
vanishing obligations. B186 proves no rung vanishes.
