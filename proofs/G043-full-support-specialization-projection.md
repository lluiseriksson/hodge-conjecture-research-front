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
dependencies: B057-B058, B063, B071-B081, G032, G042, G045-G046, NG053-NG058
claim: The nearby specialization of the B058 non-equator tube has nonzero canonical perverse associated-graded component whose strict-support projection inside pH^0 to full support is nonzero before the two B022 quotient tests and remains paired nontrivially with the prescribed Hodge class.
falsifier: specialization zero, confinement to the point-support perverse grade, confinement to divisor support inside pH^0, or orthogonality of the full-support graded class
---

# G043 — Full-support projection of the specialized tube

**Status:** EXPLORATORY  
**Parent gates:** G042 / G032

## Falsifiable theorem target

Let \(\operatorname{sp}(c)\) denote the canonical nearby specialization of
the B058 tube. B081/NG058 show that a total derived projection supplied by a
chosen decomposition-theorem splitting is not canonical. Replace it by

\[
E_\infty^{-1,0}(K,p)
\longrightarrow
H^{-1}(i_p^*{}^pH^0(K)_{\mathrm{fs}}),
\]

where the second arrow comes from the unique strict-support decomposition
inside \({}^pH^0(K)\). Prove

\[
\operatorname{pr}_{\mathrm{fs}}
[\operatorname{sp}(c)]_{E_\infty^{-1,0}}\ne0
\]

and that its Saito ambient image is not orthogonal to the prescribed
primitive rational Hodge class.

## What is closed

- B076 removes finite-cover trace as a source of loss.
- B077 proves the pure strict-support decomposition exists.
- NG054 shows why the projection of the specified class remains separate.
- B081/NG058 replace the noncanonical total projection by the canonical
  perverse-grade and perverse-heart strict-support projection.

## Smallest next calculation

Prove G046: compute the two canonical perverse-filtration edge components of
the B057 extension chain. The point term is the separate
\(E_\infty^{0,-1}\) grade; only the divisor term shares
\(E_\infty^{-1,0}\) with full support. Project that grade by its canonical
strict-support decomposition before applying the two B022 quotient maps.
