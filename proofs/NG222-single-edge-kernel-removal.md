---
brick_id: NG222
status: NO-GO
base_field: C
variety: the smooth split even-dimensional quadric X=Q^d with d=2n>=14, primitive ruling difference zeta=a-b, cubic or quartic A=O_Q(k) with k=3 or 4, and H=A^2
smoothness: Q^d and the seven displayed reduced supports are smooth and pairwise distinct; no central ODP package is asserted
projectivity: the split quadric, tangent hyperplane, pair lines, good-edge graph, and restriction to the first infinitesimal neighborhood 2u are projective
dimension: dim X=d=2n>=14; every single good-edge variable space can have first-jet rank exactly d-1, so this route cannot raise B261's floor from 7d+5 to 7d+6
codimension: the primitive codimension-n ruling difference supplies the surrounding universal test input; the countermodel concerns only the proposed single-edge strengthening inside G190
coefficient_field: Q for zeta and C for split coordinates, hyperplanes, tangent jets, kernels, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to the reduced supports and 2u
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); algebraicity of zeta is not used to infer a detector
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B260-B263, G190, S081
claim: Good-edge avoidance alone does not force a d-dimensional seventh first-jet image. On a split Q^d there are u,p_1,...,p_6 for which every pair edge is good but every pair line lies in the tangent hyperplane at u, so the B261 variable-edge map has its one-dimensional tangent-hyperplane kernel and rank exactly d-1 for every edge.
falsifier: a proof that the displayed split configuration has a pair line outside T_uQ, that the tangent hyperplane does not lie in I_pair-line(1), or that a single variable-edge restriction nevertheless has rank d
---

# NG222 — A good edge need not remove the tangent kernel

Let \(V\) have hyperbolic basis

\[
 e_0,f_0,e_1,f_1,\ldots,e_6,f_6,\ldots,
 \qquad B(e_i,f_j)=\delta_{ij}, \tag{1}
\]

and let \(Q^d\subset\mathbf P(V)\) be the smooth split quadric. Put

\[
 u=[e_0],\qquad p_i=[e_i]\quad(1\le i\le6). \tag{2}
\]

The seven points are distinct and isotropic. No pair line
\(\overline{p_ip_j}\) contains \(u\), so every edge is good in B260's
sense. The first four points also have no collinear triple.

However

\[
 p_i\in\mathbf P(u^\perp)=T_uQ \tag{3}
\]

for every \(i\). Consequently every pair line lies in \(T_uQ\). If

\[
 V_{ij}=I_{\overline{p_ip_j}}(1), \tag{4}
\]

then the tangent hyperplane section at \(u\) belongs to \(V_{ij}\).
It is precisely the one-dimensional kernel of the complete restriction

\[
 H^0(Q,O_Q(1))\longrightarrow H^0(2u,O_{2u}(1)). \tag{5}
\]

Since \(\dim V_{ij}=d\), B261's lower bound and (3)-(5) give

\[
 \operatorname{rank}\bigl(V_{ij}\to H^0(2u,O_{2u}(1))\bigr)=d-1 \tag{6}
\]

for every edge. Thus the proposed inference

\[
 \text{good edge}\Longrightarrow\text{single-edge rank }d \tag{7}
\]

is false. This countermodel concerns only the one-edge strengthening;
it does not show that a complete G190 package exists. A viable re-entry
must combine at least two variable-edge images or prove, using stronger
geometric hypotheses than the good graph, that the totally orthogonal
configuration cannot occur. No detector, cycle, proof, or disproof of
HC is produced.
