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
dependencies: B009-B010, B022, B058, B081-B084, B093-B107, G048-G055, G058, G070, NG068-NG072, NG082-NG083
claim: For the actual collision, restrict the special-to-nearby map to the canonical relation-grade filtration step S_0, compute u_0^* and F_0, then prove either [F_0] is nonzero in coker(u_0^*) or [F_0]=0 and its descended functional evaluates nontrivially on t_psi; G070 is the corrected concrete formulation.
falsifier: an undefined type-(0,0) dual map or detector functional, or simultaneous vanishing of the cokernel branch and descended evaluation for every admissible collision
---

# G059 — Compute the dual detector certificate

**Status:** EXPLORATORY

On rational type-$(0,0)$ parts, the original formulation wrote

\[
 u:S=H^{-1}(i_H^*K)\longrightarrow
 P_\psi=H^{-1}(i_H^*\Psi_fK)
\]

for B083's special-to-nearby map. B107/NG083 show that B093's
associated-grade/full-support coordinate does not define a canonical
functional on all of $S$. Let $S_0$ be the relevant canonical filtration
step, put $u_0=u|_{S_0}$, and first prove
$t_\psi\in\operatorname{im}u_0$. Construct $F_0\in S_0^*$ from the canonical
grade, the two B022 quotients, and pairing with the prescribed Hodge class.

Compute the exact alternative:

\[
 [F_0]\ne0\text{ in }\operatorname{coker}u_0^*,
\]

or, if $F_0=u_0^*\lambda$,

\[
 \lambda(t_\psi)\ne0.
\]

B095 proves that either certificate is equivalent to existence of a
detecting special lift inside the filtered domain. The first branch uses
filtered ambiguity; the second is lift-independent. Both retain the full
rational type and quotient checks.
B096/G060 identify the first branch with $F\circ d\ne0$ and reduce the
second to the pairing square with B058's known nonzero value.

B106/NG082 reactivate this disjunction as the exact collision gate. The later
G060-G068 chain attacks a sufficient realization of the descended branch,
whereas G069 cancels the auxiliary detector and becomes the terminal B010
condition. Neither replacement retains both exhaustive branches together
with the actual special-to-nearby provenance encoded here. G070 is now the
smallest fully well-defined version of this gate.
