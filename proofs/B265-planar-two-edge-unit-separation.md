---
brick_id: B265
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=14, primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2
smoothness: Q^d and the seven reduced marked supports are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: complete quadric embeddings, a residual P^2 through u, distinct good secant lines, normalized pair-line hyperplanes, first-jet graph planes, and connected selected multigraphs are projective
dimension: dim X=d=2n>=14; cubic and quartic polarizations have h_Z(1)>=7d+6; the common floor is M(d)=6d+6 for d=14,16,18,20, M(22)=159, and M(d)=7d+6 for even d>=24
codimension: the primitive codimension-n ruling difference supplies a valid universal input; excluding the planar residual locus closes G190 as a universal gate and leaves low-dimensional square, d=22 standard, and high-dimensional cubic/quartic regimes
coefficient_field: Q for zeta and C for plane equations, local units, tangent jets, annihilator graphs, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to finite unions of reduced and double points
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B247, B254-B264, G190, NG222, S081
claim: In B264's planar residual locus, two geometrically distinct selected pair lines give different normalized unit jets on the plane and hence variable-edge images of combined rank at least d. Therefore every cubic and quartic polarization has h_Z(1)>=7d+6. Together with B260-B264, the common floor is M(d)=6d+6 for d=14,16,18,20, M(22)=159, and M(d)=7d+6 for every even d>=24. G190 is NO-GO as a universal gate.
falsifier: a connected selected graph with no two geometrically distinct pair lines, two distinct plane secants with the same normalized linear equation, failure of the fixed-unit jet difference, combined edge rank below d, a cubic/quartic span below 7d+6, or a different common floor
---

# B265 — Distinct planar secants separate the missing jet

Assume B264's residual case: the six supports and the seventh point lie
in a projective plane

\[
 \Pi=\mathbf P(\langle u,U\rangle)\simeq\mathbf P^2, \tag{1}
\]

and every selected good edge has endpoint tangent plane \(U\).

## Two selected secants are geometrically distinct

B260's selected multigraph is connected on all six supports. If every
selected edge had the same pair line \(L\subset\Pi\), connectivity
would put all six supports on \(L\). In particular the first four
would contain a collinear triple, contrary to their construction.
Hence choose selected edge occurrences \(e,f\) whose pair lines
\(L_e,L_f\subset\Pi\) are distinct. Both avoid \(u\).

For every selected edge occurrence \(g\), choose a hyperplane
\(\ell_g\) containing its pair line and avoiding \(u\), normalized by

\[
 \ell_g(u)=1. \tag{2}
\]

Its restriction to \(\Pi\) is the unique normalized equation of that
pair line. Therefore

\[
 \ell_e|_\Pi\ne\ell_f|_\Pi. \tag{3}
\]

Since both have value one at \(u\), their first jets on \(U\) differ.

## The two graph planes cannot coincide

For the variable edge \(e\), fix the product

\[
 g_e=\prod_{g\ne e}\ell_g, \tag{4}
\]

and vary the factor in \(V_e=I_{L_e}(1)\). Define \(g_f\) analogously,
using the same indexed collection of fixed factors. On the square-zero
first-jet algebra at \(u\), write the unit jets as

\[
 j(g_e)=(1,\beta_e),\qquad j(g_f)=(1,\beta_f). \tag{5}
\]

The product rule and (2) give

\[
 \beta_e-\beta_f=j_1(\ell_f)-j_1(\ell_e). \tag{6}
\]

By (3), the right side is a nonzero functional on \(U\).

B264 identifies each image annihilator as the graph over \(U\) of the
negative fixed-unit functional. Thus the two annihilator planes are
distinct graphs over the same two-dimensional space. Their intersection
is the graph over the one-dimensional kernel of
\((\beta_e-\beta_f)|_U\), so

\[
 \dim(R_e^\perp\cap R_f^\perp)=1. \tag{7}
\]

Since the first-jet target has dimension \(d+1\),

\[
 \dim(R_e+R_f)=d. \tag{8}
\]

Both product spaces vanish on \(2P_6\), because replacing one factor
by another hyperplane through the same edge preserves every incidence
degree. Combining their rank with the six independent double blocks
gives

\[
 k=3,4\quad\Longrightarrow\quad h_Z(1)\ge6d+6+d=7d+6. \tag{9}
\]

## The next common boundary

Combining (9) with the standard floor \(8d-17\) from B263 and the
square/higher-power floors from B260 gives

\[
 M(d)=
 \begin{cases}
 6d+6,&d=14,16,18,20,\\
 159,&d=22,\\
 7d+6,&d\ge24\text{ even}.
 \end{cases} \tag{10}
\]

At equality, only \(k=2\) survives in dimensions \(14,16,18,20\),
only \(k=1\) survives at \(d=22\), and only \(k=3,4\) survive in even
dimensions at least 24. B265 is a necessary special-input obstruction.
It constructs no ODP package, rational detector, specified pairing,
algebraic cycle, proof, or disproof of HC.
