---
brick_id: B269
status: PROVED
base_field: C
variety: the smooth split even-dimensional quadric X=Q^d with d=2n>=22, an isotropic plane Pi, two generator lines through u carrying three further supports each, cubic A=O_Q(3), and H=O_Q(6)
smoothness: Q^d, Pi, and every reduced support are smooth; no central ODP divisor or incidence package is asserted
projectivity: the split quadric, isotropic plane, its two generator lines, the complete sextic embedding, and restrictions to double finite schemes are projective
dimension: dim X=d=2n>=22; every eighth distinct double neighborhood raises the rank of any such seven-support 3+3 configuration by at least one; at cubic equality the initial rank is 7d+5
codimension: the primitive codimension-n ruling difference remains only a universal test input; the theorem obstructs extending any exact 3+3 seven-support cubic equality witness to G190's reduced marked scheme of length N=2(7d+5)
coefficient_field: Q for the explicit planar coordinates and connector lines, Q for the ruling difference, and C for global sections and first jets
cohomology_theory: rational singular cohomology and coherent restriction to double finite schemes
hodge_type: the ruling difference is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); algebraicity of an arbitrary target is neither assumed nor proved
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B196, B213, B268, G190, S081
claim: Let P7 consist of u and three distinct points on each of two distinct generator lines through u in an isotropic plane of Q^d. Every point x outside P7 admits a sextic section vanishing on 2P7 but not on 2x. Hence the dual span of 2P7 contains no eighth tangent osculator, and no exact cubic 3+3 equality witness can extend to the N=2(7d+5) reduced marked scheme required by G190.
falsifier: a point x outside P7 for which every sextic vanishing doubly at P7 also vanishes doubly at x, failure of the connector-product construction on Pi, failure of the square-hyperplane construction off Pi, or a G190 marked scheme extending the exact B268 supports without increasing h_Z(1)
---

# B269 — No planar \(3+3\) witness absorbs an eighth double

Choose affine coordinates on the isotropic plane:

\[
 u=(0,0),\qquad p_i=(a_i,0),\qquad q_i=(0,b_i),
 \qquad i=1,2,3, \tag{1}
\]

where the \(a_i\) and the \(b_i\) are nonzero and pairwise distinct.

Write \(L_p,L_q\) for the two coordinate generator lines and
\(\ell_p,\ell_q\) for their linear equations.
We prove that for every \(x\notin P_7\) there is

\[
 F_x\in H^0\bigl(Q,I_{2P_7}(6)\bigr)
 \quad\text{with}\quad F_x|_{2x}\ne0. \tag{2}
\]

## Points outside the isotropic plane

If \(x\notin\Pi\), choose an ambient hyperplane \(E\) containing
\(\Pi\) and avoiding \(x\), and another hyperplane \(M\) avoiding
\(x\). Then

\[
 F_x=E^2M^4 \tag{3}
\]

vanishes to order at least two along all of \(\Pi\), hence on \(2P_7\),
while \(F_x(x)\ne0\).

## Connector products on the plane

For \(1\le i,j\le3\), let \(C_{ij}\) be the line joining \(p_i\) to
\(q_j\), with linear equation \(c_{ij}\). If
\(x\in\Pi\setminus(L_p\cup L_q)\), at most one of the nine
connectors contains \(x\): a line through \(x\) meets each coordinate
axis in a unique point. Therefore there is a permutation \(\sigma\)
whose three connectors \(C_{i,\sigma(i)}\) all avoid \(x\). If \(x\)
lies on one coordinate line but is not in \(P_7\), every connector
already avoids \(x\).

Choose a plane line \(M\) avoiding \(x\) and put

\[
 F_x=\ell_p\ell_q
 \prod_{i=1}^3 c_{i,\sigma(i)}\,m. \tag{4}
\]

This homogeneous plane sextic lifts to an ambient sextic depending
only on three linear coordinates along \(\Pi\). Choose the ambient
coordinate splitting so those coordinates vanish on a complement to
the isotropic vector space defining \(\Pi\). For \(p\in\Pi\), every
class in \(T_pQ/T_p\Pi\) has a representative in that complement:
isotropy makes the complementary component of a vector in \(p^\perp\)
remain in \(p^\perp\). The lifted polynomial has zero derivative on
those representatives. Hence a double zero on \(\Pi\) is also a double
zero on \(Q\).

At each \(p_i\), the factors \(\ell_p\) and \(c_{i,\sigma(i)}\) vanish;
at each \(q_j\), the factors \(\ell_q\) and the unique matched connector
vanish; and at \(u\), the factors \(\ell_p\ell_q\) vanish. Thus (4) lies in
\(I_{2P_7,Q}(6)\).

If \(x\) is off the coordinate lines, every factor in (4) is nonzero
at \(x\), so \(F_x(x)\ne0\). If \(x\) is on exactly one coordinate
line, that factor has a simple zero and every other factor is a unit
at \(x\); hence \(dF_x(x)\ne0\). In either case (2) holds.

## Consequence for G190

If the configuration occurs at cubic equality, its rank is

\[
 \operatorname{rank}\bigl(H^0(Q,O_Q(6))\to
 H^0(2P_7,O_{2P_7}(6))\bigr)=7d+5. \tag{5}
\]

Equation (2) says that adding any eighth distinct double neighborhood
strictly raises this rank. In a G190 equality candidate with
\(h_Z(1)=7d+5\), lower-profile extinction and tangent absorption place
the double neighborhood of every marked point inside the degree-one
point span. Since G190 requires

\[
 |Z|=N=2(7d+5)>7, \tag{6}
\]

the exact B268 support configuration cannot be extended to the required
marked scheme.

This rejects every direct promotion after a \(3+3\) classification.
It does not itself prove that all planar cubic equality configurations
have that form, construct an ODP package, produce a rational detector
or specified pairing, construct a cycle, or prove or disprove HC.
