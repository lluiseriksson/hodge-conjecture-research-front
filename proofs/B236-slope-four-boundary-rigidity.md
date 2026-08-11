---
brick_id: B236
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=4, primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2
smoothness: Q^d and the reduced marked points are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: the standard O_Q(2) embedding, tangent osculators, isotropic lines, and symmetric-tensor decompositions are projective
dimension: dim X=d=2n; no m=2 candidate exists with slack s<=4d+1; at the first unexcluded value s=4d+2 one has N=6d+4 and h_Z(1)=3d+2=N/2
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the boundary obstruction raises the degree-two floor by two layers
coefficient_field: Q for zeta and C for quadratic forms, symmetric tensors, tangent jets, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to double-point schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B221-B235, S081
claim: On (Q^d,a-b), no m=2 G144 candidate exists with slack s<=4d+1. At the first unexcluded value s=4d+2, necessarily A=O_Q(1), delta_1=2d+1, N=6d+4, h_Z(1)=3d+2=N/2, and the degree-one relation transport is an isomorphism.
falsifier: a slope-four boundary candidate, a third tangent whose quotient rank is d-1 without being orthogonal to the initial nonorthogonal pair, a fourth tangent absorbed by the three-tangent boundary span, or a different next rank
---

# B236 — The slope-four boundary cannot absorb a fourth tangent

B235 excludes \(s<4d\) on \((Q^d,a-b)\) and excludes every
nonstandard polarization through \(s<4d+4\). It remains to test

\[
 4d\le s\le4d+1,\qquad A=O_Q(1). \tag{1}
\]

If \(\delta_1<2d\), B235 already applies. Thus the only remaining rank is

\[
 \delta_1=2d,\qquad \dim S=h_Z(1)=3d+1. \tag{2}
\]

## Equality forces an orthogonal third point

Choose a nonorthogonal marked pair \(v,w\); the all-orthogonal case is
excluded by B231. Write \(V=\langle v,w\rangle\perp U\), normalizing
\(B(v,w)=1\). For a third marked point

\[
 r=av+bw+u,\qquad u\in U, \tag{3}
\]

the projection of its tangent osculator modulo \(T_v\oplus T_w\) is
generated, as \(y\in U\) varies, by

\[
 u\mathbin{\odot}y-B(u,y)\,vw. \tag{4}
\]

If \((a,b)\ne(0,0)\), every \(y\in U\) occurs after solving the single
orthogonality equation for the \(v,w\) coordinates. The map in (4) is
injective, so its image has dimension \(d\). But (2) leaves only
\(d-1\) quotient dimensions. Hence \(a=b=0\), and

\[
 r=u\in U,\qquad B(r,v)=B(r,w)=0. \tag{5}
\]

Now the image in (4) is \(r\mathbin{\odot}(r^\perp\cap U)\), of
dimension \(d-1\), so the three tangent osculators fill \(S\).

## No fourth point has its tangent inside this span

Choose a hyperbolic partner \(r'\in U\) with \(B(r,r')=1\) and write

\[
 U=\langle r,r'\rangle\perp U_1. \tag{6}
\]

The three-tangent span has the symmetric-monomial description

\[
 S=\langle v^2,w^2,vU,wU,r^2,rU_1\rangle. \tag{7}
\]

Let a fourth marked representative be

\[
 t=\alpha v+\beta w+\gamma r+\varepsilon r'+z,
 \qquad z\in U_1. \tag{8}
\]

The condition \(t^2\in S\) is tested in the direct complementary
summands

\[
 \langle vw,rr',r'^2\rangle\oplus r'U_1
 \oplus\operatorname{Sym}^2U_1. \tag{9}
\]

It forces

\[
 \varepsilon=0,\qquad z=0,\qquad \alpha\beta=0. \tag{10}
\]

Thus \(t\) lies on one of the isotropic planes
\(\langle v,r\rangle\) or \(\langle w,r\rangle\).

Suppose \(t=\alpha v+\gamma r\) with \(\alpha\gamma\ne0\). The vector

\[
 x=\alpha r'-\gamma w \tag{11}
\]

satisfies \(B(t,x)=0\), but

\[
 t\mathbin{\odot}x
 \equiv\alpha\gamma(rr'-vw)\pmod S, \tag{12}
\]

which is nonzero by (9). Hence \(T_t\not\subset S\). The symmetric
argument with \(x=\beta r'-\gamma v\) excludes a nontrivial point on
\(\langle w,r\rangle\). Therefore a point whose full tangent is absorbed
by \(S\) must be one of \([v],[w],[r]\), contradicting the existence of
the many distinct marked points.

This excludes both slack values in (1), so

\[
 m=2\quad\Longrightarrow\quad s\ge4d+2. \tag{13}
\]

At \(s=4d+2\), B235-B236 exclude \(\delta_1\le2d\), while the budget
gives \(\delta_1\le2d+1\). Hence

\[
 \delta_1=2d+1,\qquad N=6d+4,\qquad
 h_Z(1)=3d+2=N/2,\qquad s-2\delta_1=0. \tag{14}
\]

Only \(A=O_Q(1)\) can occur because B235 requires \(s\ge4d+4\) for
every \(k\ge2\). B236 constructs no threshold configuration, ODP
package, rational detector, specified pairing, or cycle.
