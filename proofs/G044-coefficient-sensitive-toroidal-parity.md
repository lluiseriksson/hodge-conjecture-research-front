---
brick_id: G044
status: EXPLORATORY
base_field: C with all coefficient and descent data over Q
variety: the B071 semistable log-stack, its toroidal modification and finite descent maps, and the original plane-net hyperplane family
smoothness: regular semistable source and base stacks; smooth generic hyperplane fibers
projectivity: every factor used in the pushdown is projective or finite
dimension: arbitrary ambient dimension 2n and odd hyperplane-fiber dimension 2n-1
codimension: arbitrary proper boundary support; terminal cycles have codimension n
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, nearby cycles, perverse cohomology, strict support, local toric decomposition, and étale descent
hodge_type: detector target is rational type (0,0) after Q(n); coefficient Hodge modules may have non-Tate fiber cohomology
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B057-B058, B071-B080, G043, G045, NG055-NG057
claim: In the exact perverse degree containing the B057-B058 nearby specialization, every proper-support constituent of the B071 pushdown is excluded by a coefficient-sensitive toroidal parity or amplitude bound, so the class has full support whenever its total specialization is nonzero.
falsifier: an odd coefficient shift, nontrivial descent local system, or boundary gluing term that contributes on proper support in the detector degree
---

# G044 — Coefficient-sensitive toroidal parity

**Status:** EXPLORATORY  
**Parent gate:** G043

## Falsifiable theorem target

Factor the proper map underlying B077 into its finite/root-cover,
monoidal-toroidal modification, and global semistable-family pieces. Let
(P) be the rational Hodge module whose nearby specialization contains the
B057 extension chain. Prove, with all shifts displayed, that every
strict-support constituent (N_Z[-b]) on a proper boundary support (Z)
misses the ordinary detector degree. Equivalently, prove that the normal
toric parity of B078 survives with the actual coefficient Hodge modules and
through étale/stack descent.

Then

\[
 \operatorname{sp}(c)\ne0
 \quad\Longrightarrow\quad
 \pi_{\mathrm{fs}}\operatorname{sp}(c)\ne0.
\]

## Required calculation

1. Write the exact factorization of the B071 proper pushdown.
2. Identify the perverse cohomology object and ordinary degree containing
   the B057 thimble-extension chain.
3. On every toroidal chart, separate the toric normal factor from the
   coefficient Hodge module contributed by the global fiber stratum.
4. Convolve the normal support degree with every coefficient degree, as
   B079 shows is necessary, and prove none equals the detector degree; then
   check descent across chart overlaps and finite stabilizers.
5. If step 4 fails, exhibit the first support and coefficient degree that
   does contribute; that datum becomes the explicit subtraction term in
   G043.

## Current evidence and boundary

B078 proves the needed parity only for the globally toric constant/IC model.
B079/NG056 prove that arbitrary coefficient convolution can create odd
proper-support terms, so a coefficient-blind extension is false. B076
controls the finite-cover trace, and B077 supplies the decomposition, but
neither identifies the coefficient index of the B057 chain. B080/NG057 now
perform the exact detector normalization and show that parity allows both
relevant shifts: divisor (b=0) and point (b=-1). G045 is therefore the
remaining multiplicity-and-class calculation inside this gate. This gate does
not yet prove that the total
specialization is nonzero, survive either B022 quotient, or retain the
prescribed pairing.
