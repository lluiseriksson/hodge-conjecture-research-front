---
brick_id: B235
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=4, primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: complete quadric embeddings, tangent osculators, three-double-point restrictions, and collinear loci are projective
dimension: dim X=d=2n; every m=2 candidate has slack s>=4d, and every candidate with A=O_Q(k), k>=2, has s>=4d+4
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the obstruction gives the first slope-four degree-two slack floor
coefficient_field: Q for zeta and C for sections, tangent jets, symmetric tensors, ranks, and projective coordinates
cohomology_theory: rational singular cohomology and coherent restriction to finite double-point schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B221-B234, S081
claim: On (Q^d,a-b), every m=2 G144 candidate has slack s>=4d. If its polarization is O_Q(k) with k>=2, then s>=4d+4. At the first possible value s=4d, necessarily A=O_Q(1), delta_1=2d, N=6d+2, h_Z(1)=3d+1=N/2, and the degree-one relation transport is an isomorphism.
falsifier: a candidate below the displayed floors, a standard-quadric third tangent osculator with quotient rank below d-1, failure of ambient quartics to separate three noncollinear double points, or a different equality signature
---

# B235 — Three tangent spaces force slope-four slack

Fix the valid input \((Q^d,a-b)\), \(d=2n\ge4\), and write

\[
 h_Z(1)=d+1+\delta_1,\qquad 2\delta_1\le s. \tag{1}
\]

Let \(S\) denote the \(H=A^2\) point span.

## Standard polarization

Take \(A=O_Q(1)\). If all marked pairs are orthogonal, B231's
isotropic-span argument contradicts tangent absorption. Otherwise choose
a nonorthogonal pair \(v,w\) and write

\[
 V=\langle v,w\rangle\perp U. \tag{2}
\]

Their tangent osculators \(T_v,T_w\) are disjoint and have total
dimension \(2d+2\). For any third marked
\(r=av+bw+u\), one has \(u\ne0\). B233 computes that the image of
\(T_r\) modulo \(T_v\oplus T_w\) contains

\[
 \{u\mathbin{\odot}y:y\in U,\ B(u,y)=0\}, \tag{3}
\]

of dimension \(d-1\). Consequently

\[
 \dim S\ge2d+2+(d-1)=3d+1. \tag{4}
\]

Using (1), this is

\[
 \delta_1\ge2d,\qquad s\ge4d. \tag{5}
\]

## Square polarization

Take \(A=O_Q(2)\), so \(H=O_Q(4)\). We first record an exact elementary
separation fact. Three noncollinear ambient points may be put at
coordinate vertices \(e_0,e_1,e_2\). At \(e_i\), the monomials

\[
 X_i^4,\qquad X_i^3X_j\quad(j\ne i) \tag{6}
\]

realize its constant and every linear jet while vanishing to order at
least three at the other two vertices. Ambient quartics therefore
separate the three ambient double points, and hence their intrinsic
quadric quotients.

If \(Z\) contained a noncollinear triple, its three dual tangent
osculators would form a direct sum of dimension \(3(d+1)\) inside
\(S\). Otherwise every marked triple would be collinear, so all of
\(Z\) would lie on one quadric line and have \(O(4)\) rank at most five.
The latter contradicts \(h_Z(1)\ge d+2\), while the former forces

\[
 h_Z(1)\ge3d+3,\qquad
 \delta_1\ge2d+2,\qquad s\ge4d+4. \tag{7}
\]

## Every higher polarization

If \(A=O_Q(k)\), \(k\ge3\), then \(H=O_Q(2k)\) has exponent at least
six. B215 separates three double neighborhoods from exponent five.
Their dual tangent spaces again give (7).

Thus every polarization satisfies \(s\ge4d\), and every \(k\ge2\)
satisfies the stronger \(s\ge4d+4\).

At \(s=4d\), only the standard polarization remains. Equations (1) and
(5) force \(\delta_1=2d\), and therefore

\[
 N=2(d+1)+4d=6d+2,\qquad
 h_Z(1)=3d+1=N/2,\qquad
 s-2\delta_1=0. \tag{8}
\]

The relation transport is an isomorphism and the degree-one code is
diagonally self-dual. B235 is a necessary floor only; it constructs no
threshold configuration, ODP package, rational detector, specified
pairing, or cycle.
