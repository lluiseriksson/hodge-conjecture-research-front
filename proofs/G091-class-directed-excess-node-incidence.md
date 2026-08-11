---
brick_id: G091
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X, a specified primitive rational Hodge class zeta, and the universal ordered-node incidence for high powers H^m
smoothness: X and the sought nodal member are smooth away from isolated ordinary double points; the ordered-node incidence is required to be smooth at the selected excess point
projectivity: X and the high-power linear system are projective; the ordered configuration and incidence are quasi-projective
dimension: dim_C X=2n with n at least 2; the selected member has N nodes, value-evaluation rank R<N, and ordered-incidence tangent codimension 2nN+R
codimension: the projected simultaneous-node germ has codimension R; middle cycles have codimension n
coefficient_field: C for jets and incidence geometry; Q for Hodge classes, vanishing relations, and Saito pairings
cohomology_theory: principal-parts evaluation, ordered-node incidence deformation theory, adjoint coherent defect, rational vanishing cycles, local intersection cohomology, and primitive Betti Hodge structures
hodge_type: zeta and the selected local relation functional have rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative of zeta may be assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B007, B010, B026-B028, B054, and B134-B145
claim: For every specified nonzero primitive rational Hodge class, some high-power ordered-node incidence has a nodal point with uniform value matroid U_(R,N), R<N, smooth excess codimension 2nN+R, positive adjoint defect, and a rational relation whose Saito ambient class pairs nontrivially with the specified class.
falsifier: a polarized smooth projective 2n-fold and nonzero primitive rational Hodge class for which every rank-smooth excess ordered-node component has zero adjoint defect, nonuniform value matroid, or Saito image contained in zeta-perp
---

# G091 — Class-directed smooth excess in the ordered-node incidence

## Exact theorem sought

For

\[
 0\ne\zeta\in
 H_{\mathrm{prim}}^{2n}(X,\mathbf Q(n))\cap H^{0,0},
\]

construct a high power \(L=H^m\), a nodal
\([Y]\in|L|\) with ordered node set \(\Delta\), and a relation \(\beta\)
such that:

1. the value-evaluation matroid is uniform \(U_{R,N}\) with \(R<N\);
2. the ordered-node incidence \(\mathcal I_N\) is smooth at
   \(([Y],\Delta)\) of codimension \(2nN+R\);
3. \(h^1(X,I_\Delta\otimes K_X\otimes L^n)>0\);
4. \(\langle\zeta,\gamma_\beta\rangle\ne0\).

B145 turns items 1-2 into G090's smooth saturated codimension-\(R\) germ.
B144 makes the nonlinear discriminant Li clean, B054 supplies the local
type-\((0,0)\) relation channel, and items 3-4 give detection through
B026/B010. Universal G091 is therefore sufficient for rational HC through
B007.

For any scalable sequence, B141 additionally forces the node count to be
superlinear relative to \(mn-c\).

## Attempt 1 — The generic ordered incidence

For a sufficiently jet-ample \(L\) and a general ordered configuration, the
first-jet evaluation map is surjective. The incidence is then a smooth
projective bundle over the configuration space of expected codimension
\((2n+1)N\).

NG116 records why this does not solve the gate. First-jet surjectivity forces
value rank \(R=N\). B027-B028 then give zero adjoint defect and zero
vanishing-cycle relation space. The generic multisingularity stratum is too
transverse.

## Remaining construction

The target must lie on the degeneracy locus of first-jet evaluation while
remaining smooth with the smaller exact codimension \(2nN+R\). This is not
mere rank drop: all nonlinear incidence equations must have no additional
obstruction beyond the \(N-R\) value relations. B142-B143 realize precisely
this phenomenon through moving algebraic fibers, but that construction is
anchored.

The smallest unanchored obligation is therefore:

\[
 \text{construct a smooth excess component of }\mathcal I_N
 \text{ from }(X,\zeta),
\]

then prove its adjoint relation functional is nonzero. No audited
determinantal or Thom-Porteous argument supplies the specified component or
the class pairing; an expected-codimension calculation alone cannot do so.
