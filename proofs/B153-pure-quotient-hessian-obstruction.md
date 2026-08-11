---
brick_id: B153
status: PROVED
base_field: C
variety: a smooth projective complex 2n-fold X, a line bundle L, and an ordered N-node configuration in B151's synchronized branch satisfying B152's mixed Hessian condition
smoothness: X and the nodes are smooth/ordinary double points; smooth excess remains an explicit hypothesis only when invoking all B146 identities
projectivity: X and the linear system are projective; the obstruction is local analytic and finite-dimensional
dimension: the synchronized quotient Q has dimension n; value rank is R<N; the pure obstruction space has dimension (N-R)n(n+1)/2
codimension: vanishing requires the N quotient Hessian forms to lie in the R-dimensional value-evaluation image tensor Sym^2(Q^*)
coefficient_field: C for Hessians, splittings, quotient forms, and ranks; Q only in downstream Hodge applications
cohomology_theory: second-order nodal deformation theory and finite-dimensional symmetric bilinear algebra
hodge_type: none asserted; downstream local relation functionals must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) downstream; no algebraic cycle or specified detector is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B146, B151-B152, polarization, and exact quotient linear algebra
claim: After the mixed Hessian condition, the nodewise Hessian squares of any splitting of the synchronized quotient define a canonical class Omega_Q in coker(E) tensor Sym^2(Q^*), independent of the splitting. In the synchronized branch, the full B146 relation-isotropy condition is equivalent to the mixed condition plus Omega_Q=0. The pure obstruction space has dimension (N-R)n(n+1)/2.
falsifier: two quotient splittings producing distinct classes modulo im E, vanishing mixed and pure classes with a nonzero B146 relation pairing, or a pure obstruction space of different dimension
---

# B153 — The remaining second-order obstruction is a canonical pure class

Let

\[
 \mathcal T=\bigoplus_{i=1}^N L|_{p_i},\qquad
 E:W\longrightarrow\mathcal T,\qquad
 \operatorname{rank}E=R,
\]

and retain B151-B152's synchronized quotient

\[
 0\longrightarrow C\longrightarrow V=\ker E
 \longrightarrow Q\longrightarrow0,\qquad \dim Q=n.
\]

Assume B152's mixed condition holds. Choose a linear splitting
\(s:Q\to V\). At node \(i\), let \(B_i\) denote the symmetric bilinear form
defined by the inverse Hessian. Define

\[
 g_i^s(u,v)=
 B_i\bigl(Ds(u)_i,Ds(v)_i\bigr)
 \in L|_{p_i}.
\]

The tuple \(g^s=(g_i^s)_i\) is an element of
\(\mathcal T\otimes\operatorname{Sym}^2Q^*\). Put

\[
 \Omega_Q(s)=
 [g^s]\in
 \operatorname{coker}(E)\otimes\operatorname{Sym}^2Q^*.
\]

## Independence of the splitting

Let \(s'=s+c\), where \(c:Q\to C\). Then

\[
 g_i^{s'}(u,v)-g_i^s(u,v)
 =
 B_i(Ds(u)_i,Dc(v)_i)
 +B_i(Dc(u)_i,Ds(v)_i)
 +B_i(Dc(u)_i,Dc(v)_i).
\]

The last term is zero at every node because \(D(C)_i\subset\Lambda_i\) and
\(\Lambda_i\) is isotropic. Every value relation annihilates the first two
tuples by B152's mixed condition. Hence their sum lies in
\(\operatorname{im}E\), and

\[
 \Omega_Q(s')=\Omega_Q(s).
\]

Write the resulting canonical class simply as \(\Omega_Q\).

## Exact decomposition of B146

Every pair of vectors in \(V\) is a sum of:

1. a core-core pair in \(C\times C\), whose Hessian pairing vanishes
   nodewise by Lagrangian isotropy;
2. a core-quotient pair, annihilated by every value relation exactly when
   B152's mixed condition holds;
3. a quotient-quotient pair, annihilated by every value relation exactly
   when \(g^s(u,v)\in\operatorname{im}E\), equivalently
   \(\Omega_Q=0\).

Therefore, in the synchronized branch,

\[
 \text{B146 common relation isotropy}
 \quad\Longleftrightarrow\quad
 \bigl(\text{B152 mixed condition and }\Omega_Q=0\bigr).
\]

## Size and nonautomaticity

Since \(\dim\operatorname{coker}E=N-R\),

\[
 \dim\left(
 \operatorname{coker}E\otimes\operatorname{Sym}^2Q^*
 \right)
 =(N-R)\binom{n+1}{2}.
\]

The class is not forced by synchronization or the mixed condition. In an
adapted decomposition \(G_i=\Lambda_i\oplus Q_i\), an inverse-Hessian form
with matrix

\[
 \begin{pmatrix}0&I\\I&C_i\end{pmatrix}
\]

is nondegenerate for every symmetric \(C_i\). Taking the core conormal map
to be zero satisfies the mixed condition, while the arbitrary tuple
\((C_i)\) realizes an arbitrary pure class modulo \(\operatorname{im}E\).

Thus B153 closes the full second-order bookkeeping but neither forces
\(\Omega_Q=0\) geometrically nor integrates the smoothing equations.
