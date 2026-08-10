---
brick_id: NG064
status: NO-GO
base_field: C with rational homology
variety: a B058 detector in a one-parameter collision family of plane nets
smoothness: generic fibers smooth and collision endpoint singular
projectivity: ambient and hyperplane families projective
dimension: ambient 2n, hyperplane fibers 2n-1, and collision parameter 1
codimension: middle codimension n
coefficient_field: Q
cohomology_theory: Hurwitz transport, reference-fiber Gauss-Manin monodromy, relative thimbles, and B022 quotients
hodge_type: no type conclusion; obstruction precedes the Hodge test
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B023, B057, B088, G051
claim: Because collision monodromy acts by Hurwitz moves and preserves boundary rank, it automatically fixes the marked composite detector loop g, the reference class alpha, and the B057 chain tau_g(alpha).
falsifier: collision transport that conjugates g or acts nontrivially on alpha while preserving the Hurwitz-equivalence class and all ranks
---

# NG064 — Hurwitz-equivalent factorizations need not fix the marked detector

**Status:** NO-GO

B023 proves that Hurwitz moves are invertible changes of distinguished
thimble data and preserve relation dimensions. B088 proves exact invariance
only when the composite loop $g$, the reference-fiber trivialization, and
$\alpha$ return unchanged.

A collision loop may carry

\[
 g\longmapsto hgh^{-1},
 \qquad
 \alpha\longmapsto h\alpha,
\]

or act by an additional Gauss-Manin automorphism of the reference fiber.
The resulting factorization is Hurwitz equivalent and has the same ranks,
but it is not the same marked detector datum. Rank invariance therefore does
not imply $M_{\mathrm{coll}}t=t$.

The re-entry condition is G052: construct the collision with a marked
reference-fiber trivialization and prove exact return of $(g,\alpha)$.
