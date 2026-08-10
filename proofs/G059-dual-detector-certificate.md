---
brick_id: G059
status: EXPLORATORY
base_field: C with all stalks, maps, and duals over Q
variety: an arbitrary polarized smooth projective complex 2n-fold, a prescribed primitive rational Hodge class, and the actual G055 collision with specified nearby B058 detector t_psi
smoothness: ambient and generic hyperplane fibers smooth; target clean nodal; semistable source regular where required
projectivity: plane-net family, collision, and proper pushdown projective
dimension: ambient 2n; hyperplane fibers 2n-1; plane base 2; collision base 1
codimension: middle codimension n; target nodal stratum of positive codimension
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, special-to-nearby map and its dual, perverse filtration, strict support, B022 quotients, and Saito pairing
hodge_type: all stalk spaces and maps restricted to rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009-B010, B022, B081-B084, B093-B095, G048-G055, G058, NG068-NG071
claim: For the actual collision, compute the dual special-to-nearby map u^* and canonical detector functional F, then prove either [F] is nonzero in coker(u^*) or [F]=0 and its descended functional evaluates nontrivially on t_psi.
falsifier: an undefined type-(0,0) dual map or detector functional, or simultaneous vanishing of the cokernel branch and descended evaluation for every admissible collision
---

# G059 — Compute the dual detector certificate

**Status:** EXPLORATORY

On rational type-$(0,0)$ parts, let

\[
 u:S=H^{-1}(i_H^*K)\longrightarrow
 P_\psi=H^{-1}(i_H^*\Psi_fK)
\]

be B083's special-to-nearby map, and let $t_\psi\in\operatorname{im}u$ be
the specified detector. Construct the canonical scalar functional
$F\in S^*$ by composing B093's associated-grade/full-support coordinate,
the two B022 quotients, and pairing with the prescribed Hodge class.

Compute the exact alternative:

\[
 [F]\ne0\text{ in }\operatorname{coker}u^*,
\]

or, if $F=u^*\lambda$,

\[
 \lambda(t_\psi)\ne0.
\]

B095 proves that either certificate is equivalent to existence of a
detecting special lift. The first branch uses ambiguity; the second is
lift-independent. Both retain the full rational type and quotient checks.
