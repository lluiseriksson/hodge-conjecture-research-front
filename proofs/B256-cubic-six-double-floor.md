---
brick_id: B256
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=14, primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: complete quadric embeddings, reduced and double point restrictions, collinear-triple lines, good-edge cycles, hyperplane products, and tangent point spans are projective
dimension: dim X=d=2n>=14; the cubic polarization forces h_Z(1)>=6d+6; every nonstandard k>=2 has the same floor, while every polarization has h_Z(1)>=6d-7 and slack s>=10d-16
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the obstruction closes G182 and reduces the next equality audit to the standard polarization
coefficient_field: Q for zeta and C for sections, tangent jets, spans, hyperplanes, graphs, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to finite unions of reduced and double points
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B247, B249, B253-B255, S081
claim: On (Q^d,a-b), d even and at least fourteen, the cubic polarization A=O_Q(3) has h_Z(1)>=6d+6. Hence every nonstandard polarization has h_Z(1)>=6d+6, while B253 gives the common all-polarization floor h_Z(1)>=6d-7 and slack s>=10d-16. G182 and every layer through s=10d-17 are NO-GO; at equality only A=O_Q(1) remains.
falsifier: more than two collinear-triple lines through the fifth support, a sextic point rank above fourteen on their union plus the five supports, failure of a good graph with largest part two to have a spanning five-cycle, failure of the quintic product times O_Q(1) to separate the sixth double, a cubic span below six double blocks, or a different common floor
---

# B256 — The cubic polarization forces six double blocks

Let \(A=O_Q(3)\), \(H=O_Q(6)\), and let \(S\) be the marked point
span. B249 supplies five marked points

\[
 P_5=\{p_1,p_2,p_3,p_4,p_5\} \tag{1}
\]

with independent double neighborhoods, where no three of
\(p_1,p_2,p_3,p_4\) are collinear.

## The hard locus has tiny point rank

For a further marked point \(x\), B255 partitions \(P_5\) by the lines
through \(x\). A class of size three can occur only when \(x\) lies on
a line containing \(p_5\) and two of the first four points.

There are at most two such triple lines. Indeed, encode one by the edge
\(ij\) of the complete graph on \(p_1,\ldots,p_4\) for which
\(p_5\in\overline{p_ip_j}\). Two such edges cannot share a vertex:
their lines would both contain that vertex and \(p_5\), hence coincide
and put three of the first four points on one line. The possible edges
therefore form a matching of size at most two.

Let \(D\) be the union of those triple lines. If there is one line, then
\(D\cup P_5\) is that line plus two reduced points, of sextic point rank
at most

\[
 h^0(\mathbf P^1,O(6))+2=9. \tag{2}
\]

If there are two lines, the coarser upper bound is

\[
 2h^0(\mathbf P^1,O(6))=14. \tag{3}
\]

B249 gives \(h_Z(1)\ge5d+5>14\). Thus the marked support cannot lie in
\(D\cup P_5\); choose a marked

\[
 x\notin D\cup P_5. \tag{4}
\]

Every line-through-\(x\) class in \(P_5\) now has size at most two.

## A quintic unit supplies the sixth double

The good-edge graph on \(P_5\) is complete multipartite with largest
part at most two. It has a spanning five-cycle. For each cycle edge
choose an ambient hyperplane containing its pair line and avoiding
\(x\). Their product \(U\) is a quintic satisfying

\[
 U|_{2P_5}=0,\qquad U|_{2x}\ \text{is a unit}. \tag{5}
\]

The complete linear system restricts surjectively,

\[
 H^0(Q,O_Q(1))\longrightarrow H^0(2x,O_{2x}(1)), \tag{6}
\]

because \(O_Q(1)\) is the ambient embedding. Multiplication by the unit
in (5) therefore makes

\[
 U\cdot H^0(Q,O_Q(1))
 \longrightarrow H^0(2x,O_{2x}(6)) \tag{7}
\]

surjective, while every source section vanishes on \(2P_5\). The sixth
double neighborhood contributes all \(d+1\) dimensions, so

\[
 A=O_Q(3)\quad\Longrightarrow\quad
 h_Z(1)\ge6(d+1)=6d+6. \tag{8}
\]

## The new common floor

B254 gives the same \(6d+6\) floor for \(k=2\), and B255 gives it for
every \(k\ge4\). B253 gives \(6d-7\) for the standard polarization.
Consequently, for even \(d\ge14\),

\[
 h_Z(1)\ge6d-7,\qquad
 \delta_1\ge5d-8,\qquad s\ge10d-16. \tag{9}
\]

Thus G182 and every layer through \(s=10d-17\) are NO-GO. The next
balanced signature is

\[
 s=10d-16,\qquad \delta_1=5d-8,\qquad
 N=12d-14,\qquad h_Z(1)=6d-7=N/2. \tag{10}
\]

Only the standard polarization \(A=O_Q(1)\) survives at (10). B256 is
a necessary special-input obstruction. It constructs no configuration,
ODP package, rational detector, specified pairing, algebraic cycle,
proof, or disproof of HC.
