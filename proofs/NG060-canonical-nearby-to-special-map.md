---
brick_id: NG060
status: NO-GO
base_field: C
variety: a proper one-parameter collision degeneration of a plane-net hyperplane family
smoothness: generic fiber smooth and special fiber singular; semistable source may be regular
projectivity: proper/projective
dimension: ambient 2n, hyperplane fibers 2n-1, and collision parameter 1
codimension: special fiber has parameter codimension one; terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: rational nearby cycles, vanishing cycles, stalk cohomology, and mixed Hodge modules
hodge_type: rational type (0,0) after Q(n) is required downstream but is not forced by the triangle
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B083, G047, S037
claim: A chosen collision family canonically maps every nearby B057 class to a special-stalk class, with no vanishing-cycle obstruction or lift ambiguity.
falsifier: the canonical triangle i^*K -> Psi_f K -> Phi_f K[1], whose exact sequence permits a lift precisely in the kernel of can and does not select a unique preimage
---

# NG060 — Nearby cycles do not canonically map back to the special stalk

**Status:** NO-GO

For a fixed collision family, the natural arrow in the audited triangle is

\[
 i^*K\longrightarrow\Psi_fK,
\]

not an unconditional reverse map. A nearby class $t_\psi$ comes from the
special stalk only if

\[
 \mathrm{can}(t_\psi)=0
\]

in the shifted vanishing-cycle term. Even then, exactness generally leaves
a torsor of lifts rather than a preferred one.

Thus neither the existence of a semistable model nor the formal availability
of nearby cycles closes G047. The re-entry condition is G048: compute the
actual B057 nearby class, kill its vanishing-cycle obstruction, and prove
that some rational lift—and its relevant pairing/full-support component—has
the required properties.
