---
brick_id: B287
status: PROVED
base_field: C
variety: the smooth split even-dimensional quadric Q^d in P(V), d=2n>=14, primitive ruling difference zeta=a-b, nonstandard A=O_Q(k) with k>=2, H=A^2=O_Q(2k), and a reduced marked scheme satisfying lower-degree tangent absorption
smoothness: Q^d and every marked support are smooth; no central ODP divisor or incidence package is constructed
projectivity: the standard quadric, complete O_Q(2k) embedding, affine tangent osculators, linear spans of support representatives, hyperplane-square separators, and double finite schemes are projective
dimension: dim Q=d, dim V=d+2, dim v^perp=d+1; tangent absorption forces d+1 independent double neighborhoods and h_Z(1)>=(d+1)^2>7d+7
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the theorem excludes every nonstandard polarization from G206-G207 and leaves the next standard-polarized boundary open
coefficient_field: Q for zeta and C for symmetric tensors, hyperplanes, sections, first jets, tangent osculators, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B196, B221, B231, B254, B273, B286, G206-G207, S081
claim: For every k>=2, any O_Q(2k) point span that contains the affine embedded tangent osculator at every marked support contains d+1 independent double neighborhoods. Hence h_Z(1)>=(d+1)^2, so no nonstandard polarization realizes the G206-G207 rank 7d+7 on any even Q^d with d>=14.
falsifier: a tangent-absorbing nonstandard span below (d+1)^2, a tensor v^(2k-1)u with u outside W that nevertheless lies in Sym^(2k)W modulo the quadric equation, failure of the hyperplane-square full-jet extension, or a nonstandard G207 package
---

# B287 — Nonstandard tangent absorption iterates to \(d+1\) blocks

Let \(V\) have dimension \(d+2\), let \(Q\subset\mathbf P(V)\) be
defined by the nondegenerate polar form \(B\), and put

\[
 A=O_Q(k),\qquad H=A^2=O_Q(2k),\qquad k\ge2. \tag{1}
\]

Let \(S\) be the vector span of the marked points in the complete
\(O_Q(2k)\) embedding. The inherited lower-profile extinction and B196
give

\[
 \widehat T_pQ\subset S \quad\text{for every marked }p. \tag{2}
\]

## A marked point must escape every small linear span

Suppose \(P_r=\{p_1,\ldots,p_r\}\) has independent double
neighborhoods, where \(1\le r\le d\). Choose isotropic representatives
\(v_i\in V\) and write

\[
 W=\langle v_1,\ldots,v_r\rangle,\qquad \dim W\le r\le d. \tag{3}
\]

Assume for contradiction that every marked point lies in
\(Q\cap\mathbf P(W)\). Then its \(O_Q(2k)\) point vector is a pure
\(2k\)-th power, so

\[
 S\subset \operatorname{Sym}^{2k}W. \tag{4}
\]

Fix \(p_1=[v]\). Since \(\dim v^\perp=d+1>\dim W\), choose
\(u\in v^\perp\setminus W\). The affine tangent osculator at \(p_1\)
contains

\[
 v^{2k-1}u. \tag{5}
\]

This tensor represents an actual vector in
\(H^0(Q,O_Q(2k))^*\): contraction with the quadratic equation times
any degree-\((2k-2)\) form vanishes because
\(B(v,v)=B(v,u)=0\). It is not in \(\operatorname{Sym}^{2k}W\).
Indeed, choose a linear functional \(\lambda\) annihilating \(W\) but
not \(u\), and a functional \(\mu\) with \(\mu(v)\ne0\). Contracting one
slot by \(\lambda\) and the other \(2k-1\) slots by \(\mu\) kills
\(\operatorname{Sym}^{2k}W\) but not (5).

Equations (2), (4), and (5) contradict each other. Therefore some
marked point \(x\) lies outside \(\mathbf P(W)\).

## The escaping point contributes a full double block

Choose a hyperplane \(E\) containing \(\mathbf P(W)\) and avoiding
\(x\). Then \(E^2\) vanishes on \(2P_r\) and is a unit on \(2x\).
Because \(2k-2\ge2\), the complete system restricts surjectively,

\[
 H^0(Q,O_Q(2k-2))\longrightarrow
 H^0(2x,O_{2x}(2k-2)). \tag{6}
\]

Multiplication by \(E^2|_{2x}\) is an automorphism of the first-jet
algebra. Hence

\[
 E^2H^0(Q,O_Q(2k-2))\longrightarrow
 H^0(2x,O_{2x}(2k)) \tag{7}
\]

is surjective, while every source section vanishes on \(2P_r\). Thus
\(2x\) adds all \(d+1\) dimensions and \(2(P_r\cup\{x\})\) remains
independent.

One double neighborhood is independent because \(O_Q(2k)\) is very
ample. Iterating (3)--(7) for \(r=1,\ldots,d\) produces \(d+1\)
independent double neighborhoods. Since (2) places their dual blocks
inside \(S\),

\[
 h_Z(1)=\dim S\ge(d+1)^2. \tag{8}
\]

For \(d\ge14\),

\[
 (d+1)^2-(7d+7)=(d-6)(d+1)>0. \tag{9}
\]

Therefore no \(k\ge2\) polarization can realize G206 or G207 at rank
\(7d+7\). This is a necessary special-input obstruction. It constructs
no ODP package, Kuranishi vanishing, rational detector, specified
pairing, algebraic cycle, proof, or disproof of HC.
