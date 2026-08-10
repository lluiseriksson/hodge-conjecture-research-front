---
brick_id: G043
status: EXPLORATORY
base_field: C with all Hodge and descent data defined over Q
variety: the original plane-net degeneration, the B071 semistable stack, and its proper pushdown to the original base
smoothness: smooth generic fibers and smooth semistable source stack
projectivity: hyperplane family and all alterations, modifications, and pushdowns are projective
dimension: arbitrary ambient dimension 2n and odd singular-fiber dimension 2n-1
codimension: terminal cycles have codimension n; proper supports have positive codimension in the parameter base
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, nearby cycles, pure proper pushforward, strict support, and Saito detector maps
hodge_type: rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B057-B058, B063, B071-B077, G032, G042, NG053-NG054
claim: The nearby specialization of the B058 non-equator tube has nonzero projection to B077's full-support strict-support summand before the two B022 quotient tests, and that component remains paired nontrivially with the prescribed Hodge class.
falsifier: specialization zero, confinement to proper-support summands, or orthogonality of the full-support projection to the prescribed class
---

# G043 — Full-support projection of the specialized tube

**Status:** EXPLORATORY  
**Parent gates:** G042 / G032

## Falsifiable theorem target

Let \(\operatorname{sp}(c)\) denote the canonical nearby specialization of
the B058 tube and let

\[
\pi_{\mathrm{fs}}:
f_*\mathbf Q_{\mathcal Y}[\dim\mathcal Y]\longrightarrow M_{\mathrm{fs}}
\]

be the strict-support projection furnished by B077. Prove

\[
\pi_{\mathrm{fs}}\operatorname{sp}(c)\ne0
\]

and that its Saito ambient image is not orthogonal to the prescribed
primitive rational Hodge class.

## What is closed

- B076 removes finite-cover trace as a source of loss.
- B077 proves the pure strict-support decomposition exists.
- NG054 shows why the projection of the specified class remains separate.

## Smallest next calculation

Identify the specialization morphism on the perverse cohomology degree that
contains the B057 extension chain. Compute its components along every proper
support created by the semistable modification and subtract them from the
total class. The residual full-support component is the input for the two
B022 quotient maps.
