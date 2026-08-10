---
brick_id: B077
status: PROVED
base_field: C
variety: a smooth finite-stabilizer Deligne-Mumford stack with a proper morphism to a complex algebraic variety, including the B071 semistable model
smoothness: source stack smooth/regular; target arbitrary
projectivity: morphism proper/projective in the application
dimension: arbitrary
codimension: all strict supports; terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules on stacks, weights, proper pushforward, perverse cohomology, and strict-support decomposition
hodge_type: pure Hodge objects and their direct summands; no class-specific type is inferred
cycle_class_map: not used; downstream map is CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence in the downstream Hodge application
scope: relative
dependencies: B071-B072, S047
claim: Proper pushforward of the pure constant Hodge object from the smooth finite-stabilizer semistable stack is pure and admits a splitting into semisimple perverse cohomology; each canonical perverse cohomology object has a unique strict-support decomposition and a well-defined full-support summand.
falsifier: failure of proper pushforward to preserve both weight inequalities or failure of semisimplicity/decomposition for pure objects with affine stabilizers
---

# B077 — Pure stack pushdown has strict-support decomposition

**Status:** PROVED

The B071 semistable Deligne–Mumford stack has finite, hence affine,
stabilizers. Its shifted constant Hodge object is pure because the stack is
smooth/log regular.

Tubach Proposition 3.22 shows that \(f_!\) preserves the upper weight bound,
and Corollary 3.23 shows that \(f_*\) preserves the lower weight bound. For a
proper morphism represented by Deligne–Mumford stacks, Proposition 3.15 gives
\(f_!\simeq f_*\). Consequently proper pushforward of a pure object is pure.

Corollary 3.24 then proves, for stacks with affine stabilizers, that a pure
object admits a splitting as the sum of its perverse cohomology objects and that pure
objects in the perverse heart are semisimple. When the target is a variety,
Saito's strict-support decomposition of each simple pure Hodge module groups
these summands by irreducible support. After choosing such a
decomposition-theorem splitting,

\[
f_*\mathbf Q_{\mathcal Y}[\dim\mathcal Y]
\simeq M_{\mathrm{fs}}\oplus M_{<\mathrm{fs}},
\]

where \(M_{\mathrm{fs}}\) is the sum of simple constituents whose support is
the whole target and \(M_{<\mathrm{fs}}\) is the sum of constituents on
proper supports.

The objects
\({}^pH^i(f_*\mathbf Q_{\mathcal Y}[\dim\mathcal Y])\) and their
strict-support decompositions are canonical. The displayed splitting across
different perverse degrees is not canonical; B081 records the resulting
class-level correction.

## Exact boundary

The decomposition exists, but this theorem neither canonically splits the
perverse filtration on a total cohomology class nor puts the specialized
B058 class into full support. G046 gives the invariant associated-graded
formulation.
