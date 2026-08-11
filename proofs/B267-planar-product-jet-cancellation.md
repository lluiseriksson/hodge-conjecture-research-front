---
brick_id: B267
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=14, primitive ruling difference zeta=a-b, cubic or quartic A=O_Q(k) with k=3 or 4, and H=A^2
smoothness: Q^d and the seven reduced marked supports are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: the complete quadric embeddings, residual P^2 through u, selected good pair lines, normalized hyperplane factors, and first infinitesimal neighborhood 2u are projective
dimension: dim X=d=2n>=14; on B264's planar residual locus every selected variable-edge product image has the same rank d-1 subspace of the (d+1)-dimensional seventh first-jet target
codimension: the primitive codimension-n ruling difference supplies a valid universal input; B267 retracts B265's claimed planar rank improvement and restores G190 as the active universal gate
coefficient_field: Q for zeta and C for square-zero local jets, hyperplane factors, tangent directions, products, annihilators, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to finite unions of reduced and double points
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B260-B266, G190-G192, NG222-NG224, S081
claim: In B264's planar locus, if P is the product of one normalized pair-line factor for every selected edge, then for every variable edge e its product image on 2u is R_e=<j(P)> direct-sum Ann(U). Hence all R_e coincide and have rank d-1. The fixed-unit differences used in B265 cancel with the removed variable factor, so B265's claimed rank d, its floor 7d+6, and the downstream G190-to-G192 transitions are invalid.
falsifier: a variable-edge product whose unit generator is not j(P), a zero-value edge variation outside Ann(U), two planar edge images that differ, a planar combined rank at least d using only these product spaces, or a valid uncancelled term in B265 equation (6)
---

# B267 — The planar product jets cancel exactly

Retain B264's planar residual locus. Thus every selected tangent edge
has the same endpoint plane

\[
 U\subset T_uQ,\qquad \dim U=2. \tag{1}
\]

Trivialize the first-jet algebra at \(u\) as

\[
 A=\mathbf C\oplus T_u^*Q,
 \qquad(c,\alpha)(c',\alpha')=(cc',c\alpha'+c'\alpha). \tag{2}
\]

For every indexed selected edge \(e\), choose a pair-line hyperplane
\(\ell_e\) normalized by \(\ell_e(u)=1\), and write

\[
 j(\ell_e)=(1,\lambda_e). \tag{3}
\]

The restriction of its whole variable-edge space is

\[
 W_e=\langle(1,\lambda_e)\rangle\oplus D,
 \qquad D=\operatorname{Ann}(U)\subset T_u^*Q. \tag{4}
\]

Indeed, a zero-value hyperplane containing the pair line also contains
\(u\) and its two endpoint directions, so its differential lies in
\(D\); conversely every differential in \(D\) is realized. Thus
\(\dim D=d-2\).

Put

\[
 P=\prod_g\ell_g,
 \qquad \Lambda=\sum_g\lambda_g,
 \qquad j(P)=(1,\Lambda). \tag{5}
\]

When edge \(e\) varies, the fixed complementary product has jet

\[
 j(g_e)=j\!\left(\prod_{g\ne e}\ell_g\right)
       =(1,\Lambda-\lambda_e). \tag{6}
\]

Multiplying (4) by (6) gives

\[
 (1,\lambda_e)(1,\Lambda-\lambda_e)=(1,\Lambda)=j(P), \tag{7}
\]

and, for every \(\delta\in D\),

\[
 (0,\delta)(1,\Lambda-\lambda_e)=(0,\delta). \tag{8}
\]

Therefore the product image is

\[
 R_e=\langle j(P)\rangle\oplus D \tag{9}
\]

for every selected edge \(e\). In particular,

\[
 R_e=R_f,
 \qquad \dim\sum_eR_e=1+(d-2)=d-1. \tag{10}
\]

B265 compared the jets of the complementary units in (6), but omitted
the compensating \(\lambda_e\) from the variable generator in (7).
Equation (7) shows that the proposed difference cancels identically.
Hence B265's planar rank \(d\) and floor \(7d+6\) do not follow.

B264 remains valid outside the planar locus, and B266's independent
standard-polarization exclusion remains valid. Inside the planar locus,
however, the B261 rank \(d-1\) is sharp for the full family of these
single-factor variable-edge products. G190 is therefore restored as
the active gate. B267 constructs no G190 package, ODP package, rational
detector, specified pairing, algebraic cycle, proof, or disproof of HC.
