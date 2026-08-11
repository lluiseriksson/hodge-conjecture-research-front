---
brick_id: B201
status: PROVED
base_field: C
variety: the full projective tangent system at a degree-m hypersurface with ordered ODP scheme Z on a smooth projective complex d-fold
smoothness: X and the node supports are smooth and the central Hessians are nondegenerate; reduced smoothness of the simultaneous-node germ is not assumed
projectivity: X, L=H^m, the full projective section tangent space, reduced and doubled node schemes, and all jet maps are projective coherent data
dimension: dim X=d; the maximal branch has dim V=d; the value-zero projective tangent kernel splits as U plus Kbar with U isomorphic to V and Kbar=H0(I_2Z L)/C F
codimension: after quadratic vanishing, the cubic Kuranishi tensor has only a pure U^3 block and a mixed Kbar tensor U^2 block; blocks with at least two Kbar inputs vanish
coefficient_field: C for sections, Hessians, critical values, and Kuranishi tensors; Q remains required separately for the detector
cohomology_theory: coherent first and second jets, projective tangent spaces, ODP critical-value derivatives, and symmetric multilinear algebra
hodge_type: none asserted; rational type (0,0) and the specified pairing remain separate
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B146, B154, B191-B200, G124-G130
claim: In the maximal one-node branch after complete quadratic vanishing, choose ker(E)=U plus Kbar with U mapping isomorphically to V and Kbar=K_m/C F. The canonical cubic Kuranishi tensor vanishes exactly when its pure-U tensor Theta and mixed tensor Xi:Kbar -> (T/S) tensor Sym^2 U^* both vanish. Xi(a)(b,c) is the class modulo the value image S of the node vector Hess_i(a)(H_i^(-1)d_i b,H_i^(-1)d_i c). The formula is well-defined modulo F, and every cubic component with at least two Kbar inputs is zero.
falsifier: a nonzero two-Kbar cubic component, dependence of Xi on the representative modulo F, full cubic vanishing with nonzero Theta or Xi, or a nonzero cubic tensor after both filters vanish
---

# B201 — The cubic obstruction splits into pure and mixed filters

Let \(L=H^m\), let \(\mathcal T=\bigoplus_iL_{p_i}\), and let

\[
 E:H^0(X,L)/\mathbf CF\longrightarrow\mathcal T
\]

be value evaluation in the projective tangent space at the central nodal
section \(F\). Put \(S=\operatorname{im}E\). Then

\[
 \ker E=H^0(I_ZL)/\mathbf CF. \tag{1}
\]

Let \(K_m=H^0(I_{2Z}L)\), set

\[
 \overline K=K_m/\mathbf CF,
\]

and choose a splitting \(U\subset\ker E\) mapping isomorphically to

\[
 V=H^0(I_ZL)/K_m.
\]

Thus

\[
 \ker E=U\oplus\overline K. \tag{2}
\]

Assume G130's complete quadratic vanishing, so B154's canonical cubic
tensor is defined:

\[
 \kappa_3\in(\mathcal T/S)\otimes
 \operatorname{Sym}^3(\ker E)^*. \tag{3}
\]

## Directions double on Z

For a tangent direction \(a\in\overline K\), choose a representative
\(a\in K_m\). Its value and spatial derivative vanish at every node.
Therefore B154's critical-point displacement

\[
 v_{a,i}=H_i^{-1}(da_{p_i})
\]

is zero. If \(a,a'\in\overline K\) and \(b\in U\), every term of B154's
third-derivative formula contains \(v_a\) or \(v_{a'}\), so

\[
 \kappa_3(a,a',b)=0. \tag{4}
\]

The same argument kills the \(\overline K^3\) block.

## The mixed filter

For \(a\in\overline K\) and \(b,c\in U\), B154 reduces exactly to

\[
 d^3\tau_i(a,b,c)=
 \operatorname{Hess}_{p_i}(a)
 \bigl(v_{b,i},v_{c,i}\bigr),\qquad
 v_{b,i}=H_i^{-1}(d_ib). \tag{5}
\]

Indeed, the quadratic critical-value form pairs parameter gradients through
\(H_i^{-1}\). Since \(da_{p_i}=0\), it pairs \(a\) with every parameter
direction to zero. Hence \(m_2(a,b)=m_2(a,c)=0\), and all three implicit
correction terms in B154's formula vanish as well.

Define

\[
 \Xi:\overline K\longrightarrow
 (\mathcal T/S)\otimes\operatorname{Sym}^2U^* \tag{6}
\]

by taking the class modulo \(S\) of the node vector in (5).
This is well-defined modulo \(\mathbf CF\). Replacing \(a\) by \(a+cF\)
adds

\[
 c\,\operatorname{Hess}_{p_i}(F)(v_{b,i},v_{c,i})
 =c\,B_i(d_ib,d_ic)
 =c\,\lambda_iB_V(b,c), \tag{7}
\]

whose node-value vector is a scalar multiple of
\(\lambda\in S\), hence zero in \(\mathcal T/S\).

## The pure filter

Restrict B154's cubic formula to \(U^3\) and project nodewise values to
\(\mathcal T/S\). Denote the resulting tensor by

\[
 \Theta\in(\mathcal T/S)\otimes\operatorname{Sym}^3U^*. \tag{8}
\]

It contains the spatial two-jets of the selected jet generators and the
spatial third jet of \(F\). Equations (2), (4), (6), and (8) give

\[
 \kappa_3=0
 \quad\Longleftrightarrow\quad
 \Theta=0\ \text{and}\ \Xi=0. \tag{9}
\]

B201 is an exact cubic decomposition. It constructs neither filter
vanishing, does not imply any quartic or later rung, and supplies no
rational detector or algebraic cycle.
