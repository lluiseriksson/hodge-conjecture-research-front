---
brick_id: G060
status: EXPLORATORY
base_field: C with all stalk maps, duals, and pairings over Q
variety: an arbitrary polarized smooth projective complex 2n-fold, a prescribed primitive rational Hodge class, its B058 tube detector c, and the actual G055 collision to a clean nodal target
smoothness: ambient and generic hyperplane fibers smooth; target clean nodal; semistable source regular where required
projectivity: plane-net family, collision, and proper pushdown projective
dimension: ambient 2n; hyperplane fibers 2n-1; plane base 2; collision base 1
codimension: middle codimension n; target nodal stratum of positive codimension
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, nearby/vanishing-cycle exact sequence, perverse filtration, strict support, B022 quotients, tube maps, and Saito pairing
hodge_type: every term restricted to rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009-B010, B022, B058, B081-B084, B093-B097, G048-G055, G059, NG068-NG073
claim: For the actual collision exact segment W->S->P and canonical detector functional F, prove F composed with d is nonzero, or prove it is zero and construct a quotient- and Hodge-compatible descended pairing square with lambda(t_psi)=<zeta,c> nonzero.
falsifier: simultaneous vanishing of F composed with d and failure or zero value of every descended pairing square for every admissible collision
---

# G060 — Compute the ambiguity boundary or the pairing square

**Status:** EXPLORATORY

Construct the type-$(0,0)$ exact segment

\[
 W\xrightarrow{d}S\xrightarrow{u}P
\]

for the actual topology-changing collision and construct $F:S\to\mathbf Q$
through the canonical perverse grade, full support, both B022 quotients, and
pairing with $\zeta$.

There are exactly two tasks:

1. if $F\circ d\ne0$, record the resulting ambiguity-adjusted detecting lift;
2. if $F\circ d=0$, descend $F=u^*\lambda$ and prove the commutative
   comparison identity

   \[
   \lambda(t_\psi)=\langle\zeta,c\rangle.
   \]

The right side is already nonzero by B058. B096 proves that either completed
branch closes G059. The unresolved content is the actual topology-changing
comparison square, not linear algebra. B097 shows that G061's
quotient-compatible constant-target morphism would force the square and close
this gate.
