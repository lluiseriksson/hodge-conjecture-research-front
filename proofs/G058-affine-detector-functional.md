---
brick_id: G058
status: EXPLORATORY
base_field: C with all lift and pairing data over Q
variety: an arbitrary polarized smooth projective complex 2n-fold, a prescribed primitive rational Hodge class, and the actual G055 collision with clean nodal target H
smoothness: ambient and generic hyperplane fibers smooth; target clean nodal; semistable source regular where required
projectivity: plane-net family, collision, and proper pushdown projective
dimension: ambient 2n; hyperplane fibers 2n-1; plane base 2; collision base 1
codimension: middle codimension n; target nodal stratum of positive codimension
coefficient_field: Q
cohomology_theory: rational mixed Hodge modules, nearby/special exactness, perverse filtration, strict support, local relation cohomology, B022 quotients, and Saito pairing
hodge_type: lift torsor and ambiguity restricted to rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B009-B010, B022, B081-B084, B093-B095, G048-G055, NG068-NG071
claim: For the actual collision, prove the rational type-(0,0) lift torsor is nonempty and compute the canonical quotient-level pairing functional F so that, for one lift beta_0 and ambiguity space A, F(beta_0) is nonzero or F(A) is nonzero.
falsifier: no type-(0,0) lift, an undefined canonical functional, or simultaneous vanishing F(beta_0)=0 and F(A)=0 for every admissible collision
---

# G058 — Compute the affine detector functional

**Status:** EXPLORATORY

For the actual collision and nearby B058 class, let

\[
 \mathcal L^{(0,0)}=\beta_0+A
\]

be the rational type-$(0,0)$ special-lift torsor supplied by B083 after the
obstruction is killed. Define $F$ only through canonical operations:

\[
 H^{-1}(i_H^*K)^{(0,0)}
 \to E_\infty^{-1,0}
 \to H^{-1}(i_H^*P)^{(0,0)}
 \to \mathcal T(Y)/K
 \to \mathbf Q,
\]

where the last arrow is pairing with the prescribed primitive Hodge class
after both B022 quotient stages.

The exact gate is the disjunction

\[
 F(\beta_0)\ne0
 \quad\text{or}\quad
 F(A)\ne0.
\]

B094 proves that this is equivalent to existence of at least one detecting
lift. No exact recovery of B058's original ambient class and no
ambiguity-independence is required. B095/G059 give the equivalent dual
cokernel/evaluation certificate, which avoids choosing $\beta_0$.
