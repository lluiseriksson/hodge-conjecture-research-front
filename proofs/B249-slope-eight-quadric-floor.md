---
brick_id: B249
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=8, primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: complete quadric embeddings, restrictions to double points, pair-line four-cycles, variable hyperplane families, and tangent point spans are projective
dimension: dim X=d=2n>=8; the standard polarization forces h_Z(1)>=5d-3, the square polarization forces h_Z(1)>=5d+3, every k>=3 forces h_Z(1)>=5d+5, and every m=2 candidate therefore has slack s>=8d-8
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the obstruction replaces G172's unspecified growing excess by the exact first possible standard slope-eight boundary
coefficient_field: Q for zeta and C for sections, tangent jets, spans, hyperplanes, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to finite unions of double points
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B231, B235, B244-B248, S081
claim: On (Q^d,a-b), d even and at least eight, every square-polarized m=2 candidate has h_Z(1)>=5d+3, and every polarization O_Q(k) with k>=3 has h_Z(1)>=5d+5. Together with B246's standard floor h_Z(1)>=5d-3, every m=2 candidate has s>=8d-8. At equality the only unexcluded signature is standard-polarized with delta_1=4d-4, N=10d-6, and h_Z(1)=5d-3=N/2.
falsifier: a square fifth tangent contributing fewer than d-1 residual dimensions, failure of the four-cycle unit family, a k>=3 fifth double dependency, a candidate below slack 8d-8, a nonstandard equality candidate, or a different equality signature
---

# B249 — The degree-two quadric floor has slope eight

Let \(S\) be the \(H=A^2\) point span. B247 supplies four marked points

\[
 P=\{p_1,p_2,p_3,p_4\}, \tag{1}
\]

with no three collinear and with independent double neighborhoods for
every nonstandard polarization. Their dual tangent span has dimension
\(4d+4\).

## The square polarization

Take \(A=O_Q(2)\), so \(H=O_Q(4)\), and let \(u\) be a fifth marked
point. As in B247, declare a pair edge bad when its line contains \(u\).
The good-edge graph on \(P\) has a four-cycle.

Fix one cycle edge \(e\), and choose hyperplanes for the other three
cycle edges, all avoiding \(u\). Their product is a unit on \(2u\).
Let

\[
 V_e=I_{\overline e}(1) \tag{2}
\]

be the vector space of hyperplanes containing the pair line of \(e\).
Since the ambient space is \(\mathbf P^{d+1}\),

\[
 \dim V_e=d. \tag{3}
\]

The complete \(O_Q(1)\) restriction to \(2u\) has target dimension
\(d+1\) and one-dimensional kernel, the tangent hyperplane at \(u\).
Therefore

\[
 \operatorname{rank}\bigl(V_e\longrightarrow H^0(2u,O_{2u}(1))\bigr)
 \ge d-1. \tag{4}
\]

Multiplying \(V_e\) by the three fixed unit hyperplanes gives quartics
vanishing twice at every point of \(P\). Multiplication by the fixed
unit is an automorphism on \(O_{2u}\), so (4) is exactly a residual
rank-\((d-1)\) family beyond the four-double span. Hence

\[
 k=2\quad\Longrightarrow\quad
 h_Z(1)\ge4d+4+(d-1)=5d+3. \tag{5}
\]

## Every higher polarization

Let \(k\ge3\). B247's four-cycle product \(F_u\) is a quartic vanishing
on \(2P\) and a unit on \(2u\). Multiplication gives

\[
 F_u\cdot H^0(Q,O_Q(2k-4))
 \longrightarrow H^0(2u,O_{2u}(2k)). \tag{6}
\]

Because \(2k-4\ge2\), the second factor supplies every constant and
first jet at \(u\); multiplication by \(F_u|_{2u}\) is an automorphism.
Thus the fifth double neighborhood contributes all \(d+1\) dimensions:

\[
 k\ge3\quad\Longrightarrow\quad
 h_Z(1)\ge5(d+1)=5d+5. \tag{7}
\]

## The common floor

B246 already proves

\[
 k=1\quad\Longrightarrow\quad h_Z(1)\ge5d-3. \tag{8}
\]

Equations (5), (7), and (8) give the common lower bound

\[
 h_Z(1)\ge5d-3. \tag{9}
\]

Using

\[
 h_Z(1)=d+1+\delta_1,\qquad 2\delta_1\le s, \tag{10}
\]

we obtain

\[
 m=2\quad\Longrightarrow\quad s\ge8d-8. \tag{11}
\]

At equality the rank budget forces

\[
 \delta_1=4d-4,\qquad
 N=2(d+1)+8d-8=10d-6,\qquad
 h_Z(1)=5d-3=N/2. \tag{12}
\]

The square and all higher polarizations lie strictly above (12), so
only the standard polarization can remain at the first boundary.

B249 is a necessary special-input obstruction. It constructs no
configuration, ODP package, rational detector, specified pairing,
algebraic cycle, proof, or disproof of HC.
