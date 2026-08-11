---
brick_id: B253
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=10, primitive ruling difference zeta=a-b, standard A=O_Q(1), and H=O_Q(2)
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: the standard quadratic embedding, residual orthogonal quadrics, tangent quotient spaces, self-adjoint annihilators, rank-one maps, and projective-four-space contact bounds are projective
dimension: dim X=d=2n>=10; every standard candidate has h_Z(1)>=6d-7; combining B249 gives the common all-polarization floor h_Z(1)>=5d+3 and slack s>=8d+4
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the parametric exclusion closes every standard rank 5d-1+q for 0<=q<=d-7
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B231, B237, B245-B252, S081
claim: On (Q^d,a-b), d even and at least ten, the standard polarization requires h_Z(1)>=6d-7. Together with B249, every polarization requires h_Z(1)>=5d+3 and slack s>=8d+4. Hence G176-G178 and their adjacent odd layers are NO-GO. For even d>=12, the only polarization not excluded at equality h_Z(1)=5d+3 is A=O_Q(2).
falsifier: a standard tangent-absorbing point span with h_Z(1)<=6d-8, a residual configuration below B246's floor, a mixed branch whose surviving quotient is not controlled by Sym^2(J), a residual tangent rank below d-4, a non-square equality candidate in even dimension at least twelve, or a different common floor
---

# B253 — A parametric standard band is impossible

Let the standard-polarized point span have

\[
 h=\dim S=5d-1+q,\qquad 0\le q\le d-7,\qquad d\ge10. \tag{1}
\]

Choose a nonorthogonal marked pair \(v,w\), put

\[
 U=\langle v,w\rangle^\perp, \tag{2}
\]

and use B231 to exclude the all-orthogonal alternative.

## The residual branch

If every other marked point lies in \(U\), the quotient by
\(T_v\oplus T_w\) is the standard quadratic point span of the residual
scheme on \(Q(U)\), of dimension at most

\[
 h-(2d+2)=3d-3+q\le4d-10. \tag{3}
\]

The residual quadric has dimension \(D=d-2\ge8\). B246's intrinsic
standard tangent-absorption floor requires residual dimension at least

\[
 5D-3=5d-13. \tag{4}
\]

Since \(4d-10<5d-13\) for \(d>3\), this branch is impossible.

## The uniform escape bound

The mixed branches below repeatedly leave a subspace
\(J\subset V\), \(\dim J=d-3\), with
\(\operatorname{Sym}^2J\) inside the current annihilator. The
rank-one maps

\[
 E_z(y)=B(z,y)z,\qquad z\in J, \tag{5}
\]

then have two consequences, as in B250-B252:

1. if the current span is full, every marked point is a common
   eigenvector of the \(E_z\), hence lies in
   \(\mathbf P(J^\perp)\simeq\mathbf P^4\), of quadratic point rank at
   most fifteen;
2. if the span is not full, some marked \(x\notin J^\perp\), and
   contraction of \(\operatorname{Sym}^2J\) at \(x\), modulo
   \(\mathbf Cx\), has rank at least

\[
 d-4. \tag{6}
\]

Thus any branch with such a \(J\) is impossible whenever its remaining
rank budget is strictly smaller than \(d-4\).

## The mixed branches

Choose \(r\notin U\), and put

\[
 S_0=T_v+T_w+T_r,\qquad
 R=\langle v,w,r\rangle,\qquad W=R^\perp. \tag{7}
\]

B237 gives \(\dim S_0=3d+2\). Choose a marked \(t\notin R\).

### The case \(t\notin W\)

Here

\[
 \dim(S_0+T_t)=4d+1,\qquad
 (S_0+T_t)^\perp=\operatorname{Sym}^2K,\qquad
 K=W\cap t^\perp,\quad\dim K=d-2. \tag{8}
\]

Choose a marked \(u\notin K^\perp\). If \(u\notin K\), its tangent
contributes \(d-2\), leaving rank budget

\[
 h-(5d-1)=q. \tag{9}
\]

If \(u\in K\), it contributes \(d-3\), leaving

\[
 h-(5d-2)=q+1. \tag{10}
\]

In either case \(J=K\cap u^\perp\) has dimension \(d-3\) and supplies
(5). Since

\[
 q+1\le d-6<d-4, \tag{11}
\]

the uniform escape bound gives a contradiction.

### The case \(t\in W\)

Now

\[
 S_1=S_0+T_t,\qquad \dim S_1=4d,\qquad
 L=S_1^\perp=
 \{A\in\operatorname{Sym}^2W:At\in\mathbf Ct\}. \tag{12}
\]

Its contact locus is \(R\cup\mathbf Ct\). Choose a marked \(u\)
outside it and put \(K=t^\perp\cap W\).

If \(u\in K^\perp\), B245 shows that \(T_u\) contributes one
dimension and leaves \(\operatorname{Sym}^2K\) as annihilator. Choose
a marked \(x\notin K^\perp\). According as \(x\notin K\) or
\(x\in K\), it contributes \(d-2\) or \(d-3\), leaving rank budget
\(q\) or \(q+1\). The space \(J=K\cap x^\perp\) again has dimension
\(d-3\), so (11) and the uniform escape bound exclude both cases.

It remains to take \(u\notin K^\perp\). If \(u\notin K\),
\(\operatorname{Sym}^2K\subset L\) contributes \(d-2\), so the
remaining budget is at most

\[
 h-(5d-2)=q+1<d-4. \tag{13}
\]

With \(J=K\cap u^\perp\), the maps (5) survive and give a
contradiction.

Finally suppose \(u\in K\). Then
\(\operatorname{Sym}^2K\subset L\) contributes \(d-3\), and
\(J=K\cap u^\perp\), \(\dim J=d-3\), again survives in the
annihilator. The remaining budget is at most

\[
 h-(5d-3)=q+2\le d-5<d-4. \tag{14}
\]

The uniform escape bound gives the final contradiction.

## The improved floors

Thus no standard rank in (1) occurs. B246 and B250-B251 exclude every
smaller standard rank through \(5d-2\), so

\[
 A=O_Q(1)\quad\Longrightarrow\quad h_Z(1)\ge6d-7. \tag{15}
\]

B249 gives

\[
 A=O_Q(2)\Longrightarrow h_Z(1)\ge5d+3,\qquad
 A=O_Q(k),\ k\ge3\Longrightarrow h_Z(1)\ge5d+5. \tag{16}
\]

For \(d\ge10\), (15)-(16) imply the common floor

\[
 h_Z(1)\ge5d+3,\qquad
 \delta_1\ge4d+2,\qquad s\ge8d+4. \tag{17}
\]

Consequently G176-G178 and every layer through \(s=8d+3\) are
NO-GO. At the first balanced value

\[
 s=8d+4,\qquad \delta_1=4d+2,\qquad
 N=10d+6,\qquad h_Z(1)=5d+3=N/2, \tag{18}
\]

every \(k\ge3\) is excluded. For even \(d\ge12\),
\(6d-7>5d+3\), so the standard polarization is excluded as well and
only the square polarization \(A=O_Q(2)\) remains.

B253 is a necessary special-input obstruction. It constructs no
configuration, ODP package, rational detector, specified pairing,
algebraic cycle, proof, or disproof of HC.
