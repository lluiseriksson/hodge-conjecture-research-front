---
brick_id: B237
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=4, primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: the standard quadratic embedding, tangent osculators, plane-conic contact loci, orthogonal complements, and isotropic spans are projective
dimension: dim X=d=2n; no m=2 candidate exists with slack s<=4d+3; at the first unexcluded value s=4d+4 one has N=6d+6 and h_Z(1)=3d+3=N/2
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the contact dichotomy raises the degree-two floor to the nonstandard-polarization threshold
coefficient_field: Q for zeta and C for quadratic forms, self-adjoint endomorphisms, tangent jets, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to double-point schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B221-B236, S081
claim: On (Q^d,a-b), no m=2 G144 candidate exists with slack s<=4d+3. At the first unexcluded value s=4d+4, necessarily delta_1=2d+2, N=6d+6, h_Z(1)=3d+3=N/2, and the degree-one relation transport is an isomorphism; standard and nonstandard quadric polarizations all re-enter the audit.
falsifier: a candidate in the excluded band, failure of the self-adjoint contact-locus characterization, a marked point outside the resulting plane conic in the nonorthogonal-third branch, a residual nonorthogonal pair fitting in the d-dimensional quotient, or a different next rank
---

# B237 — The post-boundary contact dichotomy

B235-B236 exclude \(m=2\) through slack \(4d+1\), and B235 excludes
every nonstandard quadric polarization below \(4d+4\). It remains to test

\[
 4d+2\le s\le4d+3,\qquad A=O_Q(1). \tag{1}
\]

The only rank not already excluded is

\[
 \delta_1=2d+1,\qquad \dim S=h_Z(1)=3d+2. \tag{2}
\]

Choose a nonorthogonal marked pair \(v,w\); otherwise B231 applies. Put
\(H_0=\langle v,w\rangle\) and \(U=H_0^\perp\). The quotient of \(S\)
by \(T_v\oplus T_w\) has dimension \(d\).

## A third point meeting the hyperbolic plane

Suppose some third marked point \(r\) is not orthogonal to \(H_0\).
B236's projection computation then gives quotient rank exactly \(d\), so

\[
 S=T_v+T_w+T_r. \tag{3}
\]

We compute the entire tangential contact locus of (3). Use the quadric
form \(B\) to identify a quadratic section, modulo the defining equation,
with a \(B\)-self-adjoint endomorphism \(A\), modulo scalars. For an
isotropic vector \(x\),

\[
 A\text{ annihilates }T_x=x\mathbin{\odot}x^\perp
 \quad\Longleftrightarrow\quad Ax\in\mathbf Cx. \tag{4}
\]

Hence the annihilator of (3) consists of self-adjoint \(A\) for which
\(v,w,r\) are eigenvectors. Self-adjointness and the nonorthogonality
graph force their three eigenvalues to agree. Therefore every such
\(A\) acts as a scalar on

\[
 R=\langle v,w,r\rangle. \tag{5}
\]

Conversely, a vector \(t\notin R\) is not a common eigenvector of this
annihilator. Indeed, since \((R^\perp)^\perp=R\), choose
\(z\in R^\perp\) with \(B(z,t)\ne0\) and \(z\notin\mathbf Ct\). The
rank-one self-adjoint map

\[
 E_z(x)=B(z,x)z \tag{6}
\]

vanishes on \(R\), belongs to the annihilator, and sends \(t\) to a
nonzero vector not proportional to \(t\). Thus

\[
 T_t\subset S\quad\Longleftrightarrow\quad t\in R. \tag{7}
\]

Every marked point lies on the plane conic \(Q\cap\mathbf P(R)\),
possibly degenerate. Its \(O_Q(2)\) point span has dimension at most

\[
 h^0(Q\cap\mathbf P(R),O(2))=5, \tag{8}
\]

contradicting (2).

## Every remaining point orthogonal to the pair

Suppose instead that every marked point other than \(v,w\) lies in
\(U\). Modulo \(T_v\oplus T_w\), their squares span a
\(d\)-dimensional space \(S_U\). At a residual point \(r\), the image of
the full tangent osculator is

\[
 r\mathbin{\odot}(r^\perp\cap U), \tag{9}
\]

the \((d-1)\)-dimensional tangent osculator of the smaller quadric
\(Q(U)\).

If two residual representatives were nonorthogonal, their two
osculators in (9) would be disjoint and have total dimension
\(2d-2>d=\dim S_U\). Hence every residual pair is orthogonal. Their
span \(W\subset U\) is totally isotropic, and
\(S_U\subset\operatorname{Sym}^2W\). But
\(\dim(r^\perp\cap U)=d-1>\dim W\), so one may choose
\(y\in(r^\perp\cap U)\setminus W\). Then
\(r\mathbin{\odot}y\notin\operatorname{Sym}^2W\), contradicting (9).

Both branches are impossible. Therefore

\[
 m=2\quad\Longrightarrow\quad s\ge4d+4. \tag{10}
\]

At \(s=4d+4\), the preceding obstruction excludes
\(\delta_1\le2d+1\), while the budget gives
\(\delta_1\le2d+2\). Thus

\[
 \delta_1=2d+2,\qquad N=6d+6,\qquad
 h_Z(1)=3d+3=N/2,\qquad s-2\delta_1=0. \tag{11}
\]

The relation transport is an isomorphism. This is also the first value
where B235 permits \(O_Q(k)\), \(k\ge2\), so all polarizations re-enter
the next audit. B237 constructs no threshold configuration, detector,
pairing, or cycle.
