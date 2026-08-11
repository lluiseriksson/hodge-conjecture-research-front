---
brick_id: B250
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=8, primitive ruling difference zeta=a-b, standard A=O_Q(1), and H=O_Q(2)
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: the standard quadratic embedding, tangent quotient spaces, smaller orthogonal quadrics, self-adjoint annihilators, rank-one maps, and projective-four-space contact bounds are projective
dimension: dim X=d=2n>=8; no standard candidate exists at h_Z(1)=5d-3, so the slope-eight layers s=8d-8 and s=8d-7 are excluded
codimension: the primitive codimension-n ruling difference supplies a valid universal input; B249 already excludes every nonstandard polarization at this rank
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B231, B235-B237, B245-B249, S081
claim: On (Q^d,a-b), d even and at least eight, the standard polarization cannot realize h_Z(1)=5d-3 with every marked tangent osculator absorbed. Hence G173 and its adjacent odd layer are NO-GO. The next balanced signature is s=8d-6, delta_1=4d-3, N=10d-4, and h_Z(1)=5d-2=N/2.
falsifier: a residual-Q^(d-2) equality span surviving B236, a nonorthogonal-third equality branch outside the classified cases, failure of the rank d-2 versus d-3 test, a common eigenvector outside J-perp, point rank above fifteen on P(J-perp), or a different next balanced signature
---

# B250 — The standard slope-eight equality is impossible

Assume the standard polarization and

\[
 \dim S=h_Z(1)=5d-3. \tag{1}
\]

Choose a nonorthogonal marked pair \(v,w\), put

\[
 U=\langle v,w\rangle^\perp, \tag{2}
\]

and use B231 to exclude the all-orthogonal alternative.

## Every residual point lies in \(U\)

Modulo \(T_v\oplus T_w\), the residual span has dimension at most

\[
 (5d-3)-(2d+2)=3d-5. \tag{3}
\]

The smaller quadric \(Q(U)\) has dimension

\[
 D=d-2,\qquad 3d-5=3D+1. \tag{4}
\]

Every residual tangent osculator maps to the standard quadratic tangent
osculator on \(Q(U)\). B235-B236 prove that a span of rank at most
\(3D+1\) cannot absorb the tangents at the many distinct residual
points: ranks below the boundary fail by B235, and equality fails by
B236. Thus the residual-\(U\) branch is impossible.

## A third point meets the hyperbolic plane

Choose \(r\notin U\) and put

\[
 S_0=T_v+T_w+T_r,\qquad
 R=\langle v,w,r\rangle,\qquad
 W=R^\perp. \tag{5}
\]

B237 gives \(\dim S_0=3d+2\). Choose a marked \(t\notin R\).

If \(t\notin W\), B246 gives tangent contribution \(d-1\). Its
annihilator is \(\operatorname{Sym}^2K\), where

\[
 K=W\cap t^\perp,\qquad \dim K=d-2. \tag{6}
\]

The contact locus \(K^\perp\) has point rank at most ten, so a further
marked point lies outside it and contributes at least \(d-3\). The
total rank is at least

\[
 (3d+2)+(d-1)+(d-3)=5d-2, \tag{7}
\]

contrary to (1). Hence equality forces \(t\in W\).

Then \(T_t\) contributes \(d-2\), so

\[
 S_1=S_0+T_t,\qquad \dim S_1=4d, \tag{8}
\]

and the annihilator is

\[
 L=\{A\in\operatorname{Sym}^2W:At\in\mathbf Ct\}. \tag{9}
\]

Its contact locus is \(R\cup\mathbf Ct\). Choose a marked
\(u\) outside this locus and retain \(K=t^\perp\cap W\).

If \(u\in K^\perp\), B245 shows that \(T_u\) contributes one dimension
and leaves annihilator \(\operatorname{Sym}^2K\). A further marked
point outside \(K^\perp\) contributes at least \(d-3\), again giving
rank \(5d-2\). Therefore equality also forces

\[
 u\notin K^\perp. \tag{10}
\]

## Equality forces \(u\in K\)

The rank-one maps from \(\operatorname{Sym}^2K\subset L\) make
contraction at \(u\) surjective onto \(K\), because (10) says that
\(B(-,u)|_K\ne0\). Modulo \(\mathbf Cu\), their image has dimension

\[
 \begin{cases}
 d-3,&u\in K,\\
 d-2,&u\notin K.
 \end{cases} \tag{11}
\]

Only \(d-3\) dimensions remain in \(S/S_1\). Hence (1) forces
\(u\in K\), and \(T_u\) fills the span.

Put

\[
 J=K\cap u^\perp. \tag{12}
\]

Because \(u\notin K^\perp\), the functional \(B(u,-)|_K\) is nonzero,
so

\[
 \dim J=d-3. \tag{13}
\]

For every \(z\in J\), the rank-one self-adjoint map

\[
 E_z(x)=B(z,x)z \tag{14}
\]

lies in \(\operatorname{Sym}^2K\subset L\) and satisfies \(E_z u=0\).
Thus every \(E_z\) belongs to the annihilator of
\(S_1+T_u=S\).

Any common eigenvector of all \(E_z\), \(z\in J\), lies in
\(J^\perp\). Indeed, if \(x\notin J^\perp\), choose
\(z\in J\) with \(B(z,x)\ne0\) and \(z\notin\mathbf Cx\); then
\(E_zx\) is not proportional to \(x\).

Consequently every marked point lies in

\[
 \mathbf P(J^\perp)\simeq\mathbf P^4. \tag{15}
\]

Its quadratic point rank is at most

\[
 h^0(\mathbf P^4,O(2))=15<5d-3 \qquad(d\ge8), \tag{16}
\]

contradicting (1).

Thus the standard polarization cannot attain the B249 equality rank.
The layers \(s=8d-8\) and \(s=8d-7\) have the same maximal integral
rank. The next balanced signature is

\[
 s=8d-6,\qquad
 \delta_1=4d-3,\qquad
 N=10d-4,\qquad
 h_Z(1)=5d-2=N/2. \tag{17}
\]

B250 is a necessary special-input obstruction. It constructs no
configuration, ODP package, rational detector, specified pairing,
algebraic cycle, proof, or disproof of HC.
