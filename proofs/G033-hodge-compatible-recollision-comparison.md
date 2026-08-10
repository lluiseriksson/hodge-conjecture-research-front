---
brick_id: G033
status: EXPLORATORY
base_field: C, with a finitely generated subfield model if arithmetic specialization is invoked
variety: a two-parameter algebraic degeneration connecting a distributed detector to a Li-clean multipart nodal collision
smoothness: generic fibers are smooth; the collision fiber is singular and the total-space stratification or resolution must be stated explicitly
projectivity: generic fibers and the intended hyperplane family are projective
dimension: arbitrary ambient middle-degree dimension
codimension: target cycles have codimension p; parameter boundary divisors have codimension one
coefficient_field: Q for the target Hodge comparison and C after microlocal or D-module complexification
cohomology_theory: rational Betti cohomology, mixed Hodge modules and structures, and iterated nearby cycles
hodge_type: target class (p,p), equivalently type (0,0) after Q(p)
cycle_class_map: CH^p(X)_Q -> H^(2p)(X,Q(p))
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B061-B064, G032, G034, NG042, and NG043
claim: For the explicit recollision family, a verified conditional nearby-cycle equivalence lifts rationally and preserves type, the B022 quotient maps, and the nonzero Saito detector pairing.
falsifier: failure of all published sufficient commutation hypotheses at the collision, failure of a rational Hodge lift, or loss of the quotient-level nonzero pairing
---

# G033 — Hodge-compatible recollision comparison

**Status:** EXPLORATORY  
**Parent gate:** G032  
**Dependencies:** B022, B061-B064

## Mathematical type record

- **Base field:** \(\mathbf C\), with a model over a finitely generated subfield when spreading or arithmetic specialization is invoked.
- **Variety/class:** a two-parameter algebraic degeneration whose boundary fibers encode the distributed detector and clean nodal-collision configurations used in G031–G032.
- **Smoothness/projectivity:** generic fibers smooth and projective; total space and boundary require an explicit stratification or resolution statement. No smooth-total-space assumption is silently imposed.
- **Dimension:** arbitrary ambient dimension relevant to the parent family.
- **Codimension:** the target cycle has codimension \(p\); nearby-cycle divisors are codimension one in parameter space.
- **Coefficient field:** \(\mathbf Q\) for the desired Hodge comparison; complexification may be used for microlocal or \(\mathcal D\)-module tests.
- **Cohomology theory:** rational Betti cohomology, rational mixed Hodge modules/structures, and nearby cycles; regular holonomic \(\mathcal D\)-modules after complexification.
- **Hodge type:** target class \((p,p)\), equivalently Tate-twisted type \((0,0)\).
- **Cycle class map:** \(cl^p_{\mathbf Q}:CH^p(X)_{\mathbf Q}\to H^{2p}(X,\mathbf Q(p))\).
- **Equivalence relation on cycles:** rational equivalence.
- **Scope:** relative during degeneration; the desired conclusion is fiberwise and must specialize back to an arbitrary smooth projective complex fiber.

## Falsifiable theorem target

For the explicit two-parameter recollision family used by G032, prove all of the following:

1. the actual coefficient object satisfies either a published without-slopes hypothesis or a published microlocal non-characteristic plus Thom hypothesis along every flag used in the collision;
2. the resulting equivalence between the two orders of iterated nearby cycles lifts to rational mixed Hodge modules (or an equally strong rational Hodge-theoretic category), preserves Tate-twisted type \((0,0)\), and is monodromy-compatible;
3. under the B022 quotient identifications, the comparison intertwines the two detector maps and preserves the nonvanishing of the decisive pairing \(\langle\zeta,\Phi(\beta)\rangle\);
4. no component supported on an exceptional or boundary stratum supplies the nonzero pairing while disappearing on return to the target smooth fiber.

A counterexample to any item, or failure of the stated hypotheses at the forced collision locus, falsifies this target as written.

## Attempt 1 — make the base map a submersion by graph embedding

Embed the family map \(g:Y\to D^2\) as its graph and use the smooth projection \(Y\times D^2\to D^2\). This does not establish the required non-characteristic hypothesis. By B062, the graph conormal is non-characteristic exactly where \(g\) itself is a submersion. A topology-changing collision necessarily passes through a critical locus, so the ambient graph trick cannot certify item 1 there.

**Result:** failed. The precise obstruction is a nonzero base covector annihilated by \(dg\), hence lying in the singular support of the graph-supported coefficient object.

## Attempt 2 — infer comparison from clean boundary geometry

Clean intersection or normal-crossing equations control the incidence of boundary divisors, but B061 shows that order-independence is a statement about the coefficient object's slopes or singular support, not merely the reduced boundary arrangement. The current clean-collision model does not compute the relevant characteristic variety, verify Thom isotropy, or prove absence of slopes.

**Result:** incomplete. Boundary cleanliness alone does not discharge item 1.

## Attempt 3 — lift the comparison to mixed Hodge modules

B063 proves that this lift is already part of the comparison when the
underlying \(\mathcal D\)-module pair is without slopes. Thus item 2 is
conditionally closed on that branch. B064 then shows that the raw \(A_2\)
collision morphism fails the simpler geometric without-slopes condition; the
exact graph-pair condition is uncomputed, and proper resolution requires the
stronger strict-multispecialisability input. G034 isolates that calculation.

## Current smallest obligation

For the explicit B064 \(A_2\) equation, either compute the graph-pushed
constant Hodge module's Bernstein-Sato/\(V\)-multifiltration condition
directly, or perform G034's cusp resolution and test strict
\(R\)-multispecialisability. Then calculate compatibility with the B022
quotients and the Saito pairing.

## Propagation if proved

G033 would justify transporting the detector through a recollision without an order ambiguity and would return the argument to G032's pairing-survival obligation. It would not itself construct the terminal algebraic cycle and therefore would not prove G031 or the Hodge Conjecture.
