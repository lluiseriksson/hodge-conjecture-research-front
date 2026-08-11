---
brick_id: B254
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=14, primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: complete quadric embeddings, restrictions to double points, low-dimensional linear spans, hyperplane-square separators, and tangent point spans are projective
dimension: dim X=d=2n>=14; the square polarization forces h_Z(1)>=6d+6; together with B249 and B253 every polarization forces h_Z(1)>=5d+5 and slack s>=8d+8
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the obstruction closes G179-G180 and reduces the next equality audit to powers k>=3
coefficient_field: Q for zeta and C for sections, tangent jets, spans, hyperplanes, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to finite unions of double points
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B247, B249, B253, S081
claim: On (Q^d,a-b), d even and at least fourteen, every square-polarized candidate has h_Z(1)>=6d+6. Together with B249's k>=3 floor and B253's standard floor, every polarization has h_Z(1)>=5d+5 and slack s>=8d+8. Hence G179-G180 and their adjacent odd layers are NO-GO; at equality only polarizations O_Q(k), k>=3, remain.
falsifier: a square-polarized tangent-absorbing point span of rank below 6d+6, failure of the P^3 or P^4 point-rank bounds, failure of hyperplane-square first-jet separation, a candidate below the common floor, a standard or square equality candidate, or a different next balanced signature
---

# B254 — The square polarization forces six double blocks

Let \(A=O_Q(2)\), so \(H=O_Q(4)\), and let \(S\) be the marked point
span. B249 gives

\[
 \dim S=h_Z(1)\ge5d+3. \tag{1}
\]

B247 supplies four marked points

\[
 P_4=\{p_1,p_2,p_3,p_4\} \tag{2}
\]

whose double neighborhoods are independent. Their tangent span has
dimension \(4(d+1)\), and their projective linear span has dimension
at most three.

## A hyperplane-square extension lemma

Let \(P_r=\{p_1,\ldots,p_r\}\) be marked points with independent
double neighborhoods, and let \(u\) be a marked point outside
\(\langle P_r\rangle\). Choose an ambient hyperplane \(E\) containing
\(\langle P_r\rangle\) and avoiding \(u\). Then \(E^2\) vanishes on
every \(2p_i\) and is a unit on \(2u\).

The complete \(O_Q(1)\) system already separates constant and first
jets at \(u\), so the restriction

\[
 H^0(Q,O_Q(2))\longrightarrow H^0(2u,O_{2u}(2)) \tag{3}
\]

is surjective. Multiplication by the unit \(E^2|_{2u}\) is an
automorphism of the target. Hence

\[
 E^2H^0(Q,O_Q(2))
 \longrightarrow H^0(2u,O_{2u}(4)) \tag{4}
\]

is surjective while every source section vanishes on \(2P_r\).
Therefore \(2u\) contributes all \(d+1\) dimensions beyond the
independent double span of \(P_r\).

## The fifth double block

If every marked point lay in \(\langle P_4\rangle\simeq\mathbf P^a\),
\(a\le3\), its quartic point rank would be at most

\[
 h^0(\mathbf P^3,O(4))=\binom74=35. \tag{5}
\]

For \(d\ge14\), (1) gives \(h_Z(1)\ge73>35\). Thus there is a marked
\(p_5\notin\langle P_4\rangle\). The extension lemma shows that the
five double neighborhoods are independent, with tangent span

\[
 5(d+1)=5d+5. \tag{6}
\]

## The sixth double block

The projective span \(\langle P_4,p_5\rangle\) has dimension at most
four. If every marked point lay in it, the quartic point rank would be
at most

\[
 h^0(\mathbf P^4,O(4))=\binom84=70. \tag{7}
\]

Again (1) gives \(h_Z(1)\ge73>70\). Choose a marked
\(p_6\notin\langle P_4,p_5\rangle\). Applying the extension lemma to
the five independent doubles proves that \(2p_6\) contributes another
\(d+1\) dimensions. Hence

\[
 A=O_Q(2)\quad\Longrightarrow\quad
 h_Z(1)\ge6(d+1)=6d+6. \tag{8}
\]

## The improved common floor

B253 gives the standard floor \(6d-7\), while B249 gives
\(h_Z(1)\ge5d+5\) for every \(O_Q(k)\), \(k\ge3\). For even
\(d\ge14\),

\[
 \min\{6d-7,\,6d+6,\,5d+5\}=5d+5. \tag{9}
\]

Thus every polarization satisfies

\[
 h_Z(1)\ge5d+5,\qquad
 \delta_1\ge4d+4,\qquad s\ge8d+8. \tag{10}
\]

Consequently G179-G180 and every layer through \(s=8d+7\) are
NO-GO. At the next balanced signature

\[
 s=8d+8,\qquad \delta_1=4d+4,\qquad
 N=10d+10,\qquad h_Z(1)=5d+5=N/2, \tag{11}
\]

the standard and square polarizations are strictly above the rank
budget. Only \(A=O_Q(k)\), \(k\ge3\), remains.

B254 is a necessary special-input obstruction. It constructs no
configuration, ODP package, rational detector, specified pairing,
algebraic cycle, proof, or disproof of HC.
