---
brick_id: B091
status: PROVED
base_field: C with rational homology
variety: a polarized smooth projective complex 2n-fold, a nonzero B058 plane-net detector, and a marked comparison to a normal-crossing nodal cluster
smoothness: ambient and marked reference fibers smooth; target hyperplane has only independently smoothable ordinary double points
projectivity: ambient hyperplane family and plane net projective
dimension: ambient 2n; hyperplane fibers 2n-1; plane-net base 2
codimension: middle codimension n; target nodal stratum of positive codimension
coefficient_field: Q
cohomology_theory: Picard-Lefschetz monodromy, relative thimble homology, tube maps, and primitive ambient homology
hodge_type: the input ambient detector is rational type (0,0) after Q(n); the conclusion is topological vanishing
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no cycle is constructed
cycle_equivalence: rational equivalence in the terminal application
scope: relative and fiberwise
dependencies: B022, B057-B059, B088-B090
claim: A nonzero B058 detector cannot be compared to the positive total boundary of a normal-crossing nodal cluster solely by marked Hurwitz moves while preserving its input class and relative extension chain.
falsifier: a pure marked Hurwitz comparison carrying a nonzero B058 extension to a positive local-boundary extension without changing the reference fiber or input class
---

# B091 — Pure Hurwitz collapse kills the detector

**Status:** PROVED

Let $t=\tau_g(\alpha)$ be a B057 extension whose B022 ambient image pairs
nontrivially with the prescribed Hodge class. In particular, $t$ is nonzero
before the B022 quotients.

Assume a marked comparison carries this chain to a normal-crossing nodal
target using only Hurwitz moves, keeps the reference-fiber identification and
$\alpha$ fixed, and identifies the composite loop with the positive total
local boundary $h$. B088 says that the relative extension chain is unchanged:

\[
 t=\tau_h(\alpha).
\]

Because the original loop fixes $\alpha$ and the marked comparison identifies
the composites, $h\alpha=\alpha$. B090 then gives

\[
 \tau_h(\alpha)=0.
\]

Thus $t=0$, contradicting its nonzero ambient pairing. No comparison with all
the stated properties exists.

## Consequence

The missing specialization in G054 cannot be a pure change of distinguished
paths or thimble basis. It must contain a genuine topology-changing
correction not chain-homotopic to the marked Hurwitz identification. G055
isolates the construction and nonvanishing of that correction.
