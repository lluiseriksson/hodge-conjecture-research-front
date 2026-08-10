---
brick_id: NG078
status: NO-GO
base_field: C with rational homology
variety: an arbitrary B058 distributed plane-net detector and a projective collision to a fiber with finitely many isolated ordinary double points
smoothness: detector fibers smooth; target nodal; each local Milnor fiber smooth
projectivity: global hyperplane family and collision projective; local collapse theorem analytic
dimension: ambient 2n; hyperplane fibers 2n-1; local analytic germ dimension 2n
codimension: middle codimension n; target singular locus finite
coefficient_field: Q, with local collapse maps integral before extension
cohomology_theory: relative thimble homology, Milnor fibers, vanishing polyhedra, boundary specialization, and primitive ambient homology
hodge_type: no Hodge type is supplied by the local topological maps
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B057-B058, B101-B102, G055, G065, S049-S050
claim: The existence of local collapsing maps at every isolated target singularity, together with a local boundary-specialization morphism, automatically produces G065's marked comparison for an arbitrary distributed B057 detector and preserves its ambient class c.
falsifier: a distributed detector not already supported in the chosen local vanishing zones, or two different localization maps with the same local collapse data but different marked relation vectors
---

# NG078 — Local collapses do not globalize the distributed detector

**Status:** NO-GO

B102 supplies a map from a *local Milnor fiber* to its local special fiber.
S050 supplies a homology specialization from the boundary of a local Milnor
fiber to the link, built from inclusion in a vanishing-zone neighborhood and
deformation retraction. Both constructions start after a class is already
inside the relevant local space.

B057's detector instead traces a generally nonlocal word through the smooth
plane-net family. Neither source constructs a map

\[
 C_{\mathrm{dist}}\longrightarrow
 \bigoplus_{p\in\operatorname{Sing}Y_0}C_{\mathrm{Milnor},p}
\]

or proves which marked local vector receives its boundary. The local
collapsing maps also contain no B022 quotient or fixed-ambient closure data.

Therefore local collapses cannot be composed with the detector until a
localization map and compatible exterior gluing have been constructed. G066
is the exact re-entry condition.
