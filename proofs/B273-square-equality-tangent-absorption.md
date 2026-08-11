---
brick_id: B273
status: PROVED
base_field: C
variety: the smooth split even-dimensional quadric X=Q^d with d=2n>=14, primitive ruling difference zeta=a-b, square A=O_Q(2), H=A^2=O_Q(4), and a hypothetical G192 marked scheme
smoothness: Q^d and the reduced marked scheme are smooth; no central ODP package is constructed
projectivity: the complete quartic embedding, marked point span, tangent osculators, original linear spans, and hyperplane-square separators are projective
dimension: dim X=d=2n>=14; six independent double neighborhoods have rank 6d+6 and a seventh marked double neighborhood contributes all d+1 dimensions, so h_Z(1)>=7d+7
codimension: the primitive codimension-n ruling difference supplies a universal test input; the theorem excludes square equality h_Z(1)=6d+6 in dimensions 14,16,18,20 but leaves the next piecewise boundary and every detector clause open
coefficient_field: Q for zeta and C for sections, symmetric tensors, tangent osculators, and restriction ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B196, B231, B254, B260-B272, G192-G193, S081
claim: On every split even Q^d with d>=14, a square-polarized m=2 candidate satisfying the G144 tangent-absorption hypotheses has h_Z(1)>=7d+7. Hence square equality 6d+6 is impossible in dimensions 14,16,18,20; G192 is NO-GO and G193 is the next active piecewise boundary.
falsifier: a square G192 candidate of rank 6d+6, containment of p^3 u in Sym^4(W) for p in W and u outside W, failure of tangent-osculator absorption, failure of the B254 hyperplane-square full-jet extension, or a different next piecewise boundary
---

# B273 — Square equality contradicts tangent absorption

Let \(S\) be the vector span of the marked points in the complete
\(H=O_Q(4)\) embedding. Under the inherited lower-extinction condition,
B196 places the full quartic tangent osculator \(T_p\) inside \(S\) at
every marked point.

B254 chooses six marked supports

\[
 P_6=\{p_1,\ldots,p_6\} \tag{1}
\]

whose double neighborhoods are independent. Thus their tangent
osculators form a direct sum of dimension \(6(d+1)=6d+6\). Let
\(W\) be the vector span of representatives of the six points in the
standard quadric vector space. Then

\[
 \dim W\le6. \tag{2}
\]

## The marked points cannot all lie in \(\mathbf P(W)\)

Assume that every marked point lies in \(Q\cap\mathbf P(W)\). Their
quartic embedding vectors are fourth powers \(z^4\), so

\[
 S\subset\operatorname{Sym}^4W. \tag{3}
\]

Fix \(p=[v]\in P_6\). If \(B\) is the polar form of the quadric, the
quartic tangent osculator contains

\[
 v^3u\qquad(u\in v^\perp). \tag{4}
\]

These tensors lie in the dual space of \(H^0(Q,O_Q(4))\): contraction
by the quadric vanishes because \(B(v,v)=B(v,u)=0\).
Since \(\dim v^\perp=d+1>6\), choose

\[
 u\in v^\perp\setminus W. \tag{5}
\]

Then \(v^3u\notin\operatorname{Sym}^4W\). For example, choose a linear
functional annihilating \(W\) but not \(u\), and contract it against
one tensor factor while contracting the other three against a
functional nonzero on \(v\). This separates \(v^3u\) from
\(\operatorname{Sym}^4W\).

Equations (3)-(5) contradict \(T_p\subset S\). Therefore some marked
point \(x\) lies outside \(\mathbf P(W)\).

## The seventh double block is full

Choose a hyperplane \(E\) containing \(\mathbf P(W)\) and avoiding
\(x\). Then \(E^2\) vanishes on \(2P_6\) and is a unit on \(2x\).
B254's hyperplane-square lemma gives a surjection

\[
 E^2H^0(Q,O_Q(2))
 \longrightarrow H^0(2x,O_{2x}(4)). \tag{6}
\]

Thus \(2x\) contributes all \(d+1\) dimensions beyond the independent
six-double span. Consequently

\[
 h_Z(1)\ge6(d+1)+(d+1)=7d+7. \tag{7}
\]

Square equality \(6d+6\) is impossible for every even \(d\ge14\).
In particular it cannot realize G192 in dimensions \(14,16,18,20\).
B273 constructs no ODP package, Kuranishi vanishing, rational detector,
specified pairing, algebraic cycle, proof, or disproof of HC.
