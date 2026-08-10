---
brick_id: B083
status: PROVED
base_field: C
variety: a proper one-parameter degeneration obtained by restricting a plane-net collision family to a pointed algebraic curve
smoothness: generic fiber smooth; special fiber arbitrary; total space may be replaced by the B071 regular semistable stack
projectivity: degeneration and semistable pushdown are proper/projective
dimension: arbitrary for the sheaf theorem; ambient 2n and hyperplane fibers 2n-1 in the Hodge application
codimension: special fiber is a divisor in the one-parameter total space; terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: rational constructible derived category, nearby cycles, vanishing cycles, stalk cohomology, and rational mixed Hodge modules in the application
hodge_type: all maps are rational Hodge morphisms after lifting to mixed Hodge modules; no lift is asserted to exist or have type (0,0)
cycle_class_map: not used; downstream map is CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence in the downstream Hodge application
scope: relative and fiberwise
dependencies: S037, B063, B072
claim: For a fixed one-parameter collision degeneration, the canonical nearby-cycle triangle maps special-stalk cohomology to nearby cohomology; a nearby class lifts to the special stalk exactly when its canonical vanishing-cycle obstruction is zero, and when lifts exist their ambiguity is the preceding image in the associated long exact sequence.
falsifier: a nearby class with nonzero image in the vanishing-cycle term that nevertheless lifts from the special stalk, or a canonical reverse map supplied by the cited triangle
---

# B083 — The nearby-to-special problem is a lift criterion

**Status:** PROVED

Let $f:\mathfrak X\to T$ be a one-parameter degeneration, let
$i:\mathfrak X_0\hookrightarrow\mathfrak X$, and let $K$ be a rational
constructible complex. In the conventions audited in S037, the natural map
$i^*K\to\Psi_fK$ fits into the nearby/vanishing-cycle distinguished
triangle

\[
 i^*K\longrightarrow\Psi_fK
 \xrightarrow{\mathrm{can}}\Phi_fK[1]
 \xrightarrow{+1}.
\]

Taking a stalk at the collision point and cohomology gives an exact segment

\[
 H^q(i_p^*K)\longrightarrow H^q(i_p^*\Psi_fK)
 \xrightarrow{\mathrm{can}}
 H^q(i_p^*\Phi_fK[1]).
\]

Therefore a nearby class $t_\psi$ has a special-stalk lift $\beta$ if and
only if

\[
 \mathrm{can}(t_\psi)=0.
\]

When the condition holds, exactness gives existence but not uniqueness.
Two lifts differ by the kernel of the first arrow, equivalently by the image
of the preceding cohomology group in the long exact sequence.

This direction matters for G047: the canonical morphism carries a special
class to its nearby realization. The triangle does not canonically send an
arbitrary nearby class, much less an ambient homology class, back to the
special stalk.

## Boundary

B083 gives an exact falsifiable obstruction, not its vanishing. G048 must
construct the B057 nearby class for an algebraic collision family, prove its
vanishing-cycle image is zero, choose a rational lift, and control the lift
ambiguity under the prescribed pairing and perverse filtration.
