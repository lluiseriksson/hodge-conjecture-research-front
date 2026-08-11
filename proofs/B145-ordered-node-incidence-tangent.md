---
brick_id: B145
status: PROVED
base_field: C
variety: a smooth projective complex 2n-fold X, a line bundle L, a hypersurface Y in |L| with N ordered isolated ordinary double points, and the ordered-node incidence over Conf_N(X)
smoothness: X is smooth and every selected singularity is an ordinary double point; the incidence need not be smooth unless the explicit rank-smooth hypothesis is imposed
projectivity: X and |L| are projective; Conf_N(X) and the local ordered-node incidence are quasi-projective
dimension: dim_C X=2n; the ordered configuration space has dimension 2nN; the value-evaluation rank is R
codimension: the incidence Zariski tangent has codimension 2nN+R in |L| x Conf_N(X); a rank-smooth image germ has codimension R in |L|
coefficient_field: C for jets, Hessians, and analytic tangent spaces; Q only in downstream Hodge applications
cohomology_theory: first-jet deformation theory, evaluation matroids, analytic incidence germs, and downstream adjoint and vanishing-cycle cohomology
hodge_type: none asserted by the tangent theorem; downstream B054/B134 supply the normalized type-(0,0) relation functional
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) in downstream applications; no cycle is constructed or assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B015, B027-B028, B144, the local holomorphic Morse lemma, and the analytic constant-rank theorem
claim: At an ordered N-node pair, the incidence tangent projects injectively to the hyperplane-system tangent with image exactly the kernel of value evaluation at the nodes. If the incidence is smooth with this tangent dimension, its image is a smooth codimension-R germ contained in every labeled node branch; with a uniform value matroid, B144 makes the discriminant Li clean.
falsifier: a tangent vector with zero hypersurface deformation but nonzero node motion, a value-kernel deformation that cannot be completed by node motions, a different tangent codimension, or failure of the smooth incidence image to give the saturated germ
---

# B145 — Tangent space of the ordered-node incidence

Let \(d=2n\), let \(V=H^0(X,L)\), and let

\[
 [s]=[Y]\in P:=\mathbf P(V)
\]

have ordered distinct nodes
\(\Delta=(p_1,\ldots,p_N)\). Over
\(\operatorname{Conf}_N(X)\), define the ordered singular-point incidence

\[
 \mathcal I_N=
 \{([t],x_1,\ldots,x_N):j^1_{x_i}t=0\text{ for every }i\}
 \subset P\times\operatorname{Conf}_N(X).
\]

Write

\[
 E_\Delta:T_{[s]}P=V/\langle s\rangle
 \longrightarrow\bigoplus_{i=1}^N L|_{p_i}
\]

for value evaluation and put \(R=\operatorname{rank}E_\Delta\). The map is
well defined because \(s(p_i)=0\).

## Linearized singular-point equations

Choose local coordinates and trivializations at every \(p_i\). A tangent
vector to \(P\times\operatorname{Conf}_N(X)\) is

\[
 (\dot s,v_1,\ldots,v_N),
 \qquad v_i\in T_{p_i}X.
\]

Linearizing the value equation \(t(x_i)=0\) gives

\[
 \dot s(p_i)+ds_{p_i}(v_i)=\dot s(p_i)=0,
\]

because \(p_i\) is critical. Linearizing the critical-point equation gives

\[
 d\dot s_{p_i}+\operatorname{Hess}_{p_i}(s)(v_i)=0.
\]

The Hessian is an isomorphism
\(T_{p_i}X\to T_{p_i}^*X\otimes L|_{p_i}\) because the singularity is an
ordinary double point. Therefore, for every \(\dot s\) satisfying
\(E_\Delta(\dot s)=0\), there is a unique solution

\[
 v_i=-\operatorname{Hess}_{p_i}(s)^{-1}(d\dot s_{p_i}).
\]

Consequently

\[
 T_{([s],\Delta)}\mathcal I_N
 \xrightarrow[\ d\pi\ ]{\ \sim\ }
 \ker E_\Delta\subset T_{[s]}P.
\]

In particular \(d\pi\) is injective, and the Zariski tangent codimension of
\(\mathcal I_N\) inside
\(P\times\operatorname{Conf}_N(X)\) is

\[
 dN+R.
\]

This formula is valid whether or not \(\mathcal I_N\) is smooth.

## Rank-smooth excess and the saturated germ

Assume now that \(\mathcal I_N\) is smooth at \(([s],\Delta)\) with the
dimension of the displayed tangent space. Since \(d\pi\) is injective, the
analytic constant-rank theorem makes the local image

\[
 F:=\pi(\mathcal I_N,([s],\Delta))\subset(P,[s])
\]

a smooth embedded germ of codimension \(R\). Every member of \(F\) retains
all \(N\) labeled nodes, so \(F\) lies in every labeled discriminant branch.

If the value-evaluation matroid on \(\Delta\) is uniform \(U_{R,N}\), B144
applies: all branch intersections are Li clean, and every intersection of
at least \(R\) branches equals \(F\).

Thus G090's saturated germ is equivalent to a concrete excess-smoothness
condition on the universal ordered-node incidence. No algebraic carrier is
used in this implication.

## Generic expected incidence is insufficient

If the full first-jet evaluation

\[
 V\longrightarrow\bigoplus_i P^1(L)|_{p_i}
\]

is surjective, then \(\mathcal I_N\) is smooth of the usual expected
codimension \((d+1)N\). It also forces \(E_\Delta\) surjective, so \(R=N\).
The resulting node branches are independent. In the high-power range of
B027-B028, independence for \(L\) implies independence for
\(K_X\otimes L^n\), so the adjoint defect and vanishing-cycle relation space
are zero.

Therefore the useful case is necessarily an **excess** component:
\(R<N\), the ordered incidence remains smooth of codimension \(dN+R\), and
the adjoint evaluation still has positive corank. Constructing such a
component with a specified nonzero Hodge pairing is G091.
