---
brick_id: B149
status: PROVED
base_field: C
variety: a smooth projective complex 2n-fold X, a line bundle L with H^1(X,L)=0, N distinct points Z, and one n-dimensional cotangent subspace Lambda_i at each point
smoothness: X and the support points are smooth; no hypersurface or incidence smoothness is inferred
projectivity: X and the zero-dimensional oriented subscheme Xi are projective
dimension: dim_C X=2n; Z has length N; each oriented half-double local scheme has length n+1, so Xi has length (n+1)N
codimension: if value evaluation has rank R and projected conditional gradients have rank rho, Xi imposes R+rho conditions and has H^1 defect (n+1)N-R-rho
coefficient_field: C for coherent cohomology, jets, ranks, and the oriented schemes; Q only in downstream Hodge applications
cohomology_theory: coherent sheaf cohomology, first principal parts, zero-dimensional schemes, and local nodal deformation theory
hodge_type: none asserted; downstream relation functionals must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) in downstream applications; no algebraic cycle representing a specified Hodge class is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B136, B145-B148, the ideal-sheaf exact sequence, and rank-nullity
claim: The node-value map together with gradients modulo Lambda_i is evaluation on a canonical length-(n+1)N oriented half-double scheme Xi. If the value rank is R and projected conditional-gradient rank is rho, then h^1(I_Xi tensor L)=(n+1)N-R-rho and h^1(I_Xi tensor L)-h^1(I_Z tensor L)=nN-rho. In particular G093's rho<=n forces an additional defect at least n(N-1).
falsifier: an oriented scheme with the stated local ideals but different length, a jet-evaluation rank other than R+rho, or failure of either cohomology identity when H^1(X,L)=0
---

# B149 — The rank-\(n\) gate is an oriented half-double defect

At each \(p_i\in Z\), let \(\mathfrak m_i\) be the maximal ideal and let

\[
 \Lambda_i\subset \mathfrak m_i/\mathfrak m_i^2
 \simeq T_{p_i}^*X
\]

have dimension \(n\). Define the local ideal

\[
 I_{\Xi_i}:=\mathfrak m_i^2+\widetilde{\Lambda}_i,
\]

where \(\widetilde{\Lambda}_i\subset\mathfrak m_i\) is any inverse image.
The ideal is independent of that lift. Since

\[
 \mathcal O_{\Xi_i}\simeq
 \mathbf C\oplus
 \left((\mathfrak m_i/\mathfrak m_i^2)/\Lambda_i\right),
\]

it has length \(n+1\). Put
\(\Xi=\coprod_i\Xi_i\), of length \((n+1)N\).

## Rank decomposition

Evaluation on \(\Xi\) records the value of a section and, after the value
vanishes, its differential modulo \(\Lambda_i\). Therefore, if

\[
 E:H^0(X,L)\longrightarrow\bigoplus_iL|_{p_i}
\]

has rank \(R\), and

\[
 P:\ker E\longrightarrow
 \bigoplus_i
 (T_{p_i}^*X\otimes L|_{p_i})/
 (\Lambda_i\otimes L|_{p_i})
\]

has rank \(\rho\), the full evaluation map on \(\Xi\) has rank
\(R+\rho\).

Assume \(H^1(X,L)=0\). The two ideal-sheaf sequences for \(Z\) and \(\Xi\)
then give

\[
 h^1(X,I_Z\otimes L)=N-R
\]

and

\[
 h^1(X,I_\Xi\otimes L)
 =(n+1)N-R-\rho.
\]

Subtracting,

\[
 h^1(X,I_\Xi\otimes L)-h^1(X,I_Z\otimes L)
 =nN-\rho.
\]

Thus G093's carrier-shadow bound \(\rho\le n\) forces

\[
 h^1(X,I_\Xi\otimes L)\ge (n+1)N-R-n,
\]

with at least \(n(N-1)\) defect beyond the value scheme itself.

This is an exact reformulation of the projected-gradient rank gate, not an
existence theorem. The maximal inverse-Hessian isotropy of the
\(\Lambda_i\), B146's relation-weighted quadratic identities, nonlinear
integration, adjoint defect, primitive ambient image, and specified pairing
remain separate obligations.
