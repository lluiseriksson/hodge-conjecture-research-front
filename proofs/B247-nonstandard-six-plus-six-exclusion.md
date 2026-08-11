---
brick_id: B247
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=8, primitive ruling difference zeta=a-b, arbitrary nonstandard very ample A=O_Q(k) with k>=2, and H=A^2
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: complete quadric embeddings, restrictions to double and reduced points, ambient pair lines, hyperplane separators, and their point spans are projective
dimension: dim X=d=2n>=8; at h_Z(1)=4d+4 four marked tangent osculators fill the point span and a fifth marked point escapes it for every k>=2
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the obstruction closes G170 and the adjacent odd layer s=6d+7
coefficient_field: Q for zeta and C for sections, tangent jets, spans, hyperplanes, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to finite unions of double and reduced points
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B231, B235, B243-B246, G170, S081
claim: On (Q^d,a-b), d even and at least eight, no nonstandard polarization A=O_Q(k), k>=2, can attain the G170 rank h_Z(1)=4d+4. For k=2 and k=3, four double neighborhoods are independent and a four-cycle of pair-line hyperplanes separates every fifth marked point; for k>=4, B215 separates four doubles and one reduced point. Together with B246 this closes G170 and s=6d+7. The next balanced signature is s=6d+8, delta_1=3d+4, N=8d+10, and h_Z(1)=4d+5=N/2.
falsifier: a dependent four-double restriction for k=2 or 3, a fifth point not separated by the four-cycle product, a failure of B215 at exponent 2k>=8, a G170 candidate on a valid quadric, or a different next balanced signature
---

# B247 — The nonstandard boundary also fails

At G170 the point span \(S\) has

\[
 \dim S=h_Z(1)=4d+4. \tag{1}
\]

B246 excludes the standard polarization. We test every
\(A=O_Q(k)\), \(k\ge2\), so \(H=A^2=O_Q(2k)\).

## Four double neighborhoods fill the boundary for \(k=2,3\)

Choose a noncollinear marked triple \(p,q,r\), as in B231, and let
\(\Delta\) be the union of its three pair lines. For \(k=2\), every
marked point on \(\Delta\) has total point rank at most

\[
 3h^0(\mathbf P^1,O(4))=15<4d+4. \tag{2}
\]

For \(k=3\), the corresponding bound is

\[
 3h^0(\mathbf P^1,O(6))=21<4d+4. \tag{3}
\]

Thus in either case there is a marked point \(t\notin\Delta\), and no
three of \(p,q,r,t\) are collinear.

B235 proves that the three quartic double neighborhoods at \(p,q,r\)
are independent. Choose hyperplanes containing \(pq,pr,qr\), each
avoiding \(t\), and let \(P\) be their cubic product. It vanishes twice
at \(p,q,r\) and is a unit on \(2t\). Therefore

\[
 P\cdot H^0(Q,O_Q(1))\longrightarrow H^0(2t,O_{2t}(4)) \tag{4}
\]

is surjective: multiplication by \(P|_{2t}\) is an automorphism, and
the complete \(O_Q(1)\) embedding supplies all \(d+1\) constant and
first-jet coordinates. Hence the four double neighborhoods are
independent in degree four and have total dimension \(4d+4\).

For \(k=3\), multiply \(P\) by two additional hyperplanes avoiding all
four supports before varying the last linear factor. The same unit-jet
argument gives four independent double neighborhoods in degree six.
In both cases their dual span has the dimension in (1), so it equals \(S\).

## A four-cycle separates every fifth point

Let \(u\) be any fifth marked point. Call an edge among
\(p,q,r,t\) bad when its pair line contains \(u\). The bad edges are
exactly the pairs lying in one equivalence class of points on the same
line through \(u\). Since no three of \(p,q,r,t\) are collinear, every
class has size at most two.

The complementary good-edge graph is therefore a complete multipartite
graph on four vertices with largest part at most two. It contains a
four-cycle. For each edge of that cycle choose a hyperplane containing
the corresponding pair line and avoiding \(u\). Their product \(F\)
is a quartic with

\[
 F|_{2p\sqcup2q\sqcup2r\sqcup2t}=0,
 \qquad F(u)\ne0, \tag{5}
\]

because every cycle vertex meets exactly two factors. Equation (5)
separates \(u\) from the four-double dual span in degree four,
contradicting \(S\) equal to that span when \(k=2\).

For \(k=3\), multiply \(F\) by two hyperplanes avoiding the five
supports. The resulting sextic gives the same contradiction.

## Higher powers and the next gate

For \(k\ge4\), apply B215 to four double neighborhoods and one reduced
point. Their mixed interpolation degree is

\[
 2\cdot4+1-1=8\le2k, \tag{6}
\]

so their dual span has dimension

\[
 4(d+1)+1=4d+5>\dim S. \tag{7}
\]

Thus no nonstandard polarization survives G170. B246 already excludes
the standard one, so the universal G170 claim and the adjacent odd layer
\(s=6d+7\), which has the same integral rank budget, are NO-GO.

The next balanced signature is

\[
 s=6d+8,\qquad \delta_1=3d+4,\qquad
 N=8d+10,\qquad h_Z(1)=4d+5=N/2. \tag{8}
\]

B247 is a necessary special-input obstruction. It constructs no
configuration, ODP package, rational detector, specified pairing,
algebraic cycle, proof, or disproof of HC.
