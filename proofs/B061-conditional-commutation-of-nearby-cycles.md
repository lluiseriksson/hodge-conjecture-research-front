---
brick_id: B061
status: PROVED
base_field: C
variety: complex analytic spaces, or complex algebraic varieties after analytification, mapped to a polydisk or affine coordinate space
smoothness: Nadler assumes the ambient map is a submersion; Kochersperger assumes a regular holonomic D-module and a graph pair without slopes
projectivity: not required by either source; any projective Hodge application needs separate verification
dimension: arbitrary finite dimension
codimension: not a cycle-codimension statement; nearby cycles are taken along coordinate divisors
coefficient_field: C for the regular holonomic D-module theorem; an abstract coefficient category for the constructible-sheaf statement; B063 separately supplies a Q-structured mixed-Hodge lift under without slopes
cohomology_theory: topological nearby cycles and algebraic nearby cycles of regular holonomic D-modules
hodge_type: none asserted by S041 alone; B063 separately proves rational mixed-Hodge preservation under without slopes
cycle_class_map: none
cycle_equivalence: none
scope: relative and fiberwise
dependencies: primary-source audit S041
claim: Natural maps compare the orders of iterated nearby cycles, but invertibility requires explicit hypotheses such as without slopes or non-characteristic plus Thom; it does not hold formally in general.
falsifier: a source-level demonstration that arbitrary multi-parameter nearby-cycle functors commute without any condition
---

# B061 — Conditional commutation of iterated nearby cycles

**Status:** PROVED (imported theorem boundary; not a proof of the Hodge Conjecture)  
**Gate:** G032 / G033  
**Primary sources:** S041

## Mathematical type record

- **Base field:** \(\mathbf C\).
- **Variety/class:** complex analytic spaces, or complex algebraic varieties after analytification, equipped with a map to a polydisk or affine coordinate space.
- **Smoothness/projectivity:** Nadler assumes the ambient map \(f:X\to D^n\) is a submersion; projectivity is not assumed. Kochersperger works with a regular holonomic \(\mathcal D\)-module and a graph construction; projectivity is not assumed. Any projective Hodge application needs additional verification.
- **Dimension:** arbitrary finite dimension.
- **Codimension:** not a cycle-codimension statement; each nearby-cycle functor is taken along one coordinate divisor.
- **Coefficient field:** \(\mathbf C\) in the regular-holonomic \(\mathcal D\)-module comparison; an abstract coefficient category for the constructible-sheaf statement. B063 separately supplies the rational mixed-Hodge lift under the without-slopes hypothesis.
- **Cohomology theory:** topological nearby cycles and algebraic nearby cycles of regular holonomic \(\mathcal D\)-modules.
- **Hodge type:** none asserted by S041 alone. B063 proves preservation of rational mixed-Hodge structure under without slopes, but not compatibility with the detector pairing.
- **Cycle class map:** none.
- **Equivalence relation on cycles:** none.
- **Scope:** relative and fiberwise comparison over a multi-parameter degeneration.

## Claim

For a two- or multi-parameter degeneration there are natural comparison maps among the multi-nearby-cycle object and the objects obtained by taking one-variable nearby cycles in different orders. These maps are **not equivalences in general**.

Two audited sufficient frameworks do make them equivalences:

1. **Without-slopes framework.** For a regular holonomic \(\mathcal D\)-module \(M\), if the graph pair \((H,i_{f+}M)\) is without slopes, Kochersperger's Theorem 3.6 and Corollary 3.7 identify algebraic and topological nearby cycles and show that iterated nearby cycles are independent of the coordinate order, compatibly with monodromy.
2. **Microlocal framework.** If \(f:X\to D^n\) is a submersion, \(F\) is weakly constructible with singular support in a closed conic Lagrangian \(\Lambda\), and \(\Lambda\) is both \(f\)-non-characteristic and \(f\)-Thom at the origin, Nadler's Theorem 4.2.1 makes the natural flag-comparison maps equivalences, compatibly with monodromy.

These are distinct sufficient packages; this repository does not identify them as equivalent.

## Proof audit

Kochersperger explicitly states that nearby-cycle functors associated to several functions do not commute in general. His comparison theorem proves order-independence only after imposing the without-slopes condition. Nadler first constructs a lax diagram
\[
\psi_{f_1}\psi_{f_2}F \longleftarrow \Psi_fF
\longrightarrow \psi_{f_2}\psi_{f_1}F,
\]
then proves the arrows are equivalences under the non-characteristic and Thom hypotheses. Thus existence of comparison arrows is formal, while their invertibility is geometric/microlocal content.

## Consequence for the vertical map

An attempted recollision argument may use order-independent iterated nearby cycles only after checking a named sufficient hypothesis for the actual family and actual coefficient object. B063 closes the rational mixed-Hodge lift under without slopes. A separate compatibility argument is still required for the B022 quotients and decisive Saito pairing.

## Non-claims

- This does not construct an algebraic cycle.
- This does not prove that a collision family is without slopes, non-characteristic, or Thom.
- This does not prove compatibility with the two quotient maps in B022.
- This does not prove the rational Hodge Conjecture.
