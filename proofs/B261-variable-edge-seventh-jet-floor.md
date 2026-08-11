---
brick_id: B261
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=14, primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: complete quadric embeddings, restrictions to reduced and double points, good-edge cycles and covers, variable pair-line hyperplanes, and tangent point spans are projective
dimension: dim X=d=2n>=14; cubic and quartic polarizations force h_Z(1)>=7d+5; with B259-B260 the new common floor is J(d)=7d-12 except J(20)=126
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the obstruction closes G187 as a universal gate and returns every high-dimensional equality branch to the standard polarization
coefficient_field: Q for zeta and C for sections, tangent jets, spans, variable hyperplanes, multipartite graphs, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to finite unions of reduced and double points
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B247, B249, B254-B260, S081
claim: On (Q^d,a-b), d even and at least fourteen, every cubic or quartic polarization has h_Z(1)>=7d+5. Together with B259-B260, every polarization has h_Z(1)>=J(d), where J(d)=7d-12 for d=14,16,18 and every even d>=22, while J(20)=126. G187 is NO-GO as a universal gate.
falsifier: a variable pair-line hyperplane family of rank below d-1 on the first jets of the seventh point, failure of the fixed remaining factors to be units, a cubic or quartic span below 7d+5, an equality candidate in an excluded high-dimensional regime, or a different piecewise floor
---

# B261 — A variable edge supplies \(d-1\) seventh-point jets

Retain B260's six independent double supports \(P_6\) and a seventh
marked point \(u\).

## The variable-edge lemma

Let \(e\) be one selected good edge, and let

\[
 V_e=I_{\overline e}(1) \tag{1}
\]

be the vector space of ambient hyperplanes containing its pair line.
Since the ambient space is \(\mathbf P^{d+1}\),

\[
 \dim V_e=d. \tag{2}
\]

The complete \(O_Q(1)\) restriction to \(2u\) is surjective onto a
target of dimension \(d+1\), with one-dimensional kernel given by the
tangent hyperplane at \(u\). Therefore

\[
 \operatorname{rank}\bigl(V_e\longrightarrow
 H^0(2u,O_{2u}(1))\bigr)\ge d-1. \tag{3}
\]

Fix every other selected pair-line hyperplane so that it avoids \(u\).
Their product is a unit on \(2u\). Varying the factor in \(V_e\)
preserves at least two incident factors at every support of \(P_6\):
the variable factor always contains both endpoints of \(e\). Hence the
resulting products vanish on \(2P_6\), and multiplication by the fixed
unit preserves the rank in (3).

## Cubic and quartic floors

For \(k=3\), B260 chooses \(u\) outside the unique possible hard
four-point line and uses a Hamiltonian good six-cycle. Applying the
variable-edge lemma to one cycle edge gives a residual rank of at least
\(d-1\). Since the six independent doubles contribute \(6d+6\),

\[
 k=3\quad\Longrightarrow\quad
 h_Z(1)\ge6d+6+(d-1)=7d+5. \tag{4}
\]

For \(k=4\), use B260's eight-edge cover, repeating good edges when a
six-cycle suffices. The same variable-edge argument gives

\[
 k=4\quad\Longrightarrow\quad h_Z(1)\ge7d+5. \tag{5}
\]

## The updated common boundary

B259 gives the standard floor \(7d-12\). B260 gives \(7d+7\) for
\(k\ge5\), and also for \(k=2\) when \(d\ge22\). Combining with
(4)-(5), every polarization satisfies

\[
 h_Z(1)\ge J(d),\qquad
 J(d)=
 \begin{cases}
 7d-12,&d=14,16,18,\\
 126,&d=20,\\
 7d-12,&d\ge22\text{ even}.
 \end{cases} \tag{6}
\]

At equality the survivors are:

\[
\begin{array}{c|c}
 d & \text{survivors}\\ \hline
 14,16 & k=1\\
 18 & k=1,2\\
 20 & k=2\\
 d\ge22\text{ even} & k=1.
\end{array} \tag{7}
\]

B261 is a necessary special-input obstruction. It constructs no
configuration, ODP package, rational detector, specified pairing,
algebraic cycle, proof, or disproof of HC.
