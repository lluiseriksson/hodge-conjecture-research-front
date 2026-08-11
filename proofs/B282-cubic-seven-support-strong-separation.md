---
brick_id: B282
status: PROVED
base_field: C
variety: the smooth split even-dimensional quadric Q^d in P^(d+1) with d=2n>=14, primitive ruling difference zeta=a-b, cubic A=O_Q(3), H=O_Q(6), six independent double supports P6, a seventh support u, and any eighth point x
smoothness: Q^d and all eight reduced supports are smooth and distinct; no central ODP package is constructed
projectivity: the standard quadric embedding, secant lines, hyperplane products, complete sextic system, double-support spans, and tangent osculators are projective
dimension: dim X=d=2n>=14; five collinear members of P6 force rank at most 6d+3<6d+6; every admissible seven-support sextic tangent span absorbs no eighth tangent osculator
codimension: the primitive codimension-n ruling difference supplies a valid universal test input; the theorem excludes the cubic polarization from G200 at rank 7d+6 but leaves the next piecewise boundary and every detector clause open
coefficient_field: Q for zeta and C for hyperplanes, sections, tangent jets, incidence graphs, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B196, B260-B281, G200-G203, NG237-NG239, S081, S085
claim: If P6 has six independent O_Q(6) double neighborhoods, then for every seventh support u and every x outside P7=P6 union {u}, there is a sextic in H0(Q,I_(2P7)(6)) whose restriction to 2x is nonzero. Hence cubic rank 7d+6 is impossible, G200 is NO-GO, and G203 is the next active boundary.
falsifier: five collinear supports inside an independent P6, failure of the complete-multipartite matching argument, a seven-support span absorbing an eighth Q-tangent osculator, a cubic rank-7d+6 G200 package, or a different next boundary
---

# B282 — Seven admissible sextic tangent spaces absorb no eighth

Let \(P_7=P_6\cup\{u\}\) and fix \(x\in Q^d\setminus P_7\).
Call a pair of supports **good** if its secant line does not contain
\(x\). Collinearity with \(x\) partitions \(P_7\) into classes, and
the good-pair graph is the complete multipartite graph on those
classes.

## Independence forbids a six-point class

Suppose five points of \(P_6\) lie on one line \(\ell\subset Q\).
For their five double neighborhoods, the value and tangent-along-line
quotient has rank at most

\[
 h^0(\ell,O_\ell(6))=7. \tag{1}
\]

The remaining normal-to-line quotient has dimension at most
\(5(d-1)\). Thus the five blocks have rank at most \(5d+2\), and adding
the sixth double block contributes at most \(d+1\). Consequently

\[
 \operatorname{rank}(2P_6)\le(5d+2)+(d+1)=6d+3<6d+6, \tag{2}
\]

contrary to B260's independence.

If the good-pair graph had no matching of size two, its complete
multipartite structure would have one class of size at least six:
indeed its matching number is

\[
 \min\!\left(\left\lfloor\frac72\right\rfloor,\,
 7-\max_j|C_j|\right). \tag{3}
\]

At least five members of such a six-point class belong to \(P_6\),
contradicting (2). Therefore there are two disjoint good pairs.

## The degree-six separator

Partition \(P_7\) into the two disjoint good pairs and three singleton
supports. Choose hyperplanes \(K_1,K_2\) containing the respective
pairs and avoiding \(x\), and hyperplanes \(K_3,K_4,K_5\) containing
the singletons and avoiding \(x\).

Put \(L=\langle P_7\rangle\), so \(\dim L\le6<d=\dim T_xQ\). As in
B281, choose a hyperplane \(M\supset L\) avoiding \(x\) when
\(x\notin L\), and choose \(M\supset L\) with \(T_xQ\not\subset M\)
when \(x\in L\). Then

\[
 F_x=M\prod_{j=1}^5K_j \tag{4}
\]

has degree six and has at least two vanishing factors at every support:
\(M\) and the factor covering that support. Hence

\[
 F_x|_Q\in H^0(Q,I_{2P_7}(6)). \tag{5}
\]

All \(K_j\) are units at \(x\). If \(M(x)\ne0\), then \(F_x(x)\ne0\);
otherwise \(d(M|_Q)_x\ne0\), so \(d(F_x|_Q)_x\ne0\). Thus
\(F_x|_{2x}\ne0\).

In a cubic rank-\((7d+6)\) candidate, B260's six independent blocks
and B264's residual lower bound \(d\) force seven supports to span the
entire candidate space. Equation (5) prevents that span from absorbing
any eighth tangent osculator, contradicting
\(N=2(7d+6)>7\). Therefore the cubic floor is at least \(7d+7\).

B282 constructs no ODP package, Kuranishi vanishing, rational detector,
specified pairing, algebraic cycle, proof, or disproof of HC.
