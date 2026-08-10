---
brick_id: B076
status: PROVED
base_field: C
variety: a finite etale Galois cover on the generic locus, its finite stack extension, and any one- or multi-parameter degeneration to which the nearby-cycle functors apply
smoothness: generic locus smooth; special fiber arbitrary; the application uses the B071 semistable stack
projectivity: the finite map is proper/projective
dimension: arbitrary
codimension: arbitrary boundary codimension; terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules on stacks, six operations, finite-cover unit and trace, and iterated nearby cycles
hodge_type: unit, trace, and nearby-cycle maps are morphisms of rational Hodge objects and preserve Hodge subobjects
cycle_class_map: not used; downstream map is CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence in the downstream Hodge application
scope: relative and fiberwise
dependencies: B063, B072, B075, S047
claim: Finite-cover unit and trace commute with each nearby-cycle functor; after rational normalization their composition remains the identity on iterated nearby cycles, so the original nearby-cycle object is a split retract of the invariant covered object.
falsifier: failure of proper-pushforward compatibility of nearby cycles or failure of trace composed with unit to equal the cover degree after applying nearby cycles
---

# B076 — Nearby cycles preserve the finite-trace retract

**Status:** PROVED

Let \(p:\widetilde{mathcal X}\to\mathcal X\) be a finite degree-\(d\)
cover in the stack MHM setting of B072. On the generic locus there are the
unit and trace morphisms

\[
\eta:M\longrightarrow p_*p^*M,
\qquad
\operatorname{tr}:p_*p^*M\longrightarrow M,
\]

and

\[
\operatorname{tr}\circ\eta=d\,\operatorname{id}_M.
\]

The identity may be checked after the conservative rational-realization
functor, where it is the usual sum over the \(d\) sheets.

Tubach's Theorem 3.28 and the discussion following it make unipotent nearby
cycles compatible with proper pushforward; full nearby cycles are built from
that construction in Theorem 3.36. Applying nearby cycles to the unit and
trace therefore gives

\[
\Psi(\operatorname{tr})\circ\Psi(\eta)
=d\,\operatorname{id}_{\Psi M}.
\]

The same argument can be iterated for every boundary coordinate because the
finite map remains proper after base change. Under B063's stated
strict-multispecialisability hypothesis, the result is independent of the
chosen order and lies in rational mixed Hodge modules. Hence

\[
\frac1d\Psi(\operatorname{tr})
\]

is a retraction of \(\Psi(\eta)\), including for the iterated nearby-cycle
object.

## Consequence and boundary

No nonzero original nearby-cycle class can be killed merely by passing to the
finite root cover and tracing back: its pullback is split injective. Conversely,
the trace formalism cannot manufacture a nonzero original boundary class if
the original specialization is zero. Proper semistable modifications and the
two B022 quotient maps still require their own compatibility calculation.
