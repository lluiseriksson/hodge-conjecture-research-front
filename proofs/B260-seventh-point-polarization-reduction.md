---
brick_id: B260
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=14, primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: complete quadric embeddings, restrictions to reduced and double points, good-edge multipartite graphs, pair-line hyperplane products, low-dimensional linear spans, and tangent point spans are projective
dimension: dim X=d=2n>=14; k=3 and k=4 force h_Z(1)>=6d+7; k>=5 forces h_Z(1)>=7d+7; k=2 forces h_Z(1)>=7d+7 for d>=22; combined with B259 the new common floor is H(d)=7d-12 for d=14,16, H(18)=114, H(20)=126, and H(d)=6d+7 for even d>=22
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the obstruction closes G186 as a universal gate and reduces the next piecewise equality audit to explicit dimension/polarization regimes
coefficient_field: Q for zeta and C for sections, tangent jets, spans, hyperplanes, multipartite graphs, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to finite unions of reduced and double points
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B247, B254-B259, S081
claim: On (Q^d,a-b), d even and at least fourteen, the cubic and quartic polarizations have h_Z(1)>=6d+7, every k>=5 has h_Z(1)>=7d+7, and the square polarization has h_Z(1)>=7d+7 for d>=22. With B259 this gives the piecewise common floor H(d): 7d-12 for d=14,16; 114 for d=18; 126 for d=20; and 6d+7 for even d>=22. G186 is NO-GO as a universal gate.
falsifier: a complete multipartite good graph on six vertices with largest part at most three and no Hamiltonian cycle, failure of the eight-edge cover when the largest part is four, more than one cubic hard four-point line, sextic point rank above nine on that hard locus plus P6, quartic point rank above 126 on P^5, failure of a residual full-jet extension, an equality candidate in an excluded polarization regime, or a different piecewise floor
---

# B260 — A seventh point reduces the polarization regimes

Let \(S\) be the marked point span. B254-B256 provide six marked points

\[
 P_6=\{p_1,\ldots,p_6\} \tag{1}
\]

with independent double neighborhoods for every nonstandard
polarization. The first four points may be chosen with no three
collinear. Their tangent span has dimension \(6(d+1)\).

## Good graphs on six supports

Fix a further marked point \(u\). Partition \(P_6\) by the lines through
\(u\), and call an edge good when its pair line avoids \(u\). Since no
three of the first four points are collinear, every class has size at
most four.

If the largest class has size at most three, the complete multipartite
good graph has a Hamiltonian six-cycle. If a class has size four, join
each of its four vertices to each of the other two vertices. These eight
good edges have degree two on the four-class and degree four on the
remaining vertices.

Choosing a pair-line hyperplane avoiding \(u\) for every selected edge
therefore gives:

- a sextic vanishing on \(2P_6\) and a unit at \(u\) when all classes
  have size at most three;
- an octic with the same properties in every case.

## The cubic polarization

For \(k=3\), a four-element class consists of \(p_5,p_6\) and two of
the first four points. Hence every such class lies on the unique line
\(\overline{p_5p_6}\); there is at most one hard line.

That line together with the two remaining first-four points has sextic
point rank at most

\[
 h^0(\mathbf P^1,O(6))+2=9. \tag{2}
\]

Since \(h_Z(1)\ge6d+6>9\), choose a marked \(u\) outside this hard
locus. The Hamiltonian six-cycle produces a sextic vanishing on
\(2P_6\) and nonzero at \(u\). Equality
\(h_Z(1)=6d+6\) would make the six tangent blocks fill \(S\), contrary
to this separator. Therefore

\[
 k=3\quad\Longrightarrow\quad h_Z(1)\ge6d+7. \tag{3}
\]

## The quartic and higher polarizations

For \(k=4\), the octic good-edge product separates every seventh marked
point from the six-double span. Thus

\[
 k=4\quad\Longrightarrow\quad h_Z(1)\ge6d+7. \tag{4}
\]

For \(k\ge5\), multiply the octic unit by

\[
 H^0(Q,O_Q(2k-8)). \tag{5}
\]

The exponent is at least two, so (5) supplies every constant and first
jet at \(u\). The seventh double neighborhood is independent and

\[
 k\ge5\quad\Longrightarrow\quad h_Z(1)\ge7(d+1)=7d+7. \tag{6}
\]

## The square polarization in high dimension

For \(k=2\), B254 chooses its six independent double supports with
projective span of dimension at most five. If all marked points lay in
that span, their quartic point rank would be at most

\[
 h^0(\mathbf P^5,O(4))=\binom94=126. \tag{7}
\]

For even \(d\ge22\), B254's floor gives \(6d+6>126\). Choose a marked
point \(u\) outside the span. A hyperplane \(E\) containing the span and
avoiding \(u\) has \(E^2|_{2P_6}=0\) and is a unit on \(2u\).
Multiplication by the complete \(O_Q(2)\) system supplies every first
jet at \(u\), proving

\[
 k=2,\ d\ge22\quad\Longrightarrow\quad
 h_Z(1)\ge7d+7. \tag{8}
\]

## The reduced piecewise boundary

Combine (3)-(8) with B259's standard floor \(7d-12\). Every
polarization satisfies \(h_Z(1)\ge H(d)\), where

\[
 H(d)=
 \begin{cases}
 7d-12,&d=14,16,\\
 114,&d=18,\\
 126,&d=20,\\
 6d+7,&d\ge22\text{ even}.
 \end{cases} \tag{9}
\]

At equality the surviving polarizations are:

\[
\begin{array}{c|c}
 d & \text{survivors}\\ \hline
 14,16 & k=1\\
 18 & k=1,2\\
 20 & k=2\\
 d\ge22\text{ even} & k=3,4.
\end{array} \tag{10}
\]

B260 is a necessary special-input obstruction. It constructs no
configuration, ODP package, rational detector, specified pairing,
algebraic cycle, proof, or disproof of HC.
