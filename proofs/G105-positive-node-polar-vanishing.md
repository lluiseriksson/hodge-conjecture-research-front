---
brick_id: G105
status: EXPLORATORY
base_field: C
variety: an arbitrary polarized smooth projective complex 2n-fold X, a specified nonzero primitive rational middle Hodge class zeta, and the universal hypersurface family restricted to a class-directed smooth basis-node germ F_B
smoothness: X and F_B are smooth; the central hypersurface has exactly the tracked ODPs and no other nearby singularities
projectivity: the family is the proper base change of the full complete-linear-system incidence
dimension: hyperplane dimension 2n-1; arbitrary basis-germ dimension; finitely many off-zero conormal components
codimension: every nonpersistent extra-node value cuts a positive-codimension escape divisor, generically codimension one
coefficient_field: Q
cohomology_theory: rational proper direct images, perverse cohomology, positive characteristic cycles, normal Morse groups, mixed Hodge modules, and rational Betti cohomology
hodge_type: the retained relation functional must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative of zeta may be assumed
cycle_equivalence: rational equivalence
scope: relative
dependencies: B134-B166, G090-G104, NG118-NG130
claim: Construct the carrier-free class-directed full-linear-system data and prove, without alternating cancellation, that every off-zero coefficient M_alpha of CC^+(K_B) vanishes, equivalently that every generic node-polar normal Morse group is zero, while retaining the superlinear uniform matroid, positive adjoint defect, nonzero primitive ambient image, rational type, and nonzero specified Saito pairing.
falsifier: one positive generic normal Morse rank, one escaping tracked node, an untracked singularity, or loss of any detector clause
---

# G105 — Kill every positive node-polar multiplicity

For \(K_B=Rg_*\mathbf Q\), form B165's positive package

\[
 CC^+(K_B)=\sum_jCC({}^pH^jK_B).
\]

G105 asks for a class-directed theorem proving that every off-zero
coefficient of this cycle is zero. By B166, in the exhaustive ODP model the
generic coefficient along \(D_\alpha\) is the positive integer
\(k_\alpha\) counting the nodes that escape across that reduced component.
Thus the target is the falsifiable collection

\[
 k_\alpha=0\quad\text{for every internal escape component }D_\alpha.
\]

The proof must be non-alternating: it must annihilate the normal Morse rank
of each perverse cohomology object or supply a geometric theorem forcing
the corresponding critical-value germs to vanish identically. It must also
retain, independently, the superlinear uniform matroid, positive adjoint
defect, nonzero primitive ambient image, rational type \((0,0)\), and the
specified nonzero Saito pairing with \(\zeta\).

B165-B166 make G105 equivalent to G104's persistence clause, but expose the
smallest local falsifier: one generic positive node-polar multiplicity.
They do not provide its vanishing.
