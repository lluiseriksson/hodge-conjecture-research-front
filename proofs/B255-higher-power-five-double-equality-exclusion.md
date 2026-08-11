---
brick_id: B255
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=14, primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: complete quadric embeddings, restrictions to double points, pair lines, hyperplane-product separators, and tangent point spans are projective
dimension: dim X=d=2n>=14; the cubic polarization forces h_Z(1)>=5d+6, every k>=4 forces h_Z(1)>=6d+6, and every polarization therefore forces h_Z(1)>=5d+6 and slack s>=8d+10
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the obstruction closes G181 and reduces the next equality audit to A=O_Q(3)
coefficient_field: Q for zeta and C for sections, tangent jets, spans, hyperplanes, graphs, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to finite unions of double points
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B247, B249, B253-B254, S081
claim: On (Q^d,a-b), d even and at least fourteen, the cubic polarization has h_Z(1)>=5d+6 and every O_Q(k), k>=4, has h_Z(1)>=6d+6. Together with B253-B254, every polarization has h_Z(1)>=5d+6 and slack s>=8d+10. Hence G181 and its adjacent odd layer are NO-GO; at equality only A=O_Q(3) remains.
falsifier: a partition of five supports into line-through-x classes of size at most three whose good graph has no at-most-six-edge minimum-degree-two subgraph, failure of a good pair line to admit a hyperplane avoiding x, a cubic equality candidate, a k>=4 span below six double blocks, a candidate below the common floor, or a different next balanced signature
---

# B255 — Six good edges exclude higher-power equality

Let \(A=O_Q(k)\), \(k\ge3\), and let \(S\) be the marked point span.
B249 proves that five marked points

\[
 P_5=\{p_1,p_2,p_3,p_4,p_5\} \tag{1}
\]

have independent double neighborhoods; the first four may be chosen so
that no three are collinear. The G144 tangent-absorption clause puts their
dual tangent span inside \(S\).

## The good-edge lemma

Fix any further marked point \(x\). Partition \(P_5\) by declaring two
points equivalent when their pair line contains \(x\). A class contains
at most three points: four would contain three of
\(p_1,p_2,p_3,p_4\) on one line, contrary to their choice.

Call an edge good if its endpoints lie in distinct classes. The good graph
is complete multipartite and has a set of at most six edges in which every
vertex has degree at least two. Indeed:

- if every class has size at most two, the graph has a spanning five-cycle;
- if a class has size three, join each of its vertices to both remaining
  vertices, giving six edges and degrees \(2,2,2,3,3\).

For each selected good edge \(e\), its pair line avoids \(x\), so choose an
ambient hyperplane \(L_e\) containing that line and avoiding \(x\). Repeating
an edge if fewer than six were selected, form the sextic

\[
 F=\prod_{j=1}^{6}L_{e_j}. \tag{2}
\]

Every vertex of \(P_5\) lies on at least two factors, while no factor
vanishes at \(x\). Hence

\[
 F|_{2P_5}=0,\qquad F(x)\ne0. \tag{3}
\]

## The cubic polarization

For \(k=3\), suppose equality held in B249:

\[
 \dim S=h_Z(1)=5(d+1). \tag{4}
\]

The five independent tangent blocks already have this dimension and lie in
\(S\), so they fill \(S\). But (3) separates the marked point \(x\in S\)
from that tangent span, a contradiction. Since rank is integral,

\[
 k=3\quad\Longrightarrow\quad h_Z(1)\ge5d+6. \tag{5}
\]

## Every higher power

For \(k\ge4\), multiply (2) by the complete system
\(H^0(Q,O_Q(2k-6))\). Since \(2k-6\ge2\), restriction to \(2x\) supplies
all \(d+1\) constant and first-jet coordinates. Multiplication by the unit
\(F|_{2x}\) is an automorphism, while every product still vanishes on
\(2P_5\). Thus the sixth double neighborhood is independent and

\[
 k\ge4\quad\Longrightarrow\quad h_Z(1)\ge6(d+1)=6d+6. \tag{6}
\]

## The improved common floor

B253 gives \(6d-7\) for \(k=1\), and B254 gives \(6d+6\) for \(k=2\).
Together with (5)-(6), for even \(d\ge14\),

\[
 h_Z(1)\ge5d+6,\qquad
 \delta_1\ge4d+5,\qquad s\ge8d+10. \tag{7}
\]

Therefore G181 and its adjacent odd layer \(s=8d+9\) are NO-GO. The
next balanced signature is

\[
 s=8d+10,\qquad \delta_1=4d+5,\qquad
 N=10d+12,\qquad h_Z(1)=5d+6=N/2. \tag{8}
\]

At (8), only \(A=O_Q(3)\) can remain. B255 is a necessary special-input
obstruction. It constructs no configuration, ODP package, rational
detector, specified pairing, algebraic cycle, proof, or disproof of HC.
