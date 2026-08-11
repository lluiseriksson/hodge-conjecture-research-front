---
brick_id: B264
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=14, primitive ruling difference zeta=a-b, cubic or quartic A=O_Q(k) with k=3 or 4, and H=A^2
smoothness: Q^d and the seven reduced marked supports are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: the complete quadric embeddings, first infinitesimal neighborhood 2u, good-edge connected graphs, pair-line hyperplanes, tangent hyperplane, and residual planar locus are projective
dimension: dim X=d=2n>=14; outside the six-support planar locus through u, two variable-edge images have combined first-jet rank at least d and force h_Z(1)>=7d+6 for k=3,4
codimension: the primitive codimension-n ruling difference supplies a valid universal input; B264 reduces cubic/quartic equality inside G190 to configurations whose six independent-double supports lie in a P^2 through the seventh point
coefficient_field: Q for zeta and C for local jets, hyperplanes, tangent directions, annihilators, graph incidence, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to finite unions of reduced and double points
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B247, B254-B263, G190, NG222, S081
claim: For B260's cubic six-cycle or quartic connected eight-edge cover, either the sum of at most two variable-edge product spaces has rank at least d on the seventh first-jet target, forcing h_Z(1)>=7d+6, or all six independent-double supports lie in one projective plane through the seventh point u. Thus cubic/quartic equality h_Z(1)=7d+5 can survive only on that planar locus.
falsifier: a nontangent edge of rank below d, two tangent edge images with distinct endpoint planes whose sum has rank below d, a connected selected graph with all edge planes equal but vertices outside one P^2 through u, a nonplanar equality candidate, or a failure of the fixed-factor products to vanish on 2P_6
---

# B264 — Two edge images leave only a planar obstruction

Retain B260's six independent double supports \(P_6\), seventh marked
point \(u\), and selected connected good graph \(\Gamma\): a six-cycle
in the cubic case and either its repeated-edge quartic version or the
connected eight-edge cover in the quartic case.

## One nontangent edge already suffices

For an edge \(e=\{i,j\}\), put

\[
 V_e=I_{\overline{p_ip_j}}(1),\qquad \dim V_e=d. \tag{1}
\]

The complete restriction to \(2u\) has one-dimensional kernel, the
tangent hyperplane at \(u\). If \(\overline{p_ip_j}\not\subset T_uQ\),
that kernel is not in \(V_e\). Hence

\[
 \operatorname{rank}(V_e\to H^0(2u,O_{2u}(1)))=d. \tag{2}
\]

Multiplication by B260's remaining fixed unit factors preserves this
rank and the double vanishing on \(P_6\).

## Two tangent edges with distinct endpoint planes

It remains to suppose every selected edge under consideration lies in
\(T_uQ\). Write the first-jet target, after a local trivialization, as

\[
 A=\mathbf C\oplus T_u^*Q,\qquad \dim A=d+1. \tag{3}
\]

For a good tangent edge \(e=\{i,j\}\), the tangent directions
\(\bar p_i,\bar p_j\in T_uQ\) are independent: dependence would put
\(u,p_i,p_j\) on one projective line, contrary to goodness. Put

\[
 U_e=\langle\bar p_i,\bar p_j\rangle\subset T_uQ. \tag{4}
\]

Before multiplying by the fixed unit, the image \(R_e\subset A\) is
cut out by evaluation on \(\bar p_i,\bar p_j\), so \(R_e^\perp\) is a
two-plane projecting isomorphically to \(U_e\). Multiplication by any
unit \((1,\beta)\) sends

\[
 (c,\alpha)\longmapsto(c,\alpha+c\beta); \tag{5}
\]

dually, it replaces that two-plane by a graph over the same \(U_e\).
Thus the fixed factors do not change its projected endpoint plane.

For two selected edges \(e,f\) with \(U_e\ne U_f\),

\[
 \dim(U_e\cap U_f)\le1. \tag{6}
\]

The graph projections are injective, hence

\[
 \dim(R_e^\perp\cap R_f^\perp)\le1. \tag{7}
\]

Using \((R_e+R_f)^\perp=R_e^\perp\cap R_f^\perp\), (3) and (7) give

\[
 \dim(R_e+R_f)\ge d. \tag{8}
\]

The corresponding two product spaces both vanish on \(2P_6\), so
(8) supplies at least \(d\) residual first jets at \(u\).

## Equality forces a projective plane

Suppose no pair of selected edges has distinct endpoint planes. Then
all \(U_e\) equal one two-plane \(U\). The selected graph \(\Gamma\)
is connected. Along an edge path, equality

\[
 U=\langle\bar p_i,\bar p_j\rangle
  =\langle\bar p_j,\bar p_k\rangle \tag{9}
\]

forces every vertex direction \(\bar p_i\) into \(U\). Since the
supports themselves lie in \(u^\perp\), all six points lie in

\[
 \mathbf P(\langle u,U\rangle)\simeq\mathbf P^2. \tag{10}
\]

Therefore, unless (10) holds, the six double blocks contribute
\(6d+6\) and (8) contributes at least \(d\), giving

\[
 k=3,4\quad\Longrightarrow\quad h_Z(1)\ge7d+6. \tag{11}
\]

Consequently equality \(h_Z(1)=7d+5\) can survive only on the planar
locus (10). B264 does not exclude that locus and does not close G190.
It constructs no ODP package, rational detector, specified pairing,
algebraic cycle, proof, or disproof of HC.
