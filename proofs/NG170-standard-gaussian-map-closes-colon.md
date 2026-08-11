---
brick_id: NG170
status: NO-GO
base_field: C
variety: an arbitrary smooth projective complex 2n-fold with G137's finite node scheme and inverse-Hessian data, compared with varieties and canonical curves covered by standard Gaussian-map theory
smoothness: all compared varieties are smooth; Gaussian-map surjectivity does not impose G137's nodal ODP package
projectivity: the standard Gaussian maps use the diagonal in X times X and global line bundles; G137 uses a finite marked scheme and third-neighborhood obstruction maps
dimension: G137 is arbitrary even dimension; the explicit second-fundamental-form results audited in S074 concern curves
codimension: surjectivity of a standard global Gaussian map does not construct the relation-weighted finite-node functionals in im(partial_k^*)
coefficient_field: C, matching S074; Q detector data and rational comparison are absent
cohomology_theory: diagonal-ideal Gaussian maps versus finite-node coherent connecting maps and cubic Kuranishi tensors
hodge_type: S074 supplies no rational type-(0,0) detector or cycle class
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)) is downstream and unused
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B207, G137, NG169, S074
claim: Invoke standard higher Gaussian-map surjectivity or its relation to a second fundamental form as a proof of G137.
falsifier: the standard source and target do not encode S_m^perp, the finite node scheme, final inverse Hessians, or the dual connecting map for I_Z^3
---

# NG170 — Standard Gaussian maps do not close the nodal colon

- **Route:** identify the Hessian appearance in G137 with a higher Gaussian
  map and import a surjectivity theorem.
- **Valid input:** S074 constructs Gaussian maps from powers of the ideal of
  the diagonal, with targets of the form
  \(H^0(\operatorname{Sym}^j\Omega_X^1\otimes L\otimes M)\). It also records
  special links between Gaussian maps and deformation/second-fundamental-
  form data.
- **Invalid inference:** such surjectivity places every
  \(\ell_{r,e,b,c}\) in \(\operatorname{im}\partial_k^*\).

G137 depends on four extra structures not present in the standard map:

1. the finite relation space \(S_m^\perp\);
2. the selected node scheme \(Z\) and the sequence for \(I_Z^3\);
3. the final central inverse Hessians \(H_i^{-1}\);
4. compatibility with every full-system \(U\)-direction and detector.

Pareschi's S074 theorems impose their own multiplication and positivity
hypotheses, with explicit applications to abelian varieties and curves.
Frediani's audited second-fundamental-form comparison concerns canonical
curves, Torelli geometry, and Schiffer variations. Neither result gives a
comparison morphism to B207's finite-node connecting map.

- **Precise obstruction:** analogous Hessian symbols live in different
  source, target, support, and deformation categories.
- **Re-entry condition:** construct an explicit comparison commuting with
  restriction to \(Z\), relation weights, inverse-Hessian contraction, and
  \(\partial_k^*\), then prove its hypotheses for arbitrary \((X,\zeta)\).
