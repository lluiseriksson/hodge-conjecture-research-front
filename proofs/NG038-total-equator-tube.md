---
brick_id: NG038
status: NO-GO
base_field: C
variety: a smooth projective variety with one complete generic Lefschetz pencil, all critical values in one hemisphere, and the smooth total equator loop
smoothness: the reference fiber and equator family are smooth; all critical fibers have one ordinary double point
projectivity: the ambient variety, blown-up pencil total space, and fibers are projective
dimension: arbitrary complex ambient dimension; the Hodge application has dimension 2n
codimension: middle codimension n in the Hodge application
coefficient_field: Q
cohomology_theory: Picard-Lefschetz monodromy, extension chains, thimble quotient homology, and primitive ambient homology
hodge_type: none; the obstruction occurs before the Hodge-type test
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B057, and Lairez-Pichon-Pharabod-Vanhove equations (12), (42), and (43) (S029)
claim: The B013/B057 relation obtained by extending an invariant class around the total equator of one complete Lefschetz pencil lies in the equator-extension image and is zero in the thimble group, so it cannot be a nonzero primitive ambient detector.
falsifier: a total-equator extension whose thimble-coordinate vector is not in im(tau_infinity) or has nonzero class in T(Y)=ker(boundary)/im(tau_infinity)
---

# NG038 - The total-equator relation is quotiented out

## Route tested

Take the product of all Picard-Lefschetz meridians in one complete generic
pencil, apply B013 to an invariant class, and use the resulting relation as
the global detector to be collided.

## Exact obstruction

Let \(\ell_\infty=\ell_r\cdots\ell_1\) be the total equator. S029 equations
(42)-(43) state

\[
 \tau_\infty
 =\sum_{i=1}^r
 \tau_{\ell_i}M_{i-1}\cdots M_1.
\]

B057 shows that the right side is exactly the thimble-coordinate vector of
B013's telescoping relation. If the input \(\alpha\) is invariant, this
vector lies in the boundary kernel, but the thimble group is

\[
 \mathcal T(Y)
 =\ker\partial/\operatorname{im}\tau_\infty.
\]

Therefore

\[
 [\tau_{\ell_\infty}(\alpha)]=0
 \quad\text{in}\quad\mathcal T(Y),
\]

before the base-locus quotient or any Hodge pairing is considered.

This does not kill arbitrary Schnell loops in the plane net from B056.
It excludes only the tempting choice of the complete pencil's total
equator. A viable detector loop must represent a non-equator class in the
net complement, and its later collision must preserve the nonzero quotient
class.

## Re-entry condition

Start from B056's actual detecting loop in a generic plane net, use B057 to
track its extension chain, and construct a topology-changing specialization
to one clean nodal point without replacing it by the total-equator word.
This is G030.
