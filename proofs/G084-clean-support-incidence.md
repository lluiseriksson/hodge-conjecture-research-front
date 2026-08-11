---
brick_id: G084
status: EXPLORATORY
base_field: C with rational coefficients
variety: an arbitrary polarized smooth projective complex 2n-fold X, a nonzero primitive rational Hodge class zeta, and all sufficiently high universal hyperplane systems
smoothness: X smooth; sought fiber multipart nodal with Li-clean discriminant arrangement
projectivity: X and universal incidence families projective
dimension: dim_C X=2n; hyperplane fibers 2n-1; parameter dimensions grow with the embedding power
codimension: middle cycle codimension n; local support codimension at least two
coefficient_field: Q
cohomology_theory: local intersection cohomology, Green-Griffiths support, vanishing cycles, and Saito primitive ambient homology
hodge_type: zeta and the automatically supplied nodal relation rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative may be assumed
cycle_equivalence: rational equivalence
scope: absolute
dependencies: B007, B010, B012, B014, B054, B064, B125-B126, G008, G031-G032, NG011-NG012, NG040, NG101
claim: For every nonzero primitive rational Hodge class zeta, there is a sufficiently high power m such that its local restriction support Sigma_(zeta,m) meets the Li-clean multipart nodal locus C_m^(clean).
falsifier: a smooth projective complex 2n-fold and nonzero primitive rational Hodge class whose local support avoids every Li-clean multipart nodal locus in every sufficiently high hyperplane system
---

# G084 — Force the clean support incidence

**Status:** EXPLORATORY — active smallest gate

Prove for every allowed \((X,\zeta)\) that

\[
 \exists m\gg0:\qquad
 \Sigma_{\zeta,m}\cap C_m^{\mathrm{clean}}\ne\varnothing.
\]

B125 proves that this single incidence supplies the relation, rational Hodge
type, and nonzero Saito pairing required by G031. B007 then propagates to the
standard rational Hodge Conjecture.

## Attempt 1 — Dimension and generic slicing

B012 gives \(\operatorname{codim}\Sigma_{\zeta,m}\ge2\). A plane meets a
known nonempty codimension-two component generically, but neither this bound
nor the nonzero global Green-Griffiths invariant proves the local support is
nonempty. NG011-NG012 and B014 prevent a formal hypercohomology repair.

## Attempt 2 — Local nodalization of a support point

Even if a support point is given, adjacency to a clean multipart nodal point
is not formal. B126 computes the suspended \(A_2\) miniversal slice: every
noncentral discriminant fiber has exactly one node and the central fiber has
one \(A_2\) singularity. There is no two-node fiber and hence no local nodal
relation channel. NG101 closes local versal nodalization as a general proof
of the displayed incidence.

## Precise obstruction

One needs a global, class-specific topology-changing incidence theorem. It
must either prove that \(\Sigma_{\zeta,m}\) itself contains a clean multipart
nodal point, or transport nonzero local restriction to such a point while
controlling the complete nearby-cycle morphism. Nonemptiness, adjacency of
singularity types, node counts, and Milnor-number conservation do not imply
this intersection.

## Re-entry condition

Construct a global algebraic deformation outside a single local versal germ
and prove preservation of the local restriction/pairing. This is the genuine
content shared with G032; no algebraic representative of \(\zeta\) may be
used to select the deformation.
