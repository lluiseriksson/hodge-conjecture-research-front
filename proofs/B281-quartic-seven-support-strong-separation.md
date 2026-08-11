---
brick_id: B281
status: PROVED
base_field: C
variety: the smooth split even-dimensional quadric Q^d in P^(d+1) with d=2n>=14, primitive ruling difference zeta=a-b, quartic A=O_Q(4), H=O_Q(8), seven distinct marked supports P7, and any eighth point x
smoothness: Q^d and all eight reduced supports are smooth; no central ODP package is constructed
projectivity: the standard quadric embedding, hyperplane products, complete octic system, double-support spans, and tangent osculators are projective
dimension: dim X=d=2n>=14; the span of seven standard points has projective dimension at most six, strictly below dim T_xQ=d; every seven-support octic tangent span absorbs no eighth tangent osculator
codimension: the primitive codimension-n ruling difference supplies a valid universal test input; the theorem excludes the quartic polarization from the active rank 7d+6 boundary but leaves the cubic branch and every detector clause open
coefficient_field: Q for zeta and C for hyperplanes, sections, tangent jets, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B196, B260-B280, G200-G202, NG237-NG238, S081, S085
claim: For every seven distinct points P7 on Q^d and every x outside P7, there is an octic section in H0(Q,I_(2P7)(8)) whose restriction to 2x is nonzero. Hence no quartic G200 candidate of rank 7d+6 can absorb its required N=2(7d+6)>7 supports, and the quartic floor is at least 7d+7.
falsifier: seven distinct points and an eighth point whose Q-tangent osculator is contained in their O_Q(8) tangent span, failure of the hyperplane product, a quartic rank-7d+6 G200 package, or a different surviving boundary
---

# B281 — Seven octic tangent spaces absorb no eighth

Let \(P_7=\{p_1,\ldots,p_7\}\subset Q^d\) and let
\(x\in Q^d\setminus P_7\). Put

\[
 L=\langle P_7\rangle\subset\mathbf P^{d+1},
 \qquad \dim L\le6<d=\dim T_xQ. \tag{1}
\]

If \(x\notin L\), choose a hyperplane \(M\) containing \(L\) and
avoiding \(x\). If \(x\in L\), choose \(M\supset L\) that does not
contain \(T_xQ\); equation (1) guarantees that such a hyperplane
exists. In the second case \(M|_Q\) has a nonzero differential at
\(x\).

For each \(i\), choose a hyperplane \(K_i\) through \(p_i\) and avoiding
\(x\). The degree-eight product

\[
 F_x=M\prod_{i=1}^7K_i \tag{2}
\]

has two vanishing factors at each \(p_i\), namely \(M\) and \(K_i\).
Thus

\[
 F_x|_Q\in H^0(Q,I_{2P_7}(8)). \tag{3}
\]

Every \(K_i\) is a unit at \(x\). If \(x\notin M\), then \(F_x(x)\ne0\).
If \(x\in M\), then

\[
 d(F_x|_Q)_x=
 \left(\prod_i K_i(x)\right)d(M|_Q)_x\ne0. \tag{4}
\]

In both cases \(F_x|_{2x}\ne0\). Hence the span of the seven
\(O_Q(8)\) tangent osculators contains no eighth tangent osculator.

In a quartic G200 candidate of total rank \(7d+6\), B260 supplies six
independent double blocks of rank \(6d+6\), and B264 supplies a seventh
block with residual rank at least \(d\). Equality forces those seven
blocks to span the entire rank-\((7d+6)\) space. Lower-profile
extinction would then absorb all \(N=2(7d+6)>7\) marked tangent
osculators into that seven-support span, contradicting (2)--(4).
Therefore the quartic floor is at least \(7d+7\).

B281 constructs no ODP package, Kuranishi vanishing, rational detector,
specified pairing, algebraic cycle, proof, or disproof of HC.
