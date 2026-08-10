---
brick_id: G066
status: EXPLORATORY
base_field: C with comparison maps over Z before extension to Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, its class-specific B058 distributed detector, and an actual projective collision to a clean isolated nodal hyperplane fiber
smoothness: X and nearby fibers smooth; target has finitely many ordinary double points; disjoint Milnor balls chosen; exterior total space required stratified-submersive along the collision path
projectivity: X, plane-net hyperplane family, and collision projective
dimension: ambient 2n; hyperplane fibers 2n-1; collision base 1; local analytic germs dimension 2n
codimension: middle codimension n; target singular support finite
coefficient_field: Z for marked topological maps and Q after extension
cohomology_theory: relative thimble homology, Milnor fibrations, vanishing polyhedra, Ehresmann/Thom-Mather exterior trivialization, good retraction, B022 quotients, and primitive ambient homology
hodge_type: target local relation and ambient class must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B057-B058, B081-B083, B093-B102, G047-G063, NG069-NG078, S049-S050
claim: For the actual class-specific collision, localize a marked representative of the B057 detector into the disjoint union of target Milnor tubes, glue the S049 local collapsing maps to a stratified exterior trivialization, identify the resulting marked boundary with r_H(beta_sp), and construct the chain homotopy between the B057/B098 and Saito ambient realizations.
falsifier: failure of detector localization, incompatible collar maps on Milnor boundaries, a different marked local vector, nonzero residual exterior boundary, or mismatch of the two closed ambient chains
---

# G066 — Localize the detector and glue the local collapses

**Status:** EXPLORATORY

Choose disjoint Milnor tubes $U_p$ around the singular points of the target.
The first required construction is a chain-level localization

\[
 \lambda_t:C_{\mathrm{dist}}\longrightarrow
 C_*\!\left(\bigsqcup_p U_{p,t},
              \bigsqcup_p\partial U_{p,t};\mathbf Z\right)
\]

for the actual B057 representative. It must retain every marked boundary
sphere and orientation and send its rational extension to the canonical
full-support vector $r_H(\beta_{\mathrm{sp}})$.

On each $U_{p,t}$, use B102's vanishing-polyhedron collapse. On the
complement of the Milnor tubes, construct a Thom-Mather/Ehresmann
trivialization along the collision path. Prove that the local and exterior
maps agree on collars, so they glue to G065's map of pairs. Finally exhibit
a chain homotopy between:

1. closing the original distributed chain and applying B098; and
2. applying the glued collapse, Saito's good retraction, and ambient
   pushforward.

B101 then gives the boundary and ambient equalities, while B100 removes the
choice of relative lift. The unproved datum is the class-specific
localization $\lambda_t$ and its collar-compatible gluing, not existence of
the individual local collapses.
