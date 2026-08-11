---
brick_id: B152
status: PROVED
base_field: C
variety: a smooth projective complex 2n-fold X, a line bundle L, and an ordered N-node configuration in B151's synchronized branch with value rank R<N
smoothness: X and the nodes are smooth/ordinary double points; smooth excess is an explicit hypothesis inherited from B146 for the Hessian identities
projectivity: X and the linear system are projective; the proof is local analytic and finite-dimensional
dimension: each conormal Lagrangian and synchronized quotient has dimension n; the value-relation space has dimension N-R
codimension: the core conormal-gradient image has dimension at most nR and hence corank at least n(N-R); full first-jet evaluation has rank at most (n+1)R+n
coefficient_field: C for deformations, Hessians, relations, and ranks; Q only in downstream Hodge applications
cohomology_theory: second-order nodal deformation theory, coherent first-jet evaluation, and finite-dimensional bilinear algebra
hodge_type: none asserted; downstream local relation functionals must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) downstream; no algebraic cycle or specified detector is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B142-B148, B151, B146 polarization, and rank-nullity
claim: In the synchronized branch, B146's mixed Hessian identities force the conormal gradients of the common kernel into a canonical subspace of codimension n(N-R), so their rank is at most nR. Consequently the full double-point first-jet evaluation rank is at most (n+1)R+n. The B142-B143 carrier family saturates the nR conormal bound.
falsifier: synchronized surjective quotient blocks satisfying all B146 relation quadrics but whose common-kernel conormal-gradient rank exceeds nR, or a resulting full first-jet rank greater than (n+1)R+n
---

# B152 — Synchronization forces a second conormal corank

Use B151's synchronized notation

\[
 P:V=\ker E\longrightarrow\bigoplus_iQ_i,\qquad
 Q=V/C,\qquad C=\ker P,\qquad \dim Q=\dim Q_i=n,
\]

with isomorphisms \(\phi_i:Q\xrightarrow{\sim}Q_i\). Let

\[
 \Lambda_i\subset G_i=T_{p_i}^*X\otimes L|_{p_i}
\]

be the chosen maximal inverse-Hessian-isotropic subspace, so
\(Q_i=G_i/\Lambda_i\). The inverse Hessian induces a perfect cross-pairing

\[
 b_i:\Lambda_i\times Q_i\longrightarrow\mathbf C
\]

after local frames are chosen. Frame changes do not affect the ranks below.

For \(c\in C\), the projected gradient vanishes, so

\[
 D(c)=(A_i(c))_i\in
 \mathcal L:=\bigoplus_i\Lambda_i.
\]

Write \(A:C\to\mathcal L\) for this conormal-gradient map.

## Mixed Hessian equations

Let \(K=\ker E^*\) be the value-relation space, of dimension \(N-R\).
Polarizing B146 and pairing \(c\in C\) with any lift of \(u\in Q\) gives

\[
 \sum_i r_i\,b_i(A_i(c),\phi_i u)=0
 \qquad(r=(r_i)\in K).
\]

Define

\[
 F:\mathcal L\longrightarrow K^*\otimes Q^*
\]

by

\[
 F(\alpha)(r,u)=
 \sum_i r_i\,b_i(\alpha_i,\phi_i u).
\]

The mixed equations say

\[
 A(C)\subseteq\ker F.
\]

## Exact rank of the mixed map

Let \(\epsilon_i\in K^*\) be the \(i\)-th coordinate restricted to \(K\).
The \(\epsilon_i\) span \(K^*\), because every functional on the subspace
\(K\subset\mathbf C^N\) extends to \(\mathbf C^N\). Since \(b_i\) is perfect
and \(\phi_i\) is an isomorphism, the image of the \(i\)-th summand
\(\Lambda_i\) under \(F\) is

\[
 \epsilon_i\otimes Q^*.
\]

Therefore \(F\) is surjective and

\[
 \operatorname{rank}F=n(N-R),\qquad
 \dim\ker F=nN-n(N-R)=nR.
\]

It follows that

\[
 \operatorname{rank}A\le nR.
\]

Thus even after the first \(n(N-1)\)-dimensional oriented defect of B149,
smooth synchronized excess forces a second conormal-gradient corank of at
least \(n(N-R)\).

## Full double-point defect

The gradient map \(D:V\to\bigoplus_iG_i\) has

\[
 \operatorname{rank}D
 =\operatorname{rank}P+\operatorname{rank}A
 \le n+nR.
\]

Adding the value rank \(R\), evaluation on the full first infinitesimal
neighborhood \(2Z\), of length \((2n+1)N\), has rank at most

\[
 R+n+nR=(n+1)R+n.
\]

If \(H^1(X,L)=0\), this implies

\[
 h^1(X,I_{2Z}\otimes L)
 \ge (2n+1)N-(n+1)R-n.
\]

For B142-B143, the common quotient is motion of the product fiber.
Normal-jet surjectivity and the degree-\(m\) evaluation rank \(R\) give
\(n\) independent conormal blocks of rank \(R\), so
\(\operatorname{rank}A=nR\). The anchored family saturates the new bound.

B152 remains necessary only. It does not impose the pure-\(Q\) quadratic
part of B146, integrate the smoothing ideal, or produce a specified pairing.
