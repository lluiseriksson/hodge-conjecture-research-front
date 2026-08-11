---
brick_id: B245
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=8, primitive ruling difference zeta=a-b, standard A=O_Q(1), and H=O_Q(2)
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: the standard quadratic embedding, tangent quotient spaces, self-adjoint annihilators, orthogonal linear sections, and their point spans are projective
dimension: dim X=d=2n>=8; no m=2 candidate exists at h_Z(1)=4d+1, so the slope-six layers s=6d and s=6d+1 are excluded
codimension: the primitive codimension-n ruling difference supplies a valid universal input; B244 already excludes every nonstandard polarization at this rank
coefficient_field: Q for zeta and C for tangent jets, symmetric tensors, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to reduced and double finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B221-B244, G168, S081
claim: On (Q^d,a-b), d even and at least eight, the standard polarization cannot realize h_Z(1)=4d+1 with every marked tangent osculator absorbed. Hence G168 and its adjacent odd layer are NO-GO. The next balanced signature is s=6d+2, delta_1=3d+1, N=8d+4, and h_Z(1)=4d+2=N/2.
falsifier: a third residual tangent contributing at most one dimension, a rank-one point outside K-perp, a common eigenvector outside K-perp after the last tangent condition, point rank above ten on the resulting projective three-space, or a different next balanced signature
---

# B245 — The standard slope-six boundary is impossible

B244 excludes every \(A=O_Q(k)\), \(k\ge2\), at the rank

\[
 \dim S=h_Z(1)=4d+1. \tag{1}
\]

It remains to test \(A=O_Q(1)\), so \(H=O_Q(2)\). Choose a
nonorthogonal marked pair \(v,w\) and put

\[
 U=\langle v,w\rangle^\perp. \tag{2}
\]

The all-orthogonal alternative is already excluded by B231.

## Every residual point lies in \(U\)

Modulo \(T_v\oplus T_w\), the available dimension is

\[
 (4d+1)-(2d+2)=2d-1. \tag{3}
\]

If all residual pairs were orthogonal, B237's isotropic absorption
contradiction would apply. Choose a nonorthogonal residual pair
\(r,t\). Their two tangent images inside \(\operatorname{Sym}^2U\) are
disjoint and have total dimension \(2d-2\), leaving one dimension.

The smaller quadric \(Q(U)\) has dimension \(D=d-2\). B233's direct
symmetric-square calculation shows that the image of the tangent at
any third distinct residual point contributes at least

\[
 D-1=d-3>1. \tag{4}
\]

There are many residual marked points, so this branch is impossible.

## A third point meets the hyperbolic plane

Choose \(r\notin U\), and put

\[
 S_0=T_v+T_w+T_r,\qquad R=\langle v,w,r\rangle,\qquad
 W=R^\perp. \tag{5}
\]

B237 gives \(\dim S_0=3d+2\) and \(\dim W=d-1\). Not every marked point
can lie on the plane conic \(Q\cap\mathbf P(R)\), so choose
\(t\notin R\).

If \(t\notin W\), contraction with \(B(-,t)|_W\) has rank \(d-1\) and
fills all dimensions remaining in (1). With

\[
 K=W\cap t^\perp,\qquad \dim K=d-2, \tag{6}
\]

the annihilator becomes \(\operatorname{Sym}^2K\). Its common
eigenvector locus is \(K^\perp\). Hence every marked point lies in the
projective three-space \(\mathbf P(K^\perp)\), whose \(O(2)\) point rank
is at most

\[
 h^0(\mathbf P^3,O(2))=10<4d+1. \tag{7}
\]

This case is impossible.

Suppose instead that \(t\in W\). Its tangent contributes \(d-2\)
dimensions, so

\[
 S_1=S_0+T_t,\qquad \dim S_1=4d. \tag{8}
\]

Modulo scalars, the annihilator is

\[
 L=\{A\in\operatorname{Sym}^2W:At\in\mathbf Ct\}. \tag{9}
\]

B244 identifies its common eigenvector locus as
\(R\cup\mathbf Ct\), of point rank at most six. Choose a further marked
point \(u\) outside this locus. Only one dimension remains in (1).

Put \(K=t^\perp\cap W\), again of dimension \(d-2\). If
\(u\notin K^\perp\), contraction of
\(\operatorname{Sym}^2K\subset L\) with \(u\) has image \(K\). After
quotienting by \(\mathbf Cu\), the tangent contribution has dimension
at least

\[
 \dim K-1=d-3>1, \tag{10}
\]

a contradiction. Thus \(u\in K^\perp=R+\mathbf Ct\). Because
\(u\notin R\cup\mathbf Ct\), write

\[
 u=r_0+ct,\qquad 0\ne r_0\in R,\quad c\ne0. \tag{11}
\]

Every \(A\in L\) kills \(R\) and has \(At=\lambda(A)t\). The condition
\(Au\in\mathbf Cu\) therefore forces \(\lambda(A)=0\). Consequently the
annihilator after adding \(T_u\) is exactly

\[
 \{A\in\operatorname{Sym}^2W:At=0\}
 =\operatorname{Sym}^2K. \tag{12}
\]

Its common eigenvector locus is again \(K^\perp\), and (7) gives the
same point-rank contradiction.

Thus the standard polarization cannot realize (1). The layers
\(s=6d\) and \(s=6d+1\) have the same maximal integral rank, while all
lower ranks were excluded by B244. The next balanced signature is

\[
 s=6d+2,\qquad \delta_1=3d+1,\qquad
 N=8d+4,\qquad h_Z(1)=4d+2=N/2. \tag{13}
\]

B245 is a necessary special-input obstruction. It constructs no
configuration, ODP package, rational detector, specified pairing,
algebraic cycle, proof, or disproof of HC.
