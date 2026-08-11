---
brick_id: G106
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X, a specified nonzero primitive rational middle Hodge class zeta, the complete linear system P, and a class-directed smooth basis-node germ i:F_B->P
smoothness: X, P, the universal hypersurface incidence, and F_B are smooth; the central hypersurface has exactly the tracked ODPs and no other nearby singularities
projectivity: the universal hypersurface map h:U->P and its base change to F_B are projective
dimension: hyperplane dimension 2n-1; ambient base dimension dim P; basis-germ codimension R
codimension: every relevant ambient higher-discriminant or sheaf-support component has its full normal-cone transform tested on F_B
coefficient_field: Q
cohomology_theory: rational proper direct images, microsupport, microlocal inverse image, higher discriminants, perverse characteristic cycles, mixed Hodge modules, and rational Betti cohomology
hodge_type: the retained relation functional must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative of zeta may be assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B134-B169, G090-G105, NG118-NG133
claim: Construct the carrier-free class-directed full-linear-system data and prove that i-sharp SS(Rh_*Q_U) is contained in the zero section of T^*F_B, or prove the stronger sufficient inclusion for the full higher-discriminant envelope h-dagger(0_U), while retaining the superlinear uniform matroid, positive adjoint defect, nonzero primitive ambient image, rational type, and nonzero specified Saito pairing.
falsifier: one nonzero covector in the microlocal normal-cone transform, one escaping tracked node, an untracked singularity, or loss of any detector clause
---

# G106 — Absorb the full ambient microlocal normal cone

Let \(h:\mathcal U\to P=|L|\) be the universal hypersurface family and
\(i:F_B\hookrightarrow P\) the proposed class-directed basis germ. G106
asks for

\[
 i^\#SS(Rh_*\mathbf Q_{\mathcal U})
 \subseteq T^*_{F_B}F_B. \tag{1}
\]

B167 makes (1) sufficient for G105's componentwise positive vanishing.
One may instead prove the stronger, more geometric condition

\[
 i^\#h^\dagger(0_{\mathcal U})
 \subseteq T^*_{F_B}F_B, \tag{2}
\]

where Migliorini--Shende express the ambient envelope in (2) as the union
of conormals to components of all higher discriminants of \(h\).

The obligation is germwise and normal-cone sensitive. B168 shows that it
cannot be replaced by pointwise containment of ambient conormal fibers in
\(N^*_{F_B}P\), tangent-space containment at the central point, or any
fixed finite jet test.

Together with (1), the construction must retain the superlinear uniform
value matroid, isolated exhaustive ODPs, positive adjoint defect, nonzero
primitive ambient image, rational type \((0,0)\), and the specified nonzero
Saito pairing with \(\zeta\). Neither higher-discriminant support nor
microlocal absorption supplies that pairing automatically.

B169 closes the apparent weakening in (1)--(2). In the exhaustive
tracked-ODP neighborhood required here, the envelope is exactly the union
of the nodal conormals, each nodal conormal occurs in the actual sheaf
microsupport, and its \(i^\#\)-image is zero exactly when that node divisor
contains \(F_B\). Hence either absorption condition is equivalent to
B158's persistence clause and B156's hidden-generator equation
\(H_\tau=0\). NG133 records that the microlocal reformulation is not an
independent shortcut. The smallest unresolved geometric clause therefore
returns to G100/G101: construct those analytic syzygies in the full linear
system while retaining the specified nonzero pairing.
