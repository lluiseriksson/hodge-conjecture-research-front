---
brick_id: B112
status: PROVED
base_field: C with all chain groups over Q
variety: an arbitrary polarized smooth projective complex 2n-fold X, one selected B058 detector, and a proposed projective topology-changing collision
smoothness: X and generic hyperplane fibers smooth; target clean nodal in the application; the theorem itself is exact chain algebra
projectivity: X, hyperplane family, and collision projective in the application
dimension: dim_C X = 2n; hyperplane fibers have dimension 2n-1; comparison chains have degree 2n
codimension: middle codimension n; target is a point of the plane base
coefficient_field: Q
cohomology_theory: rational relative singular chain complexes, marked boundaries, homology classes, B022 quotients, and primitive ambient pairing
hodge_type: no Hodge type is created; downstream excess must be rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed
cycle_equivalence: rational equivalence
scope: relative and fiberwise
dependencies: B022, B091, B104, B110-B111, G055, G073
claim: Two selected comparison chains with the same marked boundary have a canonical difference cycle up to the stated chain homotopies, but their common boundary does not determine the homology class of that excess; every homology class can occur without changing the boundary.
falsifier: a pair with equal boundary whose difference is not a cycle, failure of homotopy invariance, or uniqueness of the excess class from the common boundary in the explicit rational chain model
---

# B112 — The selected topology-changing excess is a cycle

**Status:** PROVED

Let $(C_*,\partial)$ be the rational relative chain complex in the target
comparison object. Suppose the actual selected collision realization and a
marked pure-Hurwitz reference are represented by

\[
 \gamma_{\mathrm{sp}},\gamma_H\in C_k
\]

with the same fully marked boundary:

\[
 \partial\gamma_{\mathrm{sp}}=\partial\gamma_H.
\]

Then

\[
 e_t=\gamma_{\mathrm{sp}}-\gamma_H
\]

is a cycle and defines

\[
 [e_t]\in H_k(C_*;\mathbf Q).
\]

If both realizations are changed through comparison-chain homotopies with
fixed marked boundary, their difference changes by a boundary, so $[e_t]$ is
unchanged. This is the class-specific version of G055's topology-changing
excess; B111 shows that it need not arise from a map on every thimble.

## Boundary data do not determine the excess

Fix one chain $\gamma_H$ with boundary $b$. For every cycle $z\in Z_k(C)$,

\[
 \gamma_{\mathrm{sp}}=\gamma_H+z
\]

has the same boundary and excess class $[z]$. Hence every element of
$H_k(C)$ can occur while the marked boundary remains fixed. In particular,
boundary equality cannot prove that the excess is zero, nonzero, of Hodge
type $(0,0)$, survives B022, or pairs nontrivially with the prescribed
Hodge class.

An exact finite model is the complex

\[
 C_k=\mathbf Q a\oplus\mathbf Q z,
 \quad C_{k-1}=\mathbf Q b,
 \quad \partial a=b,
 \quad \partial z=0.
\]

The chains $a$ and $a+\lambda z$ have the same boundary for every
$\lambda\in\mathbf Q$, while their excess classes are
$\lambda[z]\in H_k(C)\simeq\mathbf Q[z]$.

## Scope guard

B112 only defines the correct selected invariant and proves a
non-determination result. It does not construct the actual collision chain
$\gamma_{\mathrm{sp}}$ or prove any nonzero detector property.
