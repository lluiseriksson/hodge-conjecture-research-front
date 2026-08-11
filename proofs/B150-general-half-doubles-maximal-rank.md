---
brick_id: B150
status: PROVED
base_field: C
variety: projective space P^(2n), the line bundle O(d) with d not equal to 2, and a general union Xi of N oriented half-double schemes of length n+1
smoothness: projective space and the distinct general support points are smooth; no nodal hypersurface is asserted
projectivity: P^(2n) and Xi are projective
dimension: dim_C P^(2n)=2n; every local component has length n+1; Xi has length (n+1)N
codimension: general Xi imposes maximal-rank conditions on degree-d forms; it cannot both lie on a nonzero form and have G094 rank at most R+n with R<N
coefficient_field: C, using the characteristic-zero case of S062
cohomology_theory: coherent cohomology, zero-dimensional schemes, partial first-derivative interpolation, and Hilbert functions
hodge_type: none asserted
cycle_class_map: CH^n(P^(2n))_Q -> H^(2n)(P^(2n),Q(n)); no primitive Hodge detector or algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: generic
dependencies: B149, S062 Theorem 1.1, and the exact list of S062 exceptions
claim: For d not equal to 2, a general union of oriented half-double schemes in P^(2n) has maximal-rank degree-d evaluation. If the polynomial space has dimension at most the scheme length, no nonzero form contains Xi; otherwise evaluation is surjective of rank (n+1)N>R+n for every R<N. Hence general partial-jet interpolation never supplies G094.
falsifier: an S062 exceptional case with ambient dimension 2n and component length n+1, or a maximal-rank evaluation map that both has nonzero kernel and rank at most R+n for R<N
---

# B150 — General oriented half-doubles have maximal rank

Apply S062, Theorem 1.1, with ambient projective dimension \(2n\) and

\[
 a_i=n,\qquad \operatorname{length}(\Xi_i)=a_i+1=n+1.
\]

For \(d\ne2\), none of the five exceptions applies. The even-dimensional
exceptions in S062 have \(a_i=2n\), hence full double points, not
half-doubles; the other exceptions have odd ambient dimension. Therefore

\[
 H^0(\mathbf P^{2n},\mathcal O(d))
 \longrightarrow H^0(\Xi,\mathcal O_\Xi(d))
\]

has maximal rank for general support points and general orientations.
Requiring an orientation to be maximal isotropic for a varying
nondegenerate quadratic form does not create a new generic locus of
orientations: every \(n\)-plane in a \(2n\)-space is maximal isotropic for
some nondegenerate symmetric form. This observation does **not** construct
that form as the Hessian of one global section; it only shows that the
isotropy adjective cannot rescue the general-orientation interpolation
route.

Let \(M=h^0(\mathbf P^{2n},\mathcal O(d))\) and
\(\ell=(n+1)N\).

- If \(M\le\ell\), maximal rank is injectivity. No nonzero degree-\(d\)
  hypersurface contains \(\Xi\), so there is no prospective nodal section.
- If \(M>\ell\), maximal rank is surjectivity and the evaluation rank is
  \(\ell=(n+1)N\). For every value rank \(R<N\),

  \[
  (n+1)N>R+n,
  \]

  contradicting G094's oriented evaluation bound.

Thus G094 must use a special joint configuration of supports and
orientations. This is a projective-space generic-scope theorem, not a
nonexistence theorem on arbitrary varieties or special loci. Degree two is
deliberately excluded because S062 gives a different criterion there; the
high-power Hodge route cannot infer anything from that omitted case.
