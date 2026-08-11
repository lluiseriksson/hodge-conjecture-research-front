---
brick_id: B246
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=8, primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: complete quadric embeddings, standard tangent quotients, self-adjoint annihilators, orthogonal projective three-spaces, and their point spans are projective
dimension: dim X=d=2n>=8; the standard polarization forces h_Z(1)>=5d-3, every nonstandard polarization forces h_Z(1)>=4d+4, and every m=2 candidate therefore has slack s>=6d+6
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the obstruction closes G169 and every layer through s=6d+5
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B221-B245, G169, S081
claim: On (Q^d,a-b), d even and at least eight, every standard-polarized m=2 candidate has h_Z(1)>=5d-3. Together with B244's nonstandard lower bound h_Z(1)>=4d+4, every m=2 candidate has s>=6d+6. At equality the only unexcluded signature is delta_1=3d+3, N=8d+8, and h_Z(1)=4d+4=N/2, and the standard polarization is impossible.
falsifier: a standard candidate below rank 5d-3, a residual third tangent below rank d-3, an additional tangent outside K-perp below rank d-3, point rank above ten on K-perp, a candidate below slack 6d+6, or a different equality signature
---

# B246 — The standard polarization forces a fifth block

Let \(S\) be the point span for the standard quadratic embedding.
Choose a nonorthogonal marked pair \(v,w\) and put

\[
 U=\langle v,w\rangle^\perp. \tag{1}
\]

The all-orthogonal alternative is excluded by B231.

## The residual-\(U\) branch

Suppose every residual point lies in \(U\). A nonorthogonal residual
pair \(r,t\) has two disjoint tangent images of total dimension
\(2d-2\). The all-orthogonal residual alternative is excluded by B237.

Choose a third residual marked point \(u\). On the smaller quadric
\(Q(U)\), of dimension \(d-2\), B233's direct calculation gives tangent
contribution at least \(d-3\) beyond the first pair. Therefore

\[
 \dim S\ge 2d+2+(2d-2)+(d-3)=5d-3. \tag{2}
\]

## A third point meeting the hyperbolic plane

Choose \(r\notin U\), and put

\[
 S_0=T_v+T_w+T_r,\qquad R=\langle v,w,r\rangle,\qquad
 W=R^\perp. \tag{3}
\]

Then \(\dim S_0=3d+2\) and \(\dim W=d-1\). Choose a marked
\(t\notin R\), since the plane conic in \(\mathbf P(R)\) has point rank
at most five.

If \(t\notin W\), its tangent contributes \(d-1\) dimensions. With

\[
 K=W\cap t^\perp,\qquad \dim K=d-2, \tag{4}
\]

the annihilator of \(S_0+T_t\) is \(\operatorname{Sym}^2K\), whose
contact locus is \(K^\perp\), a projective three-space of point rank at
most ten. Since \(S_0+T_t\) already has dimension \(4d+1>10\), choose a
marked \(u\notin K^\perp\). Contraction of
\(\operatorname{Sym}^2K\) with \(u\), modulo \(\mathbf Cu\), has rank at
least \(d-3\). Hence

\[
 \dim S\ge(4d+1)+(d-3)=5d-2. \tag{5}
\]

Now suppose \(t\in W\). Its tangent contributes \(d-2\) dimensions, so

\[
 S_1=S_0+T_t,\qquad \dim S_1=4d. \tag{6}
\]

Its annihilator is

\[
 L=\{A\in\operatorname{Sym}^2W:At\in\mathbf Ct\}, \tag{7}
\]

with contact locus \(R\cup\mathbf Ct\). Choose a marked point \(u\)
outside that locus and put \(K=t^\perp\cap W\).

If \(u\notin K^\perp\), the subspace
\(\operatorname{Sym}^2K\subset L\) gives tangent contribution at least
\(d-3\). Thus

\[
 \dim S\ge4d+d-3=5d-3. \tag{8}
\]

If \(u\in K^\perp\setminus(R\cup\mathbf Ct)\), B245 shows that \(T_u\)
contributes exactly one dimension and changes the annihilator to
\(\operatorname{Sym}^2K\). Its contact locus is \(K^\perp\), of point
rank at most ten. Choose a further marked point \(x\notin K^\perp\).
Its tangent contributes at least \(d-3\), giving

\[
 \dim S\ge4d+1+d-3=5d-2. \tag{9}
\]

Every standard-polarized candidate therefore satisfies

\[
 h_Z(1)\ge5d-3. \tag{10}
\]

## The common floor and next boundary

B244 already proves

\[
 k\ge2\quad\Longrightarrow\quad h_Z(1)\ge4d+4. \tag{11}
\]

For \(d\ge8\), (10) is strictly larger than \(4d+4\). Thus every
polarization satisfies \(h_Z(1)\ge4d+4\). Using
\(h_Z(1)=d+1+\delta_1\) and \(2\delta_1\le s\) gives

\[
 m=2\quad\Longrightarrow\quad s\ge6d+6. \tag{12}
\]

At \(s=6d+6\), lower ranks are excluded and the budget gives
\(\delta_1\le3d+3\). Hence the only unexcluded signature is

\[
 \delta_1=3d+3,\qquad N=8d+8,\qquad
 h_Z(1)=4d+4=N/2,\qquad s-2\delta_1=0. \tag{13}
\]

The standard polarization cannot attain this rank because
\(5d-3>4d+4\) for \(d\ge8\). The nonstandard polarizations must be
re-audited at equality.

B246 is a necessary special-input obstruction. It constructs no
configuration, ODP package, rational detector, specified pairing,
algebraic cycle, proof, or disproof of HC.
