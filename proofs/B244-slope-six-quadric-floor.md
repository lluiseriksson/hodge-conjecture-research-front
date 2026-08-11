---
brick_id: B244
status: PROVED
base_field: C
variety: the smooth even-dimensional quadric X=Q^d with d=2n>=8, primitive ruling difference zeta=a-b, arbitrary very ample A=O_Q(k), and H=A^2
smoothness: Q^d and the reduced marked scheme are smooth; central ODP and incidence clauses remain inherited hypotheses
projectivity: complete quadric embeddings, mixed double-point restrictions, tangent quotient spaces, self-adjoint contact loci, and plane conics are projective
dimension: dim X=d=2n>=8; every m=2 candidate has slack s>=6d; at the first unexcluded value s=6d one has N=8d+2 and h_Z(1)=4d+1=N/2
codimension: the primitive codimension-n ruling difference supplies a valid universal input; the obstruction replaces every fixed additive extension of the slope-four branch by a slope-six necessary floor
coefficient_field: Q for zeta and C for sections, tangent jets, spans, self-adjoint endomorphisms, and ranks
cohomology_theory: rational singular cohomology and coherent restriction to mixed double and reduced finite schemes
hodge_type: zeta is nonzero primitive rational type (n,n); no rational type-(0,0) detector is constructed
cycle_class_map: CH^n(Q^(2n))_Q -> H^(2n)(Q^(2n),Q(n)); the ruling difference only certifies the universal test input
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B215, B221-B243, G167, S081
claim: On (Q^d,a-b), d even and at least eight, every m=2 G144 candidate has slack s>=6d. More precisely, the standard polarization forces h_Z(1)>=4d and its equality case is impossible, while every nonstandard polarization forces h_Z(1)>=4d+4. At s=6d the only unexcluded rank is delta_1=3d, N=8d+2, and h_Z(1)=4d+1=N/2.
falsifier: a candidate with s<=6d-1, a nonstandard point span below 4d+4, a standard point span below 4d, a third residual point in the equality quotient, a common eigenvector outside the equality conic-plus-point locus, or a different next balanced signature
---

# B244 — The degree-two quadric floor has slope six

Let \(S\) be the \(H=A^2\) point span. The degree-two budget is

\[
 h_Z(1)=d+1+\delta_1,\qquad 2\delta_1\le s. \tag{1}
\]

Every marked tangent osculator is contained in \(S\).

## Powers \(k\ge4\)

B215 separates four double neighborhoods in exponent seven. Multiplying
by a section nonzero at their supports gives the same conclusion in
exponent \(2k\ge8\). Hence

\[
 k\ge4\quad\Longrightarrow\quad \dim S\ge4(d+1)=4d+4. \tag{2}
\]

## The sextic power

Let \(k=3\). Choose a noncollinear marked triple \(p,q,r\), and let
\(\Delta\) be its three pair lines. The three double neighborhoods are
independent and have span \(3d+3\). If every marked point lay in
\(\Delta\), the point rank would be at most

\[
 3h^0(\mathbf P^1,O(6))=21<3d+3. \tag{3}
\]

Choose \(t\notin\Delta\). As in B243, the three pair-line hyperplanes
are units at \(t\); after multiplying by two more units, the hyperplanes
through \(t\) supply all \(d\) first jets there. Thus four double
neighborhoods are independent in degree six and

\[
 k=3\quad\Longrightarrow\quad \dim S\ge4d+4. \tag{4}
\]

## The square power

Let \(k=2\). Choose noncollinear \(p,q,r\). Their three quartic tangent
osculators have span \(3d+3\), whereas the three pair lines have point
rank at most fifteen. Hence some marked \(t\) lies off their union.

B239-B242 then choose \(u,x\) so that

\[
 S_0=\langle T_p,T_q,T_r,t^4,u^4,x^4\rangle,
 \qquad \dim S_0=3d+6. \tag{5}
\]

Indeed, after \(t,u\) the residual base locus lies on at most two lines
plus the three double supports, of point rank at most thirteen; this is
smaller than the already forced span.

For every further marked \(y\), B243's variable-hyperplane family has
restriction rank at least \(d-2\) on \(2y\). Duality gives

\[
 \dim S\ge(3d+6)+(d-2)=4d+4. \tag{6}
\]

Thus every nonstandard polarization satisfies the common lower bound
(2).

## The standard power

Let \(k=1\). If all marked pairs were orthogonal, B231's isotropic
absorption contradiction would apply. Choose a nonorthogonal pair
\(v,w\), and put \(U=\langle v,w\rangle^\perp\).

First suppose every residual point lies in \(U\). Modulo
\(T_v\oplus T_w\), a residual tangent has dimension \(d-1\). If two
residual representatives are nonorthogonal, their images are disjoint,
so

\[
 \dim S\ge2d+2+2(d-1)=4d. \tag{7}
\]

If no such pair exists, B237's isotropic absorption contradiction
applies inside \(U\).

Otherwise choose \(r\notin U\), put

\[
 S_0=T_v+T_w+T_r,\qquad R=\langle v,w,r\rangle. \tag{8}
\]

B237 gives \(\dim S_0=3d+2\). Not every marked point can lie on the
plane conic \(Q\cap\mathbf P(R)\), whose \(O_Q(2)\) point rank is at most
five. Choose \(t\notin R\). B238 gives tangent quotient rank at least
\(d-2\), hence again

\[
 \dim S\ge3d+2+d-2=4d. \tag{9}
\]

## Equality cannot occur for the standard power

Assume \(\dim S=4d\). In the residual-\(U\) branch, a nonorthogonal
residual pair has two tangent images whose direct sum fills the
\((2d-2)\)-dimensional quotient. B232's symmetric-square decomposition,
applied inside \(U\), shows that their span contains no third distinct
residual point. The marked scheme has many such points, a contradiction.

In the other branch retain (8) and put \(W=R^\perp\), so
\(\dim W=d-1\). Exactly \(d-2\) dimensions remain after \(S_0\).
Contraction of \(\operatorname{Sym}^2W\) with a point
\(t\notin R\cup W\) has rank \(d-1\), so equality forces
\(t\in W\). Its tangent then fills the remaining \(d-2\) dimensions.

The annihilator of \(S_0+T_t\), modulo scalars, is

\[
 L=\{A\in\operatorname{Sym}^2W:At\in\mathbf Ct\}. \tag{10}
\]

Put \(K=t^\perp\cap W\). Since \(K^\perp=R+\mathbf Ct\), rank-one maps
\(E_z(x)=B(z,x)z\), \(z\in K\), separate every vector outside
\(R+\mathbf Ct\). To produce a self-adjoint map in \(L\) with \(At=t\),
choose \(f\in W\) with \(B(t,f)=1\) and use

\[
 A(x)=B(f,x)t+B(t,x)f-B(f,f)B(t,x)t. \tag{11}
\]

This map separates every vector in
\((R+\mathbf Ct)\setminus(R\cup\mathbf Ct)\).
Consequently the common eigenvector locus of \(L\) is exactly

\[
 R\cup\mathbf Ct. \tag{12}
\]

Tangential contact therefore confines every marked point to the plane
conic \(Q\cap\mathbf P(R)\) plus \(t\), of point rank at most six, not
\(4d\). This excludes equality.

## The new floor

For \(k\ge2\), equations (2), (4), and (6) give

\[
 h_Z(1)\ge4d+4\quad\Longrightarrow\quad s\ge6d+6. \tag{13}
\]

For \(k=1\), equations (7)-(9) give \(h_Z(1)\ge4d\), hence
\(s\ge6d-2\); the two possible layers \(6d-2,6d-1\) have
\(h_Z(1)\le4d\), and the equality argument excludes them. Therefore

\[
 m=2\quad\Longrightarrow\quad s\ge6d. \tag{14}
\]

At \(s=6d\), lower ranks are excluded while (1) gives
\(\delta_1\le3d\). Thus the only unexcluded signature is

\[
 \delta_1=3d,\qquad N=8d+2,\qquad
 h_Z(1)=4d+1=N/2,\qquad s-2\delta_1=0. \tag{15}
\]

B244 is a necessary special-input obstruction. It constructs no
configuration, ODP package, rational detector, specified pairing,
algebraic cycle, proof, or disproof of HC.
