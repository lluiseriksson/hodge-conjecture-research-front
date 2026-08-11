---
brick_id: B171
status: PROVED
base_field: C
variety: a smooth projective complex variety X, a complete-linear-system affine chart W, and N tracked ODP critical-value functions in fixed local Morse gauges
smoothness: X, W, and the tracked critical-point sections are smooth; every spatial Hessian is nondegenerate
projectivity: X and the hypersurface family are projective; the tangent obstruction is local analytic and finite-dimensional
dimension: parameter space W; central value map E of rank R<N; tangent kernel V=ker E; relation space K=ker E^* of dimension N-R
codimension: G107's rank-at-most-R determinantal locus has tangent condition Hom(V,coker E)=0 along the critical-configuration image
coefficient_field: C
cohomology_theory: determinantal tangent spaces, principal-parts evaluation, ODP critical-value Hessians, and analytic deformation theory
hodge_type: none asserted; no rational detector or specified pairing is produced
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) only downstream; no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B145-B170, G092, G107, NG117
claim: Tangency of the moving critical-evaluation map to the rank-at-most-R determinantal locus forces every relation-weighted Hessian pairing to vanish on W times ker E, not merely on ker E times ker E. If the full gradient map W->direct_sum T^*_{p_i}X is surjective and the value matroid is uniform U_(R,N), this mixed condition is impossible.
falsifier: a constant-rank critical-value germ with a nonzero induced map ker E->coker E in the derivative of its Jacobian, or a full-gradient-surjective uniform example satisfying all mixed equations
---

# B171 — G107 has a mixed Hessian obstruction on \(W\times\ker E\)

Retain B170's fixed gauges and write

\[
 \tau:(W,0)\longrightarrow(\mathbf C^N,0),\qquad
 E=d\tau_0,\qquad V=\ker E,\qquad C=\operatorname{coker}E.
\]

The tangent space at a rank-\(R\) matrix \(E\) to the determinantal
variety of matrices of rank at most \(R\) consists exactly of perturbations
\(M\) whose induced map

\[
 \ker E\longrightarrow\operatorname{coker}E
\]

is zero. Applied to the Jacobian map \(t\mapsto d\tau_t\), G107 therefore
has the necessary first-order condition

\[
 \Theta(a)(b):=
 \pi_C\bigl(d^2\tau_0(a,b)\bigr)=0
\quad
(a\in W,\ b\in V). \tag{1}
\]

Equivalently, for every value relation \(c=(c_i)\in K=\ker E^*\),

\[
 \sum_i c_i\,d^2\tau_i(0)(a,b)=0
\quad
(a\in W,\ b\in V). \tag{2}
\]

B146's critical-point elimination formula gives

\[
 d^2\tau_i(0)(a,b)
 =-\,da_{p_i}\bigl(H_i^{-1}(db_{p_i})\bigr). \tag{3}
\]

Thus (2) is the exact mixed Hessian condition

\[
 \sum_i c_i\,
 da_{p_i}\bigl(H_i^{-1}(db_{p_i})\bigr)=0
\quad
(c\in K,\ a\in W,\ b\in V). \tag{4}
\]

B146 uses only \(a,b\in V\). Hence G107 imposes strictly more
first-order determinantal geometry than smooth excess or \(H_\tau=0\).

## Full-gradient-surjective exclusion

Let

\[
 D:W\longrightarrow
 G:=\bigoplus_iT^*_{p_i}X\otimes L|_{p_i},
\qquad a\longmapsto(da_{p_i})_i,
\]

and suppose \(D\) is surjective. Assume the value matroid is uniform
\(U_{R,N}\). Fix \(b\in V\), a node \(i\), and a circuit
\(S\) of size \(R+1\) containing \(i\). Its relation \(c^S\) has every
coordinate on \(S\) nonzero.

Because \(D\) is surjective, \(Da\) can be chosen arbitrarily on the
blocks indexed by \(S\) and zero elsewhere. The direct-sum bilinear form

\[
 B_{c^S}(\alpha,\beta)=
 \sum_{j\in S}c_j^S\,
 \alpha_j(H_j^{-1}\beta_j)
\]

is nondegenerate on \(G_S\). Equation (4) for all \(a\) therefore forces
\((Db)|_S=0\), in particular \((Db)_i=0\). Circuits cover every node, so

\[
 D(V)=0. \tag{5}
\]

But then \(D\) factors through \(W/V\simeq\operatorname{im}E\), and

\[
 \operatorname{rank}D\le R.
\]

This contradicts surjectivity onto
\(\dim X\cdot N>R\) dimensions. Consequently G107 cannot occur in the
full-gradient-surjective regime. It requires a global first-jet
degeneracy even stronger than B146's conditional isotropy.

## Scope guard

Equation (1) is only the first tangent condition for determinantal
containment; higher derivatives remain. Its failure refutes G107, while
its vanishing neither proves containment nor supplies the specified
pairing.
