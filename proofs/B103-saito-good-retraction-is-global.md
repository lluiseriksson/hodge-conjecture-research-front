---
brick_id: B103
status: PROVED
base_field: C with rational (co)homology
variety: a one-parameter projective degeneration of hyperplane sections with isolated singular special fiber Y_0 and nearby smooth fiber Y_c
smoothness: nearby fiber smooth; special fiber smooth away from finitely many isolated singularities
projectivity: ambient X and hyperplane degeneration projective
dimension: ambient 2n; hyperplane fibers 2n-1
codimension: middle codimension n; singular support finite
coefficient_field: Q
cohomology_theory: good retraction, relative singular cohomology and homology, compact supports, and primitive ambient homology
hodge_type: none created by the topological retraction; downstream relation is rational type (0,0) after Q(n)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic cycle is constructed
cycle_equivalence: rational equivalence in the terminal application
scope: relative and fiberwise
dependencies: B010, B099-B102, S022 Section 2.5
claim: In Saito's isolated-singularity construction the good retraction is already a global map Y_c->Y_0 inducing an isomorphism off Sing(Y_0); with Z_c the inverse image of the singular set, it identifies the relative groups used to define the Saito ambient class, so no separate local-collapse/exterior-gluing theorem is required after that datum is fixed.
falsifier: a Saito Section 2.5 good retraction satisfying the printed hypotheses but failing to be an isomorphism off the singular set or failing to induce the stated relative-group identification
---

# B103 — Saito's good retraction already performs the global gluing

**Status:** PROVED

S022 §2.5 chooses a good retraction

\[
 \rho:Y_c\longrightarrow Y_0
\]

that induces an isomorphism over $Y_0\setminus\operatorname{Sing}Y_0$. It
then defines

\[
 Z_c=\bigcup_{y\in\operatorname{Sing}Y_0}\rho^{-1}(y)\cap Y_c
\]

and states that $H^j(Y_c,Z_c)=H_c^j(Y_c\setminus Z_c)$ and that pullback by
$\rho$ identifies $H^j(Y_0,Z_0)$ with $H^j(Y_c,Z_c)$. For $j\ge2$,
$H^j(Y_0,Z_0)=H^j(Y_0)$ in this isolated setting. The dual relative-homology
description is the one used for the cycle
$\gamma'\in H_{2n}(Y_c,Z_c;\mathbf Q(n))$.

Thus, after the actual collision and Saito good retraction have been fixed,
the local maps and exterior comparison are already one global datum. B102's
local collapse is a compatible local model, not an additional gluing gate.

## Boundary

B103 does not put B057's distributed thimble chain into
$H_{2n}(Y_c,Z_c)$. That chain lives initially in the total thimble complex
over a detector word. G067 must construct the single-fiber realization and
prove its marked boundary and ambient value.
