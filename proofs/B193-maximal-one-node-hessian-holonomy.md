---
brick_id: B193
status: PROVED
base_field: C
variety: the full complete-linear-system first-jet and ODP Hessian data of N ordered nodes on a smooth projective complex 2n-fold
smoothness: the ambient variety and node supports are smooth and every tracked singularity is an ODP; no smoothness of the excess incidence is inferred
projectivity: the line bundle, complete linear system, reduced node scheme, and doubled node scheme are projective; the proof is coherent and finite-dimensional
dimension: every gradient block has dimension 2n; the full conditional-gradient quotient has maximal one-node-determined dimension q=2n
codimension: gradient relations away from any node have a unique completion at that node, and rank-one Hessian synchronization gives a conformal transition cocycle
coefficient_field: C for jet relations, Hessians, similitudes, and ranks; Q remains required separately for the Hodge detector
cohomology_theory: coherent first jets, dual evaluation codes, ODP inverse-Hessian forms, and symmetric bilinear similitudes
hodge_type: none asserted; downstream detector data must be rational type (0,0) with specified nonzero pairing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream; no algebraic cycle or detector is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B145-B153, B188-B192, G119-G123
claim: Under B191 one-node determination, the gradient-relation space projects surjectively onto the dual gradients away from any chosen node, with kernel the local dual kernel. If q=2n these projections are isomorphisms. Under nonzero rank-one Hessian synchronization, all multiplier coordinates are nonzero, the common form is nondegenerate, and the node transition maps form a conformal cocycle with multiplier ratios. The doubled-scheme defect is at least 2n(N-1)+1 when R<N and H1(X,L)=0.
falsifier: failure of relation completion under an injective node map, nonuniqueness when q=2n, a zero multiplier coordinate with an isomorphic node map and nondegenerate Hessian, failure of the conformal cocycle, or a smaller coherent defect under the stated hypotheses
---

# B193 — Maximal one-node determination gives conformal Hessian holonomy

Use B191's notation

\[
 V=H^0(I_ZL)/H^0(I_{2Z}L),\qquad
 d_i:V\to G_i,\qquad q=\dim V,
\]

and assume every \(d_i\) is injective. Define the space of linear relations
among the conditional gradient blocks by

\[
 \mathcal R_D=
 \ker\left(
   \bigoplus_{i=1}^NG_i^*\longrightarrow V^*
 \right),
 \qquad
 (\alpha_i)_i\longmapsto\sum_i d_i^*\alpha_i. \tag{1}
\]

## Completion of every punctured gradient relation

Fix \(i\). Since \(d_i\) is injective, its dual

\[
 d_i^*:G_i^*\twoheadrightarrow V^* \tag{2}
\]

is surjective. Given arbitrary covectors \((\alpha_j)_{j\ne i}\), choose
\(\alpha_i\) satisfying

\[
 d_i^*\alpha_i=-\sum_{j\ne i}d_j^*\alpha_j. \tag{3}
\]

Then \((\alpha_j)_j\in\mathcal R_D\). Projection away from node \(i\)
therefore sits in an exact sequence

\[
 0\longrightarrow\ker d_i^*longrightarrow\mathcal R_D
 \longrightarrow\bigoplus_{j\ne i}G_j^*\longrightarrow0. \tag{4}
\]

This is the dual relation form of B191's one-node determination.

Now impose the maximal value

\[
 q=2n. \tag{5}
\]

Both sides of \(d_i:V\to G_i\) then have dimension \(2n\), so every
\(d_i\) and \(d_i^*\) is an isomorphism. Equation (3) has a unique
solution, and (4) becomes an isomorphism

\[
 \mathcal R_D\xrightarrow{\sim}
 \bigoplus_{j\ne i}G_j^* \quad\text{for every }i. \tag{6}
\]

Thus arbitrary dual gradient data away from one node have a unique
completion to a global relation.

## Conformal Hessian holonomy

Assume also B191's nonzero rank-one Hessian condition

\[
 d_i^*B_i=\lambda_iB_V \quad(1\le i\le N), \tag{7}
\]

where \(B_i\) is nondegenerate. Since \(d_i\) is an isomorphism,
\(d_i^*B_i\) is nondegenerate and nonzero. Hence

\[
 \lambda_i\ne0\quad\text{for every }i, \tag{8}
\]

and \(B_V\) is nondegenerate.

For nodes \(i,j\), define

\[
 T_{ji}=d_jd_i^{-1}:G_i\xrightarrow{\sim}G_j. \tag{9}
\]

Using (7), for \(x=d_iv\) and \(y=d_iw\),

\[
 B_j(T_{ji}x,T_{ji}y)
 =\frac{\lambda_j}{\lambda_i}B_i(x,y). \tag{10}
\]

The transitions satisfy

\[
 T_{kj}T_{ji}=T_{ki},\qquad T_{ii}=1. \tag{11}
\]

Thus the maximal branch carries a complete conformal Hessian cocycle. A
change of local frames rescales both the Hessian and multiplier at a node,
so the line-valued statement and multiplier ratios in (10) transform
consistently.

## Minimal coherent defect in this branch

If \(H^1(X,L)=0\), B191 gives

\[
 h^1(X,I_{2Z}L)=(2n+1)N-R-2n. \tag{12}
\]

Since G123 requires \(R<N\),

\[
 h^1(X,I_{2Z}L)\ge2n(N-1)+1. \tag{13}
\]

This is the least doubled-scheme defect permitted by the one-node-
determined branch. It is a necessary equality/bound only, not a dimension-
count construction. B193 supplies no node scheme, detector, higher
Kuranishi vanishing, smooth integration, or cycle.
