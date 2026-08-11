---
brick_id: B124
status: PROVED
base_field: C with rational coefficients
variety: an arbitrary polarized smooth projective complex 2n-fold X, an isolated clean nodal hyperplane section Y_0 with nearby smooth fiber Y_c, a rational local relation beta, and a preselected B058 primitive Hodge-homology class c
smoothness: X and Y_c smooth; Y_0 has finitely many ordinary double points
projectivity: X and the one-parameter hyperplane degeneration projective
dimension: dim_C X=2n; hyperplane fibers have dimension 2n-1
codimension: middle cycle codimension n; singular support finite
coefficient_field: Q
cohomology_theory: relative singular homology, the long exact sequence of the pair (Y_c,Z_c), Saito good retraction, and primitive ambient homology
hodge_type: beta and its primitive ambient image are rational type (0,0) after Q(n); c is rational type (0,0)
cycle_class_map: CH^n(X)_Q -> H^(2n)(X,Q(n)); no algebraic representative is assumed or constructed
cycle_equivalence: rational equivalence in the terminal application
scope: relative and fiberwise
dependencies: B010, B059, B100-B101, G030-G031, G064-G065, S022 Section 2.5
claim: For a fixed local relation beta, Saito's primitive ambient realization is constant on the affine space of relative lifts of beta; consequently a relative lift with primitive value c exists if and only if Phi_(Y_0)(beta)=c, and every G065 witness necessarily contains G030's exact-target equality.
falsifier: two relative lifts of one beta with different primitive ambient images, or a G065 witness whose target relation has primitive ambient image different from c
---

# B124 — Relative lifts cannot tune the primitive target

**Status:** PROVED

Let

\[
 \partial:H_{2n}(Y_c,Z_c;\mathbf Q(n))
 \longrightarrow H_{2n-1}(Z_c;\mathbf Q(n))
\]

be the boundary map in Saito's isolated-singularity construction and fix a
local relation \(\beta\in\operatorname{im}\partial\). Its relative lifts form
the affine space

\[
 L_\beta=\partial^{-1}(\beta)=\gamma_0+A,
 \qquad
 A=\operatorname{im}\bigl(H_{2n}(Y_c)\to H_{2n}(Y_c,Z_c)\bigr).
\]

Let \(q_S\) be good retraction, inclusion in \(X\), and primitive
projection. B100, directly from S022 §2.4–§2.5, proves

\[
 q_S(A)=0.
\]

Therefore \(q_S\) is constant on \(L_\beta\), with value precisely Saito's
class \(\Phi_{Y_0}(\beta)\):

\[
 q_S(\gamma)=\Phi_{Y_0}(\beta)
 \quad\text{for every }\gamma\in L_\beta.
\]

For the preselected B058 class \(c\), it follows that

\[
 \boxed{
 \exists\gamma\in L_\beta\text{ with }q_S(\gamma)=c
 \iff
 \Phi_{Y_0}(\beta)=c.
 }
\]

In particular, changing the relative representative, its absolute nearby
ambiguity, or the marked map used to present it cannot tune the primitive
ambient value.

## Consequence for G065

A G065 witness has \(\partial F_*\widetilde t=\beta\) and, by its ambient
chain-homotopy clause, \(q_S(F_*\widetilde t)=c\). Hence it necessarily
proves

\[
 \Phi_{Y_0}(\beta)=c,
\]

which is G030's exact-target collision obligation. Conversely, that equality
guarantees that every Saito relative lift of \(\beta\) has the desired
primitive value, but it does not construct G065's continuous map of pairs or
its marked chain homotopy. Thus G065 is a still stronger geometric mechanism,
not a smaller reduction of G030.

B059 proves that exact recovery of \(c\) is strictly stronger than the
terminal requirement
\(\langle\zeta,\Phi_{Y_0}(\beta)\rangle\ne0\). Consequently G065 remains a
valid sufficient research route, but it cannot be labeled the narrowest
active gate. B125 identifies that gate as G084's clean-support incidence.

## Scope guard

This is rigidity of the relative-lift torsor, not a proof that any detecting
relation exists. It constructs neither a singular hyperplane nor an
algebraic cycle and gives no positive general-case Hodge result.
